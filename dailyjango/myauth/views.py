from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import UserCreateForm
# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login,logout

# class IndexView(CreateView):
#     template_name = 'myauth/regitser.html'
#     render()

def register(request):
    if request.method == 'POST':
        # print "hahah"
        sss = UserCreateForm(request.POST)
        if sss.is_valid():
            sss.save()
            return HttpResponseRedirect('/register/registrationok/')

    else:
        form = UserCreateForm()

        token = {}
        token.update(csrf(request))
        token['form'] = form
        return render_to_response('myauth/register.html', token)


def registration_ok(request):

    content = {'username':request.user.username}
    print content
    return render_to_response('myauth/registration_ok.html',context=content)


def mylogin(request):
    print "ssss"
    if request.method=="POST":
        print "mmmmm"
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response("myauth/loginok.html",context={"msg":"ok"})
            else:
                pass
        else:
            error_message = "invalid user"
            return render_to_response('myauth/log_invalid',context={"msg":error_message})
    else:
        return render_to_response('myauth/login.html',context_instance=RequestContext(request))

def mylogout(request):
    logout(request)
    pass