import requests
import time
import socket
from dotenv import load_dotenv
import os

load_dotenv()

MASTER_URL = os.getenv('MASTER_URL')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
AGENT_NAME = os.getenv('AGENT_NAME')

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def sync_ip():
    public_ip = get_public_ip()
    headers = {'Authorization': f'Bearer {SECRET_TOKEN}'}
    data = {'name': AGENT_NAME, 'ip': public_ip}
    response = requests.post(MASTER_URL, json=data, headers=headers)
    if response.status_code == 200:
        print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} IP address synced successfully: {public_ip}')
    else:
        print('Failed to sync IP address' + response.text)

if __name__ == '__main__':
    while True:
        sync_ip()
        time.sleep(60)  # Sync every second