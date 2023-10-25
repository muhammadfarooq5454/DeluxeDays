from django.shortcuts import render,redirect
from .models import Blog, HomeContent, Stat, \
    GuestSectionContent, HostSectionContent, \
    GuestSectionSlider, HostSectionSlider, Feedback, \
    AboutSectionContent, TeamMember, SocialLink, Message, AboutWhyChooseUs, \
    ContactContent, CompanyInformation
from .email import send_message_notification_to_company

# Create your views here.

def index(request):

    context = {
        'title': HomeContent.objects.get(key='Header Title').value,
        'description': HomeContent.objects.get(key='Header Description').value,
        'accomodations': Stat.objects.get(key='Accomodations').value,
        'cars': Stat.objects.get(key='Cars').value,
        'boats': Stat.objects.get(key='Boats').value,
        'users': Stat.objects.get(key='Trusted Users').value,
        'experiences': Stat.objects.get(key='Experiences').value,
        'hosts': Stat.objects.get(key='Verified Hosts').value,
        's1Title': HomeContent.objects.get(key='Section 1 Title').value,
        's1Description': HomeContent.objects.get(key='Section 1 Description').value,
        'guestSections': GuestSectionContent.objects.all(),
        'hostSections': HostSectionContent.objects.all(),
        'guestSliders': GuestSectionSlider.objects.all(),
        'guestSliderTitle': HomeContent.objects.get(key="Guest Slider Title").value,
        'hostSliders': HostSectionSlider.objects.all(),
        'hostSliderTitle': HomeContent.objects.get(key="Host Slider Title").value,
        'feedbacks': Feedback.objects.all(),
    }
    return render(request, 'index.html', context)


def contact(request):

    context = {
        'content': ContactContent.objects.get(key='Contact Content').value,
        'whatsapp': CompanyInformation.objects.get(key="Whatsapp Number").value,
        'email': CompanyInformation.objects.get(key="Email").value,
        'map': CompanyInformation.objects.get(key="Map").value,
        'address': CompanyInformation.objects.get(key="Address").value
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'aboutSections': AboutSectionContent.objects.all(),
        'teamMembers': TeamMember.objects.all(),
        'facebookLink': SocialLink.objects.get(social_name="Facebook"),
        'instagramLink': SocialLink.objects.get(social_name="Instagram"),
        'tiktokLink': SocialLink.objects.get(social_name="Tiktok"),
        'LinkedInLink': SocialLink.objects.get(social_name="LinkedIn"),
        'features': AboutWhyChooseUs.objects.all()
    }
    return render(request, 'about.html', context)


def blog(request):

    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def sendMessage(request):

    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')

    message = Message(firstname=firstname, lastname=lastname, email=email, phone_number=phone, message=message)
    message.save()

    send_message_notification_to_company(message)

    return redirect('about')