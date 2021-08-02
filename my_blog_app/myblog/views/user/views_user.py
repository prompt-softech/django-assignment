#!/usr/bin/env python
"""User Related Functionality."""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from myblog.models import UserMessage


def index(request):
    """
    Index Page

    """
    try:
        ustatus = {}
        ustatus['loginstatus'] = False
        ustatus['user_comment'] = UserMessage.objects.all().order_by(
            '-time_added')

        if request.user.is_authenticated:
            ustatus['loginstatus'] = True
            ustatus['uname'] = request.user.username

        return render(request, 'myblog/index.html', ustatus)

    except Exception as error_not_found:
        raise Http404('<h1>Sorry, Page Not Found! </h1>') from error_not_found


def login_user(request):
    """
    User Login

    """
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if username not in ['', None] and password not in ['', None]:
                gusername = authenticate(username=username, password=password)

                if gusername:
                    login(request, gusername)

                    if not request.POST.get('remember_me', None):
                        request.session.set_expiry(0)

                    return redirect("/myblog")
                else:
                    return redirect("/myblog?error=Invalid+Credentials")

    except Exception as error_not_found:
        raise Http404('<h1>Sorry, Page Not Found! </h1>') from error_not_found


def logout_user(request):
    """
    User Logout

    """

    try:
        logout(request)
    except Exception as error_not_found:
        raise Http404('<h1>Sorry, Page Not Found! </h1>') from error_not_found
    return redirect("/myblog")


def user_signup(request):
    """
    Signup User

    """
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if username not in ['', None] and password not in ['', None]:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                login(request, user)
            return redirect("/myblog")
    except Exception as error_not_found:
        raise Http404('<h1>Sorry, Page Not Found! </h1>') from error_not_found
