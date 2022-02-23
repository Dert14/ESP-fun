import network
import urequests as requests
from machine import Pin
from dht import DHT11
from time import sleep


aio_key = "aio_cdoJ53R2nDzRkEvcNcpVDzGuUV3D"
username = "Dert14"
feed_name = "button"

def do_connect():
    wlan.active(True)             # Activate the interface so you can use it.
    if not wlan.isconnected():    # Unless already connected, try to connect.
        print('connecting to network...')
        wlan.connect(settings["wifi_name"], settings["password"])  # Connect to the station using
                                                                   # credentials from the json file.
        if not wlan.isconnected():
            print("Can't connect to network with given credentials.")
            usys.exit(0)  # This will programmatically break the execution of this script and return to shell.
    print('network config:', wlan.ifconfig())

wlan = network.WLAN(network.STA_IF) # This will create a station interface object.
                                    # To create an access point, use AP_IF (not covered here).
do_connect()
dht11 = DHT11(Pin(4))
while True:
    dht11.measure()
    temperature = dht11.temperature()
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': str(temperature)}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
    except Exception as e:
        print(e)
    sleep(2)    
