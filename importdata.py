import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from oursite.models import Covid
data_date = list()
data_country = list()
data_cases = list()
data_new_cases = list()
data_deaths = list()
data_new_deaths = list()
with open("world.txt","r",encoding='utf-8') as fp:
    txtfile = fp.readlines()
for d in txtfile:
    country,date,cases,new_cases= d.split(",")
    data_country.append(country)
    data_date.append(date)
    data_cases.append(cases)
    data_new_cases.append(new_cases)

for i in range(len(data_country)):
    t = Covid(country=data_country[i], date=data_date[i], cases=data_cases[i], new_cases=data_new_cases[i])
    t.save()
print('done')
