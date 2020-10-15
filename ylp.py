from sys import argv
from module.error import unword
from module._analyzing import analyzing
from module._runcode import _run
import os
import sys

dates = []

def _input_and_jie_xi_function(line):
    codestr = input(">>>")

    #Is word "exit"
    if codestr[0:5] == "exit;":

        sys.exit(0)
    
    elif codestr[0:4] == "EXIT":

        sys.exit(0)
    
    elif codestr[0:2] == "//":
        return 1001

    elif not ";" in codestr:
        
        return unword.text_unknown_Stopsymbol(line+1)


    dates.append(())

    i_str = ""
    i = 0
    z_str = ""
    space_i = 1
    stop_state = 0
    while stop_state == 0:
        i_str = codestr[i:i+1]
        

        if i_str == " ":
            
            tupledate = dates[line]
            tupledate = list(tupledate)
            tupledate.append(z_str)
            tupledate = tuple(tupledate)
            dates[line] = tupledate
            z_str = ""
            space_i += 1
            i += 1
            continue
        
        elif i_str == ";":
            try:
                tupledate = dates[line]
            except IndexError:
                return
            tupledate = list(tupledate)
            tupledate.append(z_str)
            tupledate = tuple(tupledate)
            dates[line] = tupledate
            z_str = ""
            space_i += 1
            i += 1

            stop_state = 1

        z_str += i_str
        
        i += 1
    date_line = list(dates[line])
    i_state = 0
    z_word_str = ""
    i_num = 0
    check_i_num = 0
    end_i_num = 0
    for t_i in date_line:
        if '"' in t_i:

            i_state += 1
            if i_state == 2:
                z_word_str += " "
                z_word_str += t_i
                end_i_num = i_num
                break
            
            check_i_num = i_num
        if i_state == 1:
            z_word_str += " "
            z_word_str += t_i
        i_num += 1

    if end_i_num != 0:

        del date_line[check_i_num:end_i_num+1]
        

        date_line.insert(check_i_num,z_word_str)
        

        
    else:
        pass

    analyzing.analyzing(date_line,codestr,line+1)

        

    


if __name__ == "__main__" and len(argv) == 1:
    print("*****************************************************")
    
    print("Welcome use YLP(yubadboy language in Python)")
    print("This is interactive programming environment")
    
    print("*****************************************************")
    func_code = 0
    i = 0
    while True:

        func_code = _input_and_jie_xi_function(i)
        if func_code == 1:
            continue
        elif func_code == 1001:
            continue
        i += 1


elif __name__ == "__main__" and len(argv) == 2 and argv[1] == "--run":
    print("missing parameter")

elif __name__ == "__main__" and len(argv) == 3 and argv[1] == "--run":
    try:
        _run.__get_and_run__(argv[2])
    except UnicodeEncodeError:
        print("encode error")
