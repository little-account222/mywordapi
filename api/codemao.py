
import random
import string
import requests
from json import loads
from time import time,sleep

own_headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Client-ID': 'WEB',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': '__ca_uid_key__=3fc85641-5aaa-40fa-b9cf-cf34b3a32a74; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221566444444%22%2C%22first_id%22%3A%2219150f89be5a83-097f313bc4b9228-4c657b58-2073600-19150f89be6faf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNTBmODliZTVhODMtMDk3ZjMxM2JjNGI5MjI4LTRjNjU3YjU4LTIwNzM2MDAtMTkxNTBmODliZTZmYWYiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxNTY2NDQ0NDQ0In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221566444444%22%7D%2C%22%24device_id%22%3A%2219150f89be5a83-097f313bc4b9228-4c657b58-2073600-19150f89be6faf%22%7D; aliyungf_tc=0146969fa934458118383c5f6ebb79b2f865ae07bfa36059d32fb9227ad27f36; acw_tc=ac11000117250101936296404e146e8baf7a1ac15116c422ff857a658fcfb1',
        'Net': '4g',
        'Origin': 'https://shequ.codemao.cn',
        'Platform': 'web',
        'Product-Code': 'community',
        'Referer': 'https://shequ.codemao.cn/',
        'SDK-Account-Version': '0.16.2',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'X-Captcha-Id': '6',
        'X-Captcha-Ticket': 'ff0d55df7c7e4cbf85b1fb05ea7625f2',
        'pid': '65edCTyg',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
}

def login(username, password):
        session_obj = requests.session()
        session_obj.post('https://open-service.codemao.cn/captcha/rule/v3',json={"identity": username, "scene": "", "pid": "65edCTyg","deviceId": "1d27f5d94b53fa2516874fe0a184b7b9", "timestamp": int(time())},headers=own_headers)
        ticket = loads(session_obj.post('https://open-service.codemao.cn/captcha/rule/v3',json={"identity": username, "scene": "", "pid": "65edCTyg","deviceId": "1d27f5d94b53fa2516874fe0a184b7b9", "timestamp": int(time())},headers=own_headers).text)['ticket']
        session_obj.post('https://api.codemao.cn/tiger/v3/web/accounts/login/security',json={"identity": username, "password": password, "pid": "65edCTyg", "agreement_ids": [-1]},headers={'x-captcha-ticket': ticket})
        return session_obj.cookies.get('authorization')
