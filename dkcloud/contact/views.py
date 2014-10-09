from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def contact_page(request, contact_template, message_template, mail_list, mail_from):
    """
    Contact page for the website, supply page with a template with an area
    for a POST form
    """
    
    # check if the message was submitted
    if request.method == 'POST':
        
        # Check if the data is valid
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            
            # Send an email to recipients on the mail_list
            email_message = '''
            {0}\n
            {1}
            UserN: {2}
            Email: {3}
            Phone: {4}
            '''.format(message, name, request.user.username, email, phone_number)
            send_mail('DK Cloud Contact: ' + name, email_message, mail_from, mail_list)
            
            # Show confirmation page
            return render(request, message_template, {
                'username': request.user.username,
                'message': 'Thank you for contacting us, we will be in touch shortly!',
            })
            
        # TODO: find a better way to do this
        else:
            form = ContactForm(request.POST)
            return render(request, contact_template, {
                'username': request.user.username,
                'form': form,
            })

    # if message was not submitted    
    else:
        form = ContactForm()
        return render(request, contact_template, {
            'username': request.user.username,
            'form': form,
        })
