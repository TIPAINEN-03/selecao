from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView (TemplateView):
    template_name = "general/index.html"
    
class BlogView  (TemplateView):
    template_name = "general/blog.html"
    
class PortfolioView (TemplateView):
    template_name = "general/portfolio-details.html"
    
class BlogdetailsView (TemplateView):
    template_name = "general/blog-details.html"
    
class ServiceView (TemplateView):
    template_name = "general/service-details.html"
    
