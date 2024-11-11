def timeInSeconds(hours, minutes, seconds):
    totalSec=(int(hours)*3600)+(int(minutes)*60)+seconds
    return totalSec

def timeInHour(seconds):
    hour=(int(seconds)//3600)
    minutes=((int(seconds)//60))-hour*60
    seconds=(int(seconds))-hour*3600-minutes*60
    return(hour, minutes, seconds)
    
sec=3601
hour=1
minutes=1
seconds=1

time=timeInSeconds(hour, minutes, seconds)
print(time)
h, m, s=timeInHour(sec)
print("Hour:" +str(h)+", Minutes: "+str(m)+", Seconds: "+str(s))
