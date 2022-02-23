from machine import SoftI2C, Pin, Timer
import dht
import OLED_HTD11_modules as modules
import ssd1306
import ujson as json
import network, usys


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

dht_11 = dht.DHT11(Pin(4))

with open("/wifi_credencials.json") as credentials_json:   # This pattern allows you to open and read an existing file.
    settings = json.loads(credentials_json.read())
wlan = network.WLAN(network.STA_IF)

modules.do_connect(wlan, settings)

def work_isr(event):
    modules.get_conditions(dht_11)
    modules.send_data(settings)
#   modules.send_hum(settings)
    modules.clear(oled)
    modules.write_text(oled)
#   modules.dynamic_text(oled)
    print(dht_11.temperature())
    oled.show()

    
blink_timer = Timer(1)
blink_timer.init(period=1500, mode=Timer.PERIODIC, callback=work_isr)




