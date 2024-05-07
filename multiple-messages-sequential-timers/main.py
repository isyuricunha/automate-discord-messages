from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import json

# Load Config
with open('./config.json') as f:
    data = json.load(f)
    for c in data['Config']:
        print('Loading...')
        channelid = c['channelid']  # modify this in config.json
        token = c['token']  # modify this in config.json
        messages = c['messages']  # modify this in config.json

header_data = {
    "content-type": "application/json",
    "user-agent": "discordapp.com",
    "authorization": token
}

def get_connection():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v7/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("Message Sent")
            pass

        else:
            stderr.write(f"HTTP {resp.status}: {resp.reason} / Or blank message (maybe not a problem)\n")
            pass

    except:
        stderr.write("Error\n")

def main():
    while True:
        for message in messages:
            msg_content = message.get('content', '')
            msg_interval = message['interval']  # Intervalo em segundos

            message_data = {
                "content": msg_content,
                "tts": "false"
            }
            
            send_message(get_connection(), channelid, dumps(message_data))
            sleep(msg_interval)

if __name__ == '__main__':
    main()  # O loop principal agora está dentro da função main()
