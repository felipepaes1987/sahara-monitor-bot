def interpretar_contexto(dados):
    ultimos_precos = [float(candle[4]) for candle in dados]
    if ultimos_precos[-1] > ultimos_precos[-2]:
        return "📊 O preço está subindo nas últimas velas. Potencial tendência de alta se mantido o volume."
    else:
        return "📉 O preço está caindo. Atenção a possíveis rompimentos de suporte."