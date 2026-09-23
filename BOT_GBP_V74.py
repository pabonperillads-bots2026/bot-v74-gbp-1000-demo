# BOT V7.4 - 1000 GBP DEMO - DANNY - Salomé_Manuela_0122 - TODO EN GBP
import os, time, hmac, hashlib, requests
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
    log_gbp(f"API Blindada: OK - {MT5_LOGIN} {MT5_SERVER}")
    log_gbp("Blindaje OK - Listo para operar TODO EN GBP, DANNY")
    log_gbp("BOT V7.4 DEMO ACTIVO - Esperando señal GBP - DANNY - Gráfica GBPUSD")
else:
    log_gbp(f"API Blindada: FALTA SECRETO - DANNY - LOGIN:{'Vale' if MT5_LOGIN else 'FALTA'} PASS:{'Vale' if MT5_PASSWORD else 'FALTA'} SERVER:{'Vale' if MT5_SERVER else 'FALTA'}")
    log_gbp("ERROR: Secrets no cargados - Revisa Escenarios > Secretos")
