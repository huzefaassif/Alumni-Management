from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import BlogForm

# Create your views here.

def index(request):
    return render(request,"alumni/index.html")

def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,"alumni\index.html", context)

def home(request):
    context ={}
    context['user'] = request.user
    context['student'] = Student.objects.all()
    context['alumni'] = Alumni.objects.all()
    status = '1'

    if request.user.is_authenticated:
        student = Student.objects.all()
        alumni = Alumni.objects.all()

        for data in student:
            if request.user.username == data.user.username:
                status = data.status



        if status == '0':
            return render(request, 'alumni/studenthome.html', context)
        else:
            return render(request, 'alumni/alumnihome.html', context)

    else:
        return render(request, 'alumni/index.html')


def logout_request(request):
        logout(request)
        return render(request, 'alumni/index.html')

def studentupdate(request):
    context ={}
    if request.user.is_authenticated:
        return render(request, 'alumni/studentprofileupdate.html', context)

def alumniupdate(request):
    context ={}
    if request.user.is_authenticated:
        return render(request, 'alumni/alumniprofileupdate.html', context)

def searchalumni(request):
    context ={}
    if request.user.is_authenticated:
        context['alumni'] = Alumni.objects.all()
        return render(request, 'alumni/searchalumni.html', context)


def contactus(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'alumni/contactus.html', context)


def aboutus(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'alumni/aboutus.html', context)



def studentprofileupdate(request):
    student=Student.objects.all()
    context = {}
    a = ""
    if request.user.is_authenticated:

        for data in student:
            if request.user.username == data.user.username:
                if request.POST.get('updateemail') is not a:
                    data.email=request.POST.get('updateemail')
                if request.POST.get('updatehobbies') is not a:
                    data.hobbies=request.POST.get('updatehobbies')
                if request.POST.get('updatetechnologies') is not a:
                    data.tech_known=request.POST.get('updatetechnologies')
                if request.POST.get('updateinternships') is not a:
                    data.internships=request.POST.get('updateinternships')
                if request.POST.get('updateaboutyou') is not a:
                    data.About_you=request.POST.get('updateaboutyou')
                data.save()

        return render(request, 'alumni/updatedsuccessfully.html', context)

def alumniprofileupdate(request):
    alumni=Alumni.objects.all()
    context = {}
    a = ""
    if request.user.is_authenticated:

        for data in alumni:
            if request.user.username == data.user.username:
                if request.POST.get('updateemail') is not a:
                    data.official_id=request.POST.get('updateemail')
                if request.POST.get('updatejob') is not a:
                    data.Current_job=request.POST.get('updatejob')
                if request.POST.get('updatejobsector') is not a:
                    data.Job_Sector=request.POST.get('updatejobsector')
                if request.POST.get('updateyears') is not a:
                    data.years_of_experience=request.POST.get('updateyears')
                if request.POST.get('updatetech') is not a:
                    data.tech_known=request.POST.get('updatetech')
                if request.POST.get('updateinternships') is not a:
                    data.internships=request.POST.get('updateinternships')
                if request.POST.get('updatepcompany') is not a:
                    data.Previous_company=request.POST.get('updatepcompany')
                if request.POST.get('updateccompany') is not a:
                    data.current_company =request.POST.get('updateccompany')
                if request.POST.get('updatehobbies') is not a:
                    data.hobbies =request.POST.get('updatehobbies')
                if request.POST.get('updateaboutyou') is not a:
                    data.About_you=request.POST.get('updateaboutyou')
                data.save()

        return render(request, 'alumni/updatedsuccessfully.html', context)


def viewprofile(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['student'] = Student.objects.all()
        context['alumni'] = Alumni.objects.all()
        data = request.POST.get('sub')
        datas = request.POST.get('search')
        context['infos'] = datas
        context['info'] = data

        for s in Alumni.objects.all():
            if s.user.username == data or s.user.username == datas:
                s.noofviews = s.noofviews + 1
                s.save()






        return render(request, 'alumni/viewprofile.html', context)

def noofhits(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user

        context['alumni'] = Alumni.objects.all()


        return render(request, 'alumni/noofviews.html', context)

def cards(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user

        context['alumni'] = Alumni.objects.all()


        return render(request, 'alumni/cards.html', context)

def cardviewprofile(request):
    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['student'] = Student.objects.all()
        context['alumni'] = Alumni.objects.all()
        return render(request, 'alumni/cardviewprofile.html', context)

def cardviewprofile2(request):

    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['student'] = Student.objects.all()
        context['alumni'] = Alumni.objects.all()
        return render(request, 'alumni/cardviewprofile2.html', context)


def branchfilter(request):
    context ={}
    if request.user.is_authenticated:
        context['alumni'] = Alumni.objects.all()
        context['CSE']=request.GET.get("COMPUTER_SCIENCE")
        context['IT']=request.GET.get("INFORMATION_TECHNOLOGY")
        context['EC']=request.GET.get("ELECTRONICS")
        context['MECH']=request.GET.get("MECHANICAL")
        context['CE']=request.GET.get("CIVIL")

        return render(request, 'alumni/branchfilter.html', context)

def companyfilter(request):
    context ={}
    if request.user.is_authenticated:
        context['alumni'] = Alumni.objects.all()
        context['Worldpay'] = request.GET.get("Worldpay")
        context['Infobeans'] = request.GET.get("Infobeans")
        context['TCS'] = request.GET.get("TCS")
        context['BSNL'] = request.GET.get("BSNL")
        context['Flipkart'] = request.GET.get("Flipkart")
        context['Thermax'] = request.GET.get("Thermax")
        context['Maruti'] = request.GET.get("Maruti")

        context['Tikona'] = request.GET.get("Tikona")
        return render(request, 'alumni/companyfilter.html', context)

def viewblog(request):
    blogs = Blog.objects.all()
    context = {}
    context['blogs'] = blogs

    if request.user.is_authenticated:

        return render(request, 'alumni/viewblog.html', context)

def searchstudents(request):
    context ={}
    if request.user.is_authenticated:
        context['student'] = Student.objects.all()
        return render(request, 'alumni/searchstudents.html', context)


def studentviewprofile(request):

    context = {}
    if request.user.is_authenticated:
        context['user'] = request.user
        context['student'] = Student.objects.all()
        context['alumni'] = Alumni.objects.all()
        data = request.POST.get('sub')
        datas = request.POST.get('search')
        context['infos'] = datas
        context['info'] = data







        return render(request, 'alumni/studentviewprofile.html', context)

def addchat(request):
    if request.user.is_authenticated:

        msg=request.GET.get('msg')

        if msg == "":
            pass
        else:
            print(request.user)
            obj = Chat(user=request.user, message=msg)
            obj.save()
        context = {}
        context['chat'] = Chat.objects.all()
        return render(request, 'alumni/chats.html', context)

def chats(request):

    context = {}
    if request.user.is_authenticated:
        context['chat'] = Chat.objects.all()




        return render(request, 'alumni/chats.html',context )


def signupalumni(request):

    return render(request, 'alumni/signupalumni.html')


def signupstudent(request):
    return render(request, 'alumni/signupstudent.html')

def signedupsuccessfully(request):
    return render(request, 'alumni/signedupsuccessfully.html')

def blog_list(request):

    blogs = Blog.objects.all()
    context={}
    context['blogs']=blogs

    return render(request , 'alumni/blog_list.html',context)


def upload_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form=BlogForm()


    return render(request, 'alumni/upload_blog.html',{'form' : form,'user': request.user})


def delete_blog(request,pk):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        blog.delete()
    return redirect('blog_list')




