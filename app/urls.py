from django.urls import path
from . import views

urlpatterns = [
    path('userlogin/',views.login_view,name = 'userlogin'),
    path('details/',views.adddetails, name = 'details'),
    path('',views.home, name = 'home'),
    path('list/',views.list_data, name = 'list'),
    path('exit/',views.exit, name = 'exit'),
    path('search/',views.search, name = 'search'),
    path('edit/<int:id>',views.edit, name = 'edit'),
    path('delete/<int:id>',views.destroy, name = 'delete'),
    path('aboutus/',views.aboutus, name = 'aboutus'),
    path('privacypolicy/',views.privacypolicy, name = 'privacypolicy'),
    path('contactus/',views.contactus, name = 'contactus'),
    path('disclaimer/',views.disclaimer, name = 'disclaimer'),

]

