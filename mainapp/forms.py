from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Task


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "first_name", "last_name", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class EditUserForm(ModelForm):
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
		]

class CategoryForm(ModelForm):
	
	class Meta:
		model = Category
		fields = [
			'name',
			'desc',
		]

class TaskForm(ModelForm):

	def __init__(self, *args, user=None, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)

	class Meta:
		model = Task
		fields = [
			'name',
			'desc',
			'category',
		]
