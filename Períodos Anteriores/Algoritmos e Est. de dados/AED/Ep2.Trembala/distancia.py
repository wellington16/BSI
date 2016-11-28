def distancia(x1,y1,x2,y2):
    distancia = float((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print( "%.2f" % distancia)
    return distancia
distancia(19,16,18,9)
