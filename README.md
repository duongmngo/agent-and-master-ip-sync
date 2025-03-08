# IP Sync Agent and Master

This project consists of two programs: an agent program that syncs its public IP address to a master program. The master program has a static IP address and uses a secret token to secure communication with the agent program.

## Setup

1. Clone the repository.

2. Setup python version and virtal python environment
    ```sh
    pyenv install 3.12.3
    pyenv local 3.12.3
    python -m venv .venv
    source .venv/bin/activate
    ```    

2. Create a `.env` file in the root directory with the following content:

    ```env
    MASTER_URL=http://<master-ip>:5000/update_ip
    SECRET_TOKEN=your_secret_token
    ```

3. Install the required packages:

    ```sh
    pip install flask requests python-dotenv
    ```
4. (Optionall). Pip freeze lib version to requirements.txt    
    ```sh
    pip freeze > requirements.txt
    ```
## Running the Master Program

The master program receives the IP address from the agent and updates the `/etc/hosts` file.

1. Run the master program with `sudo` to have permission to modify the `/etc/hosts` file:

    ```sh
    sudo python master.py
    ```

## Running the Agent Program

The agent program periodically sends its public IP address to the master program.

1. Run the agent program:

    ```sh
    python agent.py
    ```

## Environment Variables

- `MASTER_URL`: The URL of the master program.
- `SECRET_TOKEN`: The secret token used for authentication.

## Note

Replace `<master-ip>` with the actual IP address of the master program and adjust the `SECRET_TOKEN` to a secure value of your choice.