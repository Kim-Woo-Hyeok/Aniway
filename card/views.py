from card.forms import UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Card


def card(request):
    return render(request, 'card/business_card.html', {})


def main(request):
    return render(request, 'card/hello_world.html', {})


def signup_page(request):
    return render(request, 'registration/signup.html', {})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('card:card')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})


def now(request):
    cards = Card.objects.all()
    return render(request, 'card/card_new.html', {'cards' : cards})


def card_new(request):
    return render(request, 'card/card_new.html')


def business(request):
    if (request.method == "POST"):
        card = Card()
        card.name = request.POST['name']
        card.content1 = request.POST['content1']
        card.content2 = request.POST['content2']
        card.business_name = request.POST['business_name']
        card.profile_img = request.FILES['profile_img']
        card.save()
        return redirect('card:now')













