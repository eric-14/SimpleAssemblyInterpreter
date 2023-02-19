def simpleAssembler(program):
    
    registers={}
    Pindex  = 0
    while Pindex < len(program):

        str = program[Pindex].split(" ")

        match str[0]:
            case "mov":
              
                register1 = str[1]  #first register

                register2 = str[2]   # second register or constant 
                #if second value of the move instruction is a digit push it to the memory map \
                
                if(not (register2.isalpha())):
                    
                    #if(registers[register1]): # if register1 exists in the hash map 
                    registers[register1] = int(register2)

                else:
                    if(register2 in registers):
                        value =  int(registers[register2])
                        #adding the value of register2 to register1 
                        registers[register1] = int(value)
                   # else:
                       # continue
                         #registers[register1] = 0

            case "inc":
                if(str[1].isdigit()):
                    value = int(str[1])
                    value = value + 1
                else: 
                    # get the value of the registers 
                    value = int(registers.get(str[1]))
                    value = value + 1 

                    registers[str[1]] = int(value)
            
                #break

            case "dec":
                if(str[1].isdigit()):
                    value = int(str[1])
                    value = value + 1
                else: 
                    # get the value of the registers 
                    value = int(registers.get(str[1]))
                    value = value - 1 

                    registers[str[1]] = int(value)
            
               # break
            case "jnz":
                    skipTo = int(str[2])
                    if(str[1].isdigit()):
                        counter = int(str[1])
                        if(counter == 0):
                            Pindex = Pindex +1 
                            continue
                    else:
                        counter = int(registers[str[1]])
                        if(counter == 0):
                            Pindex = Pindex +1 
                            continue
                    #check the value of the last register
                    #  
                    if(not (program[Pindex].split(" ")[1].isalpha())):
                        #if register value is digit
                        registerValue = int(program[Pindex].split(" ")[1])
                    else:
                        registerValue =  int(registers[program[Pindex].split(" ")[1]])

                    if(registerValue != 0):
                       # counter = registers.get(str[1])
                        Pindex = Pindex + skipTo
                        continue

                    
                
                   # break
        Pindex = Pindex +1 
    print("this is the result ", registers)
    return registers


# #problem return does is not okay

# program2 = ["mov c 12","mov b 0","mov a 200","dec a","inc b","jnz a -2","dec c","mov a b","jnz c -5","jnz 0 1","mov c a"]
# program  = ["mov a 5", "inc a", "dec a","dec a","inc a"]
# simpleAssembler(program2)



#problem return does is not okay

# program2 = ["mov c 12","mov b 0","mov a 200","dec a","inc b","jnz a -2","dec c","mov a b","jnz c -5","jnz 0 1","mov c a"]
# program  = ["mov a 5", "inc a", "dec a","dec a","inc a"]


simpleAssembler(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2'])
