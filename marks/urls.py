from django.urls import path
from . import views

urlpatterns = [
    path('marksheet/', views.marksheet_view, name='marksheet_view'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('', views.marksheet_view, name='marksheet_view'),
]