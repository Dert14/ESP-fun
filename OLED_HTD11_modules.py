import dht
import ssd1306
from utime import sleep_ms
import network, usys
import urequests  as requests
import ujson as json

hum = 0
temp = 0

def clear(display):
    display.fill(0)

def write_text(display):
    global hum
    global temp
    display.text('Temp:'+str(temp), 0, 0)
    display.text('Hum:'+str(hum), 0, 10)
#   display.text(str(temp), 35, 0)
#   display.text(str(hum), 30, 10)


    
def get_conditions(dht_11):
    global hum
    global temp
    dht_11.measure()
    hum = dht_11.humidity()
    temp = dht_11.temperature()

def do_connect(wlan, settings):
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(settings["wifi_name"], settings["password"])
                                                                   
        if not wlan.isconnected():
            print("Can't connect to network with given credentials.")
            usys.exit(0)  # This will programmatically break the execution of this script and return to shell.
        print('network config:', wlan.ifconfig())
        
def send_data(settings):
    global temp
    global hum
    url = 'https://io.adafruit.com/api/v2/' + settings["username"] + '/feeds/' + settings["feed_1"] + '/data'
    body = {'value': str(temp)+','+str(hum)}
    headers = {'X-AIO-Key': settings["aio_key"], 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
    except Exception as e:
        print(e)
        
    
'''
def send_hum(settings):
    global hum
    url = 'https://io.adafruit.com/api/v2/' + settings["username"] + '/feeds/' + settings["feed_2"] + '/data'
    body = {'value': str(hum)}
    headers = {'X-AIO-Key': settings["aio_key"], 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
    except Exception as e:
        print(e)
'''





'''
def dynamic_text(display):
    hum = 1
    temp = 2
    display.text(str(temp), 35, 0)
    display.text(str(hum), 35, 10)
    
'''

    
    




    
