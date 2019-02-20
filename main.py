import argparse
import os
import requests
from dotenv import load_dotenv


def get_short_link(token, link):
    short_link_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": link,
    }
    response = requests.post(short_link_url,
                             headers=headers,
                             json=payload)
    if response.ok:
        return response.json()['link']
    else:
        return None


def get_summary_clicks(token, bitlink):
    summary_link = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "unit": "day",
        "units": -1,
    }
    response = requests.get(summary_link,
                            headers=headers,
                            json=payload)
    if response.ok:
        return response.json()['total_clicks']
    else:
        return None


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='Программа укорачивает ссылки через сервис bitly,'
                                                 'показывает количество кликов у укороченых ссылок')
    parser.add_argument("url", help="url to short or show click counts")
    args = parser.parse_args()
    token = os.getenv('TOKEN')
    link = args.url
    clicks_count = get_summary_clicks(token, link)
    if clicks_count is not None:
        print(f"Количество кликов по ссылке: {clicks_count}")
    else:
        short_link = get_short_link(token, link)
        if short_link is not None:
            print(f"Сокращенная ссылка: {short_link}")
        else:
            print("Неверно указана ссылка")
