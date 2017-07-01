# -*- coding: utf-8 -*-
import requests
import json


def download_ans_store(headers, url, file):
    comment = requests.get(url, headers=headers)
    data = comment.json()
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)


def print_information(file):
    with open(file) as data_file:
        data_loaded = json.load(data_file)
    for i in data_loaded:
        print('PostId: {}'.format(i['postId']))
        print('Id: {}'.format(i['id']))
        print('Name: {}'.format(i['name']))
        print('E-mail: {}'.format(i['email']))
        print('Body: {}\n'.format(i['body']))


if __name__ == '__main__':
    download_ans_store(headers={'Accept': 'application/json'},
                       url='https://jsonplaceholder.typicode.com/comments',
                       file='data.json')
    print_information('data.json')
