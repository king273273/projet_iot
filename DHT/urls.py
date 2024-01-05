from django.urls import path
from . import views
from . import api
urlpatterns=[
path('',views.test),
path("api/",api.dhtser,name='json'),
path("table",views.table, name='table'),
]

