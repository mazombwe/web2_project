from django.urls import path, include
from pages import views as page_views

app_name = 'pages'
urlpatterns = [
    path('', page_views.home, name='home'),
    path('menu/', page_views.menu, name='menu'),
    path('contact/', page_views.contact, name='contact'),
    path('about/', page_views.about, name='about'),
    path('menu/add/', page_views.addPlat, name='addPlat'),
    path('menu/edit/<int:platId>', page_views.editPlat, name='editPlat'),
    path('menu/del/<int:platId>/', page_views.delPlat, name='delPlat'),
]