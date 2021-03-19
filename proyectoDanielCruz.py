#Proyecto Pensamiento computacional para la ingeniería
#Daniel Cruz Arciniega
#A01701370
#21 Blackjack
#La idea es hacer un programa en el que el usuario juegue el famoso juego de cartas 21
#Se usaran variables aleatorias y operaciones matemáticas básicas

import random  #se importa la libreria random para poder utilizar variables aleatorias
import tkinter as tk #se importa la librería tkinter para poner imagenes (competencia faltante)

#La biblioteca tkinter es usada para crear una portada en donde aparezcan las intrucciones
from tkinter import *
from tkinter import messagebox
#Funciones

def As1(carta1): #Función para que el usuario le de un valor de 1 u 11 a la carta "as" en caso de que la obtenga si en el número aleatorio sale 11
    print("Tienes un as y", carta2, "¿usar al as como 1 u 11?")
    use=int(input())
    if use==1:
        return 1
def As2(carta2): #Función para que el usuario le de un valor de 1 u 11 a la carta "as" en caso de que la obtenga si en el número aleatorio sale 11
    print("Tienes",carta1, "y un as ¿usar al as como 1 u 11?")
    use=int(input())
    if use==1:
        return 1
def As3(carta3): #Función para que el usuario le de un valor de 1 u 11 a la carta "as" en caso de que la obtenga si en el número aleatorio sale 11
    print("Te ha tocado un as ¿usar al as como 1 u 11?")
    use=int(input())
    if use==1:
        return 1

def ganador(suma,suma_jarvis): #Función para determinar quién gana la ronda en base a la suma de ambos
    if suma>suma_jarvis and suma<21:
        return 'user'
    elif suma_jarvis>suma and suma_jarvis<21:
        return 'jarvis'
    elif suma==21:
        return 'b_user'
    elif suma_jarvis==21:
        return 'b_casa'
    else:
        return 'empate'

def funcion_add_jarvis(suma_jarvis): #Esta función es clave para que Jarvis decida si quiere agregar cartas a su juego
    decision=''           #Utiliza la librería random para que la computadora se decida por la variable a tomar
    d1=['si','si','no','si',]   #No es totalmente aleatorio, ya que la decisión se basa en la suma que tenga
    d2=['si','si','no','si','si','no']  
    d3=['si','si','si','no','no']
    d4=['no','si','si','no','no']
    d5=['no','no','no','no','si']
    if suma_jarvis<=13:
        decision='si'
    elif suma_jarvis==14:
        decision=random.choice(d1)
    elif suma_jarvis==15:
        decision=random.choice(d2)
    elif suma_jarvis==16:
        decision=random.choice(d3)
    elif suma_jarvis==17:
        decision=random.choice(d4)
    elif suma_jarvis>=18 and suma_jarvis<19:
        decision=random.choice(d5)
    elif suma_jarvis<=19:
        decision='no'
    return decision

def Saludo(): #Esta función sirve para que jarvis diga algo diferente al inicio de cada ronda, para ello se usa "Random"
    x=[1,2,3,4]
    reto=['no','si','no','no']
    retar=random.choice(reto)
    preg=''
    p=random.choice(x)
    if p==1:
        preg='¿Desea iniciar señor?'
    elif p==2:
        preg='¿Está usted listo?'
        if retar=='si':
            preg=preg+' para perder.'
    elif p==3:
        preg='¿Comenzamos?'
    elif p==4:
        preg='¿Listo?'
        if retar=='si':
            preg=preg+' esto será fácil.'
    y=[1,2,3]
    saludo=random.choice(y)
    s=''
    if saludo==1:
        s='Buenas tardes'
    elif saludo==2:
        s='Que tal'
    elif saludo==3:
        s='Saludos'
    decir="Jarvis: "+s+" "+preg
    return decir
    
portada=tk.Tk() 
portada.geometry('10000x1000')

