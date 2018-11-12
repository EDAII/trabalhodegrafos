from random import randint
class No:
      nlista=[]
      bool2=False  
      def __init__(self,n):
        self.nlista.append(n)
        self.bool2=False  

      def addno(self, n):
          self.nlista.append(n)
      def getno(self, i):
           return self.nlista[i]
      def criavizinhos(self, n ):
          for i in range(n):
            a=randint(1,100)
            self.nlista.append(No(a))
      def printatipo(self): 
          n2lista=[]   
          for n in self.nlista:
           if(type(n)!=int):
              if(n.bool2==True):
                return 
              if(n.bool2==False):   
                for n2 in n.nlista:
                     n2lista.append(n2)
                n.bool2=True
              print(n.retornatamanho())           
                                
      def  retornatamanho(self):
           self.bool2=True  
           return len(self.nlista)  
def main():
   a= input("digite um numero")
   b=int(a)
   p1=No(b)  
   p1.criavizinhos(b)
   p1.printatipo()  
   p3=p1.getno(2)    
   print("o tamanho e:", p3.retornatamanho())        

main()
