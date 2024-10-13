from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
from .forms import BuyerForms
from .models import Buyer

existing_users = ['user1', 'admin', 'guest']


def index(request):
    byers = Buyer.objects.all()
    context = {
        "Buyer": byers,
    }
    return render(request, 'four_task/index.html', context)


def games_view(request):
    return render(request, 'four_task/games_base.html')


def bucket_view(request):
    return render(request, 'four_task/bucket_base.html')


def sign_up_by_django(request):
    info = {}
    message = ''

    if request.method == 'POST':
        form = BuyerForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # password = form.cleaned_data['password']
            # repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=name).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=name, age=age)
                message = f"Приветствуем, {name}!"
        else:
            info['error'] = 'Некорректные данные формы'
    else:
        form = BuyerForms()

    info['form'] = form
    byers = Buyer.objects.all()
    info['Buyer'] = byers
    if message:
        info['message'] = message
    return render(request, 'four_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()
        age = request.POST.get('age', '').strip()

        if not username or len(username) > 30:
            info['error'] = 'Некорректный логин'
        elif not password or len(password) < 8:
            info['error'] = 'Пароль должен содержать не менее 8 символов'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif not age.isdigit() or int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in existing_users:
            info['error'] = 'Пользователь уже существует'
        else:
            message = f"Приветствуем, {username}!"
            # Добавляем пользователя в список (для имитации регистрации)
            existing_users.append(username)
    return render(request, 'fifth_task/registration_page.html',
                  {'error': info.get('error', ''), 'message': message, 'form': UserRegister()})
