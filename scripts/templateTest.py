from django.conf import settings
from django import template

settings.configure()
t = template.Template('My name is {{ name }}.')
c = template.Context({'name': 'Judy'})
print t.render(c)
c = template.Context({'name': "Maxiee"})
print t.render(c)
