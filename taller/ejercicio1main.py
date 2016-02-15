__author__ = 'miguelolivares'

from ejercicio1class import Seno
from archivar import Archivo


def main():

        print ("Generador de Onda Sinusoidal")


        print ("Ingrese su opcion: ")
        Tono = input("Digite la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Frecuenciadesampleo = input("Ingrese la frecuencia de muestreo: ")
        MaxBits = input("Ingrese el numero de bits: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")


        onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        datos = onda.generar()


        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datos)

        onda.graficar(datos)


if __name__ == "__main__":
    main()
