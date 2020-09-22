from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import hashlib
from .models import Autologin
from uuid import uuid4

# Generate a unique URL and email it to the user for autologin purposes
def generate(request):
    try:
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        uniqueString = hashlib.md5(email.encode('utf-8')).hexdigest()
        urlRecord = Autologin.objects.create(user=user, unique_value=uniqueString, link_type=1)

        # Print to terminal for time being
        print(urlRecord)
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False})

# Validates a user based on the record and unique_string parameters and "logs them in" if successful
def validate(request):
  recordId = request.GET.get('record')
  uniqueString = request.GET.get('unique_string')
  urlRecord = Autologin.objects.filter(id=recordId, unique_value=uniqueString).first()
  if not urlRecord:
    return JsonResponse({'success': False})

  urlRecord.delete()
  return JsonResponse({'success': True, 'login_value':  str(uuid4())})

