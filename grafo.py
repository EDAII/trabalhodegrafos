from random import randint
class No:
      nlista=[]
      bool2=False 
      gosto=[] 
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
            print(a)  
            self.nlista.append(No(a))
      def travesialargura(self): 
          n2lista=[]
          n2lista.append(self) 
          for n in n2lista:
              # contador de visita bem aqui. 
             if(self.isunknow(n)):
                print("b")
                print(n)    
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
def main():
   a= input("digite um numero")
   b=int(a)
   p1=No(b)     
   p1.criavizinhos(b)
   p1.travesialargura()   
   print("o tamanho e:", p1.retornatamanho())        

main()
