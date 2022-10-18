def solution(number):
    if(len(number) < 1):
        return -1


    while(True):
        current_input = ""
        stack = [int(number[0])]
        number = number + " "
        print('input number', number)

        for i in range(1, len(number)):
            if(number[i] != ' ' ):
                if(stack[-1] == int(number[i])):
                    stack.append(int(number[i]))
                    print(stack)

                else:
                    current_input+=str(sum(stack))
                    if(number[i] != " "):
                        stack = [ int(number[i]) ]

            else:
                current_input+=str(sum(stack))

        # check for more such patterns present
        current_pattern_found = 0
        i = 1

        while(not current_pattern_found and i< len(current_input)):
            if(current_input[i] == current_input[i-1]):
                number = current_input
                current_pattern_found = 1
            i+=1

        if(current_pattern_found == 0):
            return current_input

        
s = '66644319333'  
s = '44886' 
solution(s)