usuario='AB1012'
y=0.03 #interés
capital=1000000
tiempo=3

def CDT(usuario,capital,tiempo):
    valortotal = (capital+(capital*y*tiempo/12))
    return valortotal

valortotal = CDT('AB1012',1000000,3)

print(f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valortotal}')
print(' ')
usuario='QW3456'
x=0.02 #pérdida
capital=5000000
tiempo=2

def CDT(usuario,capital,tiempo):
    valorperdtot = (capital-capital*x)    
    return valorperdtot

valorperdtot = CDT('QW3456',5000000,2)
print(f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorperdtot}')
print(' ')