from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import HiddenInput, ModelChoiceField, ModelForm, formset_factory, inlineformset_factory

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True)
    username = forms.CharField(label='Username', required=True)
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'autocomplete': 'current-password'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password'})

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                username = user.email
            except User.DoesNotExist:
                pass
        return username

    class Meta:
        model = User
        fields = ['username', 'password']
        # Set the 'username' field to 'email'
        username = 'email'

class AddMaltForm(forms.ModelForm):
    
    class Meta:
        model = StockMalt
        fields = ['name', 'type', 'ebc', 'producer', 'quantity','cost']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Malt name'})
        self.fields['type'].widget.attrs.update({'placeholder': 'Malt type'})
        self.fields['ebc'].widget.attrs.update({'placeholder': 'EBC'})
        self.fields['producer'].widget.attrs.update({'placeholder': 'Producer'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'Quantity'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'cost'})
        self.fields['producer'].required = False
        self.fields['type'].required = False
        self.fields['cost'].required = False
        

    def save(self, user, commit=True):
        malt = super().save(commit=False)
        malt.user = user
        if commit:
            malt.save()
        return malt

class AddHopForm(forms.ModelForm):
    class Meta:
        model = StockHop
        fields = ['name', 'pellet', 'alpha', 'producer', 'quantity','cost']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Hop name'})
        self.fields['pellet'].widget.attrs.update
        self.fields['alpha'].widget.attrs.update({'placeholder': '%'})
        self.fields['producer'].widget.attrs.update({'placeholder': 'Producer'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'Quantity'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'cost'})
        self.fields['producer'].required = False
        self.fields['cost'].required = False

    def save(self, user, commit=True):
        hop = super().save(commit=False)
        hop.user = user
        if commit:
            hop.save()
        return hop

class AddYeastForm(forms.ModelForm):
    class Meta:
        model = StockYeast
        fields = ['name', 'producer', 'quantity','cost']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Yeast name'})
        self.fields['producer'].widget.attrs.update({'placeholder': 'Producer'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'Quantity'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'cost'})
        self.fields['producer'].required = False
        self.fields['cost'].required = False
        

    def save(self, user, commit=True):
        yeast = super().save(commit=False)
        yeast.user = user
        if commit:
            yeast.save()
        return yeast

class AddExtraForm(forms.ModelForm):
    class Meta:
        model = StockExtra
        fields = ['name', 'producer', 'quantity','cost']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'extra name'})
        self.fields['producer'].widget.attrs.update({'placeholder': 'Producer'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'Quantity'})
        self.fields['cost'].widget.attrs.update({'placeholder': 'cost'})
        self.fields['producer'].required = False
        self.fields['cost'].required = False

    def save(self, user, commit=True):
        extra = super().save(commit=False)
        extra.user = user
        if commit:
            extra.save()
        return extra
    
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','family', 'volume', 'private']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'recipe name'})
        self.fields['family'].widget.attrs.update()
        self.fields['family'].label = 'Beer Type'
        self.fields['volume'].widget.attrs.update({'placeholder': 'Volume in L'})
        self.fields['private'].widget.attrs.update()

    def save(self, user, commit=True):
        recipe = super().save(commit=False)
        recipe.user = user
        if commit:
            recipe.save()
        return recipe
    

class MaltForm(forms.ModelForm):
    stock_malt = forms.ChoiceField(choices=[])
    quantity = forms.FloatField()

    class Meta:
        model = Malt
        fields = ['stock_malt', 'quantity']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MaltForm, self).__init__(*args, **kwargs)
        self.fields['stock_malt'].choices = [(stock_malt.id, stock_malt.name +' EBC = '+ str(stock_malt.ebc)) for stock_malt in StockMalt.objects.filter(user=user)]

class BrewingForm(forms.ModelForm):
    temperature = forms.FloatField()
    time = forms.FloatField()

    class Meta:
        model = Brewing
        fields = ['temperature', 'time']

class BoilingForm(forms.ModelForm):
    DryHopping = forms.BooleanField(required=False)
    time = forms.FloatField()

    class Meta:
        model = Boiling
        fields = ['DryHopping', 'time']


class HopForm(forms.ModelForm):
    stock_hop = forms.ChoiceField(choices=[])
    quantity = forms.FloatField()

    class Meta:
        model = Hop
        fields = ['stock_hop', 'quantity']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(HopForm, self).__init__(*args, **kwargs)
        self.fields['stock_hop'].choices = [(stock_hop.id, stock_hop.name +' '+ str(stock_hop.alpha) + ' % Alpha') for stock_hop in StockHop.objects.filter(user=user)]

class ExtraForm(forms.ModelForm):
    stock_extra = forms.ChoiceField(choices=[])
    quantity = forms.FloatField()

    class Meta:
        model = Extra
        fields = ['stock_extra', 'quantity']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ExtraForm, self).__init__(*args, **kwargs)
        self.fields['stock_extra'].choices = [(stock_extra.id, stock_extra.name) for stock_extra in StockExtra.objects.filter(user=user)]

class YeastForm(forms.ModelForm):
    stock_yeast = forms.ChoiceField(choices=[])
    quantity = forms.FloatField()

    class Meta:
        model = Yeast
        fields = ['stock_yeast', 'quantity']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(YeastForm, self).__init__(*args, **kwargs)
        self.fields['stock_yeast'].choices = [(stock_yeast.id, stock_yeast.name) for stock_yeast in StockYeast.objects.filter(user=user)]

class FermentationForm(forms.ModelForm):
    temperature = forms.FloatField()
    time = forms.FloatField()

    class Meta:
        model = Fermentation
        fields = ['temperature', 'time']

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'volume','alcool','ebc','ibu','cost','sale' ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'value': self.instance.__dict__[field_name]})
        
        self.fields['description'].required = False
        self.fields['alcool'].required = False
        self.fields['ebc'].required = False
        self.fields['ibu'].required = False
        self.fields['cost'].required = False
        self.fields['sale'].required = False
    
    def save(self, user, commit=True):
        recipe = super().save(commit=False)
        recipe.user = user
        if commit:
            recipe.save()
        return recipe
    
    def clean_volume(self):
        volume = self.cleaned_data.get('volume')
        if volume <= 0:
            raise forms.ValidationError('Volume must be a positive number.')
        return volume
    
    def clean_ebc(self):
        ebc = self.cleaned_data.get('ebc')
        if ebc is not None and ebc < 0:
            raise forms.ValidationError('EBC cannot be negative.')
        return ebc
    
    def clean_alcool(self):
        alcool = self.cleaned_data.get('alcool')
        if alcool is not None and alcool < 0:
            raise forms.ValidationError('ABV cannot be negative.')
        return alcool
    
    def clean_ibu(self):
        ibu = self.cleaned_data.get('ibu')
        if ibu is not None and ibu < 0:
            raise forms.ValidationError('IBU cannot be negative.')
        return ibu

class RecipeSearchForm(forms.Form):
    SORT_CHOICES = [
        ('name', 'Name'),
        ('alcool', 'Alcool'),
        ('ebc', 'ebc'),
        ('ibu', 'ibu'),
    ]
    
    search_query = forms.CharField(max_length=100, required=False)
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False, widget=forms.SelectMultiple(attrs={'size': 4}))
