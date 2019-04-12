from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'main_home_page.html'


class services(TemplateView):
    template_name ='services.html'

class services_2(TemplateView):
    template_name ='services_2.html'

class services_single(TemplateView):
    template_name ='services_single.html'



class about_us(TemplateView):
    template_name ='about_us.html'

class contact_us(TemplateView):
    template_name ='contact.html'

class team(TemplateView):
    template_name ='team.html'

class case_studies(TemplateView):
    template_name ='case_studies.html'

class testimonial(TemplateView):
    template_name ='testimonial.html'

class error(TemplateView):
    template_name ='not_found.html'



class portfolio_2(TemplateView):
    template_name ='portfolio_2.html'

class portfolio_3(TemplateView):
    template_name ='portfolio_3.html'

class portfolio_4(TemplateView):
    template_name ='portfolio_4.html'

class portfolio_masonry(TemplateView):
    template_name ='portfolio_masonry.html'

class portfolio_single(TemplateView):
    template_name ='portfolio_single.html'

class blog(TemplateView):
    template_name = 'blog.html'

class blog_single(TemplateView):
    template_name ='blog_single.html'

class blog_list(TemplateView):
    template_name ='blog_list.html'