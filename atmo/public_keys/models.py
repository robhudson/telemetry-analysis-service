# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import unicode_literals

import base64
import hashlib

from django.db import models

from ..models import CreatedByModel


def calculate_fingerprint(key):
    decoded_key = base64.b64decode(key.strip().split()[1].encode('ascii'))
    hashed_key = hashlib.md5(decoded_key).hexdigest()
    return ':'.join(a + b for a, b in zip(hashed_key[::2], hashed_key[1::2]))


class PublicKey(CreatedByModel):
    title = models.CharField(max_length=100, help_text='Name to give to this public key')
    key = models.TextField(max_length=100000, help_text='Public key')
    fingerprint = models.CharField(max_length=48, unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.fingerprint:
            self.fingerprint = calculate_fingerprint(self.key)
        super(PublicKey, self).save()

    class Meta:
        permissions = [
            ('view_public_key', 'Can view public key'),
        ]
