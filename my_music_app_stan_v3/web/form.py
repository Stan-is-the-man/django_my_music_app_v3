from django import forms

from my_music_app_stan_v3.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        # there should be a placeholder
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),

            'email': forms.TextInput(attrs={'placeholder': 'Email'}),

            'age': forms.Textarea(attrs={'placeholder': 'Age'}),
        }


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()

        Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),

            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),

            'description': forms.Textarea(attrs={'placeholder': 'Description'}),

            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),

            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class DeleteAlbumForm(forms.ModelForm):

    # On the page, the form must be filled and DISABLED
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    # delete the album
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),

            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),

            'genre': forms.Textarea(attrs={'placeholder': 'Genre'}),

            'description': forms.Textarea(attrs={'placeholder': 'Description'}),

            'image_url': forms.Textarea(attrs={'placeholder': 'Image URL'}),

            'price': forms.Textarea(attrs={'placeholder': 'Price'}),
        }
