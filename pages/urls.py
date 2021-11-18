from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # url names for pages
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    # Forget Password
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='pages/password_reset_form.html',
             subject_template_name='pages/password_reset_subject.txt',
             html_email_template_name='pages/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='pages/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='pages/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='pages/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]