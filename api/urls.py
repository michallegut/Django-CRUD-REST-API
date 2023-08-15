from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllAdd),
    path('<int:id>', views.getByIdEditDelete),
]