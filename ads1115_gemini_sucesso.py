from machine import Pin, I2C
import time
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
address = 0x48
config_bytes = bytearray([0xC3, 0x83])
for _ in range(99):
    # Usando bytearray para a configuração.
    # 0xC5 = Inicia conversão, Canal 0 (AIN0), Ganho +/- 2.048V, Single-shot
    # 0xC3 = Inicia conversão, Canal 0 (AIN0), Ganho +/- 4.048V, continus
    # 0x83 = 128 amostras/segundo, comparador desativado
    #config_bytes = bytearray([0xC5, 0x83])
    try:
        i2c.writeto(0x00, b'\x06')
        time.sleep_ms(20) # Pequena pausa para o chip processar o reset
    except OSError:
        pass # Ignora erro caso o reset falhe momentaneamente
    # Escreve a configuração no registrador de Configuração (0x01)
    # Isso inicia uma nova conversão a cada iteração do loop
    i2c.writeto_mem(address, 1, config_bytes)
    # Aguarda a conversão (8ms para 128SPS, aguardamos 10ms por margem de segurança)
    time.sleep_ms(10)
    # Lê 2 bytes do registrador de Conversão (0x00)
    data = i2c.readfrom_mem(address, 0, 2)
    # Junta os 2 bytes lidos em um único valor de 16-bits
    raw_value = (data[0] << 8) | data[1]
    # Corrige o sinal (complemento de dois) para valores negativos
    if raw_value > 32767:
        raw_value -= 65536
    # Converte o valor bruto em Volts (baseado no ganho de +/- 2.048V)
    #voltage = raw_value * (2.048 / 32767.0)
    voltage = raw_value * (4.096 / 32767.0)
    #print("Leitura AIN0 Bruta:", raw_value, "| Tensão AIN0 (V):", voltage)
    print(voltage)
    # Pausa opcional entre cada uma das 99 leituras para não poluir o terminal rápido demais
    time.sleep_ms(100)