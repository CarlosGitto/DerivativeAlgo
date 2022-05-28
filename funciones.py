
#recibe un str de una funcion exponencial, separa a y n de la forma (a)^(n)
def expo(arg):
    count=0
    a=[]
    n=[]
    for el in arg:
        if el=="^":
            count+=1
        if count<1 and el!="^":
            a.append(el)
        if count>=1 and el!="^":
            n.append(el)
        if el=="^" and count>1:
            n.append(el)   
    a="".join([str(item) for item in a if str(item)!="(" and str(item)!=")"])
    n="".join([str(item) for item in n if str(item)!="(" and str(item)!=")"])
    
    if "e" in a and n=="x":             #e^x
        return("{}^x".format(a))

    if "e" in a and "x" in n and len(n)>1:  #descubre que la base tiene e
        if "+" in n:                        
            m=go_to_derpol(n) #analiza si el exponente es un polinomio de varios terminos
        else:
            m=deriv_pol(n)     # sino, directamente lo deriva
        if m=="1":
            return("{}^({})".format(a,n))   
        else:
            return("({}^({}))*({})".format(a,n,m)) 

    if "e" not in a and n=="x":                     #a^x
        return("({}^x)*ln({})".format(a,a))     
        
    if "e" not in a and "x" in n and len(n)>1:      #a^pol

        if "+" in n:
            m=go_to_derpol(n)
        else:
            m=deriv_pol(n)
        if m=="1":
            return("({}^({}))*ln({})".format(a,n,a))
        else:
            return("({}^({}))*({})*ln({})".format(a,n,m,a))

#devuelve la derivada de una multiplicacion

def multp(first,second,der_f,der_s):
    
    return("({})*({})+({})*({})".format(der_f,second,first,der_s))


#deriva UN termino de un polinomio que viene desde la func de go_to_derpol

def deriv_pol(pol):
    if "x" not in pol:                      #respuesta nula para lasa cttes
        return

    if "x" in pol and "^" not in pol:      
        pol_lst=list(pol)                          #diferencia ax de x, devolviendo a o 1 

        if len(pol_lst)>1:
            pol_lst.remove("x")
            return("".join(pol_lst))
        else:
            return("1")
    else:
        args=pol.split("x^")
        a=args[0]                                   #divide el pol en a y n
        n=int(args[1])
        if (n-1)==1:
            if a=="":
                return("{}x".format(n))
            else:
                a=int(a)
                return("{}x".format(a*n))
        else:
            if a=="":
                return("{}x^{}".format(n,n-1))
            else:
                a=int(a)
                return("{}x^{}".format(a*n,n-1))

#Separa los terminos de los polinomios por + y los deriva termino a termino, luego devuelve la derivada completa,
#  recibe polinomios que tengan terminso entre parentesis
def go_to_derpol(str):
    str="".join(val for val in str if val !="(" and val !=")")
    str=str.split("+")
    func_der=[]

    for pol in str:
        pol_der=deriv_pol(pol)
        if pol_der!=None:
            func_der.append(pol_der)
        else:
            continue 
    if len(func_der)==0:
        func_der="0"
    else:
        func_der="+".join(func_der)

    return(func_der)

