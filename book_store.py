from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask import make_response

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

import crud
import httplib2
import json
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']


# Get JSON book info
@app.route('/bookstore/<int:genre_id>/<int:book_id>/JSON')
def showBookJSON(genre_id, book_id):
    book = crud.findBook(book_id)
    return jsonify(Book=book.serialize)


# Login page
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Google Login
@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # See if a user exists, if it doesn't make a new one
    user_id = crud.getUserID(login_session['email'])
    if not user_id:
        user_id = crud.createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " class=\"usr_pic\" > '
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'),
            401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = (
        'https://accounts.google.com/o/oauth2/revoke?token=%s'
        % login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Home Page
@app.route("/")
@app.route("/bookstore")
def showGenres():
    genres = crud.allGenres()
    if 'username' not in login_session:
        return render_template(
            'publicShowGenres.html', genres=genres)
    else:
        return render_template(
            'showGenres.html',
            genres=genres,
            login_id=login_session['user_id'])


# Create a Genre
@app.route("/bookstore/new", methods=['GET', 'POST'])
def newGenre():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        crud.createGenre(request.form['name'], login_session['user_id'])
        return redirect(url_for('showGenres'))
    else:
        return render_template('newGenre.html')


# Edit a Genre
@app.route("/bookstore/<int:genre_id>/edit", methods=['GET', 'POST'])
def editGenre(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedGenre = crud.findGenre(genre_id)
    if editedGenre.user_id != login_session['user_id']:
        return redirect('/bookstore')
    if request.method == 'POST':
        if request.form['name']:
            editedGenre.name = request.form['name']
            crud.editGenre(editedGenre)
            return redirect(url_for('showGenres'))
    else:
        return render_template('editGenre.html', genre=editedGenre)


# Delete a Genre
@app.route("/bookstore/<int:genre_id>/delete", methods=['GET', 'POST'])
def deleteGenre(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    genreToDelete = crud.findGenre(genre_id)
    if genreToDelete.user_id != login_session['user_id']:
        return redirect('/bookstore')
    if request.method == 'POST':
        crud.deleteGenre(genreToDelete)
        return redirect(url_for('showGenres', genre_id=genre_id))
    else:
        return render_template('deleteGenre.html', genre=genreToDelete)


# List all books from a Genre
@app.route("/bookstore/<int:genre_id>")
def showBooks(genre_id):
    genre = crud.findGenre(genre_id)
    books = crud.allBooks(genre_id)
    if 'username' not in login_session:
        return render_template(
            'publicShowBooks.html',
            genre=genre,
            books=books)
    else:
        return render_template(
            'showBooks.html',
            genre=genre,
            books=books,
            login_id=login_session['user_id'])


# Show a Book information
@app.route("/bookstore/<int:genre_id>/<int:book_id>")
def showBook(genre_id, book_id):
    genre = crud.findGenre(genre_id)
    book = crud.findBook(book_id)
    creator = crud.getUserInfo(book.user_id)
    if 'username' not in login_session:
        return render_template('publicShowBook.html', genre=genre, book=book)
    else:
        return render_template(
            'showBook.html',
            genre=genre,
            book=book,
            creator=creator,
            login_id=login_session['user_id'])


# Create a new Book
@app.route("/bookstore/<int:genre_id>/new", methods=['GET', 'POST'])
def newBook(genre_id):
    if 'username' not in login_session:
        return redirect('/login')
    genre = crud.findGenre(genre_id)
    if request.method == 'POST':
        crud.createBook(
            request.form['title'],
            request.form['synopsis'],
            request.form['cover'],
            request.form['price'],
            request.form['author'],
            genre_id,
            login_session['user_id'])
        return redirect(url_for('showBooks', genre_id=genre_id))
    else:
        return render_template('newBook.html', genre_id=genre_id)


# Edit a book
@app.route(
    "/bookstore/<int:genre_id>/<int:book_id>/edit",
    methods=['GET', 'POST'])
def editBook(genre_id, book_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedBook = crud.findBook(book_id)
    if editedBook.user_id != login_session['user_id']:
        return redirect('/bookstore')
    if request.method == 'POST':
        if request.form['title']:
            editedBook.title = request.form['title']
        if request.form['synopsis']:
            editedBook.synopsis = request.form['synopsis']
        if request.form['cover']:
            editedBook.cover = request.form['cover']
        if request.form['price']:
            editedBook.price = request.form['price']
        if request.form['author']:
            editedBook.author = request.form['author']
        crud.editBook(editedBook)
        return redirect(url_for(
            'showBook',
            genre_id=genre_id,
            book_id=book_id))
    else:
        return render_template(
            'editBook.html',
            book=editedBook,
            genre_id=genre_id)


# Delete a book
@app.route(
    "/bookstore/<int:genre_id>/<int:book_id>/delete",
    methods=['GET', 'POST'])
def deleteBook(genre_id, book_id):
    if 'username' not in login_session:
        return redirect('/login')
    bookToDelete = crud.findBook(book_id)
    if bookToDelete.user_id != login_session['user_id']:
        return redirect('/bookstore')
    if request.method == 'POST':
        crud.deleteBook(bookToDelete)
        return redirect(url_for('showBooks', genre_id=genre_id))
    else:
        return render_template(
            'deleteBook.html',
            book=bookToDelete,
            genre_id=genre_id)


# Serve the application
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
