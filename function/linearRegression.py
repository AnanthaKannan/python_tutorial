import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("../test.csv")
needToPredict = 62

x = data["x_axis"].values
y = data["y_axis"].values
x_mean = np.mean(x)
y_mean = np.mean(y)
# print(x_mean, y_mean)

length = len(x)

m_top = []
m_bot = []
for indx in range(length):
    m_top.append((x[indx] - x_mean) * (y[indx] - y_mean)) 
    m_bot.append(np.square((x[indx] - x_mean)))

m = np.sum(m_top) / np.sum(m_bot)

c = y_mean - (m * x_mean)
prediction = []
for indx in range(length):
    yp = (m * x[indx]) + c
    prediction.append(yp)

# print("prediction", prediction)


ans = (m * needToPredict) + c
accuracy =   np.square((np.sum(prediction) - y_mean)) /  np.square((np.sum(y) - y_mean))
print("prediciton" ,needToPredict  , "==>", ans)
print("accuracy", accuracy , " %")


# trend
plt.scatter(x, y, label= "stars", color= "green",   marker= "*", s=30) 
plt.plot(x, prediction, label = "line 2") 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Linear Regression') 
plt.legend() 
plt.show() 


