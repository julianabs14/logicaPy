def fibonacci():
    a = 0
    b = 1
    print(a)
    print(b)
    
    for i in range(13):
        soma = a + b
        a = b
        b = soma
        print(soma)

fibonacci()