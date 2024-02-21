import paramiko
import getpass

def ssh_command(ip, port, user, passwd):
    client = paramiko.SSHClient()

    # Now we set a policy which will auto-add the host keys if they are not there
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Now the client will connect using the below provided data
    client.connect(ip, port=port, username=user, password=passwd)

    try:
        while True:  # Keep asking for commands until 'exit' is entered
            cmd = input("Enter command (or type 'exit' to disconnect): ")
            if cmd.lower() == 'exit':  # Check if the user wants to exit
                print("Exiting...")
                break  # Exit the loop, which will lead to disconnection

            _, stdout, stderr = client.exec_command(cmd)

            # Storing the output and checking for any errors
            output = stdout.readlines() + stderr.readlines()
            if output:
                print('--- Output ---')
                for line in output:
                    print(line.strip())
    finally:
        client.close()  # Ensure the connection is closed even if an error occurs

if __name__ == '__main__':
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = int(input('Enter port or <CR>: ') or 2222)  # Ensure port is an integer

    ssh_command(ip, port, user, password)
