from django.urls import path
from .views import log_in,sign_up,log_out,index,batch

urlpatterns = [
    path('',index,name='index'),
    path('login/',log_in,name='login'),
    path('signup/',sign_up,name='signup'),
    path('batch/',batch,name='batch'),
    path('logout/',log_out,name='logout'),
]
