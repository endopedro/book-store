# Item Catalog
This project is a RESTful CRUD web app with a JSON endpoint and OAuth2.

## Application context
This is a Book Store application, you can insert, delete and edit books and genres

## Requisites
- [Python 2.7](https://www.python.org/downloads)
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Flask](http://flask.pocoo.org/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)

## Instructions
- Install VirtualBox and Vagrant
- Clone or download the Udacity Vagrantfile
- Go to Vagrant directory and and place this project folder there
- Launch the Vagrant VM (`vagrant up`)
- Access the VM (`vagrant ssh`)
- go to `/vagrant` directory
- Setup application database `python /item-catalog/database_setup.py`
- Insert data `python /item-catalog/stock.py`
- Run application `python /item-catalog/book_store.py`
- Access the application at http://localhost:5000

## JSON Endpoint
- To display the book JSON information use: `/bookstore/"GENRE_ID"/"BOOK_ID"/JSON`

## Google OAuth2
### To login in the application follow the steps:
- Go to [Google Developers Console](https://console.developers.google.com)
- Sign up or Login
- Go to Credentials
- Create Crendentials (OAuth Client ID)
- Go to Web application
- Create application name
- Authorize JavaScript origins "http://localhost:5000"
- Authorize redirect URIs "http://localhost:5000/login" and "http://localhost:5000/gconnect"
- Copy the Client ID and paste it in the login.html
- Download the JSON, rename it to `client_secrets.json` and put it in the item-catalog folder
- Run application using `python /item-catalog/book_store.py`
