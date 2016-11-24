# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import get_objects_for_user

from .models import PublicKey
from .forms import NewPublicKeyForm
from ..decorators import view_permission_required


@login_required
def list_public_keys(request):
    public_keys = get_objects_for_user(
        request.user,
        'public_keys.view_publickey',
        PublicKey.objects.all().order_by('-created_on'),
        use_groups=False,
        with_superuser=False,
    )
    if request.method == 'POST':
        form = NewPublicKeyForm(
            request.user,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return redirect('public-key-list')
    else:
        form = NewPublicKeyForm(request.user)
    context = {
        'form': form,
        'public_keys': public_keys
    }
    return render(request, 'atmo/public-key.html', context)


@login_required
@view_permission_required(PublicKey)
def delete_public_keys(request, id):
    job = get_object_or_404(PublicKey, pk=id)
    if request.method == 'POST':
        job.delete()
        return redirect('public-key-list')
    context = {
        'job': job,
    }
    return render(request, 'atmo/public-key-delete.html', context=context)
