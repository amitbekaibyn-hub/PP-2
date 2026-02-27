#example 1
from datetime import datetime
now=datetime.now()
print(now)

#example 2
from datetime import datetime
date=datetime(2026,5,27)
print(date)

#example 3
from datetime import datetime, timedelta
today=date.now()
future =today + timedelta(days=7)
print(future)                        
#example 4
from datetime import datetime
d1=datetime(2026,1,11)
d2=datetime(2025,1,11)
difference=d2-d1    
print(difference.days)

#example 5
from datetime import datetime

now=datetime.now()
formatted=now.strftime("%d-%m-%Y")
print(formatted)
