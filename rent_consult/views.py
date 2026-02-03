from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ConsultationRequestForm
from .models import ConsultationRequest

class LandingView(CreateView):
    template_name = 'rent_consult/index.html'
    model = ConsultationRequest
    form_class = ConsultationRequestForm

    success_url = reverse_lazy('index')
