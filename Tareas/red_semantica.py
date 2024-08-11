class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.arcos = []

    def agregar_arco(self, destino, etiqueta_arco):
        self.arcos.append(Arco(self, destino, etiqueta_arco))

class Arco:
    def __init__(self, origen, destino, etiqueta):
        self.origen = origen
        self.destino = destino
        self.etiqueta = etiqueta

    def __str__(self):
        return f"{self.origen.etiqueta} -- {self.etiqueta} --> {self.destino.etiqueta}"

class RedSemantica:
    def __init__(self):
        self.nodos = []

    def crear_nodo(self, etiqueta):
        nodo = Nodo(etiqueta)
        self.nodos.append(nodo)
        return nodo

    def mostrar_red(self):
        for nodo in self.nodos:
            for arco in nodo.arcos:
                print(arco)

def main():
    red = RedSemantica()

    # Creación de nodos
    animal = red.crear_nodo("Animal")
    vida = red.crear_nodo("Vida")
    sentir = red.crear_nodo("Sentir")
    moverse = red.crear_nodo("Moverse")
    ave = red.crear_nodo("Ave")
    mamifero = red.crear_nodo("Mamifero")
    plumas = red.crear_nodo("Plumas")
    bien = red.crear_nodo("Bien")
    huevos = red.crear_nodo("Huevos")
    avestruz = red.crear_nodo("Avestruz")
    albatros = red.crear_nodo("Albatros")
    largas = red.crear_nodo("Largas")
    no_puede = red.crear_nodo("No Puede")
    muy_bien = red.crear_nodo("Muy Bien")
    ballena = red.crear_nodo("Ballena")
    piel = red.crear_nodo("Piel")
    mar = red.crear_nodo("Mar")
    tigre = red.crear_nodo("Tigre")
    leche = red.crear_nodo("Leche")
    pelo = red.crear_nodo("Pelo")
    carne = red.crear_nodo("Carne")

    # Creación de arcos
    animal.agregar_arco(vida, "tiene")
    animal.agregar_arco(sentir, "puede")
    animal.agregar_arco(moverse, "puede")
    animal.agregar_arco(ave, "tipo_de")
    animal.agregar_arco(mamifero, "tipo_de")

    ave.agregar_arco(plumas, "tiene")
    ave.agregar_arco(huevos, "pone")
    ave.agregar_arco(avestruz, "tipo_de")
    ave.agregar_arco(albatros, "tipo_de")

    plumas.agregar_arco(bien, "vuelve")
    avestruz.agregar_arco(largas, "tiene")
    avestruz.agregar_arco(no_puede, "vuelve")

    albatros.agregar_arco(muy_bien, "vuelve")

    mamifero.agregar_arco(leche, "da")
    mamifero.agregar_arco(pelo, "tiene")
    mamifero.agregar_arco(ballena, "tipo_de")
    mamifero.agregar_arco(tigre, "tipo_de")

    ballena.agregar_arco(piel, "tiene")
    ballena.agregar_arco(mar, "vive_en")

    tigre.agregar_arco(carne, "come")

    # Mostrar la red semántica
    red.mostrar_red()

if __name__ == "__main__":
    main()
