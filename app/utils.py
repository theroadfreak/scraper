def myString(input_):
    
    input_ = input_.split(" ")
    temp = list()
    for n in range(len(input_)):
        if input_[n] != "":
            temp.append(input_[n])   
    input_ = temp

    last = input_[len(input_)-1]
    input_.remove(last)

    final = str()
    for words in input_:
        final += str(words) + "+"
    final+=last
    
    return final

def myPrint(class_):
    print("\n", class_.name ,"\n")
    for n in range(class_.size):
        print(class_.titles[n],'    ',class_.prices[n])
        print('_________________________________________________________________________')
