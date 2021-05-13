import threading

contador = 0

class contadorS():
    def __init__(self):
        self.lock = threading.Lock()
    
    def funcion(self):
        self.lock.acquire()
        try:
            global contador
            for i in range(1000000):
                contador += 1
        finally:
            self.lock.release()

print("Inicio programa principal")
print("Valor Inicial: " + str(contador))

#thread_1=threading.Thread(target=funcion)
#thread_2=threading.Thread(target=funcion)
#thread_3=threading.Thread(target=funcion)

contadorsito = contadorS()

thread_1=threading.Thread(target=contadorsito.funcion)
thread_2=threading.Thread(target=contadorsito.funcion)
thread_3=threading.Thread(target=contadorsito.funcion)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Valor Final: " + str(contador))



#1. Cual es el valor esperado de la variable contador. En que condiciones se obtendría este valor esperado.
#Rsta: el valor esperado serian 3 millones, para obtener el valor esperado lo mas recomendable seria usar locks
#2. Ejecute el programa varias veces y explicar a que se deben los resultados que observa.
#Rsta: dan resultados que no son los esperados, esto se debe a que todos los thread se pisan entre si haciendo que muchas de las sumas de los contadores no se registren y provoquen que el resultado sea erratico
#3. Identifique las Secciones Críticas (incluir las lineas de código en la respuesta).
#Rsta: 
#4. Modifique el programa, utilizando Locks de modo que se asegure la exclusión mutua en las secciones críticas.
#5. Que es una "condición de carrera"? Que consecuencias trae y cuando se produce?
#6. Que es una Sección Crítica?
#7. Que es la Exclusión Mútua? Rsta: 
# la exclucion mutua se produce cuando un recurso no puede ser compartible, debido a que cuando un proceso lo usa se termina volviendo exclusivo de dicho proceso y hasta que no termine de utilizar a dicho recurso, no va a ser liberado para que otro proceso pueda utilizarlo, la necesidad de exclusion mutua se debe a que hay algunos recursos que es mejor que no sean compartidos, por que pueden llevar al mal funcionamiento del programa

#8. Que son los Locks o Mutex? Bonus (opcional): que es un "deadlock"?, como se produce y que consecuencias tiene?

#que es un deadlock: un deadlock se produce cuando varios procesos no pueden ejecutarse debido a la necesidad de mas de 1 recurso que esta siendo utilizado por otro proceso haciendo que este en un estado de espera perpetuo
#las caracteristicas para se que considere que se produjo un deadlock son:
# *Debe haber exclucion mutua: significa que si hay 2 procesos o mas que necesiten 2 recursos o mas, tiene que existir la posibilidad de que cada recurso tome solo 1 de los tantos procesos que necesita y no pueda tomar el otro por que lo 
# tendra otro proceso, que no tiene ningun metodo o posibilidad de devolver el recurso en caso de que no pueda tomar todos los recursos que necesita.
# *Debe poder retener y esperar: cuando un proceso consigue un recurso pero no consigue todos los recursos que necesita tiene que ponerse en un estado de espera, sin soltar el recurso que posee, y solo saldra de ese estado si consigue el recurso que le falta
# caso contrario estara en un estado de espera perpetuo sin liberar el recurso que posee(aun cuando ese recurso pueda ser necesario para otro proceso)
#
# *Los recursos deben formar un ciclo de espera circular: cuando los procesos quedan en espera por la falta de recursos necesarios este bucle de espera debe poder representar en la forma de un circulo(un ciclo de espera circular)


