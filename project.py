from ADS1115 import *
from machine import Pin, I2C
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000) 
import micropython,  time, ubinascii  
micropython.kbd_intr(ord('q'))
ADS1115_ADDRESS = 0x48
adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)
adc.setMeasureMode(ADS1115_CONTINUOUS)
adc.setPermanentAutoRangeMode(False)

try:
    adc.setConvRate(ADS1115_860_SPS)
    adc.setVoltageRange_mV(ADS1115_RANGE_6144)
    sleep_ms(200)
    adc.setCompareChannels(ADS1115_COMP_0_GND)
    sleep_ms(200)
    voltage = adc.getResult_V()
    sleep_ms(200)
    if voltage <0:
        voltage = voltage *(-1)
    print(voltage)
except:
    print("erro")
