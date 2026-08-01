#7 Day Temperature Tracker
# Takes temperature input from user for 7 days and shows a graph

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp_list = []

print("Enter temperature for 7 days:")

for i in range(7):
    t = float(input(days[i] + ": "))
    temp_list.append(t)

# calculate average, max, min
total = sum(temp_list)
avg = total / 7
highest = max(temp_list)
lowest = min(temp_list)

# which day was hottest and coldest
hot_day = days[temp_list.index(highest)]
cold_day = days[temp_list.index(lowest)]

# print the results
print("\n--- Weekly Report ---")
for i in range(7):
    print(days[i], "-", temp_list[i], "C")

print("\nAverage Temp:", round(avg, 1), "C")
print("Hottest Day:", hot_day, "with", highest, "C")
print("Coldest Day:", cold_day, "with", lowest, "C")

# plotting the graph
plt.plot(days, temp_list, marker='o', color='red')
plt.title("7 Day Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.show()
