from django.urls import path 
from general.views import HomepageView, BlogView,BlogdetailsView, PortfolioView,ServiceView
urlpatterns = [
    path('', HomepageView.as_view(),name = 'home'),
    path('blog', BlogView.as_view(),name = 'blog'),
    path('blogdetails', BlogdetailsView.as_view(),name = 'blogdetails'),
    path('portfolio', PortfolioView.as_view(),name = 'portfolio'),
    path('service', ServiceView.as_view(),name = 'service'),
   
]



