from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['get'])
def greeting():
    if request.method == 'GET':
        print('say hello to a stranger')
        return '[sender_ping] Hello stranger, I am pong container! nice to meet u!!!!!!'

@app.route('/pong', methods=['get','post'])
def pong_message():
    if request.method =='POST':
        print('got a message from ping container.')
        send_data = request.get_json()
        send_msg = send_data['msg']
        receive_msg = '[receiver_pong] Hi Hi Hi'
        print('send a response to the ping conatiner.')
        return send_msg + receive_msg

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5001, debug = True)

