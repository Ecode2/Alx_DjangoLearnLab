from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@permission_required('app_name.can_edit', raise_exception=True)
def my_view(request):
    # Your view logic here
    pass

""" @login_required
@permission_required('app_name.can_edit', raise_exception=True)
def my_other_view(request):
    # Your view logic here
    pass """