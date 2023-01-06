from django.urls import path
from . import views as p 
urlpatterns = [
    #path('admin/', admin.site.urls),
        #path('',views.django),
        path('h/', p.home_page),
        path('i/', p.hom_pag),

       # path('Rk/', p.Roket),
        #path('Ad/', p.add),
        #path('pow/', p.power),
        #path('au/',ngo),
        #path('pa/',views.pay),
        
]