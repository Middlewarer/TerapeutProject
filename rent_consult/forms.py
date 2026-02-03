from django.forms import ModelForm
from .models import ConsultationRequest

class ConsultationRequestForm(ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = '__all__'