from django import forms
from .models import Messages

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'

        choice = forms.CharField(
            label='selectVillagers',
            widget=forms.Select(choices=[
                ('Ankha', 'Ankha'),
                ('Bob', 'Bob'),
                ('Punchy', 'Punchy'),
                ('Cranston', 'Cranston'),
                ('Kid Cat', 'Kid Cat'),
                ('Raymond', 'Raymond'),
                ('Pietro', 'Pietro'),
                ('Sasha', 'Sasha'),
                ('Audie', 'Audie'),
                ('Lolly', 'Lolly'),
            ])
        )





