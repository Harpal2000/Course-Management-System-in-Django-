from django.contrib import admin
from django.urls import path
from . import views
from cmsappli.views import register,login,index,home,admin_login,add_stream,addcourse,addstream,showdata
from cmsappli.views import delc,dels,showstreams,showuserd,updates,updatec


app_name='cmsappli'

urlpatterns = [
    path('', views.index,  name='index'),
    path('admin_login', views.admin_login,  name='admin_login'),
    # path('crudop', crudop,  name='crudop'),
    path('addcourse', addcourse,  name='addcourse'),
    path('addstream', addstream,  name='addstream'),
    path('updates', updates,  name='updates'),
    path('updatec', updatec,  name='updatec'),
    path('delc', delc,  name='delc'),
    path('dels', dels,  name='dels'),
    path('showdata', views.showdata,  name='showdata'),
    path('showstreams', views.showstreams,  name='showstreams'),
    path('showuserd', views.showuserd,  name='showuserd'),
    # path('adddata', adddata,  name='adddata'),
    path('add_stream', add_stream,  name='add_stream'),
    path('login', views.login,  name='login'),
    path('home',home, name='home'),
    path('register',register, name='register'),
    
]