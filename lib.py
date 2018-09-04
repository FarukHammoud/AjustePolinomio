pontos = []
curvas = []
constantes = []
original_millis = 0

def MultiplicaPolinomios(poli_1 = [0],poli_2 = [0]): #coeficientes de traz pra frente: 1 + 2x +3x^2 -> [1,2,3]
    novo_poli = []
    for i in range(len(poli_1)+len(poli_2)):
        novo_poli.append(0)
    for i in range(len(poli_1)):
        for j in range(len(poli_2)):
            novo_poli[i+j] += (poli_1[i]*poli_2[j])
    return novo_poli        
def GeraPolinomio(raizes = []):
    polinomio = [1]
    for raiz in raizes:
        polinomio = MultiplicaPolinomios(polinomio,[-raiz,1])
    for i in range(len(polinomio)-1,0,-1):
        if polinomio[i] == 0:
            polinomio.pop(i)
        else: break    
    return polinomio    
def DesenhaPolinomio():
    strokeWeight(5)
    stroke(0,255,0)
    global constantes
    global pontos
    for x in range(0,1280,1):
        point(x,CalculaPonto(x))
    for ponto in pontos:
       stroke(255,50-50*random(1),50-50*random(1))
       point(ponto.x,ponto.y)      
def CalculaPonto(x):
    global pontos
    global constantes
    soma_termos = 0
    for ponto_i in pontos:
        produto_termos = 1
        for ponto_j in pontos:
            if ponto_i != ponto_j:
               produto_termos *= ( x - ponto_j.x )
               produto_termos /= float( ponto_i.x - ponto_j.x )
        produto_termos *= ponto_i.y
        soma_termos += produto_termos     
    return soma_termos                  
def Inicializa():
    background(30,200,40)
def Clear(imagem):
    image(imagem,0,0,width,height)    
class GE_PASSOS:
    
    def __init__(self,passo = 1):
        self.passo = passo
    def Passo(self,imagem_fundo):
        if self.passo == 1:
            Clear(imagem_fundo)
            self.Passo1()
        elif self.passo == 2:
            Clear(imagem_fundo)
            self.Passo2()
        elif self.Passo == 3:
            self.Passo3()
    def Passo1(self):
        global pontos
        fill(200-200*random(1)/8,200-200*random(1)/8,255)
        textSize(35)
        text("Passo 1: Clique nos pontos que voce deseja unir com um polinomio:",50,60)
        global mousePressed
        if Ponto.numero_de_pontos > 0 :
            noStroke()
            if mouseX > 1000 and mouseX < 1300 and mouseY > 600 and mouseY < 700 :
                if mousePressed :
                    self.passo = 2
                    print("n pontos: "+str(len(pontos)))
                    return 0
                fill(200,200,200,200)
            else:
                fill(200,200,200,50)
            rect(1000,600,300,100,20)
            textSize(60)
            fill(250,250,250,200)
            text("Concluir",1020,674)
        if mousePressed:
            global original_millis
            if millis() > original_millis + 500:
                global original_millis
                original_millis = millis()
                ponto = Ponto()
                ponto.MudaPonto([mouseX,mouseY])
                pontos.append(ponto)
        for ponto in pontos:
            strokeWeight(5)
            stroke(255,50-50*random(1),50-50*random(1))
            point(ponto.x,ponto.y)
    def Passo2(self):
        DesenhaPolinomio()
        self.passo = 3
    def Passo3(self):
        pass           
class Ponto:
    numero_de_pontos = 0
    def __init__(self,lista = [0,0]):
        self.x = lista[0]
        self.y = lista[1]
        self.constante = 0
        Ponto.numero_de_pontos += 1
    def ListaPontos(self):
        lista = []
        lista.append(self.x)
        lista.append(self.y)
        return lista
    def MudaPonto(self,lista):
        if len(lista) == 2:
           self.x = lista[0]
           self.y = lista[1]
               