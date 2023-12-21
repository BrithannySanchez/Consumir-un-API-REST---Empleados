import requests

# Realizar solicitud GET al API
url ='https://dummy.restapiexample.com/api/v1/employees'
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    data = response.json()['data']

    # Obtener cantidad de empleados
    cantidad_empleados = len(data)

    # Obtener salarios y edades para cálculos
    salarios = [employee['employee_salary'] for employee in data]
    edades = [employee['employee_age'] for employee in data]

    # Calcular promedio de salario y edad
    promedio_salario = sum(salarios) / cantidad_empleados
    promedio_edad = sum(edades) / cantidad_empleados

    # Obtener salario mínimo y máximo
    salario_minimo = min(salarios)
    salario_maximo = max(salarios)

    # Obtener edad mínima y máxima
    edad_minima = min(edades)
    edad_maxima = max(edades)

    # Mostrar los resultados
    print(f"Cantidad de empleados: {cantidad_empleados}")
    print(f"Promedio de salario de los empleados: {promedio_salario}")
    print(f"Promedio de edad de los empleados: {promedio_edad}")
    print(f"Salario mínimo: {salario_minimo}")
    print(f"Salario máximo: {salario_maximo}")
    print(f"Edad mínima: {edad_minima}")
    print(f"Edad máxima: {edad_maxima}")


else:
    print('Error al obtener datos del API')
