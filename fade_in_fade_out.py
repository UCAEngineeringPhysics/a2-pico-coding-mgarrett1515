from machine import Pin, PWM
import time


# SETUP
led = PWM(Pin(15))   
led.freq(1000)       
MAX_DUTY = 65535


# LOOP
while True:
    
    for duty in range(0, MAX_DUTY, 650):   
        led.duty_u16(duty)
        time.sleep(0.02)  

    
    for duty in range(MAX_DUTY, -1, -650): 
        led.duty_u16(duty)
        time.sleep(0.01)  

#Used AI to help code this 
