from django import forms
def_widget = forms.TextInput(attrs={'class': 'form-control input-lg'})
pass_widget = forms.TextInput(attrs={'class': 'form-control input-lg', 'type': 'password'})

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Username', widget=def_widget)
	password = forms.CharField(label = 'Password', widget=pass_widget)

class EventForm(forms.Form):
	name = forms.CharField(label = 'Event Title', widget=def_widget)
	date = forms.CharField(label = 'Date', widget=forms.TextInput(attrs={'class': 'form-control input-lg','style':'width: 45%;','type':'date'}))
	time = forms.CharField(label = 'Time', widget=forms.TextInput(attrs={'class': 'form-control input-lg','style':'width: 45%;','type':'time'}))
	location = forms.CharField(label = 'Location', widget=def_widget)
	description = forms.CharField(label = 'Description', widget=def_widget)

class UserForm(forms.Form):
	username = forms.CharField(label = 'Username', widget=def_widget)
	password = forms.CharField(label = 'Password', widget=pass_widget)
	firstname = forms.CharField(label = 'Firstname', widget=def_widget)
	lastname = forms.CharField(label = 'Lastname', widget=def_widget)
	
