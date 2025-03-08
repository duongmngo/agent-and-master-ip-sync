import os

def sync_hosts_file():
    # Check if agent_ip_list.txt exists
    if not os.path.exists('agent_ip_list.txt'):
        print("agent_ip_list.txt does not exist. Nothing to sync.")
        return

    with open('agent_ip_list.txt', 'r') as file:
        lines = file.readlines()

    with open('/etc/hosts', 'r') as file:
        existing_lines = file.readlines()
        print(existing_lines)

    with open('/etc/hosts', 'w') as file:
        for line in existing_lines:
            if not any(line.strip().endswith(name) for name in [l.split()[1] for l in lines]):
                file.write(line)
        for line in lines:
            file.write(line)

if __name__ == '__main__':
    sync_hosts_file()