yusuario='AB1012'
xusuario='ER3366'

def CDT(usuario,capital,tiempo):
    valortotal = (capital+(capital*y*tiempo/12))
    return valortotal
def CDTP(usuario,capital,tiempo):
    valorperdtot=int(capital-capital*x)
    return valorperdtot

#usuario=(str(input('Ingrese usuario ')))
if xusuario=='AB1012':
    print('BIENVENIDO')
    capital=(float(input('Ingrese el monto ')))
    tiempo=(float(input('Ingrese el tiempo en meses ')))
    x=0.02 #pérdida
    y=0.03 #interés
    
    if tiempo>2:
        resultado_de_funcion = CDT(xusuario,capital,tiempo)
        print(f'Para el usuario {yusuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: '+CDT('AB1012',1000000,3))
                           
    elif tiempo<=2:
        resultado_de_funcion1 = CDTP(yusuario,capital,tiempo)
        print(f'Para el usuario {yusuario} la cantidad de dinero a recibir, según el monto inicial PC {capital} en un tiempo de {tiempo} meses es ')
        print(CDTP('ER3366',650000,2))
    if xusuario='AB1012' xusuario or usuario==yusuario:

else:
    print('favor revisar su usuario pues es incorrecto')