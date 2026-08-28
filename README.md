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
As per internship guidelines, I am on Mobile Data (airtel 4G). I don't have WiFi router to scan 192.168.1.0/24. External online scanners cannot scan private IP 127.0.0.1. So as per "Technology Flexibility" rule, I used the official public test server provided by Nmap.

## Steps Followed
1. Tried scanning 127.0.0.1 on hackertarget.com - Got error "IP address or host name only" (screenshot 1)
2. Used allowed public target scanme.nmap.org
3. Ran Quick Nmap Scan (-sV for version detection)
4. Got results showing 2 open ports
5. Analyzed security risks


# Task 2: Phishing Email Analysis

**Objective:** To identify phishing characteristics in a suspicious email sample.

### 1. Sender's Email Spoofing
- Official domain should be `microsoft.com` but attacker used `micorsoft-support.com` (missing 'o').
- This is called Typosquatting.
- Reply-To is also fake domain.

### 2. Email Header Analysis (using MxToolbox)
- SPF: FAIL - Email not sent from Microsoft's authorized server.
- DKIM: FAIL - Signature not aligned.
- Return-Path is fake domain.
- Result: This confirms email spoofing.

### 3. Suspicious Link & Mismatched URL
- Link text shows microsoft.com but on hovering, real URL is `https://microsoft.com.secure-login.verify-account.com/login`
- Actual domain is `verify-account.com`, not microsoft.com. This is a credential harvesting link.

### 4. Suspicious Attachment
- File name: `Invoice_2026.pdf.exe`
- Double extension used to trick user. .exe is an executable malware file.

### 5. Urgent & Threatening Language (Social Engineering)
- Subject: "URGENT: Your Account Will Be Suspended in 24 Hours!"
- Body uses fear: "SUSPENDED within 24 HOURS", "permanent loss".
- Attacker creates panic so user clicks without thinking.

### 6. Spelling & Grammar Errors
- Generic greeting "Dear Customer" instead of user name.
- Unprofessional language for Microsoft.

### 7. Summary of Phishing Traits Found
This email contains all major phishing traits: Spoofed Sender, Header FAIL, Fake URL, Malicious Attachment, Urgency Tactics, and Spelling Errors.

### 8. Recommended Action
- Do NOT click link.
- Do NOT download attachment.
- Report as Phishing.
- Delete email.

**Conclusion:** This is a 100% Phishing Email aimed at stealing credentials and installing malware.

**Tools Used:** MxToolbox Header Analyzer, Google Admin Toolbox

## Header Analysis - Practical Proof

### Example 1: Legitimate Email (Unstop)
- SPF: PASS, DKIM: PASS, DMARC: PASS
- Screenshot: [UNSTOP screenshot]
- Conclusion: This is a safe email.

### Example 2: Phishing Email (Simulated Sample)
If we analyze the phishing sample `security-alert@micorsoft-support.com`:
- SPF: FAIL (Not from Microsoft servers)
- DKIM: FAIL
- DMARC: FAIL
- Screenshot: [If this were phishing, it would show RED FAIL EXAMPLEscreenshot].
- Conclusion: This is SPOOFED / Phishing.

This comparison proves how to differentiate Real vs Phishing email using Google Admin Toolbox.
## 🔍 Email Header Verification

To verify if the internship offer was genuine, I checked the email's original header in Gmail (⋮ > Show original) and analyzed it with Google Admin Toolbox > Messageheader.

### Example: Genuine Mail (Unstop)

**Observations from the screenshot:**
- **From:** `updates@unstop.email`
- **SPF:** PASS | **DKIM:** PASS with domain `unstop.email` | **DMARC:** PASS
- **Delivered after 1 second** via `amazonses.com` (Amazon SES - used by legit companies for bulk emails)
- Domain matches, so it's verified as original and not spoofed.

I will give the screenshot above[unstop.jpg]

#Google-support-phishing_email_sample Example
┌────────────────────────────────────────────────────────────────────────┐
│ FROM: Google Security <security-alert@g00gle-support.net> ◄── [1. Spoofed Domain]
│ TO: user@gmail.com                                                     │
│ SUBJECT: CRITICAL SECURITY ALERT: Action Required! ◄── [2. Urgent/Fear Tone]
├────────────────────────────────────────────────────────────────────────┤
│ Dear User,                                                             │
│                                                                        │
│ Someone just tried to log into your Google Account from Moscow, Russia.│
│ If this wasn't you, please change your password immediately to prevent │
│ total account termination within 12 hours.                             │
│                                                                        │
│ ┌─────────────────┐                                                    │
│ │ SECURE ACCOUNT ─┼─────────────────────────────────┐                  │
│ └─────────────────┘                                 │                  │
│                                                     ▼                  │
│                             [Actual Link: http://login-google-alert.tk]
│                             ◄── [3. Mismatched URL / Phishing Link]    │
│                                                                        │
│ Sincerely,                                                             │
│ Googel Security Team       ◄── [4. Spelling Error: "Googel"]           │
└────────────────────────────────────────────────────────────────────────┘

