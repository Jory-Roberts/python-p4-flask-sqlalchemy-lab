#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    if animal is None:
        response_body = "<h1>404 animal not found</h1>"
        response = make_response(response_body, 404)
        return response
    else:
        response_body = f"""

                            <ul>Id: {animal.id}</ul>
                            <ul>Name: {animal.name}</ul>
                            <ul>Species: {animal.species}</ul>
                            <ul>Zookeeper: {animal.zookeeper.name}</ul>
                            <ul>Enclosure: {animal.enclosure.environment}</ul>

                    """

    return response_body


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    return ""


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    return ""


if __name__ == "__main__":
    app.run(port=5555, debug=True)
