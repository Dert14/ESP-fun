from machine import SoftI2C, Pin
import dht
import OLED_HTD11_modules as modules
import ssd1306

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


dht_11 = dht.DHT11(4)
while True:
    modules.static_text(oled)
