import re

class String:
    def __init__(self,name,value,vars,joinchar=""):
        self.name = name
        tmp_b01_value = list(re.findall('"(.*?)"',value))

        if len(tmp_b01_value) != 0:

            self.value = tmp_b01_value[0]   
        else:
            tmp_a01_value = value
            self.value = vars[value][1]
            
        self.value = self.value.replace('[/n]','\n')
        self.value = self.value.replace('[/s]',' ')
        #Is joinchar String class
        if joinchar != "":
            
            tmp_a01_value = re.findall('"(.*?)"',joinchar)
            if len(tmp_a01_value) != 0:
                
                self.value = self.value.replace('[~set]',joinchar[0])
            else:
                tmp_a01_value = joinchar
                self.value = vars[joinchar][1]
        else:
            pass

