total_second=int(input("Enter the total number of seconds: \n"))  
weeks=total_second//604800
# calculate remainig seconds after extracting weeks
remaining_seconds=total_second%604800
# calculate days for remaining seconds 
days=remaining_seconds//86400
# calculate remaining seconds_2 after extracting days 
remaining_seconds_2=remaining_seconds%86400
# calculate hours for remaining seconds_2
hours=remaining_seconds_2//3600
# calculate remaining seconds after extracting hours 
remaining_seconds_3=remaining_seconds_2%3600
# calculate minutes for remaining seconds_3
minutes=remaining_seconds_3//60
# calculate seconds_3 after extracting minutes
seconds=remaining_seconds_3%60
print(f"the totale time is {weeks} weeks, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")
