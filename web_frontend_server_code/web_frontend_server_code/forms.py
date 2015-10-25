from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Username: ')
	password = forms.CharField(label = 'Password: ')

class EventForm(forms.Form):
	name = forms.CharField(label = 'Name')
	start_time = forms.DateTimeField(label = 'Start Time')
	location = forms.CharField(label = 'Location')
	description = forms.CharField(label = 'Description')

class UserForm(forms.Form):
	username = forms.CharField(label = 'Username')
	password = forms.CharField(label = 'Password')
	firstname = forms.CharField(label = 'Firstname')
	lastname = forms.CharField(label = 'Lastname')
	
