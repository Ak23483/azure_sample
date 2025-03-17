from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Username',
            'required': True
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form__input',
            'placeholder': 'Your Email',
            'required': True
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'placeholder': 'Your Password',
            'required': True
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'placeholder': 'Confirm Password',
            'required': True
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form with additional validation
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Username',
            'required': True
        }),
        label='Username',
        help_text='Choose a unique username'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form__input',
            'placeholder': 'Your Email',
            'required': True
        }),
        label='Email',
        help_text='Enter a valid email address'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'placeholder': 'Password',
            'required': True
        }),
        label='Password',
        help_text='Choose a strong password'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'placeholder': 'Confirm Password',
            'required': True
        }),
        label='Confirm Password',
        help_text='Repeat your password'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        """
        Validate email is unique
        """
        email = self.cleaned_data['email']
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        
        return email

    def clean_username(self):
        """
        Validate username is unique and meets requirements
        """
        username = self.cleaned_data['username']
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        
        # Additional username validation
        if len(username) < 3:
            raise ValidationError("Username must be at least 3 characters long.")
        
        return username

    def save(self, commit=True):
        """
        Save the user with hashed password
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Enter Username',
            'required': True,
            'type': 'text'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'placeholder': 'Your Password',
            'required': True
        })
    )

    error_messages = {
        'invalid_login': 'Invalid username or password. Please try again.',
        'inactive': 'This account is inactive.',
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(request=self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Invalid username or password. Please try again.',
                    code='invalid_login'
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    'This account is inactive.',
                    code='inactive'
                )
        return self.cleaned_data


   