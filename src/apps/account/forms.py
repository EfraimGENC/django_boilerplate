from django.core.exceptions import ValidationError
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        """Reject usernames that differ only in case."""
        email = self.cleaned_data.get("email")
        if (
            email
            and self._meta.model.objects.filter(email__iexact=email).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "email": self.instance.unique_error_message(
                            self._meta.model, ["email"]
                        )
                    }
                )
            )
        else:
            return email


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
