import requests
import json
from config import API_KEY


def get_token(task_name):
    response = requests.post(
        url = f'https://tasks.aidevs.pl/token/{task_name}',
        data=json.dumps({'apikey': API_KEY})
                        )
    try:
        token = response.json()['token']
        return token
    except Exception as e:
        print(e)
        return e


def get_task(token):
    response = requests.get(
        url=f"https://tasks.aidevs.pl/task/{token}",
        data=json.dumps({'apikey': API_KEY})
    )
    task = response.json()
    return task


def send_answer(token, answer):
    data = json.dumps({'answer' : answer})
    response = requests.post(
        url=f"https://tasks.aidevs.pl/answer/{token}",
        data=data
    )
    print(data)
    return response.json()


