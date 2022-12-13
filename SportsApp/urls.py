from django.urls import path
from .views import *

urlpatterns = [
    path('', SportLingoPageView, name='index'),
    path('lingo/', SportLingoPageView, name='lingoview'),
    path('deleteTerm/<int:lingoid>/', DeleteTermPageView, name='deleteTerm'),
    path('showTerm/<int:lingoid>/', TermPageView, name='showTerm'),
    path('updateTerm/', UpdateTermPageView, name='updateTerm'),
    path('addTerm', AddTermPageView, name='addTerm')
]