imagen=tk.PhotoImage(file="bj.png")
imagen=imagen.subsample(3,3)
fondo=tk.Label(portada,image=imagen)
fondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)

etq1=tk.Label(portada,text="Blackjack",font=("Times New Roman",50),bg='black',fg='white')
etq1.pack(fill=tk.X)
etq2=tk.Label(portada,text="Daniel Cruz Arciniega",font=("Times New Roman",20),bg='black',fg='white')
etq2.pack(padx=0,pady=10)
etq3=tk.Label(portada,text="A01701370",font=("Times New Roman",20),bg='black',fg='white')
etq3.pack(padx=0,pady=10)
etq4=tk.Label(portada,text="Bienvenido, se jugarán las manos que usted desee",font=("Times New Roman",16),bg='black',fg='white')
etq4.pack()
etq5=tk.Label(portada,text="O hasta que la baraja se quede sin cartas suficientes",font=("Times New Roman",16),bg='black',fg='white')
etq5.pack()
etq6=tk.Label(portada,text="Usted gana si la suma de sus cartas da un valor igual a 21",font=("Times New Roman",16),bg='black',fg='white')
etq6.pack()
etq7=tk.Label(portada,text="Si se pasa de la suma aunque sea por un número usted pierde",font=("Times New Roman",16),bg='black',fg='white')
etq7.pack()

def cerrar():
    portada.destroy()

boton=tk.Button(portada,text="Continuar", fg='black',command=cerrar)
boton.pack()

portada.mainloop()

win=tk.Tk() 
win.geometry('10000x1000')
win.configure(background='black')

etq8=tk.Label(win,text="Esta es una baraja de cartas",font=("Times New Roman",16),bg='black',fg='white')
etq8.pack()

imagen1=tk.PhotoImage(file="cards.png")
imagen1=imagen1.subsample(1,1)
fondo1=tk.Label(win,image=imagen1)
fondo1.pack()

etq9=tk.Label(win,text="Si le toca un As podrá usarlo como 1 u 11 según le convenga",font=("Times New Roman",16),bg='black',fg='white')
etq9.pack()
etq10=tk.Label(win,text="Las cartas reales (J,Q y K) tendrán un valor numérico de 10",font=("Times New Roman",16),bg='black',fg='white')
etq10.pack()
etq11=tk.Label(win,text="Jugará contra Jarvis, la Inteligencia Artificial que representa a la casa",font=("Times New Roman",16),bg='black',fg='white')
etq11.pack()
etq12=tk.Label(win,text="Al final del juego, quien junte más puntos después de cada ronda gana",font=("Times New Roman",16),bg='black',fg='white')
etq12.pack()
etq12=tk.Label(win,text="Buena suerte",font=("Times New Roman",16),bg='black',fg='white')
etq12.pack()

def continuar():
    win.destroy()

boton1=tk.Button(win,text="Continuar", fg='black',command=continuar)
boton1.pack()

win.mainloop()

