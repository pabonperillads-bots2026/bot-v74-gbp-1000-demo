# BOT V7.4 - 1000 GBP DEMO - DANNY - TODO EN GBP
import hmac, hashlib, time, requests
API_KEY = "PEGA_AQUI_TU_API_KEY_Salome_Manuela_0122"
SECRET = "PEGA_AQUI_TU_SECRET"
BASE = "https://testnet.binance.vision"

def get_price(sym):
    try:
        r = requests.get(f"{BASE}/api/v3/ticker/price?symbol={sym}", timeout=5)
        return float(r.json()['price'])
    except:
        return None

def get_balances():
    ts = int(time.time()*1000)
    q = f"timestamp={ts}"
    sig = hmac.new(SECRET.encode(), q.encode(), hashlib.sha256).hexdigest()
    headers = {"X-MBX-APIKEY": API_KEY}
    url = f"{BASE}/api/v3/account?{q}&signature={sig}"
    return requests.get(url, headers=headers).json()

# === VER SALDO EN GBP ===
data = get_balances()
if 'balances' not in data:
    print("Error:", data)
else:
    gbp_usdt = get_price("GBPUSDT") or 1.27
    print(f"GBPUSDT: {gbp_usdt} - 1 GBP = {gbp_usdt} USDT")
    total_gbp = 0
    for b in data['balances']:
        free = float(b['free']) + float(b['locked'])
        if free == 0: continue
        if b['asset'] == "GBP": gbp = free
        elif b['asset'] == "USDT": gbp = free / gbp_usdt
        else: 
            # BTC, BNB etc -> USDT -> GBP
            p = get_price(f"{b['asset']}USDT")
            gbp = (free * p / gbp_usdt) if p else 0
        if gbp > 0.001:
            print(f"{b['asset']}: {free} = {gbp:.2f} GBP")
            total_gbp += gbp
    print(f">>> TOTAL: {total_gbp:.2f} GBP / OBJETIVO 1000.00 GBP DEMO - DANNY <<<")
