#!/usr/bin/env python
"""Post a Comment Method"""

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from myblog.models import UserMessage


@login_required
def add_post(request):
    """
    Method to add Messages in comment

    """
    try:
        if request.method == "POST":
            user_message = request.POST['user_message']
            if user_message:
                logged_user = request.user.username
                usr_msg = UserMessage(username=logged_user,
                                      text_message=user_message)
                usr_msg.save()
        return redirect("/myblog")

    except:
        return HttpResponseNotFound('<h1>Sorry, Page Not Found! </h1>')
