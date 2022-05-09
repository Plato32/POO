from numpy import append


class Conjunto:
    __conjunt=[]

    def __init__(self, l):
        self.__conjunt=l
       
    def getconj(self):
        return(self.__conjunt)
    
    # def borrardobles(self,lis):
    #     i=0
    #     for elem in lis:
    #         for eleme in lis:
    #             print(elem,eleme)
    #             if(elem==eleme):
    #               print("repetido")
    #               lis.pop(elem)
    #     return(lis)
            
    def __add__(self, otro):
        newconjunto=[]
        if(type(self)==type(otro)):
            
            a=set(self.getconj())
            print(a,self.getconj())
            b=set(otro.getconj())
            c=a|b  
        else: print("Error")
        return(list(c))
    def __sub__(self, otro):
        
        if(type(self)==type(otro)):
            a=set(self.getconj())
            b=set(otro.getconj())
            c=a&b  
            # d= self.getconj()
        else: print("Error")
        return(list(a-c))

    def __eq__(self, otro):
        r=False
        a=self.getconj()
        b=otro.getconj()
        if (len(a)==len(b)):
            r=True
            i=0
            while (i<len(b) and (r==True)):
                j=0
                while (j<len(b) and (a[i]!=b[j])):
                    j+=1
                if j>=len(otro.__conjunt):
                    r=False
                i+=1
        return(r)   

    