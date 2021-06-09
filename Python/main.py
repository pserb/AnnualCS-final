import matplotlib.pyplot as plt
import csv

def seventeen():
    streams = []

    with open('regional-global-weekly-2016-12-30--2017-01-06.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3].isdigit():
                streams.append(int(row[3]))
    data = []
    for i in range(1,51):
        data.append(25000000*((1-0.03)**i))
    x_data = list(range(1,51))
    plt.plot(x_data, data)
    
    plt.scatter(list(range(1,51)), streams[:50])
    plt.xticks(list(range(1,51)))
    plt.show()

seventeen()

def exponential():
    data = []
    for i in range(1,51):
        data.append(1000*((1-0.05)**i))
    x_data = list(range(1,51))
    plt.plot(x_data, data)
    plt.show()

#exponential()
