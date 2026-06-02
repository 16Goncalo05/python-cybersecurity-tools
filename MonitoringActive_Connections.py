import psutil
import time
import requests

#Discord/Telegram Webhook Configuration (Optional)
#If left empty, the script will only log alerts to the local terminal
DISCORD_WEBHOOK_URL = "" 

def send_webhook_alert(message):
    if DISCORD_WEBHOOK_URL:
        payload = {"content": message}
        try:
            requests.post(DISCORD_WEBHOOK_URL, json=payload)
        except Exception as e:
            print(f"Failed to send webhook alert: {e}")

print("Network Connection Monitor active... (Press Ctrl+C to exit)")

#Set to keep track of already discovered connections to avoid duplicate alerts
known_connections = set()

while True:
    #Retrieve all active TCP connections currently on the system
    for connection in psutil.net_connections(kind='tcp'):
        # Check if the connection state is 'ESTABLISHED' and has a valid remote address
        if connection.status == 'ESTABLISHED' and connection.raddr:
            remote_ip = connection.raddr.ip
            remote_port = connection.raddr.port
            connection_id = f"{remote_ip}:{remote_port}"
            
            #Identify if this is a new connection not seen in the previous cycle
            if connection_id not in known_connections:
                #Exclude common local loopback connections (e.g., localhost)
                if not remote_ip.startswith("127.0."):
                    alert = f"[NEW CONNECTION DETECTED] Process PID {connection.pid} connected to {remote_ip} on port {remote_port}"
                    print(alert)
                    send_webhook_alert(alert)
                    
                    #Store the connection ID to prevent repeating the alert
                    known_connections.add(connection_id)
                    
    #Wait for 5 seconds before scanning for new connections again
    time.sleep(5)
