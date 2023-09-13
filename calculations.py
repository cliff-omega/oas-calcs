from azureSqlConnector import connectAndWriteToAzureSql

def outputJson(json):
    print('calculations.py was passed the following parameters: ')
    print(json)
    connectAndWriteToAzureSql(json)
    return json