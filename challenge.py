
from funciones import *

"""Si yo le doy "3x^2" me tenes que devolver "6x", te challengeo a que contemples polinomios,
 exponenciales, sumas de funciones, y un extra plus si implementan regla de cadena
 Lo interesante aca es que hay que trabajar con strings."""


def fun_scaner(func_str):
    terms_count = 0
    count = 0
    equis = 0
    mult = 0
    pot = 0
    summ = 0
    summ_index = []
    for i in range(len(func_str)):
        if func_str[i] == "x":
            equis += 1
        if func_str[i] == "(":
            count += 1
        if func_str[i] == ")":
            count -= 1
            terms_count += 1
        if func_str[i] == "*" and count == 0:
            mult += 1
        if func_str[i] == "+" and count == 0:
            summ += 1
            summ_index.append(i)
        if func_str[i] == "^" and count == 0:
            pot += 1
            pot_index = i

    if terms_count >= 1:  # ¿hay parentesis?(si), ¿que operación hacemos?

        if mult >= 1 and summ == 0 and pot == 0:  # multp fuera de los parentesis
            term_mult = []  # (x+a)*(x^n)
            # ((x^n)+3x+5)*(x)
            args_mult = func_str.split("*")
            args_mult_d = []

            for n in range(len(args_mult)):
                args_mult_d.append(
                    "".join(value for value in args_mult[n] if value != ("(") and value != (")")))
                print("el {} termino es".format(n+1))
                term_mult.append(fun_scaner(args_mult_d[n]))
            return(multp(args_mult[0], args_mult[1], term_mult[0], term_mult[1]))

        if summ >= 1 and mult == 0 and pot == 0:  # suma fuera del parentesis
            term_summ = []
            summ_der = ""
            args_summ = []
            k = 0
            func_str_lst = list(func_str)

            for n in range(len(summ_index)):
                args_summ.append("".join(func_str_lst[k:summ_index[n]]))
                k = summ_index[n]+1
            args_summ.append("".join(func_str_lst[k:]))
            print(args_summ)

            for term in args_summ:
                term = "".join(n for n in term if n != "(" and n != ")")
                term_der = fun_scaner(term)
                term_summ.append(term_der)

            for term in term_summ:
                if term == term_summ[0]:
                    summ_der += term
                else:
                    summ_der += "+"+"("+term+")"
            return(summ_der)

        if pot == 1 and summ == 0 and mult == 0:  # potencia fuera del parentesis
            term_pot = list(func_str)
            term_pot0 = term_pot[:pot_index]
            term_pot1 = term_pot[pot_index+1:]
            #print("hay {} sumas".format(summ))

            #print("en ella hay")
            if "x" in term_pot0 and "x" in term_pot1:
                print("ambos terminos tienen x, hay que separarlos y reescanear")

                print(term_pot0)
                print(fun_scaner(term_pot0))
                print(term_pot1)
                print(fun_scaner(term_pot1))

                # pol_der=go_to_derpol(func_str)
                # return(pol_der)

            if "x" in term_pot1 and "x" not in term_pot0:
                print("exponencial simple")
                return(expo(func_str))
            else:
                print("polinomiod")
                return(go_to_derpol(func_str))

    if terms_count == 0 and "x" in func_str:  # pol simpl,polcompl,expsimpl de e o a

        if len(func_str) == 1:
            return("1")

        if equis >= 1 and len(func_str) > 1 and "^x" not in func_str and "e^" not in func_str:

            if "+" in func_str:
                pol_der = go_to_derpol(func_str)
                print("polinomio de mas de un termino")
                return(pol_der)

            else:
                pol_der = go_to_derpol(func_str)
                print("polinomio de un termino")
                return(pol_der)

        if "^x" in func_str or "e^" in func_str:
            print("exponencial")
            expo_der = expo(func_str)
            return(expo_der)

        else:
            if pot == 1:
                fun_split = func_str.split("^")
                if "x" in fun_split[0]:
                    pol_der = go_to_derpol(func_str)
                    print("polinomio")
                    return(pol_der)
                if "x" in fun_split[1]:
                    expo_der = expo(func_str)
                    print("exponencial")
                    return(expo_der)

    else:
        return("0")


"""Formas de ingreso:
        Los parentesis se usan solo si hay combinación de funciones o regla de la cadena
        ej1: 3x^2+5x+2 -> sin parentesis
        ej2: (3x^2+5x+2)*(2^x) -> parentesis
        ej3: (3x^2+5x+2)*(x^2+2)"""


#x=input("Ingrese su función:\n")


# print(fun_scaner("{}".format(x)))


# print(fun_scaner("(x^3)+(e^(3x+2))+(4x^2)"))#bien

# print(fun_scaner("(x^4)*(e^(7x+12)"))#bien

print(fun_scaner("(33x+x^33)+(2^x)"))  # bien

# print(fun_scaner("500x^1000"))#bien

# print(fun_scaner("(3x+2x^2)+(2^x)"))#bien

# print(fun_scaner("(4^x)*(3^x)"))#bien

# print(fun_scaner("3x^2"))#bien

# print(fun_scaner("34"))#bien

# print(fun_scaner("(3x^2)+5x+32"))#bien

# print(fun_scaner("e^((x^2)+3)"))#bien

# print(fun_scaner("(e^x)*(e^(x^3+x^2+2)"))#bien

# print(fun_scaner("2^(3x+4)"))#bien

# print(fun_scaner("2e^32x"))#bien

# print(fun_scaner("(3x^2)+(x^3)"))#bien

# print(fun_scaner("((5x^2)+3)*((x^2)+x+4)"))#bien

# print(fun_scaner("(e^(7x^2+5x^4+80))+(x^3+x^2)+(e^x)"))#bien

# print(fun_scaner("2x^2+3x+3"))#bien

# print(fun_scaner("2^x"))#bien

# print(fun_scaner("(3x)*(2x)"))#bien
