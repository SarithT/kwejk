from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='signin.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view()),
    path('annoucments/', views.annoucments, name='annoucments'),
    path('add-image/', views.add_image, name='add-image'),
    path('kwejk/<int:siteNumber>', views.kwejk, name='kwejk'),
    path('', views.main, name='main'),
    path('gif-monitor/', views.gif_monitor, name='gif_monitor'),
    path('gif-monitor2/', views.gif_monitor2, name='gif_monitor2'),
    path('push-to-gif-monitor/<int:pk>', views.push_to_gif_monitor, name='push_to_gif_monitor'),
    path('push-to-gif-monitor2/<int:pk>', views.push_to_gif_monitor2, name='push_to_gif_monitor2'),
    path('delete_image/<int:pk>', views.delete_image, name='delete_image'),
]