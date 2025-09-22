from machine import Pin, PWM
import time

led = PWM(Pin(15))
led.freq(1000)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

mode = 1
last = 0
duty = 0
dir = 1

while True:
    if last == 1 and button.value() == 0:
        mode = 2 if mode == 1 else 1
    last = button.value()

    led.duty_u16(duty if mode == 1 else 65535)

    if mode == 1:
        duty += dir * 650
        if duty <= 0 or duty >= 65535:
            dir *= -1

    time.sleep(0.02)
#Used AI to help code this 
