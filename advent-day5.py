
inputprogram = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]

def main(inputparameter):
    memory = inputprogram
    program(memory)
    print(len(memory))


def instruction(instructionvalue):
    opcode = int(str(instructionvalue)[-2:])
    instructionlist = [opcode]
    if len(str(instructionvalue)) >= 3:
        operation1 = int(str(instructionvalue)[-3:-2])
        instructionlist.append(operation1)
    if len(str(instructionvalue)) >= 4:
        operation2 = int(str(instructionvalue)[-4:-3])
        instructionlist.append(operation2)
    if len(str(instructionvalue)) >= 5:
        operation3 = int(str(instructionvalue)[-5:-4])
        instructionlist.append(operation3)
    return instructionlist

def add(p1,p2,p3,m,i):
    v1 = 0
    v2 = 0
    v3 = 0
    try:
        v1 = i[1]
    except:
        pass
    try:
        v2 = i[2]
    except:
        pass



def program(memory):

    instructionpointer = 0
    instructionlength = 0

    while True:
        instruction = instruction(memory[instructionpointer])
        opcode = instruction(memory[instructionpointer])[0]
        if opcode == 99:
            break
        if opcode == 1 or opcode == 2:
            instructionlength = 4
            parameter1 = memory[instructionpointer+1]
            parameter2 = memory[instructionpointer+2]
            parameter3 = memory[instructionpointer+3]
        if opcode == 3 or opcode == 4:
            instructionlength = 2
            parameter1 = memory[instructionpointer]

        if opcode == 1:
            add(parameter1,parameter2,parameter3,memory,instruction)
        if opcode == 2:
            multiply(parameter1,parameter2,parameter3,memory,instruction)
            instruction[parameter3] = instruction[parameter1]*instruction[parameter2]
        if opcode == 3:
            instruction[a]
        if opcode == 4:
#
main(inputparameter)
