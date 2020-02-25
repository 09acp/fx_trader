import pandas as pd 
import numpy as np 
import plotly.graph_objects as go




def adx(df_ta):
    trace0 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['ADX'],
                        #color='red',
                        mode = "lines+markers",
                        marker = dict(size=2),
                        name = 'ADX',
                        line = dict(shape = "spline",
                                    color = "rgb(0,0,0)",
                                    width = 1,
                                    dash = "dot"
                                   ),
                        connectgaps = True  
                       )

    data = [ trace0]
    # layout = {"xaxis" : {"zeroline": False}}    

    layout=  go.Layout( 
             title = "<b>ADX (Trend Indicator)</b>", 
             title_x=0.5,
             height = 530,  #1500,
             #width = 750,  #1500,    <----- Screws with layout 
             paper_bgcolor = "rgb(230, 230, 230)", # background colour outside plot  
             plot_bgcolor = "rgb(212, 226, 240)" ,   # in plot colour
             yaxis = dict(title ="Closing Price" ),
             xaxis = dict(title ="Historical Window: 100 Days" ),
    )     
    
    
    # TO MAKE IT WORK IN JUPYTER
    fig = go.Figure(  {"data":data,
            "layout":layout}  )   
    # ADD HORIZONTAL LINES
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=20,
                x1=df_ta['Date'].max(),
                y1=20,
                line=dict(
                    color="green",
                    width=1,
                ),
        )
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=50,
                x1=df_ta['Date'].max(),
                y1=50,
                line=dict(
                    color="red",
                    width=1,
                ),
        )

    # Create scatter trace of text labels
    fig.add_trace(go.Scatter(
        name = 'Labels',
        x=[df_ta['Date'][10] , df_ta['Date'][10] ],
        y=[52, 18],
        text=["Overbought",
              "Oversold"],
        mode="text",
    ))
    return fig

def macd(df_ta):
    trace0 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['MACD_Line'],
                        name ="EMA",
                        mode = "lines+markers",
                        marker = dict(size=2),
                        line = dict(shape = "spline",
                                    color = "red",
                                    width = 1,
                                    dash = "dot",
                                   ),
                        connectgaps = True  )
    trace1 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['MACD_Signal'],
                        name ="Signal Line",
                        mode = "lines+markers",
                        marker = dict(size=2),
                        line = dict(shape = "spline",
                                    color = "blue",
                                    width = 1,
                                    dash = "dot",
                                   ),
                        connectgaps = True  )
    trace2 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['MACD_Histogram'],
                        name ="Histogram",
                        mode = "lines+markers",
                        marker = dict(size=2),
                        fill = "tozeroy",
                        line = dict(shape = "spline",
                                    color = "rgb(98, 128, 97)",  #"rgb(190,230,180)",
                                    width = 2,
                                    #dash = "dash"
                                   ),
                        connectgaps = True  )


    data = [ trace0, trace1, trace2 ]
    #layout = {"xaxis" : {"zeroline": False}}    
    layout=  go.Layout( 
             title = "<b>MACD (Trend Indicator)</b>",
             title_x=0.5,
             height = 530,  #1500,
             #width = 900,  #1500,    <----- Screws with layout 
             paper_bgcolor = "rgb(230, 230, 230)", # background colour outside plot  
             plot_bgcolor = "rgb(212, 226, 240)" ,   # in plot colour
             yaxis = dict(title ="Closing Price" ),
             xaxis = dict(title ="Historical Window: 100 Days" ),
    )      

    # TO MAKE IT WORK IN JUPYTER
    fig = go.Figure(  {"data":data,
            "layout":layout}  ) 
        
    # ADD HORIZONTAL LINE
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=0,
                x1=df_ta['Date'].max(),
                y1=0,
                line=dict(
                    color="black",
                    width=1,
                    #dash="dash",

                ),
        )
    return fig

    
