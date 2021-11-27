from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForms
from .test import analytic
#from .test.analytic import Analytic


def index(request):
    if request.method=="POST":
        ticker = request.POST.get("ticker")
        rez1 = analytic.Analytic.info1(ticker)
        rez2 = analytic.Analytic.info2(ticker)
        rez3 = analytic.Analytic.info3(ticker)
        rez4 = analytic.Analytic.info4(ticker)
        rez5 = analytic.Analytic.info5(ticker)
        rez6 = analytic.Analytic.info6(ticker)
        rez7 = analytic.Analytic.info7(ticker)
        rez8 = analytic.Analytic.prediction(ticker)
        output="<h2>Название организации: {0}</h2>" \
               "<h2>Описание эмитента: {1}</h2>" \
               "<h2>Страна: {2}</h2>" \
               "<h2>Индустрия: {3}</h2>" \
               "<h2>Сфера деятельности: {4}</h2>" \
               "<h2>Стоимость акции на момент последнего закрытия рынка: {5}</h2>" \
               "<h2>Цена акции на данный момент: {6}</h2>" \
               "<h2>{7}</h2>".format(rez3, rez1, rez6, rez7, rez5, rez4, rez2, rez8)
        return HttpResponse(output)
    else:
        userform=UserForms
        return render(request, 'index.html', {'form': userform})

# Create your views here.
