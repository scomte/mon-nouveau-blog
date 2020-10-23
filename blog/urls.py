from django.urls import path
from . import views
from blog.views import ActivateAccount, SignUpView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/',
         ActivateAccount.as_view(),
         name='activate'),
]
