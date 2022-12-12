def prime_checker(number):
    is_prime = True
    for i in range(2, number):  # estremo finale non incluso
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("É un numero primo.")
    else:
        print("Non è un numero primo.")


n = int(input("Inserisci un numero: "))
prime_checker(n)
