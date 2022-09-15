from accounts.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Mission, SaveIp
from .models import Community
from .models import Life
from django.views import View
from django.http import JsonResponse
from ipware import get_client_ip


def dog_main(request):
    return render(request, 'dog/dog_main.html', {})


def finish(request):
    return render(request, 'dog/finish.html', {})


def need_edu(request):
    return render(request, 'dog/need_edu.html', {})


def misson_choice(request):
    return render(request, 'dog/misson_choice.html', {})


def base(request):
    return render(request, 'dog/base.html', {})


def company(request):
    return render(request, 'dog/company.html', {})


def inquiry(request):
    return render(request, 'dog/ inquiry.html', {})


def mypage(request):
    return render(request, 'dog/mypage.html', {})


def signup_page(request):
    return render(request, 'registration/signup.html', {})


def signup_pet(request):
    return render(request, 'registration/signup_pet.html', {})


def mission_page_list(request):
    return render(request, 'dog/misson_page_list.html', {})


def life_edu(request):
    missions = Mission.objects.all()
    return render(request, 'dog/life_edu.html', {'missions': missions})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('dog:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})


def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'registration/misstion_list.html', {'missions': missions})


def mission_edu(request):
    missions = Mission.objects.all()
    return render(request, 'dog/mission_edu.html', {'missions': missions})


def community(request):
    community = Community.objects.all().order_by('id')
    return render(request, 'dog/community.html', {'communitys': community})


def community_click(request):
    community = Community.objects.all()
    return render(request, 'dog/community_click.html', {'communitys': community})


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
    return render(request, 'dog/community_click.html', {'communitys': community})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def life_edu(request):
    life = Life.objects.all()
    return render(request, 'dog/life_edu.html', {'lifes': life})
