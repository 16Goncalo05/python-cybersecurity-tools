from scapy.all import sniff, IP, TCP, Raw

def packet_callback(packet):
    # Verify if the packet contains both IP and TCP layers
    if packet.haslayer(IP) and packet.haslayer(TCP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        destination_port = packet[TCP].dport
        
        #Check if it is unencrypted HTTP traffic (Port 80)
        if destination_port == 80:
            print(f"[NETWORK] Connection detected from {source_ip} to {destination_ip} on port 80 (HTTP)")
            
            # Extract and analyze payload if the packet contains raw data
            if packet.haslayer(Raw):
                payload = packet[Raw].load.decode(errors='ignore')
                
                # Trigger a visual alert if sensitive keywords are detected in cleartext
                keywords = ["user", "password", "pass", "login", "credentials"]
                if any(keyword in payload.lower() for keyword in keywords):
                    # Prints the alert in red using ANSI escape sequences
                    print("\033[91m" + f"[SECURITY ALERT] Possible cleartext credentials detected: {payload[:100]}" + "\033[0m")

print("Starting Packet Sniffer... Press Ctrl+C to stop.")
# 'sniff' captures packets and passes them to packet_callback in real-time without storing them in memory
sniff(prn=packet_callback, store=False)