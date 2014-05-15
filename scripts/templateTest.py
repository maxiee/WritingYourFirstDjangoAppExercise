from django.conf import settings
from django import template
import datetime

settings.configure()
t = template.Template('My name is {{ name }}.')
c = template.Context({'name': 'Judy'})
print t.render(c)
c = template.Context({'name': "Maxiee"})
print t.render(c)

person = {'name': 'Maxiee', 'age': '24'}
t2 = template.Template('{{person.name}} is {{person.age}} years old.')
c2 = template.Context({'person': person})
print t2.render(c2)

d = datetime.date(1999,9,9)
t3 = template.Template('The month is {{date.month}} and the year is {{date.year}}.')
c3 = template.Context({'date':d})
print t3.render(c3)
