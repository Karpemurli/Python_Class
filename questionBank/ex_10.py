
# 10.Write a program that prompts the user to input number of 
# calls and calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

calls=int(input('Enter the number of calls='))

if calls <= 100:
    calls=200
elif calls <= 150:
    calls=200+(calls-100)*0.60
elif calls <= 200:
    calls=200+50*0.60+(calls-150)*0.50
elif calls <= 300:
    calls=200+50*0.60+50*0.50+(calls-200)*0.40
else:
    calls='invalid'
print("The monthaly the telephone  bill is:Rs.",calls)

