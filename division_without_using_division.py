# Division without using division

def custom_divider(num1, num2):
    
    if num1 == 0:
        return 0
    
    counter = 0
    count_of_adding_zero = 0
    counter2 = 0.00
    counter3 = 0.00
    
    while(num1 >0 and count_of_adding_zero <= 2):
        if num1 >= num2:
            num1 -= num2

            if count_of_adding_zero == 0:
                counter += 1 
                
        if count_of_adding_zero == 1:
            counter2+= 0.10
            
        elif count_of_adding_zero == 2:
            counter3 += 0.01
            
        if num1 != 0 and num1 < num2 :
            while(num1 < num2):
                count_of_adding_zero += 1
                num1 = str(num1)
                num1 = num1 + "0"
                num1 = int(num1)
            
    if count_of_adding_zero and counter == 0:
        return format((counter2 + counter3), '.2f')
    
    if counter2  and counter3:
        return format((counter + counter2 + counter3), '.2f')
    
    if counter3:
        return format((counter + counter3), '.2f')
    
    if counter2:
        return format((counter + counter2 ), '.2f')
    
    return counter


num1, num2 = map(int, input().split("/"))

print(custom_divider(num1, num2))