while True: #Corrección de competencia 3 en entregable de listas. Con este ciclo, si en "jugar" se introduce otro valor que no sea "si" o "no" el ciclo se repetira
    print(Saludo())
    jugar=str(input("(si o no)   "))
    
    puntos_user=0
    puntos_jarvis=0
    baraja=[]

    for elem in range(4):#Hay cuatro formas en las barajas, Rombos, Diamantes, Espadas y Corazones
        for elem in range(2,12): #Por cada una de esas formas se agrega una carta del 2 al 11 siendo 11 el As
            baraja.append(elem)
    for elem in range(12): #Hay 3 cartas reales (J,Q,K) por cada una de las 4 formas
        baraja.append(10) #En 21, las cartas reales toman un valor de 10
    
    #La baraja se va reduciendo con cada ronda, si la baraja se reduce a un número muy pequeño de elementos el juego termina 
    while jugar=='si' and baraja!=[]: #Mientras el usuario quiera seguir jugando, el código se repite como si fueran rondas 
        mano=[] #esta lista es para las cartas que vaya sacando el usuario
        mano_jarvis=[]#esta es la mano de la inteligencia artificial llamada Jarvis
        random.shuffle(baraja) #Esto revuelve los elementos de la lista
        """print(baraja)""" #Quitar las comillas para ver como queda la lista antes y despues de revolverla, la baraja debería decrecer conforme pasan las rondas
    
        #Variables
        #Usuario
        carta1=random.choice(baraja)#Se elige un elemento aleatorio de la lista para después eliminarlo
        baraja.remove(carta1)
        carta2=random.choice(baraja)#El usuario comenzará el juego con 2 cartas
        baraja.remove(carta2) #Las cartas que se eligen se remueven de la lista
        
        #Jarvis
        carta1_J=random.choice(baraja)#Se elige un elemento aleatorio de la lista para después eliminarlo
        baraja.remove(carta1_J)
        carta2_J=random.choice(baraja)#Jarvis comenzará el juego con 2 cartas
        baraja.remove(carta2_J)

        As11=False #Variable necesaria para que la función de "As" no se repita cada que la carta valga 11
        carta3As=False #Variable necesaria para que la función de "As" no se repita cuando la carta 3 valga 11, es decir, As
    
