from django.shortcuts import render,redirect
from .models import MemoModel
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.mixins import LoginRequiredMixin


class MemoList(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = MemoModel


class MemoDetail(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = MemoModel


class MemoCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = MemoModel
    fields = ('title', 'memo')
    #メモの項目は題名とメモ内容の2つということ
    success_url = reverse_lazy('list')
    #メモの新規作成が終わったらlist(一覧)を表示するように設定


class MemoDelete(LoginRequiredMixin, DeleteView):
    template_name='delete.html'
    model = MemoModel
    success_url = reverse_lazy('list')


class MemoUpdate(LoginRequiredMixin, UpdateView):
    template_name='update.html'
    model = MemoModel
    fields = ('title','memo')
    success_url = reverse_lazy('list')


def signupfunc(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.create_user(username,'',password)
            return redirect('login')
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザー名は既に使われています'})
    return render(request, 'signup.html', {})


def loginfunc(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return render(request,'login.html',{'error':'ユーザー名かパスワードが間違っています'})
    return render(request, 'login.html', {})


def logoutfunc(request):
    logout(request)
    return redirect('login')