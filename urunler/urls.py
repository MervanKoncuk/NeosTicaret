from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", index, name="index"),
    path("kategori/<int:id>", filter, name="filter"),
    path('create/', create, name='create'),
    path('sepet/', sepet, name='sepet'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name="sifredegis.html"), name='password_change_done'),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


# from django.contrib.auth import views as auth_views
# path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),

#     path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
#     path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),