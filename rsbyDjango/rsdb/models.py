from django.db import models

# Create your models here.

class Person(object):
    def __init__(self,name,department,group,job):
        self.name=name
        self.department=department
        self.group=group
        self.job=job

