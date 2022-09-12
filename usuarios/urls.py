
from django.urls import path
from usuarios.views import cadastro, login, valida_cadastro, valida_login, logout

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('valida_cadastro', valida_cadastro, name='valida_cadastro'),
    path('valida_login', valida_login, name='valida_login'),
    path('logout', logout, name='logout'),
]