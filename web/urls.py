
from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path("",views.index,name='index'),
    path("course",views.course,name='course'),
    path("contact",views.contact,name='contact'),
    path("blog",views.blog,name='blog'),
    path("team",views.team,name='team'),



    path('teacher-detail/<int:product_id>/',views.TeacherDetailView, name='teacher-detail'),
    path('course_graphic/<int:product_id>/',views.graphic_detail_view, name='graphic'),
    path('course_digital/<int:product_id>/',views.digital_detail_view, name='digital'),
    path('course_translation/<int:product_id>/',views.writing_detail_view, name='translation'),
    path('course_music/<int:product_id>/',views.music_detail_view, name='music'),
    path('blog-detail/<int:product_id>/',views.BlogDetailView, name='blog-detail'),

     
]
handler404 = 'web.views.handler404'