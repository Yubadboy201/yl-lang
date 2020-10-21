import re
import time

class String:
    def __init__(self,name,value,vars,joinchar=""):
        


        self.name = name

        tmp_b01_value = list(re.findall('"(.*?)"',value))
        tmp_a100_value = list(re.findall('input<"(.*?)">',value))
        tmp_a101_value = list(re.findall('input<(.*?)>',value))

        if len(tmp_b01_value) != 0 and (len(tmp_a100_value) == 0 and len(tmp_a101_value) == 0):

            self.value = tmp_b01_value[0]  
        elif "input" in value and (len(tmp_a100_value) == 1 or len(tmp_a101_value) == 1):
            tmp_b10_value = list(re.findall('input<"(.*?)">',value))
            if len(tmp_b10_value) != 0:

                self.value = input(tmp_b10_value[0])
            else:
                
                tmp_b10_value = list(re.findall('input<(.*?)>',value))

                self.value = input(vars[tmp_b10_value[0]][1])
        else:
            tmp_a01_value = value
            
            self.value = vars[tmp_a01_value][1]

        
 
        self.value = self.value.replace('[/n]','\n')
        self.value = self.value.replace('[/s]',' ')
        pat = re.compile(r"[{](.*?)[}]")

        if "{" in self.value and "}" in self.value:
            myvartostr = pat.findall(self.value)

            for myvarp in myvartostr:
                
                self.value = self.value.replace("{"+myvarp+"}",vars[myvarp][1])
        
        

