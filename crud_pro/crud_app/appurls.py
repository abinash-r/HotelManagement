from django.urls import path
from . import views

urlpatterns=[

    path('',views.index),
    path('add',views.addrecord),
    path('view',views.viewrecord),
    path('edit/<str:id>',views.editrecord),
    path('delete/<str:id>',views.deleterecord),
    path('index',views.baseview),
    path('billing',views.billing)
]