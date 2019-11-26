from django.db import models
from datetime import date

sexo_c = [('F', 'FEMENINO'), ('M', 'MASCULINO')]
edo_c = [('S', 'SOLTER@'), ('C', 'CASAD@'), ('D', 'DIVORCIAD@'), ('V', 'VIUD@'), ('EC', 'EN UNA RELACION COMPLICADA')]
grado_c = [('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('EST', 'Estadias')]
area_c = [('MA', 'MECATRONICA'), ('MI', 'MANTENIMIENTO'), ('TI', 'TECNOLOGIAS DE LA INFORMACION'), ('DN', 'DESARROLLO DE NEGOCIOS'), ('LI', 'LENGUA INGLESA')]
area_t = [('AC', 'ACADEMIA'), ('LE', 'LENGUAS EXTRANJERAS'), ('MI', 'MANTENIMIENTO'), ('AD', 'ADMINISTRATIVAS')]
jornada_c = [('TC', 'TIEMPO COMPLETO'), ('MD', 'MEDIO TIEMPO')]
titulo_status = [('T/C' 'TITULADO'), ('T/T', 'TITULO EN TRAMITE'), ('N/A', 'NINGUNO')]
#tipo_user = [('1', 'ESTUDIANTE'), ('2', 'TRABAJADOR')]

class Persona(models.Model):

    #t_user = models.CharField(max_length=1, null=False, blank=False, default=False, choices=tipo_user)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    Apellido = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField()  #CharField(max_length =10, Null = False, blank = False)
    rfc = models.CharField(max_length=13, null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=sexo_c)
    edo_civil = models.CharField(max_length=1, null=False, blank=False, choices=edo_c)

    #def __str__(self):
        #return '{}{}'.format(self.nombre, self.Apellido)
        #pass

    @property
    def calcEdad(self):
        days_in_y = 365.2425
        age = int((date.today() - self.dob).days / days_in_y)
        return age


class Estudiante(Persona): #Persona
    matricula = models.CharField(max_length=19, null=False, blank=False)
    grado = models.CharField(max_length=2, null=False, blank=False, choices=grado_c)
    area = models.CharField(max_length=2, null=False, blank=False, choices=area_c)
    promedio = models.FloatField(null=False, blank=False)


    #def __str__(self):
       # return '{}{}'.format(self.grado, self.area)
        #pass

class Egresados(Estudiante):
    generacion = models.CharField(max_length=19, null=False, blank=False)
    no_cedula = models.CharField(max_length=39, null=False, blank=False)
    titulo = models.CharField(max_length=4, null=False, blank=False)

    def __str__(self):
        return  '{}{}'.format(self.generacion, self.titulo)
        #pass


class Trabajador(Persona): #Persona
    noEmpleado = models.CharField(max_length=20, null=False, blank=False)
    antiguedad = models.IntegerField(null=False, blank=True)
    areat = models.CharField(max_length=2, null=False, blank=False, choices=area_t)
    t_jornada = models.CharField(max_length=2, null=False, blank=False, choices=jornada_c)
    tiene_oficio = models.BooleanField(default=False)
    #oficios = models.ManyToManyField('Oficio')
    #personas = models.ManyToManyField('Persona')

    def __str__(self):
        return '{}{}'.format(self.areat, self.t_jornada)
        #pass

class Oficio(Trabajador):
    oficio_n = models.CharField(max_length=30, null=False, blank=False)
    experiencia = models.IntegerField(null=False, blank=False)
    #trabajador = models.ManyToManyField('Trabajador')

    #def __str__(self):
       # return '{}{}'.format(self.oficio_n)
        #pass


class Salario(Trabajador):
    hrs_laboradas = models.IntegerField(null=False, blank=False)
    sueldo_hr = models.FloatField(null=False, blank=False)

    #def __str__(self):
     #   return '{}{}'.format(self.hrs_laboradas, self.sueldo_hr)
        #pass


    @property
    def salario(self):
        s_bruto = self.sueldo_hr * self.hrs_laboradas * 4
        isr_month = (s_bruto * 0.7)
        s_total = s_bruto - isr_month
        return s_bruto