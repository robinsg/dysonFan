from libpurecool.const import FanSpeed, FanPower, NightMode
import dysonConnect as dyson
import sys

if len(sys.argv) != 5:   # five including the program name entry [0]
	print("Usage: %s  Device-name IP-Address Username Password" %(sys.argv[0]))
	sys.exit(1)
dysonName=sys.argv[1]
ipAddrees=sys.argv[2]
dysonUsername=sys.argv[3]
dysonPassword=sys.argv[4]

''' print("Dyson device=%s IP Address=%s Dyson account email address=%s Dyson account password=%s"  %( dysonName, ipAddrees, dysonUsername, dysonPassword))'''

# Log in to Dyson account
dyson = dyson.DYSON(dysonUsername, dysonPassword)

# Find the Dyson device matching Device-name
dev = dyson.getDevices(dysonName)

# Connect to the device using the IP address provided
connected = dev.connect(ipAddrees)

# Set the fan to night mode
dev.set_configuration(
   fan_power=FanPower.POWER_ON,
   fan_speed=FanSpeed.FAN_SPEED_4,
   night_mode=NightMode.NIGHT_MODE_ON)

# Disconnect
dev.disconnect()