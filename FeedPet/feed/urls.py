# feed/urls.py
from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    # Feed page
    path('', views.feed, name='feed'),

    # Get dog by id
    path('getDog/<int:dogId>', views.getDog, name='getDog'),

    # Get cat by id
    path('getCat/<int:catId>', views.getCat, name='getCat'),

    # Feed recommendation page
    path('feed_recommendation/', views.feed_recommendation,
         name='feed_recommendation'),

    # Feed detail page
    path('feed_detail/', views.feed_detail, name='feed_detail'),

    # Favorite feed page
    path('feed_favorite/', views.feed_favorite, name='feed_favorite'),

    # Feeding record page
    path('feeding_record/', views.feeding_record, name='feeding_record'),

    # total Feed list page
    path('feed_list/', views.feed_list, name='feed_list'),
    
    # # Home page
    # path('', views.index, name='index'),
    # # add a user's face
    # path('addmyface/', views.addmyface, name='addmyface'),
    # # show all user's face
    # path('facelist/', views.facelist, name='facelist'),
    # # recognize face
    # path('whoami/', views.whoami, name='whoami'),
]
