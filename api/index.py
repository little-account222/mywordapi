from flask import Flask , request
import requests , json , random


app = Flask(__name__)
@app.route('/')
def main():
    return '此站点属于FantasyTeam---由vercel severless提供部署服务【正在建设中】'
