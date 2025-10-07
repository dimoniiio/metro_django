from django.shortcuts import render
from users.models import User


def home(request):
    # Берём первого пользователя (или можно передать ID через параметр)
    user = User.objects.first()  # или .get(id=1), если хотите конкретного
    if not user:
        user = User(full_name="Нет пользователей", email="—", address="—")
    return render(request, 'home.html', {'user': user})


def post_list(request):
    return render(request, 'posts/list.html')


def user_list(request):
    return render(request, 'users/list.html')
