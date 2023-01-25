from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.forms import ModelForm, Form, EmailField, CharField
from django import forms
from app.models import Product, User
from root.settings import EMAIL_HOST_USER


class ProdctModelForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=155)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This email not found')
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        if email:
            password = self.data.get('password')
            # user = User.objects.filter(email=email).exists()
            # user = User.objects.filter(email=email).exists()
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise ValidationError('this password not found')
            return password


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=155)
    email = forms.EmailField()
    password = forms.CharField(max_length=55)
    confirm_password = forms.CharField(max_length=55)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email):
            raise ValidationError('This email already exists')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('confirm password is wrong')
        return password

    def save(self):
        user = User.objects.create_user(
            email=self.data.get('email'),
            password=self.data.get('password')
        )

        user.save()


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    # def send_email(self):
    #     subject = 'xabarni titlesi'
    #     message = 'python 2 ni ikkichi bollari'
    #     from_email = EMAIL_HOST_USER
    #     recipient_list = ['asilbek1721@gmail.com', 'komronxon4@gmail.com', 'qodiriyabdulla85@gmail.com', 'shohboom@gmail.com']
    #     result = send_mail(subject, message, from_email, recipient_list)
    #     print(result)


    def send_email(self):
        email = EMAIL_HOST_USER
        subject = 'xabarni titlesi'
        message = 'python 2 ni ikkichi bollari'
        from_email = EMAIL_HOST_USER
        recipient_list = [email]
        result = send_mail(subject, message, from_email, recipient_list)
        print(result)
