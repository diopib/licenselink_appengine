from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from models import UserLicense

class HomeView(CreateView):
    template_name = "index.html"
    model = UserLicense

    def get_success_url(self):
        return reverse('create_success', kwargs={'short_url': self.object.short_url})
        # return CreateSuccess.as_view()(self.request, self.object.short_url)

class CreateSuccess(TemplateView):
    template_name = "success.html"

class ViewLicense(TemplateView):
    template_name = "view_license.html"

    def get_context_data(self, **kwargs):
        context = super(ViewLicense, self).get_context_data(**kwargs)
        u_license = UserLicense.objects.get(short_url=self.kwargs['short_url'])
        context['license'] = u_license.display_license()
        context['license_name'] = u_license.license_type.name
        return context