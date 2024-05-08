import plotly.graph_objects as go
import pandas as pd

def get_graph_velas(data_candles):
    # Gráfico de velas
    fig_candles = go.Figure(data=[go.Candlestick(x=data_candles['Date'],
                    open=data_candles['Open'],
                    high=data_candles['High'],
                    low=data_candles['Low'],
                    close=data_candles['Close'])])

    fig_candles.update_layout(title='Gráfico de Velas')
    fig_candles.show()
