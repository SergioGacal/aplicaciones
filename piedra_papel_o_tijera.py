import random

class Juego:
    opciones = ['piedra', 'papel', 'tijera']
    def jugar(self):
        jugada = random.choice(self.opciones)
        return jugada

class Partida:
    jugador = 0
    computadora = 0
    ronda = 0
    def __init__(self):
        self.empezar_partida()
    def empezar_partida(self):
        while self.jugador < 10 and self.computadora < 10:
            try:
                respuesta = int(input('\nElija: 1.Piedra 2.Papel 3.Tijera: '))
                self.ronda +=1
                while respuesta != 1 and respuesta != 2 and respuesta != 3:
                    respuesta = int(input('Error: Elija: 1.Piedra 2.Papel 3.Tijera: '))
                elección = ''
                if respuesta == 1:
                    elección = 'piedra'
                elif respuesta == 2:
                    elección = 'papel'
                elif respuesta == 3:
                    elección = 'tijera'
                computadora = Juego()
                computadora_jugada = computadora.jugar()
                resultado = ''
                if respuesta == 1 and computadora_jugada == 'piedra':
                    resultado = 'Empate'
                elif respuesta == 1 and computadora_jugada == 'papel':
                    resultado = 'Perdiste'
                elif respuesta == 1 and computadora_jugada == 'tijera':
                    resultado = 'Ganaste'
                elif respuesta == 2 and computadora_jugada == 'piedra':
                    resultado = 'Ganaste'
                elif respuesta == 2 and computadora_jugada == 'papel':
                    resultado = 'Empate'
                elif respuesta == 2 and computadora_jugada == 'tijera':
                    resultado = 'Perdiste'
                elif respuesta == 3 and computadora_jugada == 'piedra':
                    resultado = 'Perdiste'
                elif respuesta == 3 and computadora_jugada == 'papel':
                    resultado = 'Ganaste'
                elif respuesta == 3 and computadora_jugada == 'tijera':
                    resultado = 'Empate'
                print(f'\n{"-"*50}\n{" "*13} Resultado de la Ronda: {self.ronda}\n{"-"*50}\n')
                print(f'\nJugador elije: \t\t{elección}\n\nComputadora elije: \t{computadora_jugada}\n')
                if resultado == 'Ganaste':
                    self.jugador += 1
                    print('Ganaste y sumás 1')
                elif resultado == 'Perdiste':
                    self.computadora += 1
                    print('Perdiste. Computadora suma 1.')
                else:
                    print('Empate. Ambos eligieron lo mismo')
                print(f'\nPuntaje jugador: \t{self.jugador}\n\nPuntaje computadora: \t{self.computadora}\n{"-"*50}\n\n')
            except ValueError:
                print('\nSelección errónea.\n')
        if self.jugador == 10:
            print('Felicitaciones, ganó la partida')
        elif self.computadora == 10:
            print('Ha perdido, mejor suerte la próxima. ')
        print('\nFin de la partida\n' )
        respuesta=input("presione enter para volver al menu")
        respuesta=Menu()

class Instrucciones:
        Instrucciones=f'\n\n{" "*28}INSTRUCCIONES DEL JUEGO{" "*28}\n{"-"*80}\nEl objetivo del juego de "Piedra, Papel o Tijera" es vencer a la computadora.\nEn el inicio de cada ronda el jugador elije Piedra, Papel o Tijera.\nLa computadora también realiza su elección.\n\nSi ambos elijen lo mismo la ronda termina en empate. \nEn otro caso: piedra gana a tijera, tijera gana a papel y papel gana a piedra.\n\nLa partida finaliza cuando un jugador llega a 10 puntos.\nMucha suerte.\n\n{"-"*80}'
        def __init__(self):
            print(self.Instrucciones)
            volver=input("presione enter para volver al menu")
            volver=Menu()
    
class Menu:
        def abrir_menu(self):
            print(f'\n{"-"*50}\n{"-"*18}Menu Principal{"-"*18}\n{"-"*50}\n')
            while True:
                try:
                    respuesta=int(input((f'\t1.Jugar\n\t2.Instrucciones\n\t3.salir\n\n{"-"*50}\n{"-"*50}\n')))
                    if respuesta == 3:
                        False
                    while respuesta != 1 and respuesta != 2 and respuesta != 3:
                        respuesta=int(input((f'\nError: Selecciones\n\t1.Jugar\n\t2.Instrucciones\n\t3.salir\n\n{"-"*50}\n{"-"*50}\n')))
                    if respuesta == 1:
                        Partida()
                    if respuesta == 2:
                        Instrucciones()
                    if respuesta == 3:
                        print('Saliendo...')
                        break
                except ValueError:
                    print('\nSeleccionó un valor erróneo\n')

m=Menu()
m.abrir_menu()
