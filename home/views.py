from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from home.serializers import HomeSerializer, AboutSerializer, SectionsSerializer
from projects.models import Project


class Home(GenericAPIView):
    serializer_class = HomeSerializer

    def get(self, request):
        summary = "Welcome! I am a Software Engineer interested in Real-Time Rendering," \
                  " Web Development and Game Programming. In this site you can see some projects" \
                  " I have developed related to Computer Graphics, Image Processing and Artificial Intelligence" \
                  ", as showcased below. If you are interested in knowing more about me or how to get in touch," \
                  " you can reach me through many ways here."
        covers = Project.objects.values_list('cover')
        data = {"summary": summary, "covers": covers}
        return Response(data=data)
    

class About(GenericAPIView):
    serializer_class = AboutSerializer

    def get(self, request):
        about = "Who am I? I’m a Brazilian computer scientist with a Master of Science in Computer Graphics." \
                " During my master’s I learned how to make statues and historical objects look pretty nice on a computer." \
                " Nowadays, I’m shifting my efforts to Real-time Rendering, Game Development and AI Programming. " \
                "I have been programming in C/C++ for over a decade now, but not in a professional environment. " \
                "I have a mild experience developing applications involving graphical interfaces using Qt. " \
                "I also have been programming in OpenGL for about 8 years, and a little less in GLSL. " \
                "I’ve been working professionally with Python for over 6 years now and some programming languages I have moderate knowledge about include JavaScript and C#." \
                "Contact\nemail: contact at dpcoutinho.com / daniel.pintocoutinho at gmail.com. You can also find me at Linkedin, Github, and Gitlab."
        image = "images/profile"
        data = {"about": about, "image": image}
        return Response(data=data)
    

class Sections(GenericAPIView):
    serializer_class = SectionsSerializer

    def get(self, request):
        data = {"sections": ['Home', 'Projects', 'Blog', 'About']}
        return Response(data=data)