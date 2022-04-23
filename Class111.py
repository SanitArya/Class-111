from tracemalloc import Statistic
from turtle import pd


import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data], ["Maths Score"], show_hist=False)
# fig.show()

mean = statistics.mean(data)
std = statistics.stdev(data)

print("Mean of population: ", mean)
print("Standard deviation of population: ", std)


def RandomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean


meanList = []

for i in range(0, 1000):
    setOfMean = RandomSetOfMean(100)
    meanList.append(setOfMean)

mean1 = statistics.mean(meanList)
std1 = statistics.stdev(meanList)

print("Mean of sampling distribution: ", mean1)
print("Standard deviation of sampling distribution: ", std1)

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.20], mode="lines", name="Mean"))
# fig.show()

firstStdStart, firstStdEnd = mean1-std1, mean1+std1
secondStdStart, secondStdEnd = mean1-(2*std1), mean1+(2*std1)
thirdStdStart, thirdStdEnd = mean1-(3*std1), mean1+(3*std1)

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.2], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[firstStdStart, firstStdStart], y=[
              0, 0.20], mode="lines", name="STD 1 Start"))
fig.add_trace(go.Scatter(x=[firstStdEnd, firstStdEnd], y=[
              0, 0.20], mode="lines", name="STD 1 End"))

fig.add_trace(go.Scatter(x=[secondStdStart, secondStdStart], y=[
              0, 0.20], mode="lines", name="STD 2 Start"))
fig.add_trace(go.Scatter(x=[secondStdEnd, secondStdEnd], y=[
              0, 0.20], mode="lines", name="STD 2 End"))

fig.add_trace(go.Scatter(x=[thirdStdStart, thirdStdStart], y=[
              0, 0.20], mode="lines", name="STD 3 Start"))
fig.add_trace(go.Scatter(x=[thirdStdEnd, thirdStdEnd], y=[
              0, 0.20], mode="lines", name="STD 3 End"))

# fig.show()

df1 = pd.read_csv("data1.csv")
df2 = pd.read_csv("data2.csv")
df3 = pd.read_csv("data3.csv")

data1 = df["Math_score"].tolist()
data2 = df["Math_score"].tolist()
data3 = df["Math_score"].tolist()

mean01 = statistics.mean(data1)
print("Mean 01:", mean01)

mean02 = statistics.mean(data2)
print("Mean 02:", mean02)


mean03 = statistics.mean(data3)
print("Mean 03:", mean03)

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.2], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean01, mean01], y=[
              0, 0.2], mode="lines", name="Mean 01"))

# fig.show()

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.2], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean02, mean02], y=[
              0, 0.2], mode="lines", name="Mean 02"))

# fig.show()

fig = ff.create_distplot([meanList], ["Student Marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.2], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[mean03, mean03], y=[
              0, 0.2], mode="lines", name="Mean 03"))

fig.add_trace(go.Scatter(x=[secondStdStart, secondStdStart], y=[
              0, 0.20], mode="lines", name="STD 2 Start"))
fig.add_trace(go.Scatter(x=[secondStdEnd, secondStdEnd], y=[
              0, 0.20], mode="lines", name="STD 2 End"))

fig.add_trace(go.Scatter(x=[thirdStdStart, thirdStdStart], y=[
              0, 0.20], mode="lines", name="STD 3 Start"))
fig.add_trace(go.Scatter(x=[thirdStdEnd, thirdStdEnd], y=[
              0, 0.20], mode="lines", name="STD 3 End"))

fig.show()
