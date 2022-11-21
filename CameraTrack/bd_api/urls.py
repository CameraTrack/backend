from django.urls import include, path
from . import views


urlpatterns = [
    path('AllowedNumber/', views.AllowedNumberView.as_view()),
    path('AllowedNumber/<int:id>', views.AllowedNumberView.as_view()),
    path('AllowedNumber/<int:id>/update/', views.AllowedNumberUpdate.as_view()),
    path('NumbersLogs/', views.NumberLogsView.as_view()),
    path('NumbersLogs<int:id>', views.NumberLogsView.as_view()),
    path('NumbersLogs/<int:id>/update/', views.NumberLogsUpdateView.as_view()),
    path('Users/', views.UsersView.as_view()),
    path('NumbersLogs<str:login>', views.UsersView.as_view()),
    path('NumbersLogs/<str:login>/update/', views.UsersUpdateView.as_view())
]