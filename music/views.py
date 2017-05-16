from django.views import generic
from .models import Album, UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, UserProfileForm, EmailForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from website import settings

'''
class EMAILView(EmailMessage):
    def sendIt(self):
        template_name = 'music/email.html'
        to = ['pishtan231@gmail.com']
        from_email = 'pishtan231@gmail.com'
        subject = 'Automation_EMAIL'
        context = {'aaa' : 'This is the automation EMAIL with your details'}
        return self.send()
'''

class EmailFormView(View):
    form_class = EmailForm
    template_name = 'music/email.html'

    # display blank form
    def get(self, request):
        emailform = self.form_class(None)
        return render(request, self.template_name, {'data': {'emailform': emailform }})

    def post(self, requset):
        emailform = self.form_class(requset.POST)

        if emailform.is_valid():

            subject = emailform.cleaned_data['subject']
            message = emailform.cleaned_data['message']
            sender = emailform.cleaned_data['sender']
            cc_myself = emailform.cleaned_data['cc_myself']

            recipients = ['pishtan231@gmail.com']

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/music/')
        else:
            return HttpResponseRedirect('/music/email/')
    '''
            # Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:
                    login(requset, user)
                    return redirect('music:index')
        return render(requset, self.template_name, {'form': form})
'''

class IndexView(generic.ListView, EmailFormView):
    template_name = 'music/index.html'
    email_template_name = 'music/email.html'
    context_object_name = 'data'
    form_class = EmailForm

    def get_queryset(self):
        emailform = self.form_class(None)
        return {
            'all_albums': Album.objects.all(),
            'emailform': emailform
        }



class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    profile_form = UserProfileForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        formTwo = self.profile_form(None)

        return render (request, self.template_name, {'form': form, 'formTwo': formTwo})


    def post(self, requset):
        form = self.form_class(requset.POST)
        formTwo = self.profile_form(requset.POST)

        if (form.is_valid() and formTwo.is_valid()):



            # cleaned (normalized) data


            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            encrypt = formTwo.cleaned_data['encrypt']

            user = form.save(commit=False)

            user_extend = formTwo.save(commit=False)
            #indexOfMethod = settings.PASSWORD_HASHERS.index('django.contrib.auth.hashers.{}'.format(user_extend.encrypt))
            #tempMethod = settings.PASSWORD_HASHERS[0]
            if user_extend.encrypt == 'MD5PasswordHasher':
                settings.PASSWORD_HASHERS[0] = 'django.contrib.auth.hashers.MD5PasswordHasher'
             #   settings.PASSWORD_HASHERS[indexOfMethod] =  tempMethod
            if user_extend.encrypt == 'PBKDF2PasswordHasher':
                settings.PASSWORD_HASHERS[0] = 'django.contrib.auth.hashers.PBKDF2PasswordHasher'
              #  settings.PASSWORD_HASHERS[indexOfMethod] = tempMethod
            if user_extend.encrypt == 'SHA1PasswordHasher':
                settings.PASSWORD_HASHERS[0] = 'django.contrib.auth.hashers.SHA1PasswordHasher'
               # settings.PASSWORD_HASHERS[indexOfMethod] = tempMethod


            user.set_password(password)
            user.save()

            user_extend.user = user
            user_extend.save()

            # Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)


            if user is not None:

                if user.is_active:
                    login(requset, user)
                    return redirect('music:index')
        return render(requset, self.template_name, {'form': form, 'formTwo': formTwo})
        '''
        def get_context_data(self, **kwargs):
            context = super(UserFormView, self).get_context_data(**kwargs)
            context['encrypt'] = 'hi1223344'
            return context
        '''