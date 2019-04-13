import matplotlib.pyplot as plt 
#sudo apt-get install python3-tk   ==> if you get the error. just run the command

x = [1,2,3,4,5,6,7,8] 
y = [2,4,5,7,6,8,9,11] 
x2 = [1,2,3,4,5,6,7,8] 
y2 = [5,6,5,7,4,8,1,9] 

plt.scatter(x, y, label= "stars", color= "green",   marker= "*", s=30) 
plt.plot(x2, y2, label = "line 2") 

plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('My scatter plot!') 
plt.legend() 

plt.show() 