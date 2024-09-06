from django.urls import path
from . import views

urlpatterns = [
    # Departamento URLs
    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('departamentos/<int:id_departamento>/', views.detalle_departamento, name='detalle_departamento'),
    path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
    path('departamentos/<int:id_departamento>/actualizar/', views.actualizar_departamento, name='actualizar_departamento'),
    path('departamentos/<int:id_departamento>/eliminar/', views.eliminar_departamento, name='eliminar_departamento'),
    
    # Curso URLs
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/<int:id_curso>/', views.detalle_curso, name='detalle_curso'),
    
    # Empleado URLs
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/<int:id_empleado>/', views.detalle_empleado, name='detalle_empleado'),
    
    # Estudiante URLs
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/<int:id_estudiante>/', views.detalle_estudiante, name='detalle_estudiante'),
    
    # Profesor URLs
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('profesores/<int:id_profesor>/', views.detalle_profesor, name='detalle_profesor'),
]
