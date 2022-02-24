from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST.get('user_id', 0)
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this listing')
                return redirect('/listings/' + listing_id)
        contact = Contact(listing=listing, listing_id=listing_id,
                          name=first_name + ' ' + last_name,
                          phone=phone, message=message,
                          email=email, user_id=user_id)
        contact.save()

        # send mail
        send_mail(
            'Property Listing Inquiry',
            'there has been an inquiry for ' + listing,
            'kisel.nf@yandex.ru',
            [realtor_email, 'kisel.nf97@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back you soon')
        return redirect('/listings/'+listing_id)