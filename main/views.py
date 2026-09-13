from django.shortcuts import render
from main.models import Experience, Project  


def show_main(request):
  context = {
      'name': 'Burhan',
      'npm': '2206000000',
      'study_program': 'S1 Ilmu Komputer',
      'bio': (
          'Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik pada'
          ' pengembangan perangkat lunak dan pendidikan.'
      ),
  }
  return render(request, 'index.html', context)


def show_experience(request):
  context = {
      'name': 'Burhan',
      'experience_list': Experience.objects.all(),
  }
  return render(request, 'experience.html', context)


def show_project(request):
  project_list = Project.objects.all()
  context = {
      'project_list': project_list,
  }
  return render(request, 'project.html', context)