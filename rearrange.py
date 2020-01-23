
def rearrange(input):
    print("Enter a string:")
    string = input()
    a = string.split(" ")

    a=a[-1::-1] 

    arranged = ' '.join(a)

    print(a)

  

rearrange(input)


   
