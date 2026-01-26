import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()


if __name__ == "__main__":
    target = "127.0.0.1"  # Scan your own computer
    ports_to_scan = [22, 80, 443, 3306, 8080]

    scan_ports(target, ports_to_scan)