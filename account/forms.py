from .models import MyUser
from django import forms
from django.contrib.auth import authenticate

class SignupForm(forms.ModelForm):
	password=forms.CharField(label="password",widget=forms.PasswordInput)
	password2=forms.CharField(label="confirm password",widget=forms.PasswordInput)
	def clean_password2(self):
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password and password2 and password!=password2:
			raise forms.ValidationError('password did not matched')
		return password2
	def clean_email(self):
		email_data=self.cleaned_data.get('email')
		if email_data and len(MyUser.objects.filter(email=email_data))>0:
			raise forms.ValidationError('email already exist')
		return email_data
	def __init__(self,*args,**kwargs):
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['email'].required=True
		self.fields['password'].required=True
	def save(self, commit=True):
		user=super(SignupForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user
	class Meta:
		model=MyUser
		fields=['first_name','last_name','username','email']
class EditProfile(forms.ModelForm):
	class Meta:
		model=MyUser
		fields=['first_name','last_name','profile_pic','sex','age','about','phone','address']
class LoginForm(forms.Form):
	username=forms.CharField(label='username')
	password=forms.CharField(label='password',widget=forms.PasswordInput)
	def __init__(self,*args,**kwargs):
		self.user_cache=None
		super(LoginForm,self).__init__(*args,**kwargs)
		#self.fields['username'].required=True
		#self.fields['password'].required=True
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			self.user_cache = authenticate(username = username, password = password)
			if self.user_cache is None:
				raise forms.ValidationError('Please enter a correct username and password')
			elif not self.user_cache.is_active:
				raise forms.ValidationError('This account is inactive')
		return self.cleaned_data
	def get_user(self):
		return self.user_cache
