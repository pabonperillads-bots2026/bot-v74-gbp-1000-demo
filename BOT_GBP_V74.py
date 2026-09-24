# BOT V8.1 INSTITUCIONAL DANNY - 0.30 - RR 1:3/1:5 - <5H - DD <2%/<10% - 1000 GBP
import os, time, csv
from datetime import datetime, timedelta
import MetaTrader5 as mt5
from telegram_alerts import enviar_telegram
from risk_guard import verificar_riesgo
from backtest_engine import hacer_backtest_20_anos

print("*** BOT V8.1 INSTITUCIONAL DANNY - 0.30 - RR 1:3/1:5 - Salomé_Manuela_0122 ===")

MT5_LOGIN = int(os.getenv("MT5_LOGIN", "0"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

CAPITAL_GBP = 1000.00
SIMBOLO = "GBPUSD"
LOTE_FIJO = 0.30
VPS = "Frankfurt"
MODO = os.getenv("MODO", "BACKTEST") # BACKTEST o LIVE

def log_v81(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] V8.1 GBP {LOTE_FIJO} | {msg}")

# --- PASO 1: BACKTEST 20 AÑOS OBLIGATORIO ---
log_v81("Iniciando validación 20 años sello Danny...")
resultado = hacer_backtest_20_anos()

if not resultado["apto"]:
    log_v81(f"❌ BACKTEST NO APTO: {resultado['motivo']}")
    # ALERTA SOLO DE NO APROBADO
    enviar_telegram(f"❌ V8.1 NO APROBADO - {resultado['motivo']} - Winrate:{resultado['winrate']}% PF:{resultado['profit_factor']} DD:{resultado['max_dd']}% - NO OPERARÁ")
    exit()

# Si llega aquí es APTO - ALERTA DE APROBADO
log_v81(f"✅ BACKTEST APROBADO 20 AÑOS - WR:{resultado['winrate']}% PF:{resultado['profit_factor']} Sharpe:{resultado['sharpe']} Sortino:{resultado['sortino']} DD:{resultado['max_dd']}% RR:1:{resultado['rr']}")
enviar_telegram(f"✅ V8.1 APROBADO 20 AÑOS - WR:{resultado['winrate']}% PF:{resultado['profit_factor']} Sharpe:{resultado['sharpe']} Sortino:{resultado['sortino']} DD:{resultado['max_dd']}% Recovery:{resultado['recovery']} RR:1:{resultado['rr']} - APTO PARA REAL 0.30")

if MODO == "BACKTEST":
    log_v81("MODO BACKTEST - Solo validación, no opera real")
    exit()

# --- PASO 2: LIVE REAL SOLO SI APROBADO ---
if not (MT5_LOGIN and MT5_PASSWORD and MT5_SERVER):
    log_v81("FALTA SECRETO MT5")
    exit()

puede, msg_riesgo = verificar_riesgo(CAPITAL_GBP)
if not puede:
    log_v81(msg_riesgo)
    enviar_telegram(f"🛑 V8.1 KILL-SWITCH - {msg_riesgo}")
    exit()

if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
    log_v81(f"MT5 no conecta {mt5.last_error()}")
    exit()

# Verificar posición y tiempo <5H
posiciones = mt5.positions_get(symbol=SIMBOLO)
if posiciones:
    for pos in posiciones:
        duracion = datetime.now() - datetime.fromtimestamp(pos.time)
        if duracion > timedelta(hours=5):
            # Cierre por tiempo >5H
            tick = mt5.symbol_info_tick(SIMBOLO)
            close_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask
            req = {"action": mt5.TRADE_ACTION_DEAL, "symbol": SIMBOLO, "volume": pos.volume, "type": close_type, "position": pos.ticket, "price": price, "deviation": 20, "magic": 742022, "comment": "V8.1 CIERRE +5H", "type_time": mt5.ORDER_TIME_GTC, "type_filling": mt5.ORDER_FILLING_IOC}
            mt5.order_send(req)
            enviar_telegram(f"⏰ V8.1 SALIDA +5H - {SIMBOLO} Ticket {pos.ticket} Duración {duracion} - Profit {pos.profit} GBP - CERRADO")
    mt5.shutdown()
    exit()

# Buscar entrada con RR 1:3 y 1:5
rates = mt5.copy_rates_from_pos(SIMBOLO, mt5.TIMEFRAME_M15, 0, 100)
if rates is None:
    mt5.shutdown()
    exit()

closes = list(rates['close'])
ema9 = sum(closes[-9:])/9
ema21 = sum(closes[-21:])/21
# Filtro Killzone Londres
hora_londres = datetime.utcnow().hour
en_killzone = 7 <= hora_londres <= 11

if en_killzone and ema9 > ema21:
    # COMPRA RR 1:3
    tick = mt5.symbol_info_tick(SIMBOLO)
    price = tick.ask
    sl = price - 0.0020  # 20 pips
    tp = price + 0.0060  # 60 pips RR 1:3
    # Si señal fuerte RR 1:5
    if ema9 - ema21 > 0.0005:
        tp = price + 0.0100 # 100 pips RR 1:5
    
    req = {"action": mt5.TRADE_ACTION_DEAL, "symbol": SIMBOLO, "volume": float(LOTE_FIJO), "type": mt5.ORDER_TYPE_BUY, "price": price, "sl": sl, "tp": tp, "deviation": 10, "magic": 742022, "comment": f"V8.1 BUY RR1:{(tp-price)/(price-sl):.1f}", "type_time": mt5.ORDER_TIME_GTC, "type_filling": mt5.ORDER_FILLING_IOC}
    res = mt5.order_send(req)
    if res.retcode == mt5.TRADE_RETCODE_DONE:
        rr_real = (tp-price)/(price-sl)
        enviar_telegram(f"🚀 V8.1 ENTRADA REAL BUY - {SIMBOLO} 0.30 - Precio {price:.5f} SL {sl:.5f} TP {tp:.5f} RR 1:{rr_real:.1f} - Max 5H - GoMarkets:{MT5_LOGIN}")

mt5.shutdown()
log_v81("V8.1 Ciclo terminado - Alertas solo en APROBADO y REAL")
