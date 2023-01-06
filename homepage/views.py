from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from .models import Community
import datetime
from .models import SaveIp
from django.views import View
from django.http import JsonResponse
from ipware import get_client_ip
from django.core.paginator import Paginator
from accounts.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from django.contrib import auth


def homepage(request):
    return render(request, 'homepage/main_page.html')


def business(request):
    return render(request, 'homepage/intro_business.html')


def business_network(request):
    return render(request, 'homepage/business_network.html')


def service_center(request):
    return render(request, 'homepage/service_center.html')


# def login_page(request):
#     return render(request, 'registration/login.html')

#
# def signup(request):
#     return render(request, 'homepage/signup.html')


def infopage(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Community.objects.order_by('id')
    paginator = Paginator(question_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'homepage/infopage_html.html', context)


def infopage_click(request):
    community = Community.objects.all()
    return render(request, 'homepage/infopage_click.html', {'communitys': community},)


##공지사항
# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):

    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    community = Community.objects.get(id=pk)

    ip = get_client_ip(request)

    if not SaveIp.objects.filter(access_ip=ip, community_id=pk).exists():
        community.counting += 1
        community.save()

        SaveIp.objects.create(
            access_ip=ip,
            community_id=pk
        )
        # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'homepage/infopage_click.html', {'communitys': community})


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=email, password=raw_password)  # 사용자 인증
#             login(request, user)  # 유저가 있는지 없는지 추가
#             return redirect('homepage:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == "GET":
        template = loader.get_template('homepage/signup.html')
        context = {}
        return HttpResponse(template.render(context, request))

    elif request.method == "POST":
        template = loader.get_template('homepage/signup.html')
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        university = request.POST.get('university', None)
        department = request.POST.get('department', None)
        date_of_birth = request.POST.get('date_of_birth', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        gender = request.POST.get('gender', None)
        phone = request.POST.get('phone', None)

        context = {
            'email': email,
            'name': name,
            'university': university,
            'department': department,
            'date_of_birth': date_of_birth,
            'password1': password1,
            'password2': password2,
            'gender': gender,
            'phone': phone,
        }
        if email is None:
            context['error_message'] = 'email 입력해주세요.'
        elif name is None:
            context['error_message'] = 'name 입력해주세요.'
        elif university is None:
            context['error_message'] = 'university 입력해주세요.'
        elif department is None:
            context['error_message'] = 'department 입력해주세요.'
        elif date_of_birth is None:
            context['error_message'] = 'date_of_birth 입력해주세요.'
        elif password1 is None:
            context['error_message'] = 'password1 입력해주세요.'
        elif password2 is None:
            context['error_message'] = 'password2 입력해주세요.'
        elif gender is None:
            context['error_message'] = 'gender 입력해주세요.'
        elif phone is None:
            context['error_message'] = 'phone 입력해주세요.'
        else:
            user = User.objects.create_user(
                email=email,
                name=name,
                university=university,
                department=department,
                date_of_birth=date_of_birth,
                password=password1,
                gender=gender,
                phone=phone,
            )

            if user is not None:
                return redirect('homepage:homepage')
            else:
                context['error_message'] = '다시 확인 필요'
        return HttpResponse(template.render(context, request))

    return render(request, 'homepage/signup.html', {})


def test(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'homepage/test.html')
    return render(request, 'homepage/test.html')