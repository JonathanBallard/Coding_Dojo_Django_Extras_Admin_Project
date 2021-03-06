
# django_admin_project URL Configuration 

# The `urlpatterns` list routes URLs to views. For more information please see: 
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/ 
# Examples: 
# Function views 
#     1. Add an import:  from my_app import views 
#     2. Add a URL to urlpatterns:  path('', views.home, name='home') 
# Class-based views 
#     1. Add an import:  from other_app.views import Home 
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home') 
# Including another URLconf 
#     1. Import the include() function: from django.urls import include, path 
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) 


'''
===============================================================================================
===============================================================================================
                                    PROJECT-LEVEL URLS.PY
===============================================================================================
===============================================================================================
'''



from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls import url 

from apps.login_reg.models import *    # User as U, Fruit, Donut, Group
class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UAdmin)

# class FruitAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Fruit, FruitAdmin)
# class DonutAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Donut, DonutAdmin)
# class GroupAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Group, GroupAdmin)




urlpatterns = [ 
    path('app/', include('apps.adminApp.urls')), 
    path('', include('apps.login_reg.urls')), 
    path('admin/', admin.site.urls), 
] 


