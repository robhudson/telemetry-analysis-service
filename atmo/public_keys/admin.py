# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from django.contrib import admin
from .models import PublicKey


@admin.register(PublicKey)
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_by',
        'fingerprint',
        'created_on',
    ]
    list_filter = [
        'created_on',
    ]
    search_fields = ['title', 'fingerprint', 'created_by__email', ]
