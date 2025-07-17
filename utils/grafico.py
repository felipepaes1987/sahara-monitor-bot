import matplotlib.pyplot as plt
import pandas as pd
import time

def gerar_grafico(dados):
    df = pd.DataFrame(dados, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])
    df["close"] = df["close"].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    plt.figure(figsize=(10, 4))
    plt.plot(df["open_time"], df["close"], marker="o")
    plt.title("Token SAHARA/USDT - Últimas 20 velas (15min)")
    plt.xlabel("Horário")
    plt.ylabel("Preço")
    plt.grid(True)

    nome_arquivo = f"grafico_{int(time.time())}.png"
    plt.tight_layout()
    plt.savefig(nome_arquivo)
    plt.close()
    return nome_arquivo