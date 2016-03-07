# Forms used by the catalog "app" of the booksite project
from django import forms
from .models import Publisher, Title

class PublisherSearchForm(forms.Form):
    ''' Used to select a publisher -- user enters publisher's name
    '''
    publisher = forms.CharField(label='Get titles of: ', max_length=100)

class TitleSearchForm(forms.Form):
    ''' Used to select a title -- user enters the whole title
    '''
    title = forms.CharField(label='Title to find', max_length=100)

class PublisherForm(forms.ModelForm):
    ''' Form for adding a publisher
    '''
    class Meta:
        model = Publisher
        fields = ('pub_id', 'pub_name', 'city')

class TitleForm(forms.ModelForm):
    ''' Form for adding a title
    '''
    class Meta:
        model = Title
        fields = ('title_id', 'title', 'category', 'price', 'pub_id')

    # def clean_name(self):
        # custom validation -- in the Titles database,
        # could check the prefix of the title ID, which matches
        # the type field (here renamed category) unless that is "UNDECIDED"
