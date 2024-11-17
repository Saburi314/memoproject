from django.urls import path
from .views import MemoList,MemoDetail,MemoCreate,MemoDelete,MemoUpdate
from .views import signupfunc,loginfunc,logoutfunc

urlpatterns = [
    path('list', MemoList.as_view(), name='list'),
    path('detail/<int:pk>',MemoDetail.as_view(), name='detail'),
    path('create', MemoCreate.as_view(), name='create'),
    path('delete/<int:pk>', MemoDelete.as_view(), name='delete'),
    path('update/<int:pk>', MemoUpdate.as_view(), name='update'),
    path('signup/',signupfunc,name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
]

