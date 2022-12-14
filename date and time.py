#current time

import time
localtime=time.localtime(time.time())
print("local current time is ",localtime)



#current date

from datetime import time
from datetime import date
from datetime import datetime
today=date.today()
print("today date is ",today)



#yesterday

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
today=date.today()
yesterday=today -timedelta(days=1)
print("today is ",today)
print("yesterday is ",yesterday)



#tomorrow

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
today=date.today()
tomorrow=today + timedelta(days=1)
print("today is ",today)
print("tomorrow is ",tomorrow)



#date and time

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import datetime
today=date.today()
time=datetime.time()
print("today is ",today)
print("time is ",time)
print("date and time is ",today,time)


#factorial





def factorial():
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
x=int(input("enter number"))
print(x)
     

