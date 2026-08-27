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

#out put
Scanning 127.0.0.1...
Port 53: OPEN
Port 80: CLOSED
Port 443: CLOSED
Port 22: CLOSED
Port 21: CLOSED
Port 8080: CLOSED
