def emprestimo(valor, sal, anos):
    print(valor, sal, anos)
    parcel = valor / (anos * 12)
    parcel_int = int(parcel)
    prestacao = sal * 0.3
    prestacao_int = int(prestacao)
    
    print(parcel, prestacao)

    if prestacao_int <= parcel_int:
        return "Empréstmo aprovado"
    else:
        return "Empréstimo negado"

resultado = emprestimo(350000, 4000, 10)
print(resultado)



