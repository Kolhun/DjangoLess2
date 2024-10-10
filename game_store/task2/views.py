from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
from .forms import UserRegister


def index(request):
    return HttpResponse("<h2>Мой сайт task4</h2>")


def games_view(request):
    return render(request, 'four_task/games_base.html')


def bucket_view(request):
    return render(request, 'four_task/bucket_base.html')

existing_users = ['user1', 'admin', 'guest']


def sign_up_by_django(request):
    info = {}
    message = ''

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in existing_users:
                info['error'] = 'Пользователь уже существует'
            else:
                message = f"Приветствуем, {username}!"
                # Добавляем пользователя в список (для имитации регистрации)
                existing_users.append(username)
        else:
            # Обработка ошибок формы
            info['error'] = 'Некорректные данные формы'
    else:
        form = UserRegister()

    info['form'] = form
    if message:
        info['message'] = message
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()
        age = request.POST.get('age', '').strip()

        # Валидация данных
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