#Los if's a continuación son para determinar si alguna de las dos cartas repartidas
#es un As, si una de ellas lo es, se mandará llamar la función As1 o As2, dependiendo
#la carta en la que haya tocado un As (osea=11).
#Si ambas son ases, automaticamente se les asignara un valor de 1 y 11, ya que de lo contrario la suma sería 22.
        if carta1==11 and carta2!=11 and As11==False:
            if As1(carta1)==1:
                carta1=1
            else:
                carta1=11
                As11=True

        if carta2==11 and carta1!=11 and As11==False:
            if As2(carta2)==1:
                carta2=1
            else:
                carta2=11
                As11=True
            
        if carta1==11 and carta2==11:
            print("Tienes 2 ases, los valores serán de 1 y 11")
            carta1=1
            carta2=11
    
        #Usuario
        mano=[carta1,carta2] #Se agregan ambas cartas a la mano
        print("Mano: ",mano)        
        print("¿Desea agregar una carta a su juego? (si o no)")
        suma=carta1+carta2
        
        #Jarvis
        mano_jarvis=[carta1_J,carta2_J]
        suma_jarvis=carta1_J+carta2_J

        """Casos prueba para estructuras de decisión
        Quitar las comillas de abajo o poner # al lado izquierdo de ellas
        """
        """
        add='no'
        suma=-5
        #Para este caso se debe imprimir "Te has reservado en este turno, tus cartas sumaron -5"
        """
        """
        add='no'
        suma=21
        #Para este caso se debe imprimir "Blackjack!!!"
        """
        """
        add='no'
        suma=1400
        #Para este caso se debe imprimir "Has perdido"
        """
        """
        add='los casos prueba ocupan mucho espacio'
        print(add)
        #Para este caso se debe imprimir "valor invalido"
        """
        add=str(input()) #esta variable se usará para determinar si el usuario quiere o no agregar más cartas a las que ya tiene
        #si el usuario introduce "si", se agregaran mas cartas
        
        add_jarvis=funcion_add_jarvis(suma_jarvis) #Jarvis también elegirá si agregar cartas o no basandose en su mano
        
        while add_jarvis=='si' and suma_jarvis<21 : #Este ciclo es para que Jarvis vaya agregando cartas a su juego
                #Jarvis
                carta3_J=random.choice(baraja)                          
                baraja.remove(carta3_J)
                mano_jarvis.append(carta3_J)
                suma_jarvis=suma_jarvis+carta3_J
                add_jarvis=funcion_add_jarvis(suma_jarvis)
        
        
        while add == 'si' and suma<21: #Mientras el usuario quiera seguir agregando cartas el ciclo se repite
                #Usuario
            carta3=random.choice(baraja)                          
            baraja.remove(carta3)
            if carta3==11 and carta3As==False:
                if As3(carta3)==1:
                    carta3=1
                else:
                    carta3=11
                    carta3As=True
            
            mano.append(carta3)
            suma=suma+carta3 #Operación. Se toma la variable suma de arriba y a esa misma variable se le suma un número aleatorio entre 1 y 10 
            #El número random.randit actúa como una nueva carta cada vez que se repite el ciclo. La suma se acumula.
            print("Mano: ",mano)
            print("¿Desea agregar otra carta a su juego?")
            add=str(input()) #El usuario debe determinar si quiere seguir agregando cartas. Si se introduce un valor diferente a "si" se rompe el ciclo
        
        if add=='no' and suma<21: #Si el usuario ya no quiere agregar cartas y la suma es inferior a 21, esto querrá decir que se ha reservado
            print("Se ha reservado en este turno, sus cartas sumaron", suma)
        
        if add_jarvis=='no' and suma_jarvis<21:
            print("Jarvis se ha reservado")
    
        if add!='si' and add!='no': #Si el usuario introduce algo diferente a 'si' o 'no' no se podrá proceder
            print("valor invalido")
        
        """print(baraja)""" #Quitar comillas para ver como queda la lista después del juego cuando se hayan removido las cartas usadas
        print("La mano de Jarvis fue la siguiente: ",mano_jarvis)
        
        if suma>21 and suma_jarvis<21:
            print("Has perdido la ronda")
            puntos_jarvis+=1
        
        if suma_jarvis>21 and suma<21:
            print("La casa ha perdido la ronda")
            puntos_user+=1
        
        if suma>21 and suma_jarvis>21:
            print("Ambos jugadores pierden")

        if ganador(suma,suma_jarvis)=='user': #Manda llamar la función que determina quién es el ganador de la ronda
            print("El jugador gana la ronda")
            puntos_user+=1
        elif ganador(suma,suma_jarvis)=='b_user':
            print("Blackjack!!!")
            puntos_user+=1
        elif ganador(suma,suma_jarvis)=='jarvis':
            print("La casa gana la ronda")
            puntos_jarvis+=1
        elif ganador(suma,suma_jarvis)=='b_casa':
            print("Blackjack de la casa")
            puntos_jarvis+=1
            
        print("¿Jugar de nuevo?")
        jugar=str(input()) #Si o no
    
    if jugar=='no':
        print("Gracias por probar el Blackjack creado por Daniel Cruz")
        break

    if baraja==[]:
        print("La baraja se ha quedado sin cartas")
        break
        
    else:
        print("Valor inválido")

print("Tus puntos: ",puntos_user)
print("Puntos de Jarvis: ",puntos_jarvis)
if puntos_user>puntos_jarvis:
    print("FELICIDADES!!! le has ganado a Jarvis")
elif puntos_user<puntos_jarvis:
    print("La casa gana")
    print("Mejor suerte para la próxima.")
else:
    print("EMPATE")
print("El juego ha terminado")
"""
Para casos prueba quitar comillas
En todos los casos se imprimirá el valor resultante de la función especificadda
Los valores de las variables cambiarán pero no afectará al resto del código
"""
#casos prueba función "As" 1 2 y 3, introducir "1" u "11"

"""
print(As1(11)) 
print(As2(10)) 
print(As3(20)) 
print(As1(30)) 
print(As2(40))
#En todos los casos esta función arrojará 1 si eso fue lo que se introdujo, de lo contrario no arrojará ningún valor
"""
#casos prueba funcion add_jarvis
"""
suma_jarvis=11
while suma_jarvis<21:
    n=0
    while n<10:
        print(funcion_add_jarvis(suma_jarvis)) #Se imprimirán más 'si' que 'no'
        n+=1
    suma_jarvis+=1 
"""
