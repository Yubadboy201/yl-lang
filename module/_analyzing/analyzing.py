from module._analyzing import typeclass
from module.error import unword
import re

vardate = {}

def analyzing(date,codestring,linenumber):

    if len(date) == 0:
        
        unword.text_unknown_ListRange(linenumber)
        return 1
        

    elif date[0] == "print":
        if date[1] == "<<":
            if len(date) == 3:
                print(typeclass.String("print-eax",date[2],vars=vardate).value,end="")

            elif len(date) == 5:
                if date[3] == "<<":

                    print(typeclass.String("print-ebx",date[2],joinchar=date[4],vars=vardate).value,end="")
                else:
                    unword.text_string_FUNCOUT(linenumber)

        else: 
            unword.text_string_FUNCOUT(linenumber)

    elif date[0] == "String":
        if len(date) == 2:
            vardate[date[1]] = [date[0],'']
        elif len(date) == 4:
            vardate[date[1]] = [date[0],typeclass.String("var-ebx",date[3],vars=vardate).value]
    elif len(date) == 3:

        if date[1] == "=":
           
            vardate[date[0]][1] = typeclass.String("var-eax",date[2],vars=vardate).value



    

    else:
        print("-------------------------------------------------------------------")
        print("CODE ERROR in line %s :  %s " % (linenumber,codestring))
        print("                         |")
        print("                         |")
        print("                         |")
        print("                   non-existent code")
        print("-------------------------------------------------------------------")

