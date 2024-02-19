from django.shortcuts import render,get_object_or_404
from . models import Graphics_Design,Digital_Marketing,Writing_Translation,Music_Audio,Teachers,SocialAccounts,Contact,Blog
# Create your views here.


def index(request):
    context={
        'course1':Graphics_Design.objects.all(),
        'course2':Digital_Marketing.objects.all(),
        'course3':Writing_Translation.objects.all(),
        'course4':Music_Audio.objects.all(),
        'teachers':Teachers.objects.all(),
        'account':SocialAccounts.objects.all(),
    }
    return render(request ,'web/index.html',context)



def course(request):
    context={
        'course1':Graphics_Design.objects.all(),
        'course2':Digital_Marketing.objects.all(),
        'course3':Writing_Translation.objects.all(),
        'course4':Music_Audio.objects.all(),
    }
    return render(request ,'web/course.html',context)




def graphic_detail_view(request, product_id):
    course_graphic = get_object_or_404(Graphics_Design, id=product_id)
    context = {
        'graphic': course_graphic,
    }
    return render(request, 'web/course-details.html', context)

def digital_detail_view(request, product_id):
    course_digital = get_object_or_404(Digital_Marketing, id=product_id)
    context = {
        'digital': course_digital,
    }
    return render(request, 'web/course-details.html', context)

def writing_detail_view(request, product_id):
    course_translation = get_object_or_404(Writing_Translation, id=product_id)
    context = {
        'translation': course_translation,
    }
    return render(request, 'web/course-details.html', context)

def music_detail_view(request, product_id):
    course_music = get_object_or_404(Music_Audio, id=product_id)
    context = {
        'music': course_music,
    }
    return render(request, 'web/course-details.html',context)



def TeacherDetailView(request, product_id):
    teacher = get_object_or_404(Teachers, id=product_id)
    context = {
        'teacher': teacher,
    }
    return render(request, 'web/team-details.html',context)



def contact(request):
    if request.method=='POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact1=Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        Contact1.save()
    return render(request ,'web/contact.html')



def blog(request):
    context={
        'blog':Blog.objects.all(),
    }
    return render(request, 'web/blog.html',context)


def BlogDetailView(request, product_id):
    blog = get_object_or_404(Blog, id=product_id)
    context = {
        'blog': blog,
    }
    return render(request, 'web/blog-details.html',context)


def team(request):
    context={
        'teachers':Teachers.objects.all(),
    }
    return render(request ,'web/team.html',context)


def handler404(request, exception):
    return render(request, 'web/404.html', status=404)