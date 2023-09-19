from django import forms


class EmailPostForm(forms.Form):
    """Create form to send message"""
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'col-md-6 col-sm-12 form-group', 'placeholder': 'Username', 'required': True}))
    my_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'col-md-6 col-sm-12 form-group', 'placeholder': 'Your address email', 'required': True}))
    recipient_email= forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'col-md-6 col-sm-12 form-group', 'placeholder': 'Email address recipient', 'required': True}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'col-md-12 col-sm-12 form-group', 'placeholder': 'Write a Message'}))
