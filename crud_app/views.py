from django.shortcuts import render,redirect

from .models import Student

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        Student.objects.create(name=name, email=email, age=age, salary=salary, address=address,image=image)
        return redirect('student_list')
    return render(request, 'student_create.html')

def student_update(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.salary = request.POST.get('salary')
        student.address = request.POST.get('address')
        student.save()
        return redirect('student_list')
    return render(request, 'student_update.html', {'student': student})

def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})