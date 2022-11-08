from django.urls import path, include
from .views import smth, smth2, smth3, smth4, smth5, smth6, smth7, logout_view, form, blog_detail, error_view

urlpatterns = [
    path('', smth, name='main'),
    path('faq/', smth2, name='faq'),
    path('login/', smth3, name='login'),
    path('blog/', smth4, name='blog'),
    path('registration/', smth5, name='registration'),
    path('profile/', smth6, name='profile'),
    path('myblogs/', smth7, name='myblogs'),
    path('logout/', logout_view, name='logout'),
    path('form/', form, name='form'),
    path('detail/<int:id>/', blog_detail, name='detail'),
    path('error/', error_view, name='error'),
]
