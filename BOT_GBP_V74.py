# BOT V7.4 - 1000 GBP DEMO - DANNY - Salome_Manuela_0122 - TODO EN GBP
import os, time, hmac, hashlib, requests
from datetime import datetime

print("=== BOT V7.4 DANNY - TODO EN GBP - 1000.00 DEMO ===")

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET = os.getenv("BINANCE_SECRET")

# CONFIG TODO EN GBP DANNY
CAPITAL_GBP = 1000.00
PEPPERSTONE_GBP = 61601283
VPS = "Frankfurt"
SYMBOL = "GBPUSDT"

def log_gbp(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')} GBP] {msg}")

log_gbp(f"Capital: {CAPITAL_GBP} GBP | Pepperstone: {PEPPERSTONE_GBP} | VPS: {VPS}")
log_gbp(f"API Blindada: {'OK' if API_KEY else 'FALTA SECRETO'} - DANNY")

if API_KEY and SECRET:
    log_gbp("Blindaje OK - Listo para operar TODO EN GBP, DANNY")
    # Aqui va tu logica V7.4
    log_gbp("BOT V7.4 DEMO ACTIVO - Esperando senal GBP - DANNY")
else:
    log_gbp("ERROR: Secrets no cargados - Revisa Escenarios > Secretos")
