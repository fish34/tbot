import requests, json

q="{'update_id': 538387460, 'message': {'message_id': 6, 'from': {'id': 528547073, 'is_bot': False, 'first_name': 'Viacheslav', 'language_code': 'ru'}, 'chat': {'id': 528547073, 'first_name': 'Viacheslav', 'type': 'private'}, 'date': 1530609640, 'text': 'Dfgt'}}"
lnk="http://127.0.0.1:8000/planet/bot//"
headers = {'content-type': 'application/json'}
r=requests.post(lnk,data=json.dumps(q),headers=headers)
print(r)
