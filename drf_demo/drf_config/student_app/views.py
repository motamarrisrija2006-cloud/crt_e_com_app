from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from student_app.api_exception import StudentNotFoundException
from student_app.models import Student
from student_app.student_serializable import StudentSerializer

@api_view(['POST','GET','PUT','DELETE'])
def student_view(request):
    if request.method == 'POST':
        data = request.data
        student_serializer = StudentSerializer(data=data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response({"message": "Data is not valid"})
@api_view(['PUT'])
def update_student(request,id):
    student_object=Student.objects.get(id=id)
    student_serializer = StudentSerializer(student_object,request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response({
            "message": "Student has been updated successfully",
            "new_data": student_serializer.data
        })
    return Response(student_serializer.errors)

@api_view(['DELETE'])
def delete_by_id(request,id):
    student_object=Student.objects.get(id=id)
    student_object.delete()
    return Response({"message": "Student has been deleted successfully"})

@api_view(['GET'])
def view_all_student(request):
    student_objects = Student.objects.all()
    serializer = StudentSerializer(student_objects,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_by_id(request,id):
    try :
        try:
            student_object = Student.objects.get(id=id)
            if student_object.id != id:
                raise StudentNotFoundException()
        except StudentNotFoundException as e:
            return Response({"message": e.default_detail})
        if student_object is not None:
            serializer = StudentSerializer(student_object)
            return Response(serializer.data)
        return Response({"message": "Student does not exist"})
    except StudentNotFoundException as e:
        return Response(e.args)
    except Exception as e:
        raise StudentNotFoundException()
