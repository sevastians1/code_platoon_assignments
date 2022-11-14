from django.shortcuts import render
from django.http import HttpResponse
import random


users = {}

def index(request):

    user_id = request.COOKIES.get('user_id')
    
    cookies = request.COOKIES

    count = users.get(int(user_id))
    print(count)

    if count is not None:
        print('works')
        users[int(user_id)] += 1

    data = {'users':users, 'cookies':cookies}

    return render(request, 'index.html', data)


def set_cookie(request):
    
    user_id = request.COOKIES.get('user_id')

    if not user_id:
        count = 0

        new_user_id = random.randint(100,1000000)
        users[new_user_id] = count

        session = request.session

        response = render(request, 'index.html')
        response.set_cookie('user_id', new_user_id, httponly=False, max_age=10000)
        response.set_cookie('count', count, httponly=False, max_age=10000)

        return response

    else:
        return HttpResponse('Session is already active')
        