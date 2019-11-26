from django.contrib import admin

from .models import Persona, Estudiante, Egresados, Trabajador, Oficio, Salario


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Apellido', 'rfc', 'edad')
    search_fields = ['nombre', 'Apellido', 'sexo']  #definir criterios de busqueda
    #fields = ('nombre', 'Apellido', 'dob', 'rfc', 'sexo', 'edo_civil')
    list_filter = ['Apellido', 'sexo']  #filtrado de información

    def edad(self, obj):
        return obj.calcEdad

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'matricula', 'area', 'grado', 'promedio')
    search_fields = ['area', 'grado']
    list_filter = ['area', 'grado', 'promedio']


class EgresadoAdmin(admin.ModelAdmin):
    list_display = ('generacion', 'titulo')
    search_fields = ['generacion', 'titulo']
    list_filter = ['generacion', 'titulo']


class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('antiguedad', 'areat', 't_jornada')
    search_fields = ['areat', 't_jornada']
    list_filter = ['areat', 't_jornada', 'tiene_oficio']
    #form = TrabajadorForm

class OficioAdmin(admin.ModelAdmin):
    #list_display = ('oficio_n')
    #search_fields = ['oficio_n']
    #list_filter = ['oficio_n', 'experiencia']
    #form = OficiosForm
    pass


class SalarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'hrs_laboradas', 'salario')
    #search_fields = ['hrs_laboradas']
    #list_filter = ['hrs_laboradas']
    def salario(self, obj):
        return obj.salario
    pass

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Egresados, EgresadoAdmin)
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Oficio, OficioAdmin)
admin.site.register(Salario, SalarioAdmin)
