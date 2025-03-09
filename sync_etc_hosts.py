import os
import logging
from datetime import datetime
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
# Configure logging
log_file = os.path.join(script_dir, 'sync_hosts.log')
logging.basicConfig(filename=log_file, level=logging.INFO)

def sync_hosts_file():
    logging.info(f'Starting sync at {datetime.now()}')
    
    agent_ip_list_path = os.path.join(script_dir, 'agent_ip_list.txt')
    if not os.path.exists(agent_ip_list_path):
        logging.warning("agent_ip_list.txt does not exist. Nothing to sync.")
        return

    with open(agent_ip_list_path, 'r') as file:
        lines = file.readlines()

    with open('/etc/hosts', 'r') as file:
        existing_lines = file.readlines()

    new_hosts_content = []
    for line in existing_lines:
        if not any(line.strip().endswith(name) for name in [l.split()[1] for l in lines]):
            new_hosts_content.append(line)
    for line in lines:
        new_hosts_content.append(line)

    if new_hosts_content != existing_lines:
        with open('/etc/hosts', 'w') as file:
            file.writelines(new_hosts_content)
        logging.info(f'Changes detected and /etc/hosts updated at {datetime.now()}')
        
        # Reload Nginx
        try:
            subprocess.run(['sudo', 'nginx', '-s', 'reload'], check=True)
            logging.info(f'Nginx reloaded at {datetime.now()}')
        except subprocess.CalledProcessError as e:
            logging.error(f'Failed to reload Nginx: {e}')
    else:
        logging.info(f'No changes detected at {datetime.now()}')

if __name__ == '__main__':
    sync_hosts_file()