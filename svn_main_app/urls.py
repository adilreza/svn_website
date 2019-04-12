from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),

    path('svn_services', views.services.as_view(), name='services'),
    path('svn_services_2', views.services_2.as_view(), name='services_2'),
    path('svn_services_single', views.services_single.as_view(), name='services_single'),

    path('about_us', views.about_us.as_view(), name='about_us'),
    path('contact_us', views.contact_us.as_view(), name='contact_us'),
    path('team', views.team.as_view(), name='team'),
    path('case_studies', views.case_studies.as_view(), name='case_studies'),
    path('testimonial', views.testimonial.as_view(), name='testimonial'),
    path('error', views.error.as_view(), name='error'),


    path('portfolio_2', views.portfolio_2.as_view(), name='portfolio_2'),
    path('portfolio_3', views.portfolio_3.as_view(), name='portfolio_3'),
    path('portfolio_4', views.portfolio_4.as_view(), name='portfolio_4'),
    path('portfolio_masonry', views.portfolio_masonry.as_view(), name='portfolio_masonry'),
    path('portfolio_single', views.portfolio_single.as_view(), name='portfolio_single'),

    path('blog', views.blog.as_view(), name='blog'),
    path('blog_single', views.blog_single.as_view(), name='blog_single'),
    path('blog_list', views.blog_list.as_view(), name='blog_list'),
]
