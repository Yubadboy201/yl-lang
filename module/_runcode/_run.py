import sys
from module.error import unword
from module._analyzing import analyzing

dates = []


def run(codestrs,lines,truelines):

    line = lines
    codestr = codestrs

    #Is word "exit"
    if codestr[0:5] == "exit;":

        sys.exit(0)
    
    elif codestr[0:4] == "EXIT":

        sys.exit(0)


    elif codestr[0:2] == "//":
        return 1001

    elif not ";" in codestr:
        
        return unword.text_unknown_Stopsymbol(truelines)


    dates.append(())

    i_str = ""
    i = 0
    z_str = ""
    space_i = 1
    stop_state = 0
    while stop_state == 0:
        i_str = codestr[i:i+1]
        

        if i_str == " ":
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


    
    analyzing.analyzing(date_line,codestr,truelines+1)

def __get_and_run__(file):
    with open(file, 'r') as f:
        readlist = f.readlines()
    lines = 0
    truelines = 0
    for codestr in readlist:
        if codestr in ['\n','\r\n']:
            #doing something
            truelines += 1
            continue
        if codestr.strip() == "":
            #doing something
            truelines += 1
            continue
        
        funcnum = run(codestr,lines,truelines)
        if funcnum == 1001:
            truelines += 1
            continue
        lines += 1
        truelines += 1