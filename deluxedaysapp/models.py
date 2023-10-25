from django.db import models
from tinymce.models import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = models.TextField()
    read_duration = models.CharField(max_length=200, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Stat(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Stat"
        verbose_name_plural = "Stats"

class HomeContent(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
    
class GuestSectionContent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Guest Section"
        verbose_name_plural = "Guest Section"

class HostSectionContent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Host Section"
        verbose_name_plural = "Host Section"


class GuestSectionSlider(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Guest Slider"
        verbose_name_plural = "Guest Slider"


class HostSectionSlider(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Host Slider"
        verbose_name_plural = "Host Slider"

class Feedback(models.Model):
    username = models.CharField(max_length=300)
    feedback = models.TextField()
    profile_image = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.feedback

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

        
class TeamMember(models.Model):
    name = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to='profile-pictures', blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

class AboutSectionContent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "About - Section"
        verbose_name_plural = "About - Section"

class SocialLink(models.Model):
    social_name = models.CharField(max_length=300)
    url = models.CharField(max_length=3000)
    
    def __str__(self):
        return self.social_name
    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"

class Message(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    
    def full_name(self):
        return self.firstname + ' ' + self.lastname
    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

        
class ContactContent(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
        
class CompanyInformation(models.Model):
    key = models.CharField(max_length=300)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"
        
class EmailForNotification(models.Model):
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Email For Notification"
        verbose_name_plural = "Email For Notifications"

class AboutWhyChooseUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "About - Why Choose Us Section"
        verbose_name_plural = "About - Why Choose Us Sections"