def rsi(df_ta):
    trace0 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['RSI'],
                        name='RSI',
                        mode = "lines+markers",
                        marker = dict(size=2),
                        line = dict(shape = "spline",
                                    color = "rgb(0,0,0)",
                                    width = 2,
                                    dash = "dot"
                                   ),
                        connectgaps = True  )

    data = [ trace0 ]
    layout=  go.Layout( 
             title = "<b>RSI (Momentum Indicator)</b>",
             title_x=0.5,
             height = 530,  #1500,
             #width = 750,  #1500,    <----- Screws with layout 
             paper_bgcolor = "rgb(230, 230, 230)", # background colour outside plot  
             plot_bgcolor = "rgb(212, 226, 240)" ,   # in plot colour
             yaxis = dict(title ="Closing Price" ),
             xaxis = dict(title ="Historical Window: 100 Days" ),
    )    

    # TO MAKE IT WORK IN JUPYTER
    fig = go.Figure(  {"data":data,
            "layout":layout}  )   
    # ADD HORIZONTAL LINE
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=50,
                x1=df_ta['Date'].max(),
                y1=50,
                line=dict(
                    color="rgb(150,150,150)",
                    width=1,
                    dash="dash",
                ),
        )
    # ADD HORIZONTAL LINES
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=70,
                x1=df_ta['Date'].max(),
                y1=70,
                line=dict(
                    color= "red",  #"rgb(250,150,150)",
                    width=1,
                    #dash="dash",
                ),
        )
    fig.add_shape(
                type="line",
                x0=df_ta['Date'].min(),
                y0=30,
                x1=df_ta['Date'].max(),
                y1=30,
                line=dict(
                    color= "green", #"rgb(130,220,130)",
                    width=1,
                    #dash="dash",
                ),
        )

    # Create scatter trace of text labels
    fig.add_trace(go.Scatter(
        name = 'Labels',
        x=[df_ta['Date'][10] , df_ta['Date'][10],df_ta['Date'][10] ],
        y=[52, 73, 28],
        text=["Trend Formation",
              "Overbought",
              "Oversold"],
        mode="text",
    ))
    
    return fig    
 
    
def candles_bollingerb (df_ta,df_raw_prices):
    # High
    trace0 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['BollingerB_High'],
                        name="BB High",
                        mode = "lines+markers",
                        marker = dict(size=1),
                        line = dict(shape = "spline",
                                    color = "rgb(0,0,0)", #color = "rgb(100,180,100)",
                                    width = 1,
                                    dash = "dot"
                                   ),
                        connectgaps = True  )
    # LOW
    trace1 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['BollingerB_Low'],
                        name="BB Low",
                        mode = "lines+markers",
                        marker = dict(size=1),
                        line = dict(shape = "spline",
                                    color = "rgb(0,0,0)", #color = "rgb(180,0,0)",
                                    width = 1,
                                    dash = "dot"
                                   ),
                        connectgaps = True  )

    # MIDDLE
    trace2 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['BollingerB_Middle'],
                        name="BB Middle",
                        mode = "lines+markers",
                        marker = dict(size=1),
                        line = dict(shape = "spline",
                                    color = "rgb(0,0,200)",
                                    width = 1,
                                    dash = "dash"
                                   ),
                        connectgaps = True  )

    # CANDLES
    trace3 = go.Candlestick(x=df_ta['Date'],
                            name="Closing Price",
                            open=df_raw_prices['Open'],
                            high=df_raw_prices['High'],
                            low=df_raw_prices['Low'],
                            close=df_raw_prices['Price'] )
    # FILLER
    trace4 = go.Scatter(x=df_ta['Date'],
                        y=df_ta['BollingerB_Low'],
                        name="Click to remove Fill",
                        mode = "lines+markers",
                        marker = dict(size=1),
                        fill = "tonexty",
                        opacity = 0, 
                        line = dict(shape = "spline",
                                    color = "rgb(190,230,180)"))
    data=[trace0 , trace4 , trace1 , trace2, trace3 ]
    layout=  go.Layout( 
             title = "<b>Candle Plot with Bollinger Bands (Volatility)</b>",
             title_x=0.5,
             height = 530,  #1500,
             #width = 900,  #1500,    <----- Screws with layout 
             paper_bgcolor = "rgb(230, 230, 230)", # background colour outside plot  
             plot_bgcolor = "rgb(212, 226, 240)" ,   # in plot colour
             yaxis = dict(title ="Closing Price" ),
             xaxis = dict(title ="Historical Window: 100 Days" ),
             xaxis_rangeslider_visible=False,
    )    
    fig =         (  {"data":data,
                      "layout":layout
                      }  ) 
#     fig.update_layout(xaxis_rangeslider_visible=False) # remove range finder
    
    return fig    
    
    
   