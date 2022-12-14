from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Mission, SaveIp
from .models import Community
from .models import Pack, Pack_detail
from .models import Life, Life_detail, Mission_detail
from django.views.generic import FormView
from django.shortcuts import render, redirect, reverse
from . import forms
from django.views import View
from django.http import JsonResponse
from ipware import get_client_ip
from accounts.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader


def dog_main(request):
    return render(request, 'dog/dog_main.html', {})


def test(request):
    return render(request, 'dog/test.html', {})


class SignUpView(FormView):
    template_name = "dog/test.html"
    form_class = forms.UserCreationForm
    success_url = reverse_lazy("dog:finish")

    def form_valid(self, form): # π formμ μ λ¬λ°μμ΅λλ€.
        form.save()    # π formμ save() λ§€μλ μ€ν
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def signup_page(request):
    if request.method == "GET":
        template = loader.get_template('registration/signup.html')
        context = {}
        return HttpResponse(template.render(context, request))

    elif request.method == "POST":
        template = loader.get_template('registration/signup.html')
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        date_of_birth = request.POST.get('date_of_birth', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        gender = request.POST.get('gender', None)
        phone = request.POST.get('phone', None)
        pet_name = request.POST.get('pet_name', None)
        pet_gender = request.POST.get('pet_gender', None)
        pet_breed = request.POST.get('pet_breed', None)
        pet_weight = request.POST.get('pet_weight', None)
        pet_neuter = request.POST.get('pet_neuter', None)
        pet_date_of_birth = request.POST.get('pet_date_of_birth', None)

        context = {
            'email': email,
            'name': name,
            'date_of_birth': date_of_birth,
            'password1': password1,
            'password2': password2,
            'gender': gender,
            'phone': phone,
            'pet_name': pet_name,
            'pet_gender': pet_gender,
            'pet_breed': pet_breed,
            'pet_weight': pet_weight,
            'pet_neuter': pet_neuter,
            'pet_date_of_birth': pet_date_of_birth,
        }
        if email is None:
            context['error_message'] = 'email μλ ₯ν΄μ£ΌμΈμ.'
        elif name is None:
            context['error_message'] = 'name μλ ₯ν΄μ£ΌμΈμ.'
        elif date_of_birth is None:
            context['error_message'] = 'date_of_birth μλ ₯ν΄μ£ΌμΈμ.'
        elif password1 is None:
            context['error_message'] = 'password1 μλ ₯ν΄μ£ΌμΈμ.'
        elif password2 is None:
            context['error_message'] = 'password2 μλ ₯ν΄μ£ΌμΈμ.'
        elif gender is None:
            context['error_message'] = 'gender μλ ₯ν΄μ£ΌμΈμ.'
        elif phone is None:
            context['error_message'] = 'phone μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_name is None:
            context['error_message'] = 'pet_name μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_gender is None:
            context['error_message'] = 'pet_gender μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_breed is None:
            context['error_message'] = 'pet_breed μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_weight is None:
            context['error_message'] = 'pet_weight μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_neuter is None:
            context['error_message'] = 'pet_neuter μλ ₯ν΄μ£ΌμΈμ.'
        elif pet_date_of_birth is None:
            context['error_message'] = 'pet_date_of_birth μλ ₯ν΄μ£ΌμΈμ.'
        else:
            user = User.objects.create_user(
                email=email,
                name=name,
                date_of_birth=date_of_birth,
                password=password1,
                gender=gender,
                phone=phone,
                pet_name=pet_name,
                pet_gender=pet_gender,
                pet_breed=pet_breed,
                pet_weight=pet_weight,
                pet_neuter=pet_neuter,
                pet_date_of_birth=pet_date_of_birth,
            )

            if user is not None:
                return redirect('dog:dog_main')
            else:
                context['error_message'] = 'λ€μ νμΈ νμ'
        return HttpResponse(template.render(context, request))

    return render(request, 'registration/signup.html', {})


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
    user = User.objects.all()
    return render(request, 'dog/mypage.html', {'users': user})


# def signup_page(request):
#     return render(request, 'registration/signup.html', {})


def signup_pet(request):
    return render(request, 'registration/signup_pet.html', {})


def mission_page_list(request):
    return render(request, 'dog/misson_page_list.html', {})


def life_edu(request):
    life = Life.objects.all().order_by('id')
    return render(request, 'dog/life_edu.html', {'lifes': life})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)  # μ¬μ©μ μΈμ¦
            login(request, user)  # μ μ κ° μλμ§ μλμ§ μΆκ°
            return redirect('dog:login')
    else:
        form = UserCreationForm()
    return render(request, 'dog/test.html', {'form': form})


