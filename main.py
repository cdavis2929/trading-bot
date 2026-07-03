import random
import time
from fastapi import FastAPI
import threading

app = FastAPI()

balance = 1000
equity = 1000
trades = []

def trading_loop():
    global balance, equity

    while True:
        move = random.uniform(-5, 5)
        equity += move

        trades.append({
            "pnl": move,
            "equity": equity
        })

        print(f"Trade PnL: {move:.2f} | Equity: {equity:.2f}")
        time.sleep(2)

@app.get("/metrics")
def metrics():
    return {
        "equity": equity,
        "trades": trades[-10:]
    }

threading.Thread(target=trading_loop, daemon=True).start()
