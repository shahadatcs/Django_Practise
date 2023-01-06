"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from Aunthentication import views
#from payments import views as p
#from Aunthentication.views import ngo
#from payment_list import views
from django.urls.conf import include, include


urlpatterns = [
    #path('admin/', admin.site.urls),
        #path('',views.django),
        #path('h/',p.home_page),
        #path('Rk/',p.Roket),
        #path('Ad/',p.add),
        #path('pow/',p.power),
        #path('au/',ngo),
        #path('pa/',views.pay),
        
        path('py/', include('payments.urls')),
        path('tr/', include('Aunthentication.urls')),
        path('pl/', include('payment_list.urls')),        
]
