s = 'We promptly judged antique ivory buckles for the prize'

alphabet = [chr(i) for i in range(97, 123)]

s = s.lower()
s_lista = s.split(' ')
s_cadena = ''.join(s_lista)

salida = str
for i in alphabet:
    if not i in s_cadena:
        salida = 'not pangram'
        break
    else:
        salida = 'pangram'
            
print(salida)

print(s_cadena)
print(alphabet)