from datetime import datetime

start_date = datetime(2001,3,3)

time_now = datetime.now();

difference = (time_now - start_date)

print("seconds since march 3, 2001: " , "{:,.3f}".format(difference.total_seconds()) , "or", "{:,.3e}".format(difference.total_seconds()), "in a scientific notation")
print(time_now.strftime("%b %d %Y"))