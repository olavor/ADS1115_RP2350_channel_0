É muito comum encontrar pequenos travamentos (freezing) no barramento I2C ao usar o modo contínuo, 
especialmente se houver ruído elétrico na bancada, cabos longos ou falta de resistores pull-up robustos. 
Voltar para o Single-Shot com um reset preventivo é uma ótima estratégia para garantir estabilidade.

Para resetar o ADS1115 via software, utilizamos um comando especial do protocolo 
I2C chamado General Call Reset. Ele é enviado para o endereço reservado 0x00 contendo
o byte 0x06. Quando o ADS1115 recebe isso, ele aborta qualquer conversão em andamento 
e reinicia seus registradores para o estado de fábrica.

Limpei as linhas duplicadas do seu código, mantive a configuração para Ganho 1 (Gain = 1)
e adicionei o reset no início do loop.
