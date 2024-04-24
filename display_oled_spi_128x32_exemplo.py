"""!
@file display_oled_spi_128x32_exemplo.py
@brief Programa para escrever em um display OLED SPI de 128x32 usando o Raspberry Pi Pico e MicroPython.
@details Este programa utiliza a biblioteca ssd1306 para escrever em um display OLED de 128x32 via comunicação SPI.
         Referência: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
@author Rodrigo França
@date 2023-03-17
"""

# Importa as classes Pin e SPI da biblioteca machine para controlar o hardware do Raspberry Pi Pico
from machine import Pin, SPI
# Importa a classe SSD1306_SPI da biblioteca ssd1306.py
from ssd1306 import SSD1306_SPI

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

#Exibe números
# display.text('6', 33, 14, 1)     # desenha algum texto em x = 33, y = 14, cor = 1
# display.text('3', 53, 14, 1)     # desenha algum texto em x = 53, y = 14, cor = 1
# display.text('1', 73, 14, 1)     # desenha algum texto em x = 73, y = 14, cor = 1
# display.text('0', 93, 14, 1)     # desenha algum texto em x = 93, y = 14, cor = 1

#Exibe textos
# display.text('Insira a senha', 10, 14, 1)
# display.text('Acesso negado', 15, 14, 1)
# display.fill_rect(5, 1, 122, 31, 1) #Para senha correta
# display.text('Acesso liberado', 6, 14, 0)
display.show()                         # escreve o conteúdo do FrameBuffer na memória do display

# Atualiza o display
display.show()

