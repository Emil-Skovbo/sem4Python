# 1 Look at the activation_function and plot the y-values for each x from -5,5 spaced with 0.5

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def activation_function(x):
    """
    Step function to respond with y = 1 or -1
    Parameter:
    x: An x (numeric) value that will have a corresponding y value of 1 or -1
    """
    if x < 0:
        return -1
    else:
        return 1
rnge = np.linspace(-5.5, 10.0, num=100)
print(rnge[0:5])
values = [activation_function(i) for i in rnge] 
#plt.plot(rnge, values)
#plt.axis([-5.5, -5, -4.5, -4])
#plt.show()
print(activation_function(0))
#2 Change the perceptron method from the notebook to use the numpy.dot() method in line 12 instead of the lengthy sum() function
def perceptron(inp, weights):
    """
    Given a list of input (x) values and a list of weights, 
    calculates the dot product of the 2 lists and returns 1 or -1 (fire or don't)
    Parameters:
    inp: vector of input predictors
    weights: vector of weights to be ajusted for precise prediction of output.
    """
    # This is the same as the dot product np.dot(i, w)
    dot_product = np.dot(inp,weights)
    output = activation_function(dot_product)
    return output


print(perceptron([1, 2, 3, 4, 5], [1, 1, 2, 1, 1]))
#part 2
# 1 Make a new scatter plot with datapoints of weights vs heights. Choose different colors for rats and mice
import pandas as pd
import perceptron as pc
rodent = pd.read_csv("rodents.csv", sep= ';')
rodent = rodent.dropna()
rodent["type"] = rodent["type"].apply(lambda x: 1 if str(x).strip() == "rat" else -1)
#print(rodent)
rodent_np = rodent.to_numpy()
rodent_fmt = [(data[:2],data[2])for data in rodent_np]
weights = pc.pla(rodent_fmt)
#print(weights)
colors = "rb"
for target, name in (zip([1,-1],["rat","mouse"])):
    #print(idx)
    data = rodent[rodent["type"]==target]
    color_idx = target if target ==1 else 0
    plt.scatter(data["weight"],data["height"] ,c=colors[color_idx], label=name) #

plt.title("mesures for mice and rats")
plt.xlabel("weight")
plt.ylabel("height")
plt.legend()
plt.show()

X = rodent.values[1:, 0:1] 
y = rodent.values[1:, 1:2] 
i = []
for a in X:
    i.append(a[0])

j = []
for a in y:
    j.append(a[0])

#print(rodent)
#print(i)
plt.plot(i,j)
plt.axis([255.5, -255, 44.5, -44-5])
#plt.show()


