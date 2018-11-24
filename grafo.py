from random import randint
class No:
      nlista=[]
      bool2=False 
      gosto=[] 
      idui=0  
      conversa=[]   
      def __init__(self,n2):
        self.idui=n2     
        self.bool2=False     
      def registrar(self,noprincipal):
          noprincipal.nlista.append(self)   
      def addno(self, n):
          self.nlista.append(n)
      def getno(self, i):
           return self.nlista[i]
      def criarindividuos(self, n, noprincipal ):
          for i in range(n):
            a=randint(1,100)
            print(a)  
            self.nlista.append(No(a))
            self.registrar(noprincipal)
      def travesialargura(self): 
          n2lista=[]
          n2lista.append(self) 
          for n in n2lista:
             if(self.isunknow(n)):
                print("b")# contador de visita bem aqui.     
                n.bool2=True      
                for n2 in n.nlista:
                        if(self.isunknow(n2)):
                              n2lista.append(n2)
                              print("a")                   
         
                           
      def  retornatamanho(self):
           self.bool2=True  
           return len(self.nlista) 

      def isunknow(self,a):
           if(type(a)==No):
             if(a.bool2==False):
               return True
             else: 
               return False
           else:
              return False   
      def procurar(self,n2):
         bool3=False
         icont=[]
         icont.append(0)
         icont.append(False)  
         for n in self.nlista:
              icont[0]=icont[0]+1 
              if(n2==n):
               bool3=True  
               icont[1]=True
               return icont            
         print("individuo não encontrado") 
         return icont        
      def criaramigo(self,noprincipal):
          a=input("digite outro numero")
          n2=int(a)     
          icont=self.procurar(n2)
          if(icont[1]==True):
            print("voces ja sao amigos")
          else:
            print(" voce  deseja se tornar amigo de  ",n2)
            resposta=input(" se sim digite s")
            if(resposta=="s"):
              print ("sua decisao e uma ordem")
              icont2=noprincipal.procurar(n2)
              if(icont2[1]==True):
                self.nlista.append(n2)
              else:
                print("essa pessoa nao existe") 
            else:
              print("por que não ,ele não morde")  
      def eindividuo(self,n2):
         n=self.nlista[n2]  
         if(type(n)==No):
            return True
         else:
            return False                                 
def main():
   a= input("digite um numero")
   b=int(a)
   p1=No(b)     
   i=0  
   p1.criarindividuos(b,p1)
   while(p1.eindividuo(i)!=True):
       i=i+1  
   n=p1.nlista[i]      
   n.nlista.append(2)
   n.criaramigo(p1) 
   p1.travesialargura()   
   print("o tamanho e:", p1.retornatamanho())        

main()
