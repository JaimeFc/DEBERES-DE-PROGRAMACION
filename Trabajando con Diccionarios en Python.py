# Diccionario

informacion_personal = {
    'nombre':'Jaime',
    'edad':29,
    'ciudad':'Joya de los Sachas',
    'provincia':'Orellana',
}
print('BIENVENIDO AL')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente a la original.
informacion_personal['ciudad'] = 'Atacames'
informacion_personal['provincia'] = 'Esmeraldas'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Soldador'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0988360712'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')