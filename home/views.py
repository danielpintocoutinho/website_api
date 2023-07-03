from rest_framework.decorators import api_view
from rest_framework.response import Response

from projects.models import Project

@api_view(['GET'])
def home(request):
    summary = "Welcome! I am a Software Engineer interested in Real-Time Rendering, Web Development and Game Programming. In this site you can see some projects I have developed related to Computer Graphics, Image Processing and Artificial Intelligence, as showcased below. If you are interested in knowing more about me or how to get in touch, you can reach me through many ways here."
    covers = Project.objects.values_list('cover')
    data = {"summary": summary, "covers": covers}
    return Response(data=data)