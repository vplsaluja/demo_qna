from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm
from django.contrib.auth.models import User
from .models import QuestionModel


# Create your views here.

def post_question(request):
    quesForm = QuestionForm(request.POST)
    if (request.method == 'POST'):

        if quesForm.is_valid():
            newForm = quesForm.save(commit=False)
            newForm.owner = User.objects.get(email=request.user.email)
            newForm.save()

        else:
            print("Form error")

    return render(request, 'question_form.html', {'quest_form': quesForm})


def go_home(request):
    return render(request, 'home.html')


def list_questions(request):
    questions = QuestionModel.objects.all()
    que = {
        "questions": questions
    }
    return render(request, 'list.html', que)


def view_question(request, pk):
    question = QuestionModel.objects.get(quest_id=pk)
    if (question is None):
        print('Question Not Found')
    else:
        que = {"ques": question}
    return render(request, 'question_view.html', que)


def edit_question(request, pk):
    question = QuestionModel.objects.get(quest_id=pk)
    # if (question is None):
    #     print('Question Not Found')
    # else:
    print("the title {}".format(question.title))
    # quesForm = QuestionForm({'title': question.title})
    instance = get_object_or_404(QuestionModel, quest_id=pk)
    quesForm = QuestionForm(request.POST or None, instance=instance)
    # quesForm.title = question.title
    if (request.method == 'POST'):
        if quesForm.is_valid():
            quesForm.save()
        # newForm.owner = User.objects.get(email=request.user.email)
        # newForm.save()

    else:
        print("Form error")

    return render(request, 'question_form.html', {'quest_form': quesForm})


def delete_question(request, pk):
    userId = request.user.id
    question = QuestionModel.objects.get(quest_id=pk)

    if (userId == question.owner_id):
        print("checking user id")
        question.delete()
        ques_dict = {'question': question}
        return render(request, 'question_delete.html', ques_dict)
    else:
        return render(request, 'question_delete.html')
