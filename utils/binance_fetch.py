import requests

def buscar_dados_binance():
    url = "https://api.binance.com/api/v3/klines?symbol=SAHARAUSDT&interval=15m&limit=20"
    r = requests.get(url)
    dados = r.json()
    return dados