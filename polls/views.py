from django.http import HttpResponse


def index(request):
    return HttpResponse("hello,world, you're at polls index")


def name(request):
    return HttpResponse("hello,world, you're at polls name")


def detail(request, question_id):
    return HttpResponse("You're looking at the question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)