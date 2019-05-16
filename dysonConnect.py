from libpurecool.dyson import DysonAccount
from libpurecool.const import FanSpeed, FanPower, NightMode

class DYSON(object):
    def __init__(self,user, password):
        # Log to Dyson account
        # Language is a two characters code (eg: FR)
        self.ConnectToDyson(user, password)

    def ConnectToDyson(self, user, password):
        # Log to Dyson account
        # Language is a two characters code (eg: FR)
        self.dyson_account = DysonAccount(user, password,"GB")
        logged = self.dyson_account.login()

        if not logged:  
            print('Unable to login to Dyson account')
            exit(999)

    def getDevices(self, dysonName):
        # List devices available on the Dyson account
        located=False
        devices = self.dyson_account.devices()
        for i in range(len(devices)):
            if devices[i].name == dysonName:
                located=True
                print('%s located' %(dysonName))
                break

        # If the device name was not found then exit
        if not located:
            print('Unable to find device %s' %(dysonName))
            exit(998)

        return devices[i]

    def night(self, dysonDev):
        # Set the fan to night mode
        dysonDev.set_configuration(
            fan_power=FanPower.POWER_ON,
            fan_speed=FanSpeed.FAN_SPEED_4,
            night_mode=NightMode.NIGHT_MODE_ON)

    # Power off the device
    def powerOff(self, dysonDev):
        dysonDev.set_configuration(fan_power=FanPower.POWER_OFF)

    def disconnect(self, dysonDev):
        # Disconnect
        dysonDev.disconnect()