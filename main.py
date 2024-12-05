import json

import requests
import warnings

warnings.filterwarnings(action='ignore')

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float


@app.get("/api")
async def read_root():
    return "This is root path from MyAPI"


@app.get("/api/user/")
async def findUser(user):
    return findUser(user)


@app.get("/api/datas")
async def read_datas():
    return main()


@app.get("/api/time")
async def gettime():
    return gettime()


@app.get("/api/ad1")
async def ad1():
    return ad1()


@app.get("/api/ad2")
async def ad2():
    return ad2()


# 요청을 숨기기 위함
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
}


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return r, g, b


def calculate_black_closeness(r, g, b):
    return 100 * (1 - ((r ** 2 + g ** 2 + b ** 2) ** 0.5) / 441.673)


def findUser(user):
    try:
        with open('data.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            data = data[user]

            headers = {
                "Content-Type": "application/json"
            }

            url2 = "https://mafia42.com/api/user/user-info"
            user_id = {'id': data['ID']}

            data2 = requests.post(url2, json=user_id, headers=headers).json()
            data2 = data2['userData']
            print(data2)

            res = {
                "todaygames": data2['win_count']+ data2['lose_count'] - data['game_count'],

                "current_win_count": data2['win_count'],
                "current_lose_count": data2['lose_count'],
                "past_win_count": data['win_count'],
                "past_lose_count": data['lose_count']

            }

            return res
    except:
        return {
            "todaygames": "null",
            "win_count": 0,
            "lose_count": 0
        }

findUser("대현")

def gettime():
    colortime = ''
    gametime = ''
    with open('min_current_time.txt', 'r', encoding='UTF-8-sig') as f:
        time = f.readline().rstrip('\n')
    with open('day_current_time.txt', 'r', encoding='UTF-8-sig') as f:
        time2 = f.readline().rstrip('\n')

    return {
        "colortime": time,
        "gametime": time2

    }



def ad1():
    with open("ad1.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def ad2():
    with open("ad2.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def main():
    # JSON 파일 읽기
    with open('colorData.json', 'r', encoding='utf-8-sig') as f:
        user_data = json.load(f)

    res = []

    for i in user_data:
        color = user_data[i]['nickname_color']
        unsigned_value = color & 0xFFFFFFFF
        hex_value = hex(unsigned_value)
        formatted_hex_value = hex_value.upper().replace('0XFF', '')
        r, g, b = hex_to_rgb(formatted_hex_value)
        closeness = calculate_black_closeness(r, g, b)
        closeness = round(closeness, 4)

        res.append({
            "nickname": i,
            "color": formatted_hex_value,
            "closeness": closeness
        })

    res.sort(key=lambda x: x['closeness'], reverse=True)

    return res