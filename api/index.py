from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
@app.route("/")
def main():
    return "ok"
