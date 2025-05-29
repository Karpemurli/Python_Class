# # Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
# # Expected Output:

# # Input the month (e.g. January, February etc.): july                     
# # Input the day: 31                                                       
# # Season is autumn


Month=input('Enter the month=').capitalize()
Day =int(input('Enter the day='))

if Month in ('Jan', 'Feb', 'Mar'):
    season='Winter'
elif Month in ('Apr','May','Jun'):
    season='Spring'
elif Month in ('Jul','Aug','Sep'):
    season='Summer'
elif Month in ('Oct','Nov','Dec'):
    season='Autumn'
else:
   season='Invalid Month'
    
    
if Month == 'Mar' and Day > 20:
   season='Spring'
elif Month == 'Jun' and Day > 20:
    season='Summer'
elif Month == 'Sep' and Day > 20:
   season='Autumn'
elif Month == 'Dec' and Day > 20:
    season='Winter'
    
print('season=',season)
    