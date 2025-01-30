from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.Home, name='home'),
    path('create/', views.CreateMemberView.as_view(), name='create'),
    path('', views.MemberListView.as_view(), name='home'),
    path('edit/<int:id>/', views.MemberUpdateView.as_view(), name='edit'),
    path('delete/<int:id>/', views.MemberDeleteView.as_view(), name='delete'),
]