from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('task-create/',views.taskCreate,name="taskCreate"),
    path('task-list/',views.taskList,name="taskList"),
    path('task-detail/<str:pk>',views.taskDetail,name="taskDetail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
