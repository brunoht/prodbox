import csv

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

    # tamanho da base de dados

    def data_size(self):
        return len(self.data)

    # lista todos os items de uma determinada coluna

    def list_all(self, column, limit=1000):
        list = []
        count = 0
        for row in self.data:
            list.append(row[column])
            if count > limit:
                break
            count += 1
        return list

    # lista todos os dispositivos

    def devices(self):
        list = []
        for row in self.data:
            if row[self.DEVICE_ID] not in list:
                list.append(row[self.DEVICE_ID])
        return list

    # lista todas as linhas de produção

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

