#import plotly.graph_objects as go
#import pandas as pd
import stocker
import yfinance as yf

class Analytic:
#РАБОТА СО stocker

    def prediction(self):
        st = stocker.predict.tomorrow(self, years=1)
        return f'Предположительная стоимость акции {self} на {st[2]} составляет: {st[0]}'

    #РАБОТА С Yahoo Finance
    def info1(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['longBusinessSummary']      #Вывод описания эмитента
    def info2(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['currentPrice']           #Вывод цены акции на данный момент
    def info3(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['shortName']              #Вывод названия организации
    def info4(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['previousClose']           #Вывод стоимости акции на момент последнего закрытия рынка
    def info5(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['sector']                  #Вывод сферы деятельности
    def info6(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['country']                 #Вывод страны, в которой располагается организация
    def info7(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['industry']                #Вывод индустрии
    def info8(self):
        hin = yf.Ticker(self)
        s = hin.info
        return s['industry']                #Вывод названия организации

#ПОСТРОЕНИЕ ГРАФИКА
#def graph(comp_name):
    #hin = yf.Ticker(comp_name)
    #df = hin.history(period="max")
    #df = df.reset_index()
    #for i in ['Open', 'High', 'Close', 'Low']:
        #df[i] = df[i].astype('float64')

    #fig = go.Figure([go.Scatter(x=df['Date'], y=df['High'])])
    #fig.update_xaxes(
        #rangeslider_visible=True,
        #rangeselector=dict(
            #buttons=list([
                #dict(count=1, label="1m", step="month", stepmode="backward"),
                #dict(count=6, label="6m", step="month", stepmode="backward"),
                #dict(count=1, label="YTD", step="year", stepmode="todate"),
                #dict(count=1, label="1y", step="year", stepmode="backward"),
                #dict(step="all")
            #])
        #)
    #)
    #fig.show()

