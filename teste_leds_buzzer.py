from machine import Pin, PWM
from servo import Servo
 
buzzer = Pin(26, Pin.OUT)

buzzer.value(1)
buzzer.value(0)

led_vermelho = Pin(19, Pin.OUT)
led_verde = Pin(20, Pin.OUT)

led_vermelho.value(1)
led_verde.value(1)


servo = Servo(27)
servo.enviaPulsos(2.2) #Vai de 0.5 a 2.5 (achar os valores que funcionam)
                
                


