from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response, render,get_object_or_404

# Create your views here.
from django.template import Template,Context
from django.utils.timezone import now
from django.views import generic
from .models import Question,Choice

def hello(request):
    time=now()
    template = Template("<html><body>My name is {{ time }}.</body></html>")
    context = Context({"time": time})
    m=template.render(context)
    return HttpResponse(m)

# def index(request):
#
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     template = loader.get_template('mybooks/index.html')
#     Context ={
#         'latest_question_list':latest_question_list,
#     }
#     return HttpResponse(template.render(context=Context,request=request))

def index(request):

    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('mybooks/index.html')
    Context ={
        'latest_question_list':latest_question_list,
    }
    return render(request,'mybooks/index.html',context=Context,status=200)

# def detail(request, question_id):
#
#     try:
#         question = Question.objects.get(pk=question_id)
#
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     print "question_id:",question_id
#     # return HttpResponse("You're looking at question %s." % question_id)
#     context={
#         'question':question
#     }
#     return render(request,'mybooks/details.html',context)

def detail(request, question_id):
    '''above is idiom method to manually raise a 404  and use objects.get()'''
    question = get_object_or_404(Question,pk=question_id)
    context={
        'question':question
    }
    return render(request,'mybooks/details.html',context)


def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)

    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request,'mybooks/result.html',{"question":question})
def vote(request, question_id):
    print request.POST,'||||||||||'
    choice_id=request.POST['choice']
    quetion = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = quetion.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request,'mybooks/deatil.html',{'question':quetion,'error_message': "You didn't select a choice."})

    select_choice.votes+=1
    select_choice.save()

    return HttpResponseRedirect(reverse('mybooks:results', args=(quetion.id,)))

class IndexView(generic.ListView):
    template_name = 'mybooks/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''return the last five published questions'''
        return Question.objects.order_by('-pub_data')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'mybooks/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'mybooks/result.html'


