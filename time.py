import time
import datetime

# 透過 datetime
d = datetime.datetime.strptime('2010-11-16 20:10:58', '%Y-%m-%d %H:%M:%S')
time.mktime(d.timetuple()) + 1e-6 * d.microsecond
1289909458.0
# 透過 time tuple
time.mktime(time.strptime('2010-11-16 20:10:58', '%Y-%m-%d %H:%M:%S'))
#1289909458.0