import get_data
import matplotlib.pyplot as plt

# first of all we want to get the date of total 
# commit, and make a chart for it

date_count = get_data.get_log("date_log.csv")#use get method to get the data
count = list(date_count.values())
date = list(date_count.keys())
print(count)
plt.figure(figsize=(1000000000000,10)) # a bigger chart
plt.xlabel('date') # x-axis presents the months of commit
plt.ylabel('commit_number') # y-axis presents how many commit in one month.
plt.plot(date, count) # paint the line chart
plt.show()
