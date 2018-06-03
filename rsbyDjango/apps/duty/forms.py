# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/6/2-10:14'

from django import forms
from datetime import datetime

class ScheduleForm(forms.Form):
    id=forms.IntegerField()
    code=forms.CharField()
    uid=forms.IntegerField()
    did=forms.IntegerField()
    duid=forms.IntegerField()
    # dutydate=forms.DateField(default=datetime.now().date())
    dutydate = forms.DateField()