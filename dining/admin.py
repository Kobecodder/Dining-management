__author__ = 'giash'

from django.contrib import admin
from dining.models import Member
from dining.models import Meal
from dining.models import Payment



admin.site.register(Member)
admin.site.register(Meal)
admin.site.register(Payment)



# class ContactAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'Title','blog']
#
# admin.site.register(Contact, ContactAdmin)
