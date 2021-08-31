from django.views.generic import View
import subprocess
from past.builtins import execfile

# from . import cons
# from .cons import fig
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
import pandas as pd
import plotly.express as px
import time
import datetime
from datetime import datetime
from .forms import PostForm

def index(request):
    if request.method == 'POST':
        ticker = 'UAH=X'
        period1 = request.POST.get("period1")
        utc_time = (time.mktime(datetime.strptime(period1, '%d-%m-%Y').timetuple()))
        inf = int(utc_time)
        period2 = request.POST.get("period2")
        utc_time_2 = (time.mktime(datetime.strptime(period2, '%d-%m-%Y').timetuple()))
        ind = int(utc_time_2)
        interval = '1d'
        url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={inf}&period2={ind}&interval={interval}&events=history&includeAdjustedClose=true'
        df = pd.read_csv(url)
        fig = px.line(df, x='Date', y='Close', title='Apple Share Prices over time (2014)')
        fig.show()



    else:
        return render(request, "create.html", {})

