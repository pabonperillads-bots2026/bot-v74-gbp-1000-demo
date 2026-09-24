# risk_guard.py - Guardián PRO+ DANNY - 2% Diario + 8% Anual
import os, csv
from datetime import datetime

CAPITAL_INICIAL = 1000.00
PERDIDA_MAX_DIA_PCT = 2.0   # <--- 2% diario = 20 GBP
DRAWDOWN_MAX_ANUAL_PCT = 8.0 # <--- 8% anual = 80 GBP

def verificar_riesgo(balance_actual, balance_inicial=1000.0):
    perdida_max_dia = balance_inicial * (PERDIDA_MAX_DIA_PCT / 100)
    drawdown_max_anual = balance_inicial * (DRAWDOWN_MAX_ANUAL_PCT / 100)
    
    # --- CANDADO 1: DRAWDOWN ANUAL <8% ---
    perdida_anual = balance_inicial - balance_actual
    if perdida_anual >= drawdown_max_anual:
        return False, f"🚨 BLOQUEO ANUAL 8%: Perdida {perdida_anual:.2f} GBP >= {drawdown_max_anual} GBP | Balance {balance_actual}"
    
    # --- CANDADO 2: PERDIDA DIARIA <2% ---
    # Si tu balance actual cayó 2% vs ayer, bloquea
    # Aquí usamos lógica simple: si balance < 980 (2% de 1000)
    limite_diario = balance_inicial - perdida_max_dia
    if balance_actual <= limite_diario:
        return False, f"🚨 BLOQUEO DIARIO 2%: Balance {balance_actual} <= Limite {limite_diario} GBP"
    
    return True, f"✅ RIESGO OK: Diario <2% ({perdida_max_dia} GBP) | Anual <8% ({drawdown_max_anual} GBP) | Balance {balance_actual} GBP"

if __name__ == "__main__":
    ok, msg = verificar_riesgo(1000)
    print(msg)
    ok2, msg2 = verificar_riesgo(975) # prueba 2% pérdida
    print(msg2)
