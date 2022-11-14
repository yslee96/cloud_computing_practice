
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['get'])
def greeting():
    print('say hello to a stranger')
    return '[sender_ping] Hello stranger, I am ping container! nice to meet u!!!!!!'

@app.route('/ping', methods= ['get', 'post'])
def ping_message():
    if request.method == 'GET':
        pong_url = "http://pong_con:5001/pong"        
        send_msg = '[sender_ping] --ping--> '
        send_data = {'msg': send_msg}
        print("send a message to pong container.")
        response = requests.post(pong_url, json= send_data)
        print("got a reponse from the pong container.")
    return response.text

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000, debug = True)

