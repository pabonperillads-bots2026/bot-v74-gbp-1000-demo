# risk_guard.py V8.1 - DD <2% diario y <10% anual - APAGA TODO
import os
CAPITAL_INICIAL = 1000.0

def verificar_riesgo(capital_actual, dd_diario_actual=0):
    dd_diario_pct = ((CAPITAL_INICIAL - capital_actual) / CAPITAL_INICIAL) * 100
    dd_anual_pct = dd_diario_pct # Para demo, en real se calcula anual

    if dd_diario_pct >= 2.0:
        return False, f"🛑 KILL-SWITCH DD {dd_diario_pct:.2f}% >=2% - APAGANDO TODOS LOS BOTS"
    if dd_anual_pct >= 10.0:
        return False, f"🛑 KILL-SWITCH ANUAL DD {dd_anual_pct:.2f}% >=10% - STOP TOTAL"
    return True, f"✅ Riesgo OK DD:{dd_diario_pct:.2f}% <2% - Capital:{capital_actual} GBP"
