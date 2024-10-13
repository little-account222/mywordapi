from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

a = 1
app=Flask(__name__)
@app.route("/")
def main():
    global a
    a+=1
    return "ok"
@app.route("/z")
def add():
    global a
    return a
