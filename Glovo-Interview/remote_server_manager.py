import paramiko

def run_command_on_servers(servers, username, key_file, command):
    for server in servers:
        print(f"\nConnecting to {server}...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(server, username=username, key_filename=key_file)
            stdin, stdout, stderr = ssh.exec_command(command)

            print("Output:")
            print(stdout.read().decode())

            ssh.close()

        except Exception as e:
            print(f"Failed to connect to {server}: {e}")


if __name__ == "__main__":
    servers = ["192.168.1.10", "192.168.1.11"]  # servers YOU own
    username = "alex"
    key_file = "/path/to/your/private_key"
    command = "uptime"

    run_command_on_servers(servers, username, key_file, command)