from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
from pypaystack import Transaction as Trans, Customer, Plan
from user.models import Biodata
from .models import Transaction

def index(request):
    return render(request, 'invoice.htm', {'pk_public':settings.PAYSTACK_PUBLIC_KEY,
                                            'bio':Biodata.objects.get(user=request.user),
                                            })

def paid(request,):
    ref = request.GET.get('reference')
    transaction = Trans(authorization_key="settings.PAYSTACK_SECRET_KEY")
    #response = transaction.verify(ref)
    response = 'b'
    #if response[2] == True and response[3] == 'Verification successful' and response[4].status == 'success':
    if Transaction.objects.filter(id=ref).count() < 0:
        return render(request,'error_page.html',{'error':'Transaction already existed!'})
    else:
        t= Transaction(id=ref, user=request.user, due_id = 1)
        t.save()
    return render(request, 'receipt.html', {'ref':ref,
                                            'response':response,
                                             'bio':Biodata.objects.get(user=request.user)
                                            })

def charge(request):
    return render(request, 'payment.html', {'pk_public':settings.PAYSTACK_PUBLIC_KEY,
                                            'bio':Biodata.objects.get(user=request.user),
                                            })

def verify(request, id):
    transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY,)
    response = transaction.verify(id)
    data = JsonResponse(response, safe=False)
    return data