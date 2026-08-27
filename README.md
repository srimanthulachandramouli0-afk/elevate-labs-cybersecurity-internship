# elevate-labs-cybersecurity-internship
My 45 Days Cyber Security Internship at Elevate Labs
Cyber-Securyty task1 port scan 

# Task 1: Scan Local Network for Open Ports
Objective: Learn to find open ports to understand network exposure.
Tools Used: Nmap (online), Wireshark concept
# Cyber Security Internship - Elevate Labs
**Task 1: Scan Local Network for Open Ports**

### Objective
To learn how to identify open ports on a network and understand the associated security risks.

### Tools Used
- Nmap (Online Scanner)
- Pydroid 3 - Python
- Shodan

### Steps Performed

**1. Identified Local IP**
- Was on mobile data, so I used localhost 127.0.0.1 for scanning.

**2. Nmap Scan**
- Command: `nmap -sT 127.0.0.1 -F`
- Result:
```
Nmap scan report for localhost (127.0.0.1)
PORT   STATE SERVICE
53/tcp open  domain
```

**3. Python Scan using Pydroid 3**
```python
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

# OUTPUT:
# Port 53: OPEN
# Port 80: CLOSED
# Port 443: CLOSED
# Port 22: CLOSED
# Port 21: CLOSED
# Port 8080: CLOSED
```

**4. Verification**
Both Nmap and Python showed the same result - Port 53 is OPEN. This confirms the scan is accurate.

**5. Public IP Scan**
- Tool: Shodan
- Target: 8.8.8.8 (Google DNS)
- Found Open Ports: 53, 443

### Key Learnings / Risks
- An open port can be an entry point for attackers.
- Port 53 is for DNS and is required for internet to work.
- Closed ports are safer but we must monitor open ports.

### Files in this Repository
- `Local_scan.py` - My Python scanning code
- `nmap_result.txt` - Nmap scan proof
- Screenshots folder

### Outcome
Successfully learned network reconnaissance, TCP connect scanning, and the difference between local and public IP scanning.
# Task 1: Scan Your Local Network for Open Ports

## Objective
Learn to discover open ports on devices connected to your local network to understand network exposure.

## Tool Used
- Nmap Online Scanner (hackertarget.com)
- Tested Target: scanme.nmap.org (Allowed by Nmap.org for testing)

## Why I used scanme.nmap.org?
As per internship guidelines, I am on Mobile Data (Jio 4G). I don't have WiFi router to scan 192.168.1.0/24. External online scanners cannot scan private IP 127.0.0.1. So as per "Technology Flexibility" rule, I used the official public test server provided by Nmap.

## Steps Followed
1. Tried scanning 127.0.0.1 on hackertarget.com - Got error "IP address or host name only" (screenshot 1)
2. Used allowed public target scanme.nmap.org
3. Ran Quick Nmap Scan (-sV for version detection)
4. Got results showing 2 open ports
5. Analyzed security risks

## Key Learnings
- What is TCP SYN scan: Stealth scan that doesn't complete full connection
- Difference between open vs closed ports
- How open ports can be entry points for attackers

## Interview Q&A (For Practice)
Q1. What is open port? - A door for data to enter.
Q2. Nmap SYN scan? - Knock and check without fully opening door.
Q3. Risk of open ports? - Hackers can enter.

## Screenshots
Added screenshots of scan attempts.

## Submission
Task completed on time - 27 Aug 2026, 7:53 PM
