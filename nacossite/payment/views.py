from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
from pypaystack import Transaction as Trans, Customer, Plan
from user.models import Biodata
from .models import Transaction

def index(request):
    return render(request, 'invoice.htm', {'bio':Biodata.objects.get(user=request.user),
                                            })

def paid(request,):
    ref = request.GET.get('reference')
    transaction = Trans(authorization_key=settings.PAYSTACK_SECRET_KEY)
    responses = transaction.verify(ref)
    response = responses[3]["status"]
    detail={
        'id':responses[3]['id'],
        'reference':responses[3]['reference'],
        'paid_at':responses[3]['paid_at'],
        'created_at':responses[3]['created_at'],
        'bank':responses[3]['authorization']['bank'],
        'account_name':responses[3]['authorization']['account_name'],
        'first_name':responses[3]['customer'][ 'first_name'],
        'last_name':responses[3]['customer']['last_name'],
        'email':responses[3]['customer'][ 'email'],
        'phone':responses[3]['customer'][ 'phone'],
    }
    if response ==  'success':
        if Transaction.objects.filter(id=ref).count() > 0:
            return render(request,'error_page.html',{'error':'Transaction already existed!'})
        else:
            t= Transaction(id=ref, user=request.user, due_id = 1)
            t.save()
    else:
        return render(request, 'error_page.html', {'error': 'Invalid transaction!'})
    return render(request, 'receipt.html', {'ref':ref,
                                            'response':response,
                                            'res':responses[3],
                                            'detail':detail,
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

def payer(request,):
    customer = Customer(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = customer.create("adesolapastorsamuel@gmail.com", "John", "Doe", phone="080123456789")  # Add new customer
    cus_code=response#[3]['customer_code']
    cus = customer.getone(cus_code)
    response = customer.getone("CUS_xxxxyy")
    plan = Plan(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response2 = plan.getone(78235)
    transaction = Trans(authorization_key=settings.PAYSTACK_SECRET_KEY)
    response = transaction.charge("adesolapastorsamuel@gmail.com", "CUS_rvrdf0ryt66ncpp", 10000)
    #response = customer.getone("CUS_xxxxyy")  # Get customer with customer code of  CUS_xxxxyy
    #response = customer.getall()  # Get all customers
    #transaction = Transaction(authorization_key=settings.PAYSTACK_SECRET_KEY,)
    #response = transaction.charge("customer@domain.com", "CustomerAUTHcode", 10000)  # Charge a customer N100.
    #data = JsonResponse(response, safe=False)
    return render(request,'invoice.htm', {'bio':Biodata.objects.get(user=request.user),
                                          'response':response,
                                          'response1':cus_code,
                                          'cus':cus,
                                          'plan':response2,
                                            })