import cv2 as cv
import numpy as np

def get_index(size, index):

    if index > size - 1:
        return 0
    
    if index < 0:
        return size - 1

    return index


def get_next_images(imgs, index):
    imgs_size = len(imgs)
    img_from = imgs[get_index(imgs_size, index-1)]
    img_to = imgs[get_index(imgs_size, index)]
    return img_from, img_to, get_index(imgs_size, index + 1)


def read_images(count=5):
    imgs = []  

    for i in range(1, count+1):
        imgs.append(cv.imread("./img/img_{}.jpg".format(i)))

    return imgs

def make_transition(img_from, img_to):
     for alpha in np.arange(0,1.1,0.1)[::-1]:
        from_base = img_from.copy()
        to_output = img_to.copy()

        cv.addWeighted(from_base,alpha,to_output,1 - alpha,0, to_output)
        cv.imshow("paisagens", to_output)
        cv.waitKey(50)

def set_border(img):
    value = [0,255,0]        
    return cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_CONSTANT, None, value)

def set_watermark(img):

        img_with_watermark = img.copy()
        img_h, img_w, img_c = img_with_watermark.shape
    
        watermark_img = cv.imread("./img/watermark.png")
        watermark_h, watermark_w, watermark_c = watermark_img.shape

        # criar uma marca da agua com tamanho da imagem
        # porem só o tamanho dela sera preenchido
        watermark = np.zeros((img_h, img_w, watermark_c), dtype='uint8')
        

        # escolher um pixel inicial
        # neste caso, esta no canto inferior
        # esquerdo
        h_base = watermark_h
        w_base = 0


        for i in range(0, watermark_h):
                for j in range(0, watermark_w):
                        if watermark_img[i,j][0] != 255 and watermark_img[i,j][1] != 255 and watermark_img[i,j][2] != 255:
                                watermark[img_h - 1 - i, w_base + j] = watermark_img[h_base - i,j]

        cv.addWeighted(watermark, 0.25, img_with_watermark, 1.0, 0, img_with_watermark)
        img_with_watermark = cv.cvtColor(img_with_watermark, cv.COLOR_BGRA2BGR)

        return img_with_watermark

imgs = read_images()
index = 0

cv.imshow("paisagens", set_watermark(set_border(imgs[get_index(len(imgs), index - 1)])))

while True:
    img_from, img_to, index = get_next_images(imgs, index)

    # espera 2 segundos para fazer a transição
    if cv.waitKey(2000) & 0xFF == ord('q'):
        break
    make_transition(set_watermark(set_border(img_from)), set_watermark(set_border(img_to)))
  
cv.destroyAllWindows()
