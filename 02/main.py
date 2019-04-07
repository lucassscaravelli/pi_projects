import numpy as np
import cv2 as cv

qtd = 0

data =  np.array([
                 [1,1,1,0,1,1,1,1,1,1],
                 [1,1,1,0,1,1,1,1,1,1],
                 [1,1,0,0,1,1,1,1,1,1],
                 [0,0,0,0,1,1,1,1,1,1],
                 [0,0,0,0,1,1,1,0,1,1],
                 [0,1,1,1,1,1,1,1,1,1],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 ], dtype = np.uint8)



def count_squares(m):

    count = 0
    result = []
    cords_used = []

    print("matriz inicial")
    print(m)

    for i in range(0, 10):
        for j in range(0, 10):
            if m[i,j] == 1:
                result.append({"i": i, "j": j})

    print("pontos centrais encontrados")
    print(result)

    for p in result:
        x = p["i"]
        y = p["j"]

        print("Ponto X[{}] Y[{}]".format(x,y))

        new = True

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):

                for t in cords_used:
                    xx = t["i"]
                    yy = t["j"]

                    # ja existe coordenada sendo usada
                    if xx == i and yy == j:
                        new = False

        if new:
            print("Novo quadrado encontrado!")
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    cords_used.append({"i": i, "j": j})
            count = count + 1   
        else:
            print("Já existe um quadrado nessa área")

    return count
        



s_element = cv.getStructuringElement(cv.MORPH_RECT,(3,3)) 
s_erosion  = cv.erode(data,s_element, iterations=1,borderType=cv.BORDER_CONSTANT,borderValue=0)

print("Total de quadrados:", count_squares(s_erosion))