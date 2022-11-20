import pandas as pd
import numpy as ny

dataset = pd.read_csv("vehicle.csv")

print(dataset.head())

std = ny.std(dataset)

print(std)

mean = ny.mean(dataset)

print(mean)


