from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import os

REG_DISABLED = os.environ.get("DJANGO_REG_DISABLED", "False") == "True"


def register(request):
    if request.method == "POST":
        if REG_DISABLED:
            return HttpResponse(status=403)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}. You can now log in."
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request, "users/register.html", {"form": form, "reg_disabled": REG_DISABLED}
    )


@login_required
def profile(request):
    return render(request, "users/profile.html")
