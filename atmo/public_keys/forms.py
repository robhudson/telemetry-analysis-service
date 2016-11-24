# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from django.core.exceptions import ValidationError
from .models import PublicKey
from ..forms.mixins import CreatedByModelFormMixin, FormControlFormMixin


class NewPublicKeyForm(FormControlFormMixin, CreatedByModelFormMixin):

    def clean_key(self):
        key = self.cleaned_data['key']
        if not key.startswith('ssh-rsa AAAAB3'):
            raise ValidationError(
                'Invalid public key (a public key should start with \'ssh-rsa AAAAB3\')'
            )
        return key

    class Meta:
        model = PublicKey
        fields = ['title', 'key', ]
