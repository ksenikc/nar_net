from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('statementes', views.statementes),
    path('<int:pk>/delete', views.StatementesDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/update', views.StatementesUpdateView.as_view(), name='task-update'),
]
