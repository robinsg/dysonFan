import paho.mqtt.client as mqttClient
import dysonConnect as dyson
import time
import os

def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to broker")
        global Connected                        # Use global variable
        Connected = True                        # Set that we are connected

    else:
        print("Connection failed")

def on_message(client, userdata, message):
    ##### print(str(message.payload.decode("utf-8")))

    # Split the message in to device name and command
    process_message(str(message.payload.decode("utf-8")).split(":"))

def process_message(msg):
    
    dev = msg[0]
    cmd = msg[1]

    if cmd == "off":
        # Find the Dyson device matching Device-name
        device = dyson.getDevices(dev)
        # Connect to the device using the IP address provided
        connected = device.connect(ipAddress)
        ####device.set_configuration(fan_power=FanPower.POWER_OFF)
        dyson.powerOff(device)

    if cmd == "night":
        # Find the Dyson device matching Device-name
        device = dyson.getDevices(dev)
        # Connect to the device using the IP address provided
        connected = device.connect(ipAddress)
        dyson.night(device)     

    dyson.disconnect(device)   

ipAddress = os.environ.get("IPADDR")
dysonUsername = os.environ.get("DYSONUSER")
dysonPassword = os.environ.get("DYSONPWD")
brokerAddress = os.environ.get("BROKER")
Connected = False                 # Global variable for connection state

# Log in to Dyson account
dyson = dyson.DYSON(dysonUsername, dysonPassword)

client = mqttClient.Client("Python")            # Create new instance
client.on_connect = on_connect                  # Attach function to callback
client.on_message = on_message                  # Attach function to callback

client.connect(brokerAddress)                   # Connect to broker
client.loop_start()

while Connected != True:                        # Wait for connection
    time.sleep(0.1)


client.subscribe("home/Dyson")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting")
    client.disconnect()
    client.loop_stop()