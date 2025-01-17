# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse , Http404 ,HttpResponseRedirect
# from .models import Question,Choices
# from django.template import loader
# from django.urls import reverse


# # Create your views here.

# def home(request):
#     # first method
#     latest_question = Question.objects.order_by("-pub_date")[:5]
#     # output = " ,".join([q.question_text for q in latest_question])
#     # template = loader.get_template("polls/index.html")
#     # context  = {
#     #     'latest_question': latest_question,
#     #     'name': "vishu"  # for testing purpose only, replace with actual name.
#     # }
#     # # return HttpResponse(f"This is a simple example {name}  name.")
#     # return HttpResponse(template.render(context,request))
#     # return HttpResponse(latest_question)
    
#     # second method
    
#     context={
#         'latest_question': latest_question,
#         'name': "vishu"  # for testing purpose only, replace with actual name.
#     }
#     return render(request, "polls/index.html", context)
    
    
# def detail(request,question_id):
#     # return HttpResponse(f"You're looking at question {question_id}")
    
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
    
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request,question_id):
#     question = Question.objects.get(pk=question_id)
#     return render(request, "polls/results.html",{"question":question})


    
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choices, Question
 
 
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detailm.html"
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    print(request.POST)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        