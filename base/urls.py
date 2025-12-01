from django.urls import *
from .views import *

urlpatterns=[path('home/',home,name='home'),
            path('booknow/<int:flight_id>/',book_now,name='book_now'),
            path('history/',history,name='history'),
            path('',login,name='login'),
            path('register/',register,name='register'),
            path('support/',support,name='support'),
            path('about/',about,name='about'),
            path('delete/<int:booking_id>/',delete, name='delete'),
]