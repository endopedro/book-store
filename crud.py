from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Book, User

from sqlalchemy.pool import StaticPool

engine = create_engine('sqlite:///book_store.db',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Genres helper Functions
def allGenres():
    return session.query(Genre).order_by(asc(Genre.name))


def createGenre(name, user_id):
    newGenre = Genre(name=name, user_id=user_id)
    session.add(newGenre)
    session.commit()


def findGenre(genre_id):
    return session.query(Genre).filter_by(id=genre_id).one()


def editGenre(editedGenre):
    session.add(editedGenre)
    session.commit()


def deleteGenre(genreToDelete):
    session.delete(genreToDelete)
    session.commit()


# Books Helper Functions
def allBooks(genre_id):
    return session.query(Book).filter_by(genre_id=genre_id).all()


def findBook(book_id):
    return session.query(Book).filter_by(id=book_id).one()


def createBook(title,
               synopsis,
               cover,
               price,
               author,
               genre_id,
               user_id):
    newBook = Book(title=title,
                   synopsis=synopsis,
                   cover=cover,
                   price=price,
                   author=author,
                   genre_id=genre_id,
                   user_id=user_id)
    session.add(newBook)
    session.commit()


def editBook(editedBook):
    session.add(editedBook)
    session.commit()


def deleteBook(bookToDelete):
    session.delete(bookToDelete)
    session.commit()


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None
