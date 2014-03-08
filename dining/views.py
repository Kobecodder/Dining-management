from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from dining.forms import MealForm, UserForm, MealadminForm, MealFilter, SearchForm
from dining.models import Meal, User, Member, Payment
import datetime
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models import Count
from django.contrib.auth.decorators import permission_required, login_required

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('diable account')
    else:
        return HttpResponse('invalid account')


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')




@login_required
def Personal_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.dining_user_id = request.user.id
            link.save()
            #form.save()
        return HttpResponseRedirect("/dining")
    else:
        form = MealForm()



    username = request.user
    #today = date.today()
    personal_meal = dict()

    personal_meal['total_breakfast'] = Meal.objects.filter(breakfast=True).filter(dining_user_id=username.id).count()
    personal_meal['total_lunch'] = Meal.objects.filter(lunch=True).filter(dining_user_id=username.id).count()
    personal_meal['total_dinner'] = Meal.objects.filter(dinner=True).filter(dining_user_id=username.id).count()

    personal_meal['todays_breakfast'] = Meal.objects.filter(order_on=date.today()).filter(breakfast=True).filter(dining_user_id=username.id).count()
    personal_meal['todays_lunch'] = Meal.objects.filter(order_on=date.today()).filter(lunch=True).filter(dining_user_id=username.id).count()
    personal_meal['todays_dinner'] = Meal.objects.filter(order_on=date.today()).filter(dinner=True).filter(dining_user_id=username.id).count()

    personal_meal['payable'] = Meal.objects.filter(breakfast=True).filter(dining_user_id=username.id).count() * 20 + Meal.objects.filter(lunch=True).filter(dining_user_id=username.id).count() * 30 + Meal.objects.filter(dinner=True).filter(dining_user_id=username.id).count() * 20
    payable = personal_meal['payable']
    payment = Payment.objects.filter(member_id=username.id).aggregate(Sum('monthly_payment'))
    for k, v in payment.items():
        member_payment = personal_meal['payment'] = v
        personal_meal['due'] = payable - member_payment

    return render_to_response('mymeal.html', {'form': form, 'username': username, 'personal_meal': personal_meal,}, context_instance=RequestContext(request))

@permission_required('is_superuser')
def admin_overview(request):
    if request.method == 'POST':
        form = MealadminForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/dining/adminview")
    else:
        form = MealadminForm()

    meal = Meal.objects.filter(order_on=datetime.date.today())
    breakfast =Meal.objects.filter(order_on=datetime.date.today()).filter(breakfast=True).count()
    lunch =Meal.objects.filter(order_on=datetime.date.today()).filter(lunch=True).count()
    dinner =Meal.objects.filter(order_on=datetime.date.today()).filter(dinner=True).count()
    #payable = Meal.objects.filter(breakfast=True).count() * 20 + Meal.objects.filter(lunch=True).count() * 30 + Meal.objects.filter(dinner=True).count() * 20

    names = User.objects.all()
    total = dict()
    for name in names:
        total[name] = dict()

        total[name]['todays_breakfast'] = Meal.objects.filter(order_on=datetime.date.today()).filter(breakfast=True).filter(dining_user_id=name.id).count()
        total[name]['todays_lunch'] = Meal.objects.filter(order_on=datetime.date.today()).filter(lunch=True).filter(dining_user_id=name.id).count()
        total[name]['todays_dinner'] = Meal.objects.filter(order_on=datetime.date.today()).filter(dinner=True).filter(dining_user_id=name.id).count()
        total[name]['breakfast'] = Meal.objects.filter(breakfast=True).filter(dining_user_id=name.id).count()
        total[name]['lunch'] = Meal.objects.filter(lunch=True).filter(dining_user_id=name.id).count()
        total[name]['dinner'] = Meal.objects.filter(dinner=True).filter(dining_user_id=name.id).count()
        total[name]['payable'] = Meal.objects.filter(breakfast=True).filter(dining_user_id=name.id).count() * 20 + Meal.objects.filter(lunch=True).filter(dining_user_id=name.id).count() * 30 + Meal.objects.filter(dinner=True).filter(dining_user_id=name.id).count() * 20
        payable = total[name]['payable']
        paid = Payment.objects.filter(member_id=name.id).aggregate(Sum('monthly_payment'))
        for k, v in paid.items():
            total[name]['Payment'] = v
            total[name]['due'] = payable - v

    return render_to_response('detail.html', {'meal': meal, 'breakfast': breakfast, 'lunch': lunch,
                                   'dinner': dinner, 'name': names, 'total':total, 'form':form , },
                                  context_instance=RequestContext(request))

@login_required
def meal_list(request):
    dat= request.GET
    print dat
    #for k,v in dat.items():
    #    print v[0]
    #    f =Meal.objects.filter(order_on=datetime.date(int(v))).filter(breakfast=True).filter(dining_user_id=request.user.id).count()
    #    print f
    #session = {}
    #mylist=[]
    #f=''
    #for k,v in dat.items():
    #
    #    d = str(v).split('-')
    #    for i in d:
    #        session['s'] = i
    #    #dat = session['d']
    #    #replace(v, '-', ',')
    #
    #
    #
    #    f = MealFilter(queryset=Meal.objects.filter(order_on=datetime.date(int(d[0]), int(d[1]), int(d[2]))).filter(breakfast=True).filter(dining_user_id=request.user.id).count())
    #    print type(f)
    #f = MealFilter(request.GET, queryset=Meal.objects.get().filter(breakfast=True).filter(dining_user_id=request.user.id).count())
    #f = MealFilter(request.GET, queryset=Meal.objects.all())


    form= SearchForm()
    f = MealFilter(request.GET, queryset=Meal.objects.filter().filter(dining_user_id=request.user.id).order_by('-order_on').reverse())
    for i in f:
        print i.dining_user_id
    print f


    return render_to_response('filter.html', {'filter': f, 'form':form}, context_instance=RequestContext(request))