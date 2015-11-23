from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from collections import Counter
import numpy as np


def initialize(context):

    context.stocks = symbols('XLY',  # XLY Consumer Discrectionary SPDR Fund   
                           'XLF',  # XLF Financial SPDR Fund  
                           'XLK',  # XLK Technology SPDR Fund  
                           'XLE',  # XLE Energy SPDR Fund  
                           'XLV',  # XLV Health Care SPRD Fund  
                           'XLI',  # XLI Industrial SPDR Fund  
                           'XLP',  # XLP Consumer Staples SPDR Fund   
                           'XLB',  # XLB Materials SPDR Fund  
                           'XLU')  # XLU Utilities SPRD Fund
    
    context.historical_bars = 100
    context.feature_window = 10
    

   
# *** handle_data ***
# 
# This function is run once per instance of the data. So if we run the program on daily
# data then it is run once per day.
def handle_data(context, data):
    prices = history(bar_count = context.historical_bars, frequency='1d', field='price')

    for stock in context.stocks:
        try:
            # create moving averages for 50 and 200 days to filter the results that we want
            # to get out of the nueral network.
            ma1 = data[stock].mavg(50)
            ma2 = data[stock].mavg(200)

            start_bar = context.feature_window
            price_list = prices[stock].tolist()

            X = []
            y = []

            bar = start_bar

            # feature creation
            # this is where I build out the Neural Network that 
            # learns from the history of the stocks.
            while bar < len(price_list)-1:
                try:
                    end_price = price_list[bar+1]
                    begin_price = price_list[bar]

                    pricing_list = []
                    xx = 0
                    for _ in range(context.feature_window):
                        price = price_list[bar-(context.feature_window-xx)]
                        pricing_list.append(price)
                        xx += 1

                    features = np.around(np.diff(pricing_list) / pricing_list[:-1] * 100.0, 1)


                    # print(features)

                    if end_price > begin_price:
                        label = 1
                    else:
                        label = -1

                    bar += 1
                    X.append(features)
                    y.append(label)

                except Exception as e:
                    bar += 1
                    print(('feature creation',str(e)))




            clf1 = RandomForestClassifier()
            clf2 = LinearSVC()
            clf3 = NuSVC()
            clf4 = LogisticRegression()

            last_prices = price_list[-context.feature_window:]
            current_features = np.around(np.diff(last_prices) / last_prices[:-1] * 100.0, 1)

            X.append(current_features)
            X = preprocessing.scale(X)

            current_features = X[-1]
            X = X[:-1]

            clf1.fit(X,y)
            clf2.fit(X,y)
            clf3.fit(X,y)
            clf4.fit(X,y)

            p1 = clf1.predict(current_features)[0]
            p2 = clf2.predict(current_features)[0]
            p3 = clf3.predict(current_features)[0]
            p4 = clf4.predict(current_features)[0]
            
            
            if Counter([p1,p2,p3,p4]).most_common(1)[0][1] >= 4:
                p = Counter([p1,p2,p3,p4]).most_common(1)[0][0]
                
            else:
                p = 0
                
            print(('Prediction',p))


            if p == 1 and ma1 > ma2:
                order_target_percent(stock,0.33)
            elif p == -1 and ma1 < ma2:
                order_target_percent(stock,-0.33)      

        except Exception as e:
            print(str(e))
            
            
    record('ma1',ma1)
    record('ma2',ma2)
    record('Leverage',context.account.leverage)