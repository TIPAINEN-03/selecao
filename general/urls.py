from django.urls import path 
from general.views import HomepageView, BlogView,BlogdetailsView, PortfoliodetailsView,ServiceView, ContactView, AboutView, PortfolioView, TeamView, SerView
urlpatterns = [
    path('', HomepageView.as_view(),
         name = 'home'),

    path('blog', BlogView.as_view(),
         name = 'blog'),

    path('blogdetails', BlogdetailsView.as_view(),
         name = 'blogdetails'),

    path('portfolio', PortfoliodetailsView.as_view(),
         name = 'portfoliodetails'),

    path('service', ServiceView.as_view(),
         name = 'service'),

    path('contact', ContactView.as_view(),
         name = 'contact'),

    path('about', AboutView.as_view(),
         name = "about"),

    path('portfolio', PortfolioView.as_view(),
         name = "portfolio"),

    path('team', TeamView.as_view(),
         name = "team"),

    path('serv', SerView.as_view(),
         name = "serv")
   
]



