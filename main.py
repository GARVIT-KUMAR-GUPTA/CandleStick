from candlestick import candlestick
import pandas as pd
import requests
candles_df=pd.read_csv(r"file:D://WebDev//QuizApp Project//candlestick-patterns/Sample.csv")

candles_df['Timestamp']=pd.to_datetime(candles_df['Timestamp'])
candles_df.set_index('Timestamp',inplace=True)
candles_df['return']=candles_df['Close'].pct_change()
candles_df.dropna(inplace=True)
print(candles_df)
dfpl = candles_df[0:100]
import plotly.graph_objects as go
from datetime import datetime

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close'])])

fig.show()
# Find candles where inverted hammer is detected

# candles = requests.get('https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1d')
# candles_dict = candles.json()

# candles_df = pd.DataFrame(candles_dict,
#                           columns=['T', 'open', 'high', 'low', 'close', 'V', 'CT', 'QV', 'N', 'TB', 'TQ', 'I'])

# candles_df['T'] = pd.to_datetime(candles_df['T'], unit='ms')

target = 'BullishRisingThree'
candles_df = candlestick.bearish_engulfing(candles_df, target=target)
# candles_df = candlestick.doji_star(candles_df)
# candles_df = candlestick.bearish_harami(candles_df)
# candles_df = candlestick.bullish_harami(candles_df)
# candles_df = candlestick.dark_cloud_cover(candles_df)
# candles_df = candlestick.doji(candles_df)
# candles_df = candlestick.dragonfly_doji(candles_df)
# candles_df = candlestick.hanging_man(candles_df)
# candles_df = candlestick.gravestone_doji(candles_df)
# candles_df = candlestick.bearish_engulfing(candles_df)
# candles_df = candlestick.bullish_engulfing(candles_df)
# candles_df = candlestick.hammer(candles_df)
# candles_df = candlestick.morning_star(candles_df)
# candles_df = candlestick.morning_star_doji(candles_df)
# candles_df = candlestick.piercing_pattern(candles_df)
# candles_df = candlestick.rain_drop(candles_df)
# candles_df = candlestick.rain_drop_doji(candles_df)
# candles_df = candlestick.star(candles_df)
# candles_df = candlestick.shooting_star(candles_df)

print(candles_df[candles_df[target] == True])