import socket

target = "127.0.0.1"
ports = [53, 80, 443, 22, 21, 8080]

print(f"Scanning {target}...")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
    s.close()
