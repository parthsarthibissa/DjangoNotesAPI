from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from rest_framework_swagger.views import get_swagger_view

@api_view(['GET'])
def getRoutes(req):
    routes = [
        {
        'name' : 'Hello',
        'external' : 'true'
    },{
        'name' : 'Hello',
        'external' : 'true'
    },{
        'name' : 'Hello',
        'external' : 'true'
    },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(req):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getNote(req,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(req):
    data = req.data

    note = Note.objects.create(
        name = data['name'],
        body = data['body']
    )

    serializer = NoteSerializer(note,many =False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(req,pk):
    data = req.data

    note = Note.objects.get(id = pk)
    serializer = NoteSerializer(note,data=req.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(req,pk):
    
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('NOTE ' + pk + ' was deleted')

