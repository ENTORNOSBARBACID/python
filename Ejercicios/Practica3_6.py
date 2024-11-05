def time(hour=0, minutes=0, seconds=0):
    if hour==0 & minutes==0 :
        hour=(int(seconds)//3600)
        minutes=((int(seconds)//60))-hour*60
        seconds=(int(seconds))-hour*3600-minutes*60
        return (hour, minutes, seconds)
    else:
        totalSec=(int(hour)*3600)+(int(minutes)*60)+seconds
        return totalSec
        

sec=int(3601)
hour=1
minutes=1
seconds=1

times=time(hour, minutes, seconds)
print(times)
h, m, s=time(seconds=sec)
print("Hour:" +str(h)+", Minutes: "+str(m)+", Seconds: "+str(s))