#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import random 
import os 

def limpia(): #FUNCION QUE LIMPIA LA PANTALLA 
    os.system('clear')

limpiar()

adivinar = random.randint(1,9) 
#print (adivinar)

print('***ADIVINA EL NUMERO***')

intentar = True 
cont = 1
while intentar:
    num=int(input('Adivina el numero que esta entre 1 y 9 = '))
    if num == adivinar:
        print ('Acertaste!!!! en '+ str(cont)+ ' intentos')
        continuar=raw_input('Desea volver a jugar? s/n = ')
        if continuar == 's':
            cont = 1
            adivinar = random.randint(1,9) 
            intentar == True
        else:
            break
    elif 8 >= abs(num-adivinar) >=4:
        print ('Estas muy lejos')
        cont= cont+1
        intentar = ('s' == raw_input('Intentar denuevo? s/n = '))
    elif 3 >= abs(num-adivinar) >= 2:
        print ('Estas cerquita!')  
        cont= cont+1     
        intentar = ('s' == raw_input('Intentar denuevo? s/n = '))
    elif abs(num-adivinar) == 1:
        print ('muy pero que muy cerquita')
        cont=cont+1
        intentar = ('s' == raw_input('Intentar denuevo? s/n = ' ))
print('Adios!!!')

