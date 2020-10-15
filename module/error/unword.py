
def text_unknown_Stopsymbol(line):
    print("***********************************ERROR**********************************")
    print("Error:Unknown terminator ';' position, this will cause an error in line %s." % line)
    print("You can add terminator to prevent this kind of error from happening.")
    print("************************************END***********************************")
    return 1

def text_unknown_ListRange(line):
    print("***********************************ERROR**********************************")
    print("Error:An error occurred in the processing of the statement in line %s." % line)
    print("It may be that you have written the termination symbol together with the code statement.")
    print("Please add a space before the termination symbol to prevent this kind of error from happening.")
    print("************************************END***********************************")
    return 1

def text_string_FUNCOUT(line):
    print("***********************************ERROR**********************************")
    print("Error:This error is caused by a conflict between the IO symbol standard and the IO symbol in the code line %s." % line)
    print("Changing the correct IO symbol will run the program correctly.")
    print("************************************END***********************************")
    return 1