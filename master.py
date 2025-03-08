from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

SECRET_TOKEN = os.getenv('SECRET_TOKEN')
ip_addresses = {}

@app.route('/update_ip', methods=['POST'])
def update_ip():
    auth_header = request.headers.get('Authorization')
    if auth_header != f'Bearer {SECRET_TOKEN}':
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    name = data.get('name')
    ip = data.get('ip')
    print(name, ip)
    if name and ip:
        ip_addresses[name] = ip      
        update_hosts_file(name, ip)  
        return jsonify({'message': 'IP address updated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/get_ip', methods=['GET'])
def get_ip():
    return jsonify(ip_addresses)

def update_hosts_file(name, ip):
    # Read existing entries
    try:
        with open('agent_ip_list.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Check if the name already exists and update the IP
    updated = False
    with open('agent_ip_list.txt', 'w') as file:
        for line in lines:
            existing_ip, existing_name = line.strip().split()
            if existing_name == name:
                file.write(f'{ip} {name}\n')
                updated = True
            else:
                file.write(line)
        
        # If the name was not found, append the new entry
        if not updated:
            file.write(f'{ip} {name}\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)