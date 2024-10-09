class Alumno:
    def __init__(self):
        # Atributos privados inicializados como vacíos o valores por defecto
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer los valores de los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores de los atributos
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre


# Diccionario para almacenar los alumnos
alumnos_dict = {}

# Bucle para ingresar 3 alumnos desde teclado
for i in range(3):
    alumno = Alumno()  # Crear un objeto Alumno vacío

    # Ingresar datos por teclado
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i + 1}: ")
    apellido_materno = input(f"Ingrese el apellido materno del alumno {i + 1}: ")
    no_control = input(f"Ingrese el número de control del alumno {i + 1}: ")
    semestre = int(input(f"Ingrese el semestre del alumno {i + 1}: "))

    # Asignar valores a los atributos usando los métodos set
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

    # Guardar el objeto alumno en el diccionario
    alumnos_dict[alumno.get_no_control()] = alumno

# Verificar los alumnos almacenados
print("\n--- Lista de Alumnos ---")
for no_control, alumno in alumnos_dict.items():
    print(f"No. Control: {no_control}, Nombre: {alumno.get_nombre()} {alumno.get_apellido_paterno()} "
          f"{alumno.get_apellido_materno()}, Semestre: {alumno.get_semestre()}")
