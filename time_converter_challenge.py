#challenge 
total_seconds = int(input("Enter the total number of seconds: \n"))
print(f"the total time is {total_seconds//3600} hours, {(total_seconds%3600)//60} minutes and {total_seconds%60} seconds")

#challenge 2
total_seconds=int(input("Enter the total number of seconds: \n"))
hours=total_seconds//3600
minutes = (total_seconds%3600)//60
seconds=total_seconds - (hours*3600+minutes*60)
print(f"the total_time is {hours} hours, {minutes} minutes and {seconds} seconds")