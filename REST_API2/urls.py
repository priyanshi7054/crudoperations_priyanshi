from django.urls import path
from .views import employeesViews

urlpatterns = [
    path('employees/', employeesViews.as_view()),
    path('employees/<int:id>', employeesViews.as_view())
]
