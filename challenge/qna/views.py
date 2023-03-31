from django.shortcuts import render, redirect
from django.http import HttpResponse
# ipmorts for user actions 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Question, Answer
from django.contrib.auth.decorators import login_required as lr
from django.views.decorators.csrf import csrf_exempt as ce


# Create your views here.
def index(request):
    return HttpResponse('''
    <h1>welcome home</h1><br>
    <p></p>login
    <a href="localhost:8000/auth/login">login</a>
    <p></p>register
    ''')
@ce
def register(request):
    if request.method == 'POST':
        this_username=request.POST['username']
        this_password=request.POST['password']
        # to check if a user with above details i.e. name exists
        if User.objects.filter(username = this_username).exists():
            print('user exists')
            # return redirect('register')
            return HttpResponse('user exists please try with a different username')
        else:
            user= User.objects.create_user(username=this_username, password=this_password)
            user.save()
            print(user)
            # return redirect('auth/login')
            return HttpResponse('user'+ this_username +'created!')
    
@ce
def userlogin(request):
    if request.method == 'POST':
        this_username=request.POST['username']
        this_password=request.POST['password']
        user=authenticate(username=this_username,password=this_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect('userhome')
                return HttpResponse(user + 'log in successfull')
        else:
            print('error at userlogin')
            # return HttpResponse('an error occured at login page')
            return HttpResponse('error on login')
    
# to fetch all questions
def questions(request):
    if request.method=='GET':
        query_fetch=Question.objects.all()
        return HttpResponse(query_fetch)
    elif request.method=='POST':
        if request.user.is_authenticated:
                # not sure
            this_author=request.user.id
            this_content=request.POST['content']
            # author=
            query_save=Question(author=this_author,content=this_content)
            query_save.save() 
            return HttpResponse(query_save) 
    else:
        return HttpResponse('error occured in questions')
@lr
# fetch specific question, delete spec question
# used **kwargs ha
def question(request, questionId):
    if request.method=='GET':
        questionId
        print(questionId)
        try:
            q=Question.objects.filter(id=questionId)
            # used during debug
            # print('passed try block')
            # get(id=this_question_id)
            # filter(question_id=this_question_id)
            if any(q) :
                print(q)
                return HttpResponse(q)
            else:
                return HttpResponse('question does not exist')    
        except:
            # breakpoint() #sleep()
            return ('error ocured in question try block')    
    elif request.method=='DELETE':
        if request.user.is_authenticated:
            this_author=request.user
            query=Question.objects.filter(author=this_author,id=questionId)
            query.delete()
            return HttpResponse(str(questionId)+' deleted')
            # return HttpResponse('could not delete question'+str(questionId))
                
            # queryIds=[x for x in query.id]   
        else:
            return HttpResponse('could not perform delete operation')
    else:
        return HttpResponse('HTTP method not handled')                

@lr
@ce
def answer(request,questionId):
    if request.method=='POST' and request.user.is_authenticated:
        this_author=request.user
        this_content=request.POST.get('content')
        answer=Answer(author=this_author,question_id=questionId,content=this_content)
        answer.save()
        return HttpResponse(answer)
    else:
        return HttpResponse('no answers found')
@lr
def answers(request,questionId,answerId):
    if request.method=='PUT' and request.user.is_authenticated:
        this_author=request.user
        this_content=request.PUT.get('content')
        answer=Answer.objects.filter(author=this_author,question_id=questionId,answerId=answerId)
        answer.content=this_content
        answer.save()
        return HttpResponse(answer)
    elif request.method=='DELETE' and request.user.is_authenticated:
        this_author=request.user
        answer=Answer.objects.filter(author=this_author,id=answerId,question_id=questionId)
        answer.delete()
        return HttpResponse('answer deleted')
    # get request. take question id 
    else: 
        return HttpResponse('http put/delete method not handled')
