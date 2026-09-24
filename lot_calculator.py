# lot_calculator.py - PRO+ Lote dinámico 1% riesgo
def calcular_lote_pro(balance, riesgo_pct=1.0, sl_pips=30):
    """
    Calcula lote según saldo real
    Ej: 1000 USD, 1% riesgo = 10 USD / trade
    """
    if balance < 100:
        return 0.01
    
    riesgo_dinero = balance * (riesgo_pct / 100)
    # Para GBP: 1 lote = 10 USD por pip aprox, ajustamos
    lote = riesgo_dinero / (sl_pips * 10)
    
    # Limites PRO
    lote = max(0.01, min(lote, 0.50))  # entre 0.01 y 0.50
    return round(lote, 2)

# Prueba
if __name__ == "__main__":
    print(f"1000 USD -> Lote: {calcular_lote_pro(1000)}")
    print(f"1500 USD -> Lote: {calcular_lote_pro(1500)}")
    print(f"2000 USD -> Lote: {calcular_lote_pro(2000)}")
