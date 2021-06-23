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
print()

print('EVENTOS DE DISPOSITIVOS AGRUPADOS POR DATA HORA')
for device in devices:
    print("Dispositivo:", device)
    events = prodbox.group_events_by_date_time(device)
    average = prodbox.average_events_by_device(device)
    print(dict(events))
    print("Total de horários:", len(events))
    print("Média de acionamentos:", "%.2f" % average)
    print()

# print('MÉDIA DE ACIONAMENTOS DIÁRIOS POR DISPOSITIVO')
# devices = prodbox.devices()
# for device in devices:
#     print("Dispositivo:", device)
#     average = prodbox.average_events_by_device(devices[0])
#     print("%.2f" % average)
# # Sugestão de análise futura:
# De quanto em quanto tempo as leituras de sensores são feitas em cada dispositivo
# horários de pico (data/hora que os sensores mais ficam ativados)
