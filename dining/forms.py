__author__ = 'geash'
from django.forms import ModelForm
from models import Meal, User
from django import forms
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django_filters.widgets import LinkWidget
import datetime
import django_filters


class MealForm(ModelForm):
    day = datetime.date.today()
    order_on = forms.DateTimeField(widget=SelectDateWidget(years=range(2014, 2020)), initial=day)

    class Meta:
        model = Meal
        fields = ('breakfast', 'lunch', 'dinner', 'order_on')


class UserForm(ModelForm):
    class Meta:
        model = User


class MealadminForm(ModelForm):
    day = datetime.date.today()
    order_on = forms.DateTimeField(widget=SelectDateWidget(years=range(2014, 2020)), initial=day)
    class Meta:
        model = Meal
        fields = ('dining_user', 'breakfast', 'lunch', 'dinner', 'order_on', )

#    breakfast = forms.BooleanField(required=False)
#    lunch = forms.BooleanField(required=False)
#    dinner = forms.BooleanField(required=False)
#    #order_on = forms.DateTimeField()


class MealFilter(django_filters.FilterSet):
    day = datetime.date.today()
    order_on = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Meal
        fields = ['order_on']


class SearchForm(forms.Form):
    day = datetime.date.today()
    searh = forms.DateTimeField(widget=SelectDateWidget(years=range(2014, 2020)), initial=day)

