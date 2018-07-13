class Hora(object):
    def __init__(self, hora=0,min=0, seg=0):
        self.hora = hora
        self.min = min
        self.seg = seg
    # Cambiar o transformar
    def toSeconds(self):
        return self.hora * 3600 + self.min * 60 + self.seg
    # El toString de java
    def __str__(self):
        return str("%02d:%02d:%02d" % (self.hora,self.min,self.seg))
    # El toString para listas
    def __repr__(self):
        return str("%02d:%02d:%02d" % (self.hora,self.min,self.seg))
    # Para ordenar sobrecargar
    def __lt__(self, hora):
        return self.toSeconds() < hora.toSeconds()
            
if __name__ == "__main__":
    h1 = Hora()
    h2 = Hora(seg=30)
    h3 = Hora(8,30)
    h4 = Hora(4,55,6)
    L = [h1,h2,h3,h4]
    print(L)
    L.sort()
    print(L)