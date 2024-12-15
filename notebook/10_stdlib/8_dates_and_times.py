# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
# datetime.date(2024, 12, 15)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '12-15-24. 15 Dec 2024 is a Sunday on the 15 day of December.'

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days
# 22052

