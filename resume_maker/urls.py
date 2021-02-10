from django.urls import path
from . import views

urlpatterns = [
    path('',views.render_page),
    #path('add/<slug:field>',views.add_field,name = "add_field")
]