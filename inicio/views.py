from django.shortcuts import render
from django.http import JsonResponse
import stripe
import json
stripe_pub = "pk_test_QjVR5rk9mW5gnKQgJBYrU4mZ00gnE32q39"
stripe_private = "sk_test_N6YjZISpM3p2R3K9wHlCCoHC00wUsuoWmv"
stripe.api_key = stripe_private

# vamos a levantar el formulario de Stripe


def home(request):
    return render(request, "home.html", {'key': stripe_pub})

# este es el primer checkout que se debe mostrar para que se devuelva todos los datos de la carga CHARGE

# Create your views here.


def checkout(request):
    amount = 10000000
    # Autenticacion del Cliente
    customer = stripe.Customer.create(
        email=request.POST['stripeEmail'],
        source=request.POST['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='aud',
        description="Venta de prueba en el full day codiGO"
    )
    print("status", charge)
    # return render(request, "ecsito.html")
    return JsonResponse(charge)
