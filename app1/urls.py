from django.urls import path
from .views import output

urlpatterns = [
    path('', output, name='testpage')
]