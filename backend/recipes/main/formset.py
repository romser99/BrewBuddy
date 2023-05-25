from .models import Malt
from .forms import MaltForm
from django.forms import modelformset_factory

MaltFormSet = modelformset_factory(
    Malt,
    form=MaltForm,
    extra=1,
    can_delete=True,  
)