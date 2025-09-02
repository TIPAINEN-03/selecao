from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView (TemplateView):
    template_name = "general/index.html"
    
class BlogView  (TemplateView):
    template_name = "general/blog.html"
    
class PortfoliodetailsView (TemplateView):
    template_name = "general/portfolio-details.html"
    
class BlogdetailsView (TemplateView):
    template_name = "general/blog-details.html"
    
class ServiceView (TemplateView):
    template_name = "general/service-details.html"

class ContactView (TemplateView):
    template_name = "general/contact.html"

class AboutView (TemplateView):
    template_name = "general/about.html"

class PortfolioView (TemplateView):
    template_name = "general/portfolio.html"

class TeamView (TemplateView):
    template_name = "general/team.html"

class SerView (TemplateView):
    template_name = "general/service.html"
    
