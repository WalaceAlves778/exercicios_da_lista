def fibonacci():
    a = 0
    b = 1
    for i in range (1,11):
        a,b = b, a+b
        print(b)
#se quiser mostrtar só o resultado basta trocar o print por
# return b
    

print (fibonacci())
            