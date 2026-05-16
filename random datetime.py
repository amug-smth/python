from datetime import datetime, timedelta
import random
start= datetime(2020,1,1)
end= datetime(2024,1,1)
bwtime= end - start
totalsec=int(bwtime.total_seconds())
randosec= random.randint(0,totalsec)
randodate= start + timedelta(seconds=randosec)
print(randodate.strftime("%Y-%m-%d %H:%M:%S"))