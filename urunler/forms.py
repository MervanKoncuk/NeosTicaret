from django.forms import ModelForm
from .models import Urun

class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['isim', 'fiyat', 'kategori', 'resim']

    def __init__(self, *args, **kwargs):
        super(UrunForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})