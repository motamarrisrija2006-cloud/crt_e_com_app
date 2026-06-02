import json
from http import HTTPStatus
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


@csrf_exempt
@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            emp = Employee.objects.create(
                id=data.get("id"),
                name=data.get("name"),
                email=data.get("email"),
                phone=data.get("phone"),
                designation=data.get("designation"),
                emp_type=data.get("emp_type"),
                salary=data.get("salary")
            )
            return JsonResponse({"id": emp.id, "status": HTTPStatus.CREATED})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Only POST allowed"}, status=405)




def get_employee_details(request):
    try:
        employees = list(Employee.objects.all().values())
        return JsonResponse({"data": employees, "status": HTTPStatus.OK})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def get_emp_by_id(request, id):
    try:
        emp = Employee.objects.get(id=id)
        return JsonResponse({
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "phone": emp.phone,
            "designation": emp.designation,
            "emp_type": emp.emp_type,
            "salary":emp.salary,
        })
    except Employee.DoesNotExist:
        return JsonResponse({"error": "NotExist"}, status=404)


@csrf_exempt
def delete_by_id(request, id):
    try:
        emp = Employee.objects.get(id=id)
        emp.delete()
        return JsonResponse({"message": "Employee deleted", "status": HTTPStatus.OK})
    except Employee.DoesNotExist:
        return JsonResponse({"error": "NotExist"}, status=404)
