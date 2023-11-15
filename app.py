#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random


app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

class PiedraPapelTijeras:
    def __init__(self):
        self.opciones =[ "piedra", "papel", "tijeras"]
        self.puntuacion_jugador = 0

    def obtener_opcion_aleatoria(self):
        return random.choice(self.opciones)

    def jugar(self):
        while True:
            print("\nElige una opcion: piedra, papel o tijeras")
            opcion_jugador = input("Tu eleccion: ").lower()

            if opcion_jugador not in self.opciones:
                print("Esa opcion no es valida")
                continue

            opcion_oponente = self.obtener_opcion_aleatoria()

            print(f"\nTu eleccion: {opcion_jugador}")
            print(f"Oponente: {opcion_oponente}\n")

            resultado = self.obtener_resultado(opcion_jugador, opcion_oponente)
            print (f"\nResultado: {resultado}")

            if resultado == "Ganaste!":
                self.puntuacion_jugador += 1
            
            print(f"\nPuntuacion: Jugador {self.puntuacion_jugador}")

            volver_a_jugar = input("\nQuieres volver a jugar? (s/n): ").lower()

            if volver_a_jugar != "s":
                print("\nGracias por jugar!")
                print(f"Puntuacion final: Jugador {self.puntuacion_jugador}")
                break

    def obtener_resultado(self, opcion_jugador, opcion_oponente):
        if opcion_jugador == opcion_oponente:
            return "Empate!"
        elif (
            (opcion_jugador == "piedra" and opcion_oponente == "tijeras")
            or (opcion_jugador == "papel" and opcion_oponente == "piedra")
            or (opcion_jugador == "tijeras" and opcion_oponente == "papel")
        ):
            return "Ganaste!"
        else:
            return "Perdiste!"

#Crear istancia del juego y empezar a jugar
juego = PiedraPapelTijeras()
juego.jugar()
