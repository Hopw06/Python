## Default Values - Beware! ##
from datetime import datetime

print(datetime.utcnow())

def delay(seconds):
    t = seconds * 100000000 // 3 # 10^8 take one second, but python slower than C so divide for 3. 
    for i in range(t):
        pass

def log(msg, *, dt=datetime.utcnow()):
    print('{0} : {1}'.format(dt, msg))

log("Hello")

log("Hello again", dt='2001-01-01 00:00:00')
delay(1)

log("Hello again")
delay(1)

log("Hello again")

# As you can see, the default for dt is calculated when the function is defined and is NOT re-evaluated when the function is called.

## Solution pattern ##

def log_1(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # check if dt is none, then set dt to datetime.utcnow()
    print('{0} : {1}'.format(dt, msg))

log_1("Hello")


log_1("Hello again", dt='2001-01-01 00:00:00')
delay(1)

log_1("Hello again")
delay(1)

log_1("Hello one again")