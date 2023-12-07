from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index ,name='index'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('status/',views.status,name='status'),
    path('withdraw/',views.withdraw,name='withdraw'),
    path('deposit/',views.deposit,name='deposit'),
    path('info/<int:pk>',views.inf_movement,name='info'),
    path('transfer/',views.transfer,name='transfer'),
]