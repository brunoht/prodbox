import csv
from collections import defaultdict

class Prodbox:

    # CONSTANTES
    ID = 0
    PRODUCTION_LINE_ID = 1
    DEVICE_ID = 2
    COUNT = 3
    CREATED_AT = 4

    # CONSTRUTOR
    def __init__(self, file_name):
        with open(file_name) as file:
            reader = csv.reader(file, delimiter=';')
            self.data = list(reader)
            del self.data[0]

    # retorna o tamanho da base de dados
    def data_size(self):
        return len(self.data)

    # retorna a lista com todos os items de uma determinada coluna
    def list_all(self, column, limit=1000):
        list = []
        count = 0
        for row in self.data:
            list.append(row[column])
            if count > limit:
                break
            count += 1
        return list

    # returna a lista de todos os dispositivos
    def devices(self):
        list = []
        for row in self.data:
            if row[self.DEVICE_ID] not in list:
                list.append(row[self.DEVICE_ID])
        return list

    # retorn a lista com todas as linhas de produção
    def lines(self):
        list = []
        for row in self.data:
            if row[self.PRODUCTION_LINE_ID] not in list:
                list.append(row[self.PRODUCTION_LINE_ID])
        return list

    # imprime uma lista, linha a linha
    def print(self, list, limit=1000):
        count = 0
        for row in list:
            print(row)
            if count >= limit:
                break
            count += 1

    # retorna o total de eventos por dispositivo
    def group_events_by_device(self, device_id):
        list = []
        for row in self.data:
            if(row[self.DEVICE_ID] == device_id):
                list.append(row)
        return list

    # retorna um dicionário com a contagem de quantos eventos um dispositivo registrou
    def count_device_events(self, device_id):
        events = self.group_events_by_device(device_id)
        device_active = 0
        device_inactive = 0
        for event in events:
            if event[3] == '1':
                device_active += 1
            else:
                device_inactive += 1
        return {
            'device': device_id,
            'active': device_active,
            'inactive': device_inactive,
            'total': len(events)
        }

    # retorna um dicionário com a soma de eventos agrupados pela data e hora
    def group_events_by_date_time(self, device_id):
        dict = defaultdict(int)
        events = self.group_events_by_device(device_id)
        for event in events:
            dict[event[self.CREATED_AT]] += 1
        return dict

    def average_events_by_device(self, device_id):
        events = self.group_events_by_date_time(device_id)
        sum = 0
        for event in events:
            sum += events[event]
        return sum / len(events)