# def registerPage(request):
#     form = UserCreationForm()
#     #---------μΆκ°ν λ΄μ© μμ-------------
#     if request.method=="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     #---------μΆκ°ν λ΄μ© λ-------------
#     context = {'form': form}
#     return render(request, 'registration/signup.html', context)


# def user_signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             name = request.POST.get('name', None)
#             gender = request.POST.get('name', None)
#             raw_password = form.cleaned_data.get('password1')
#
#             user = authenticate(username=username, password=raw_password)  # μ¬μ©μ μΈμ¦
#             login(request, user)  # μ μ κ° μλμ§ μλμ§ μΆκ°
#             return redirect('dog:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


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
    return render(request, 'dog/community_click.html', {'communitys': community},)


def life_detail(request):
    life = Life.objects.all()
    return render(request, 'dog/life_detail.html', {'lifes': life})


def mission_detail(request):
    mission = Mission.objects.all()
    return render(request, 'dog/mission_detail.html', {'missions': mission})


def pack_detail(request):
    pack = Pack.objects.all()
    return render(request, 'dog/pack_detail.html', {'packs': pack})

##κ³΅μ§μ¬ν­
# blogμ κ²μκΈ(posting)μ λΆλ₯΄λ posting ν¨μ
def posting(request, pk):
    # κ²μκΈ(Post) μ€ pk(primary_key)λ₯Ό μ΄μ©ν΄ νλμ κ²μκΈ(post)λ₯Ό κ²μ
    community = Community.objects.get(id=pk)

    ip = get_client_ip(request)

    if not SaveIp.objects.filter(access_ip=ip, community_id=pk).exists():
        community.counting += 1
        community.save()

        SaveIp.objects.create(
            access_ip=ip,
            community_id=pk
        )
        # posting.html νμ΄μ§λ₯Ό μ΄ λ, μ°ΎμλΈ κ²μκΈ(post)μ postλΌλ μ΄λ¦μΌλ‘ κ°μ Έμ΄
    return render(request, 'dog/community_click.html', {'communitys': community})


def life_ip(request, pk):
    # κ²μκΈ(Post) μ€ pk(primary_key)λ₯Ό μ΄μ©ν΄ νλμ κ²μκΈ(post)λ₯Ό κ²μ
   # life = Life.objects.get(id=pk)

    ip = get_client_ip(request)

    if not Life_detail.objects.filter(access_ip=ip, life_id=pk).exists():
        Life_detail.objects.create(
            access_ip=ip,
            life_id=pk
        )
    life_details = Life_detail.objects.filter(life_id=pk)
        # posting.html νμ΄μ§λ₯Ό μ΄ λ, μ°ΎμλΈ κ²μκΈ(post)μ postλΌλ μ΄λ¦μΌλ‘ κ°μ Έμ΄
    return render(request, 'dog/life_detail.html', {'life_details': life_details})


def mission_ip(request, pk):
    # κ²μκΈ(Post) μ€ pk(primary_key)λ₯Ό μ΄μ©ν΄ νλμ κ²μκΈ(post)λ₯Ό κ²μ
   # life = Life.objects.get(id=pk)

    ip = get_client_ip(request)

    if not Mission_detail.objects.filter(access_ip=ip, mission_id=pk).exists():
        Mission_detail.objects.create(
            access_ip=ip,
            mission_id=pk
        )
    mission_details = Mission_detail.objects.filter(mission_id=pk)
        # posting.html νμ΄μ§λ₯Ό μ΄ λ, μ°ΎμλΈ κ²μκΈ(post)μ postλΌλ μ΄λ¦μΌλ‘ κ°μ Έμ΄
    return render(request, 'dog/mission_detail.html', {'mission_details': mission_details})


def package(request):
    pack = Pack.objects.all()
    return render(request, 'dog/package.html', {'pack': pack})


def pack_ip(request, pk):
    # κ²μκΈ(Post) μ€ pk(primary_key)λ₯Ό μ΄μ©ν΄ νλμ κ²μκΈ(post)λ₯Ό κ²μ

    ip = get_client_ip(request)

    if not Pack_detail.objects.filter(access_ip=ip, pack_id=pk).exists():
        Pack_detail.objects.create(
            access_ip=ip,
            pack_id=pk
        )
    pack_details = Pack_detail.objects.filter(pack_id=pk)

        # posting.html νμ΄μ§λ₯Ό μ΄ λ, μ°ΎμλΈ κ²μκΈ(post)μ postλΌλ μ΄λ¦μΌλ‘ κ°μ Έμ΄
    return render(request, 'dog/pack_detail.html', {'pack_details': pack_details},)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get(self, request):
 template = loader.get_template('dog/mypage.html')

 context = {
     'user': request.user
 }

 return HttpResponse(template.render(context, request))


