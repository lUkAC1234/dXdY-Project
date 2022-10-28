from django.urls import path, include
from .views import smth, smth2, smth3, smth4, smth5

urlpatterns = [
    path('', smth, name='main'),
    path('faq/', smth2, name='faq'),
    path('login/', smth3, name='login'),
    path('blog/', smth4, name='blog'),
    path('registration/', smth5, name='registration'),
]
