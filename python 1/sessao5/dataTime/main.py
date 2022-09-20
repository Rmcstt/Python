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

data = datetime.strptime('18/12/1995 00:18:00', '%d/%m/%Y %H:%M:%S')

data = data + timedelta(days=1, hours=1, minutes=1 , seconds=1)

print(data.strftime('%d/%m/%Y %H:%M:%S'))


