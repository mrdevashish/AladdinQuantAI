import threading
import time

from engines.tick_listener import run_listener

from engines.regime.regime_engine import RegimeEngine

from engines.liquidity.liquidity_map import LiquidityMap
from engines.liquidity.liquidity_pool import LiquidityPool
from engines.liquidity.mm_trap import MarketMakerTrap
from engines.liquidity.sweep_detector import LiquiditySweep

from engines.orderflow.imbalance import BidAskImbalance
from engines.orderflow.volume_delta import VolumeDelta
from engines.orderflow.iceberg import IcebergDetector
from engines.orderflow.spoofing import SpoofingDetector

from engines.options.options_flow_ai import OptionsFlowAI

symbol="NSE:NIFTY50-INDEX"

regime=RegimeEngine()

liqmap=LiquidityMap()
liqpool=LiquidityPool()
trap=MarketMakerTrap()
sweep=LiquiditySweep()

imbalance=BidAskImbalance()
delta=VolumeDelta()
iceberg=IcebergDetector()
spoof=SpoofingDetector()

options_ai=OptionsFlowAI()


def run_engines():

    print("AI Engines started")

    while True:

        regime.detect(symbol)

        liqmap.detect(symbol)
        liqpool.detect(symbol)
        trap.detect(symbol)
        sweep.detect(symbol)

        imbalance.detect(symbol)
        delta.detect(symbol)
        iceberg.detect(symbol)
        spoof.detect(symbol)

        options_ai.run()

        print("engine heartbeat...")

        time.sleep(5)


listener_thread=threading.Thread(target=run_listener)

print("Starting tick listener...")

listener_thread.start()

run_engines()
