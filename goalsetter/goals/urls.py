from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/create/', views.goal_create, name='goal_create'),
    path('goals/<int:goal_id>/', views.goal_detail, name='goal_detail'),
    path('goals/<int:goal_id>/json/', views.goal_detail_json, name='goal_detail_json'),
    path('goals/<int:goal_id>/update/', views.goal_update, name='goal_update'),
    path('goals/<int:goal_id>/delete/', views.goal_delete, name='goal_delete'),
]