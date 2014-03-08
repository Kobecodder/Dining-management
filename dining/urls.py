from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
     url (r'^$', views.Personal_meal, name='index'),
     #url (r'^(?P<user>\d+)/$', views.Personal_meal, name='admin'),
     url (r'^adminview/$', views.admin_overview, name='adminmeal'),
     url(r'^list$', views.meal_list, name='search')

)






