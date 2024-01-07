from pythonosc.udp_client import SimpleUDPClient
import time
import util

# Set the IP address and port of the OSC server
server_ip = "127.0.0.1"
server_port = 8000

def sendOSC (message):
    # Create an OSC client
    client = SimpleUDPClient(server_ip, server_port) 

    # Send an OSC message
    client.send_message(message, "Sent from Rebecca")


def get_initial_data():
    for item in util.initial_osc_commands:
        sendOSC(item)
        time.sleep(1)

def interval_get_initial_data():
    while True:
        get_initial_data()
        time.sleep(10)

if __name__ == "__main__":
    for i in range(10):
        sendOSC("/eos/get/patch/" + str(i))