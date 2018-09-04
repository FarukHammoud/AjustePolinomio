#AjustePolinomio v1.0 by Faruk Hammoud,2017  IMPA
# v1.0 released 13/01/2017
#Adaptado de AjusteSpline v1.0 by Faruk Hammoud,2016  EESC/USP
# v1.0 released 05/05/2016 
from lib import *

imagem_fundo = loadImage("")
passos = GE_PASSOS()

def setup():
    size(1280,720)
    global imagem_fundo
    imagem_fundo = loadImage("back.jpg")
    Inicializa()
def draw():
    passos.Passo(imagem_fundo)