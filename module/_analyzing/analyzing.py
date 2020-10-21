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

            

        else: 
            unword.text_string_FUNCOUT(linenumber)

    elif date[0] == "String" or date[0] == "string":
        if len(date) == 2:
            vardate[date[1]] = [date[0],'']
        elif len(date) == 4:
            vardate[date[1]] = [date[0],typeclass.String("var-ebx",date[3],vars=vardate).value]
    elif len(date) == 3:

        if date[1] == "=":
           
            vardate[date[0]][1] = typeclass.String("var-eax",date[2],vars=vardate).value

    elif date[0] == "File" or date[0] == "file":
        if date[2] == "read" and date[1] == "<<":
            if date[4] == "text" and date[3] == "<<":              
                if date[6] == ":":
                    if len(date) == 8:
                        with open(typeclass.String("var-epx",date[5],vars=vardate).value,"r") as f:
                            vardate[date[7]] = ["String",f.read()]
        

                        
        elif date[2] == "write" and date[1] == "<<":

            if date[4] == "text" and date[3] == "<<":              

                if len(date) == 6:
                    tmp_date_write_text_001 = date[5].split(":")[0]
                    with open(typeclass.String("var-epx",tmp_date_write_text_001,vars=vardate).value,"w") as f:
                        f.write(typeclass.String("var-epx",date[5].replace(tmp_date_write_text_001,""),vars=vardate).value)



    

    else:
        print("-------------------------------------------------------------------")
        print("CODE ERROR in line %s :  %s " % (linenumber,codestring))
        print("                         |")
        print("                         |")
        print("                         |")
        print("                   non-existent code")
        print("-------------------------------------------------------------------")

    