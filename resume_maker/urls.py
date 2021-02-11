from django.urls import path
from . import views

urlpatterns = [
    path('resume',views.render_page,name='res'),
    path('get',views.get_input,name='input'),
    #path('add/<slug:field>',views.add_field,name = "add_field")
]