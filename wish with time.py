import time
timestamp=time.strftime('%H:%M:%S')
#print("Now, the time is,",timestamp)
a=input("Enter your name:")
h=int(time.strftime('%H'))
#print("Time is in 24 hrs format,and the hour is ",h)
if(h>0 and h<12):
    print("Good Morning",a)
elif(h>12 and h<16):
    print("Good Afternoon",a)
elif (h>16 and h<20):
    print("Good Evening",a)
else:
    print("Good Night",a)
                        
