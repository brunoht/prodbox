from prodbox import Prodbox

prodbox = Prodbox('Production_IoT.csv')

print('LINHAS DE PRODUÇÃO:')
lines = prodbox.lines()
prodbox.print(lines)
print('Total de linhas de produção:', len(lines))
print()

print('DISPOSITIVOS:')
devices = prodbox.devices()
prodbox.print(devices)
print('Total de dispositivos:', len(devices))
print()

print('EVENTOS DE DISPOSITIVOS')
for device in devices:
    print(prodbox.count_device_events(device))

# Sugestão de análise futura:
# De quanto em quanto tempo as leituras de sensores são feitas em cada dispositivo
# horários de pico (data/hora que os sensores mais ficam ativados)
