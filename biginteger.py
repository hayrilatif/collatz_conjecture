class BigInteger():
    def __init__(self,value:str):
        self.__string_value=value
    
    def __subtract(self,value1,value2):
        rev_value1, rev_value2 = list(reversed(value1)), list(reversed(value2))
        
        result=""
        
        rem=0
        max_index=max(len(value1),len(value2))
        
        for i in range(max_index):
            digit_1=int(self.__get_from_list(rev_value1,i))
            digit_2=int(self.__get_from_list(rev_value2,i))
        
    
    def __add__(self,bint):
        return self.__add(self.__string_value,bint.__string_value)
      
    def __add(self,value1,value2):
        rev_value1, rev_value2 = list(reversed(value1)), list(reversed(value2))
        
        result=""
        
        rem=0
        max_index=max(len(value1),len(value2))
        for i in range(max_index):
            digit_1=int(self.__get_from_list(rev_value1,i))
            digit_2=int(self.__get_from_list(rev_value2,i))
            
            sum_digit=digit_1+digit_2+rem
            new_digit=sum_digit%10
            rem_digit=(sum_digit-new_digit)//10
            
            result+=str(new_digit)
            rem=rem_digit
        
        if rem>0 : result+=str(rem)
        
        return "".join(reversed(result))
            
    def __get_from_list(self,ls,index):
        if index<len(ls):
            return ls[index]
        else:
            return 0