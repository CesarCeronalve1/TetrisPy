import msvcrt
import time
import os
import random
from pixeles import *
from mono import mono
class pantalla:
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        self.px = [[pixel(x, y) for x in range(self.alto)] for y in range(self.ancho)]
        self.color = color()
        self.monos = [mono(1,1,self.color.colorAleatorio())]
        self.datos = ["Datos",""]
    def iniciar(self):
        while True:
            for m in self.monos:
                self.gravedad(m)
            self.actualizarPantalla()



    def gravedad(self, obj):
        # Solo los monos activos (m.M == True) caerán
        if obj.M:
            # Comprobamos si hay otro mono en la fila de abajo o si hemos alcanzado el suelo
            if obj.y < self.alto - 1 and not any(m.x == obj.x and m.y == obj.y + 1 for m in self.monos):
                obj.y += 1  # El mono cae si no hay ningún otro mono debajo
            else:
                obj.M = False  # Detenemos el movimiento si toca el suelo o un mono


    def actualizarPixeles(self):
        self.Tecla()
        self.px = [[pixel(x, y) for x in range(self.alto)] for y in range(self.ancho)]
        for m in self.monos:
            self.px[m.x][m.y].color = m.color
            self.datos[1] = f"monox:{m.x} monoy:{m.y}"
            

    def NoPlayer(self):
        for m in self.monos:
            if m.M == True:
                return True
        return False

    def Tecla(self):
        if self.NoPlayer() == False:
            self.monos.append(mono(0,0,"rojo"))
            #self.monos.append(mono(0,0,self.color.colorAleatorio()))

        if msvcrt.kbhit():
            tecla = msvcrt.getch()
            tecla = tecla.decode()
            if tecla == ('a'):
                for m in self.monos:
                    if m.M == True:
                        if not any(m.x -1 == ms.x for ms in self.monos): 
                            m.x = m.x - 1
               # if m.x > self.ancho - 1:
               #     m.x = 0
                    if m.x < 0:
                        m.x = self.ancho - 1
            if tecla == ('d'):
                for m in self.monos:
                    if m.M == True:
                        if not any(m.x +1 == ms.x for ms in self.monos): 
                            m.x = m.x + 1
               # if m.x > self.ancho - 1:
               #     m.x = 0
                    if m.x > self.ancho-1:
                        m.x = 0
    def actualizarPantalla(self):
        for y in range(self.alto):
            for x in range(self.ancho):
                print(self.color.darColor(self.px[x][y].color) + "█",end="")
            print("\n",end="")
        print(f"{self.datos[0]}")
        print(f"{self.datos[1]}")
        time.sleep(1)
        self.actualizarPixeles()
        os.system('cls')





pantalla = pantalla(10,18)
pantalla.iniciar()

