
"""
backtestingpy
https://kernc.github.io/backtesting.py/
https://github.com/kernc/backtesting.py   -- 강추
pip install backtesting
"""

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG


class SmaCross(Strategy): # 전략
    n1 = 10
    n2 = 20

    def init(self): # 초기화   # self : 메모리 주소 할당
        close = self.data.Close # 종가 데이터
        self.sma1 = self.I(SMA, close, self.n1) # 이평 계산
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self): # 스레드 run(), 한번 구동하고 종료 --> 나만의 전략 작성
        if crossover(self.sma1, self.sma2): # sma1-sma2 > 0 일 때(단기가 장기를 넘어섰을 때 )
            self.buy() # self에서 만든 메모리 안에 buy()를 만듬
        elif crossover(self.sma2, self.sma1): # sma2-sma1 > 0 일 때(단기가 장기보다 내려갔을 때)
            self.sell()


bt = Backtest(GOOG, # 종목 : google
              SmaCross, # 내가 만든 전략
              cash=10000,  # 보유 현금
              commission=.002, # 커미션
              exclusive_orders=True) # 주문종목 보기

output = bt.run()
# bt.plot()
print(output)

"""
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                   97.067039
Equity Final [$]                  68221.96986
Equity Peak [$]                   68991.21986
Return [%]                         582.219699
Buy & Hold Return [%]              703.458242
Return (Ann.) [%]                   25.266427
Volatility (Ann.) [%]               38.383008
Sharpe Ratio                         0.658271
Sortino Ratio                        1.288779
Calmar Ratio                         0.763748
Max. Drawdown [%]                  -33.082172
Avg. Drawdown [%]                   -5.581506
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   94
Win Rate [%]                        54.255319
Best Trade [%]                       57.11931
Worst Trade [%]                    -16.629898
Avg. Trade [%]                       2.074326
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          33 days 00:00:00
Profit Factor                        2.190805
Expectancy [%]                       2.606294
SQN                                  1.990216
_strategy                            SmaCross
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
"""