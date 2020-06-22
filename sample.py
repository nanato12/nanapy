import os
import json

from time import sleep
from nanapy import Nana

if not os.path.exists('token.json'):
    token_list = []
else:
    token_list = json.load(open('token.json'))

while True:
    nana = Nana(password='TestAccount1234')
    # nana = Nana()
    nana.follow_user('8419582')
    nana.join_community('996441')
    for _ in range(30):
        nana.play_post('051a72fc')
    nana.applause_post('051a72fc')
    token_list.append(nana.token)
    json.dump(token_list, open('token.json', 'w'), indent=4)
    sleep(10)
