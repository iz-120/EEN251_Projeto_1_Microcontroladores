"""
@file teste.py
@brief Programa para integrar os periféricos (teclado matricial 4x4, display OLED, LED, Buzzer e Servo motor) usando Raspberry Pi Pico
@details Este programa integra as funcionalidades dos periféricos listados para uma aplicação
         de cofre. O código roda em MicroPython.
@authors Izabel Sampaio Goes e Júlia Galhardi Cerqueira
@date 2024-04-29
"""
#Importações necessárias
from machine import Pin, SPI, PWM
from ssd1306 import SSD1306_SPI
from matrix_keyboard_4x4 import MatrixKeyboard
from servo import Servo
from time import sleep
import utime

#--------------------------------------------------------Teclado-------------------------------------------------------------
# Configuração dos pinos do Raspberry Pi Pico conectados ao teclado matricial
rows_pins = [9, 8, 7, 6]  # Pinos GPIO para as linhas
cols_pins = [13, 12, 11, 10]  # Pinos GPIO para as colunas
debounce_time = 20  # Tempo de debounce em milissegundos

# Instancia o objeto teclado com a configuração de pinos e tempo de debounce
keyboard = MatrixKeyboard(rows_pins, cols_pins, debounce_time)

#--------------------------------------------------------Display OLED---------------------------------------------------------
# Define os pinos do Raspberry Pi Pico conectados ao barramento SPI 0
spi0_sck_pin = 2
spi0_mosi_pin = 3
spi0_miso_pin = 4


# Define os pinos do Raspberry Pi Pico conectados ao display OLED SPI
display_dc = 0  # Data/command
display_rst = 1 # Reset
display_cs = 5  # Chip select, alguns modulos não tem esse pino

# Inicializa o SPI0 com os pinos GPIO2 (SCK), GPIO3 (MOSI) e GPIO4 (MISO)
spi0 = SPI(0, baudrate=1000000, polarity=1, phase=0, sck=Pin(spi0_sck_pin), mosi=Pin(spi0_mosi_pin), miso=Pin(spi0_miso_pin))

# Inicializa o display OLED SPI de 128x32
display = SSD1306_SPI(128, 32, spi0, Pin(display_dc), Pin(display_rst), Pin(display_cs))

# Limpa o display
display.fill(0)
display.show()

# Desenha o retângulo
display.rect(5, 1, 122, 31, 1)   # desenha algum texto em x_esq = 5, y_cima = 1, x_dir = 122, y_baixo = 31, cor = 1
display.show()

#-------------------------------------------------------LEDs-----------------------------------------------------------------------
led_vermelho = Pin(19, Pin.OUT)
led_verde = Pin(20, Pin.OUT)

#------------------------------------------------------Buzzer---------------------------------------------------------------------
buzzer = Pin(26, Pin.OUT)

#-------------------------------------------------------Servo-----------------------------------------------------------------------
servo = Servo(27)
servo.__init__(27)
#inicia fechado
servo.enviaPulsos(0.5)

#-------------------------------------------------------Programa Principal----------------------------------------------------------
#Senha correta
senha_correta = ['1', '7', '0', '4']
while True:
    # Limpa o display
    display.fill(0)
    display.rect(5, 1, 122, 31, 1)
    #Insere texto no display
    display.text('Insira a senha', 10, 14, 1)
    display.show()
    
    #Armazena a senha
    senha = []
    
    #Registra a senha de 4 dígitos
    while len(senha) != 4:
        key_chars = keyboard.get_pressed_keys()  #Obtém a lista de teclas pressionadas
        #Processa cada tecla pressionada
        for key in key_chars:
            senha.append(key)
            
        if len(senha) == 1:
            display.fill(0)
            display.rect(5, 1, 122, 31, 1)
            display.text(senha[0], 33, 14, 1)
            display.show()
            
        if len(senha) == 2:
            display.fill(0)
            display.rect(5, 1, 122, 31, 1)
            display.text(senha[0], 33, 14, 1)
            display.text(senha[1], 53, 14, 1)
            display.show()
            
        if len(senha) == 3:
            display.fill(0)
            display.rect(5, 1, 122, 31, 1)
            display.text(senha[0], 33, 14, 1)
            display.text(senha[1], 53, 14, 1)
            display.text(senha[2], 73, 14, 1)
            display.show()
            
        if len(senha) == 4:
            display.fill(0)
            display.rect(5, 1, 122, 31, 1)
            display.text(senha[0], 33, 14, 1)
            display.text(senha[1], 53, 14, 1)
            display.text(senha[2], 73, 14, 1)
            display.text(senha[3], 93, 14, 1)
            display.show()
        
        #Pausa para debounce e redução do uso da CPU
        utime.sleep_ms(100)

    #Se a senha estiver correta
    if senha[0] == senha_correta[0] and senha[1] == senha_correta[1] and senha[2] == senha_correta[2] and senha[3] == senha_correta[3]:
        #Display de acesso liberado
        display.fill_rect(5, 1, 122, 31, 1)
        display.text('Acesso liberado', 6, 14, 0)
        display.show()
        #Acende LED verde
        led_verde.value(1)
        #Abre a tranca
        servo.enviaPulsos(1.5)
        #Tempo para vizualizar o display e o LED
        utime.sleep_ms(3000)
        #Apaga LED verde
        led_verde.value(0)
    #Se a senha estiver incorreta
    elif senha[0] == '*' and senha[1] == '*' and senha[2] == '*' and senha[3] == '*':
        #Fecha a tranca
        servo.enviaPulsos(0.5)
    else:
        display.fill(0)
        display.rect(5, 1, 122, 31, 1)
        display.text('Acesso negado', 15, 14, 1)
        display.show()
        #Acende LED vermelho
        led_vermelho.value(1)
        #Aciona buzzer
        buzzer.value(1)
        #Tempo para vizualizar o display e o LED
        utime.sleep_ms(3000)
        #Apaga LED vermelho
        led_vermelho.value(0)
        #Desliga buzzer
        buzzer.value(0)
        
