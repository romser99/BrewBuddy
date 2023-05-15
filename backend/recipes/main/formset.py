from .models import Malt
from .forms import MaltForm
from django.forms import modelformset_factory

MaltFormSet = modelformset_factory(
    Malt,
    form=MaltForm,
    extra=1,  # number of extra forms to display
    can_delete=True,  # allow forms to be deleted
)