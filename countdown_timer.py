import time

def count_down(t):
    while t :
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end= "\r")
        time.sleep(1)
        t -= 1
    print("Timer Completed")

t = input("Enter time in Second : ")

count_down(int(t))
 
