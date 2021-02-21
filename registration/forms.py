from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Создать аккаунт'))
        # self.helper.field_class = 'col-lg-8'

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Вас зовут',
            'password1': 'Пароль',
            'password2': 'Пароль',
        }
