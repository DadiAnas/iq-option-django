import asyncio

from django.shortcuts import render, redirect
from .api.trade import Trade
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django import forms

trade = None


# Create your views here.
def index(request):
    data = {}
    global trade
    if 'first_name' in request.session:
        data['first_name'] = request.session.get('first_name')
        data['last_name'] = request.session.get('last_name')
        try:
            data['current_balance'] = trade.option.get_balance()
            print(data['current_balance'])
            asyncio.create_task(trade.start(name="live-deal-binary-option-placed", active="NZDUSD", _type="turbo"))
            return render(request, "index.html", data)
        except Exception:
            return redirect('/iqlogin')
    else:
        return redirect('/iqlogin')


# Create your views here.
def iq_option_login(request):
    return render(request=request, template_name="iq_option/iqlogin.html")


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.Textarea)


@cache_page(60 * 15)
@csrf_protect
def login(request):
    c = {}
    if request.method == 'POST':  # 1
        # Create a form instance with the submitted data
        form = LoginForm(request.POST)  # 2
        # Validate the form
        if form.is_valid():  # 3
            # If the form is valid, perform some kind of
            request.session['first_name'] = 'Anas'
            request.session['last_name'] = 'DADI'
            global trade
            try:
                trade = Trade(email=form.data.get('email'), password=form.data.get('password'))
                return redirect('/', c)
            except:
                redirect('/iqlogin')
    return redirect('/iqlogin')
