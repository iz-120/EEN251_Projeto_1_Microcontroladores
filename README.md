# (EEN251) Projeto 1 - Cofre
Documentação e códigos desenvolvidos para o primeiro projeto da disciplina EEN251 - Microcontroladores e Sistemas Embarcados

## Descrição do Projeto
O tema escolhido para o projeto será a criação e implmentação de um cofre utilizando microcontrolador e periféricos.

## Requisitos do Sistema
![Tabela de Requisitos](/imagens/Tabela_Requisitos.png "Tabela de Requisitos do Sistema Proposto")

## Diagrama de Blocos do Sistema
Tem-se a seguir a primeira versão do Diagrama de Blocos, com o microcontrolador e os periféricos utilizados. As setas indiram se o fluxo de dados é de *input* ou *output*.

![Diagrama de Blocos](/imagens/Diagrama_Blocos_1.png "Primeira versão do Diagrama de Blocos do Sistema")

A próxima imagem já inclui de forma simplificada as conexões e pinos correspondentes do Raspberry Pi Pico que serão utilizados, além dos novos componentes que tiveram que ser adicionados para o bom funcionamento do sistema. As adições foram um conversor de nível lógico para adequar as tensões de componentes com o microcontrolador e dois resistores para permitir a utilização dos LEDs.

![Diagrama de Blocos 2](/imagens/Diagrama_Blocos_2.png "Segunda versão do Diagrama de Blocos do Sistema, agora com as conexões e pinos utilizados")

## Conexões
Essa seção irá abordar em mais detalhes as conexões de cada componente e os pinos do microcontrolador Raspberry Pi Pico que estão sendo utilizados em cada uma delas.

> ### Alimentação
> - Uma linha de GND (Pino 38)
> - Uma linha de VCC 3,3V (Pino 36)
> - Alimentar a entrada VBUS com 5V (Pino 40)

> ### Display OLED
> - GND: linha de GND (Pino 38)
> - VCC: linha de VCC 3,3V (Pino 36)
> - CLK: SPIO SCK – GP2 – Pino 4 
> - MISO: SPIO RX – GP4 – Pino 6
> - MOSI: SPI0 TX – GP3 – Pino 5 
> - DC: GP0 – Pino 1
> - RES: GP1 – Pino 2
> - CS: linha de GND (Pino38) 

> ### Servo Motor MG996R
> - PWM (laranja): TX_HV do Conversor de Nível Lógico
> - GND (marrom): linha de GND (Pino 38)
> - VCC (vermelho): alimentação 5V do VBUS (Pino 40)

> ### Conversor de Nível Lógico 3,3V-5V
> - TX_LV: PWM_A[3] - Pino 32
> - TX_HV: PWM (laranja) do Servo Motor
> - LV: linha de VCC 3,3V (Pino 36)
> - HV: alimentação 5V do VBUS (Pino 40)
> - TX2_LV: GP26 - Pino 31
> - TX2_HV: VCC (+) do Buzzer

> ### Teclado Numérico
> - L1: GP6 - Pino 9
> - L2: GP7 - Pino 10
> - L3: GP8 - Pino 11
> - L4: GP9 - Pino 12
> - C1: GP10 - Pino 14
> - C2: GP11 - Pino 15
> - C3: GP12 - Pino 16
> - C4: GP13 - Pino 17

> ### Buzzer
> - VCC (+): TX2_HV do COnversor de Nível Lógico
> - GND (-): linha de GND (Pino 38)

> ### LED Verde
> - Resistor 1k $\Omega$
> - VCC: Resistor -> Pino 26
> - GND: linha de GND (Pino 38)

> ### LED Vermelho
> - Resistor 1k $\Omega$
> - VCC: Resistor -> Pino 25
> - GND: linha de GND (Pino 38)
