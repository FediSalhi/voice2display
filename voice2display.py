import pygame
import time
import speech_recognition as sr

pygame.init()

ekran_genisligi = 900 #genislik
ekran_yukseligi = 600 #yukseklik

siyah = (0,0,0)
beyaz = (255,255,255)
kirmizi = (200,0,0)
yesil = (0,200,0)
acik_kirmizi = (255,0,0)
acik_yesil = (0,255,0)

gameDisplay = pygame.display.set_mode((ekran_genisligi,ekran_yukseligi)) # ana pencereyi göstermek 600:800
pygame.display.set_caption('VOICE2DISPLAY') #pencerenin ismini tanimlamak

gameDisplay.fill(beyaz) # pencereyi beyaz renk ile doldurmak
img1 = pygame.image.load('img.jpg') # arka planin fotografini yüklemek
img1 = pygame.transform.scale(img1, (100, 100)) # arka plandaki fotografi skale edilmesi
gameDisplay.blit(img1,(800,0)) # fotografin kaydirilmasi
img2 = pygame.image.load('img2.jpg')
gameDisplay.blit(img2,(-70,-100))




def close():
    pygame.quit()
    quit()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((500),(350))                      #metin yeri
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()




def text_objects(text, font):
    textSurface = font.render(text, True, siyah)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y: # cursor buton alaninda ise
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h)) #renk açik olsun

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h)) #renk koyu olsun

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def s2t_fr():
    gameDisplay.blit(img1,(800,0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Bir sey soyleyin!')
        audio = r.listen(source)
        print ('okundu!')


    text = r.recognize_google(audio,language='fr-FR')
    print(text)
    message_display(text)

def s2t_tr(): #sound to text
    gameDisplay.blit(img1,(800,0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Bir sey soyleyin!')
        audio = r.listen(source)
        print ('okundu!')


    try:
        text = r.recognize_google(audio,language='tr-TR')
        print(text)
        message_display(text)
    except:
        print("Hata oldu :( " )


def s2t_ar():
    gameDisplay.blit(img1,(800,0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Bir sey soyleyin!')
        audio = r.listen(source)
        print ('okundu!')


    text = r.recognize_google(audio,language='ar-UE')
    print(text)
    message_display(text)

def s2t_en():
    gameDisplay.blit(img1,(800,0))
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print ('Bir sey soyleyin!')
        audio = r.listen(source)
        print ('okundu!')



    text = r.recognize_google(audio,language='en-US')
    print(text)
    message_display(text)

def info():
    print(""" Bu proje Fedi ve Mehmet tarafindan gömüllü sistemler dersi
    final ödevi olarak tasarlamis""")
    time.sleep(1)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Türkçe Konus",150,450,190,50,yesil,acik_yesil,s2t_tr)
        button("Inglizce Konus",150,520,190,50,yesil,acik_yesil,s2t_en)
        button("Arapça Konus",350,450,190,50,yesil,acik_yesil,s2t_ar)
        button("Fransizca Konus",350,520,190,50,yesil,acik_yesil,s2t_fr)
        button("Bizim hakkimizda",550,450,190,50,kirmizi,acik_kirmizi,info)
        button("Çik",550,520,190,50,kirmizi,acik_kirmizi,close)
        pygame.display.update()

if __name__ == '__main__':
    main()
