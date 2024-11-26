
from django.urls import path
from ecomapp import views
from ecomapp.views import SimpleView


urlpatterns = [
    path('about',views.about),
    path('content',views.content),
    path('edit/<rid>',views.edit),
    path('myview',SimpleView.as_view()),
    path('hello',views.hello),
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('edited/<rid>',views.edited),
    path('delete/<rid>',views.delete),
]
