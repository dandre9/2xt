from django.urls import path
from cotacao import views

app_name = 'cotacao'

urlpatterns = [
    # /cotacao/
    path('', views.home, name='home'),

    path('opcoes/', views.opcoes, name='opcoes'),

    path('compra/', views.compra, name='compra'),

]
