import plotly.graph_objects as go
import pandas as pd

def get_serial_temporal_graph(data):
    # Gráfico de séries temporais
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Value'], mode='lines', name='Series Temporais'))
    fig.update_layout(title='Gráfico de Séries Temporais', xaxis_title='Data', yaxis_title='Valor')
    fig.show()