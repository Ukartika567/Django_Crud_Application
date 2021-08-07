from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns=[

    path('', views.index, name='index'),
    url(r'^insert$', views.insert, name='insert'),
    path('delete/<int:id>', views.delete_emp, name='delete_emp'),
    path('edit/<int:id>', views.edit_emp, name='edit_emp'),
    path('update/<int:id>', views.emp_update, name='emp_update'),
    url(r'^validate_PanNumber/$', views.validate_PanNumber, name='validate_PanNumber'),
    
]