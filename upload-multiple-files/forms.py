class AdForm(forms.ModelForm):
    pictures = forms.ImageField(widget=forms.FileInput(attrs={'multiple': 'true',}), validators=[allow_only_images_validator])
    
    class Meta:
        model = AD
        fields = ['ad_title', 'description', 'price']
