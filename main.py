import os
import requests
from bs4 import BeautifulSoup

AccessToken = os.environ.get('AccessToken')
IntercomUrl = 'https://api.intercom.io/articles'
headers = {
    'Authorization': 'Bearer ' + AccessToken,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


def get_html_from_file():
    with open('article.html') as html:
        article = BeautifulSoup(html, 'html.parser')
        html.close()
        return article


def create_parameters(title, description, body):
    params = {
        "title": title.string,
        "description": description['content'],
        "body": str(body),
        "author_id": 1339063,
        "state": "published",
        "parent_id": 512832,
        "parent_type": "collection",
    }
    return params


def create_article():
    article = get_html_from_file()
    title = article.find('title')
    description = article.find('meta', {'name': 'description'})
    body = article.find('body')
    params = create_parameters(title, description, body)
    r = requests.post(IntercomUrl, headers=headers, json=params)
    print(r.text)
    print(r.headers)
    print(r.status_code)


def update_article():
    article_id = '5202578'
    article = get_html_from_file()
    title = article.find('title')
    description = article.find('meta', {'name': 'description'})
    body = article.find('body')
    params = create_parameters(title, description, body)
    update_article_url = IntercomUrl + '/' + article_id
    r = requests.put(update_article_url, headers=headers, json=params)
    print(r.text)
    print(r.headers)
    print(r.status_code)


if __name__ == '__main__':
    create_article()