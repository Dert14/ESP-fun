import dht
import ssd1306
from utime import sleep_ms

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



'''
def dynamic_text(display):
    hum = 1
    temp = 2
    display.text(str(temp), 35, 0)
    display.text(str(hum), 35, 10)
    
'''

    
    




    

    

