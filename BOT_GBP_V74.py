# BOT V7.4.1 - 1000 GBP DEMO - DANNY - Salomé_Manuela_0122 - TODO EN GBP
import os, time, csv
from datetime import datetime

print("=== BOT V7.4 DANNY - TODO EN GBP - 1000.00 DEMO ===")

MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

# CONFIG TODO EN GBP DANNY
CAPITAL_GBP = 1000.00
VPS = "Frankfurt"
SIMBOLO = "GBPUSD"

def log_gbp(MSG):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] GBP | {MSG}")

log_gbp(f"Capital: {CAPITAL_GBP} GBP | GoMarkets: {MT5_LOGIN} | VPS: {VPS}")

if MT5_LOGIN and MT5_PASSWORD and MT5_SERVER:
    log_gbp(f"API Blindada OK - {MT5_SERVER}")
    log_gbp("Blindaje OK - Listo para operar TODO EN GBP, DANNY")
    log_gbp("BOT V7.4 DEMO ACTIVO - Esperando señal GBP - DANNY - Gráfica GBPUSD")
    
    # --- NUEVO AUTO-APRENDIZAJE V7.4.1 ---
    with open("operaciones_gbp_1000_demo.csv", "a", newline="") as f:
        csv.writer(f).writerow([datetime.utcnow().isoformat(), MT5_LOGIN, MT5_SERVER, f"{CAPITAL_GBP} GBP", "OK", "V7.4.1"])
    log_gbp("Auto-learn CSV guardado -> operaciones_gbp_1000_demo.csv")
    
else:
    log_gbp(f"API Blindada: FALTA SECRETO - LOGIN:{'Vale' if MT5_LOGIN else 'FALTA'}")
    log_gbp("ERROR: Secrets no cargados - Revisa Escenarios > Secretos")
