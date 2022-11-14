from django.shortcuts import render
from django.http import HttpResponse
import random


users = []

def index(request):

    user_id = request.COOKIES.get('user_id')
    
    cookies = request.COOKIES

    for user in users:
        if user['user_id'] == int(user_id):
            user['count'] += 1
            print(user['count'])

    data = {'users':users, 'cookies':cookies}

    return render(request, 'index.html', data)


def set_cookie(request):
    
    user_id = request.COOKIES.get('user_id')

    if not user_id:
        count = 0

        new_user_id = random.randint(100,1000000)
        new_user_data = {'user_id':new_user_id, 'count':count}

        users.append(new_user_data)

        session = request.session

        response = render(request, 'index.html')
        response.set_cookie('user_id', new_user_id, httponly=False, max_age=10000)
        response.set_cookie('count', count, httponly=False, max_age=10000)

        return response

    else:
        return HttpResponse('Session is already active')
        