import csv
import statistics
import plotly.express as px
import pandas as pd 
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data2.csv")
data = df["reading_time"].tolist()
fig = ff.create_displot([data], ["reading_time"], show_hist = False)
fig.show()

population_mean = statistics.mean(data)
print("Mean = ", population_mean)
population_stadndard_deviation = statistics.stdev(data)
print("Standard Deviation =", population_stadndard_deviation)

dataset = []
for i in range (0, 1000):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics = statistics.mean(dataset)
print("Mean of 1000 values", mean)
print("Standard deviation of 1000 values", standard_deviation)