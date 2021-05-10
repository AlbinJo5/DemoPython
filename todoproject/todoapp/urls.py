from . import views
from django.urls import path
urlpatterns = [
	path('',views.index,name='index'),
	path('delete/<int:id>/',views.delete,name='delete'),
	path('update/<int:id>/', views.update, name='update'),
	path('cbvindex/', views.TaskListview.as_view(), name='cbvindex'),
	path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
	path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
	path('cbvdelete/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdelete'),

]