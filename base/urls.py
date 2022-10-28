from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name='home'),
  path('', views.json_list),
  path('api/', views.json_list),

]