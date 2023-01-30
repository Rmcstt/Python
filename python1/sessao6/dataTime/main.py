# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

# data = datetime(2022, 9, 20, 9, 22)
# print(data.strftime('%d/%m/%y %H:%M'))

# data = datetime.strptime('20/09/2022 09:22', '%d/%m/%Y %H:%M')
# pritn(data)

# print(data.timestamp())

# data = datetime.fromtimestamp(1663676520.0)
# print(data)


# strptime(str, int)
# .strftime('%d/%m/%Y %H:%M')
# .timestamp
# .fromtimestamp()

# data = datetime.strptime('18/12/1995 00:18:00', '%d/%m/%Y %H:%M:%S')

# # data = data + timedelta(days=1, hours=1, minutes=1 , seconds=1)
# data = data + timedelta(seconds=2*60*60)

# print(data.strftime('%d/%m/%Y %H:%M:%S'))  # 


d1 = datetime.strptime('18/12/1995 00:18:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('29/12/1995 00:18:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1

print(dif)  #  11 days, 0;00:00
print(dif.seconds)  # 0
print(dif.total_seconds())  # 950400.0
print(d1.time())  # 00:18:00