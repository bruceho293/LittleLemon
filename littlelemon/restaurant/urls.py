from django.urls import path
from . import views

urlpatterns = [
    # path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menus/', views.MenuItemView.as_view()),
    path('menus/<int:pk>', views.SingleMenuItemView.as_view()),
]
