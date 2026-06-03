### 1. Multi-Threaded Port Scanner (`Portscan.py`)
* **Description:**
A lightweight network reconnaissance tool built to discover active services on a target host.
Instead of scanning ports sequentially, it leverages Python's `threading` library to scan
multiple ports concurrently, drastically reducing execution time.

  
* **Core Mechanics:**
It utilizes the `socket` library to perform TCP 3-way handshakes. By analyzing the return
value of `connect_ex()`, the script accurately determines whether a specific port is open (returning `0`) or closed.
  

* **Cybersecurity Relevance:**
Used during the reconnaissance phase (MITRE ATT&CK: Discovery) to map out the
attack surface of an infrastructure and identify potentially vulnerable entry points.



### 2. Packet Sniffer & Cleartext Analyzer (`Sniffer.py`)
* **Description:**
A real-time network traffic monitoring tool that captures packets passing through the network
interface card (NIC) and analyzes them for security risks.

  
* **Core Mechanics:**
Powered by the `Scapy` framework, the script hooks into the network layer, dissects IP
and TCP headers, and specifically isolates unencrypted HTTP traffic (Port 80). It decodes the raw payload
to scan for sensitive keywords (e.g., `user`, `password`, `login`) using ANSI escape codes to trigger red
visual alerts in the terminal upon detection.

  
* **Cybersecurity Relevance:**
Demonstrates the high risk of using unencrypted protocols and serves as a foundational tool for
Network Intrusion Detection (IDS) and traffic baseline analysis.


### 3. Network Connection Monitor (`MonitoringActive_Connections.py`)
* **Description:**
A Blue Team behavioral monitoring script designed to keep track of system network states and alert
administrators about unauthorized or unexpected external connections.

  
* **Core Mechanics:**
Using the `psutil` library, the script continuously audits all
`ESTABLISHED` TCP connections on the operating system. It maintains an internal memory state
(`set`) to track known connections, filters out local loopback traffic (`127.0.x.x`), and
triggers instant alerts detailing the specific Process ID (PID), remote IP, and destination
port of any new connection.


* **Cybersecurity Relevance:**
Acts as a host-based detection mechanism (HIDS) capable of identifying malicious outbound
traffic, indicators of compromise (IoCs), or active data exfiltration channels.
