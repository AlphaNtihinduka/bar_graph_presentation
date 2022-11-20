import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline

dataset = pd.read_csv("vehicle.csv")

# print(dataset)

vehicles=dataset["vehicleClass"]
year2020=dataset["2020"]
year2019=dataset["2019"]
year2018=dataset["2018"]
year2017=dataset["2017"]
year2016=dataset["2016"]
year2015=dataset["2015"]
year2014=dataset["2014"]
year2013=dataset["2013"]
year2012=dataset["2012"]
year2011=dataset["2011"]

x=np.arange(len(year2020))
x2=x
w=0.4
plt.bar(x,year2020,width=w)
x=x+w
plt.bar(x,year2019,width=w)
x=x+w
plt.bar(x,year2018,width=w)
x=x+w
plt.bar(x,year2017,width=w)
x=x+w
plt.bar(x,year2016,width=w)
x=x+w
plt.bar(x,year2015,width=w)
x=x+w
plt.bar(x,year2014,width=w)
x=x+w
plt.bar(x,year2013,width=w)
x=x+w
plt.bar(x,year2012,width=w)
x=x+w
plt.bar(x,year2011,width=w)
plt.xticks(x2+(w+(w/2)), vehicles)