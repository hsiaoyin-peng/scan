import socket

def scan_ports(host="127.0.0.1", start=1, end=1024):
    open_ports = []
    print(f"Scanning {host} ports {start}-{end} ...")

    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    return open_ports


def write_to_txt(filename="/pump_simm/result.txt", host="127.0.0.1", start=1, end=1024):
    open_ports = scan_ports(host, start, end)

    with open(filename, "w") as f:
        f.write(f"=== Port Scan Result for {host} (Ports {start}-{end}) ===\n")
        for port in open_ports:
            f.write(f"Port {port} is OPEN\n")

    print(f"Scan finished. Result written to {filename}")


if __name__ == "__main__":
    write_to_txt(filename="/pump_simm/result.txt", host="127.0.0.1", start=1, end=1024)

