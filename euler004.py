def largestPalindromeProduct(n):
	# calculate palindrome numbers example : The largest palindrome made from the product of
	# two 2-digits numbers is 9009 = 91 × 99
    # two 3-digits numbers is 906609
    print('please wait during calculation')
    listeA =[]
    listePalindrome = []
    # for a multiplication of 2 numbers with two-digit
    if  n == 2:
        print('You choose 2-digit calculation')
        for chiffre in range(10,100):
            for nombre in range(1,100):
                resultat = chiffre * nombre
                resultat = str(resultat)
                longueur = len(resultat)
                if  longueur == 4:
                    listeA.append(resultat)
                    liste1 =set(listeA)
                    # once the data are collected, analyse them to find out any palindrome
                    for donnee in liste1:
                        analyse1 = str(donnee[0])+str(donnee[1])+str(donnee[2])+str(donnee[3])
                        analyse2 = str(donnee[3])+str(donnee[2])+str(donnee[1])+str(donnee[0])
                        if analyse1 == analyse2:
                            listePalindrome.append(analyse1)
                    palindromeTwoDigits =set(listePalindrome)
                    palindromeTwoDigits = sorted(palindromeTwoDigits)
                    print('List palindrome :',palindromeTwoDigits)
                    laliste = palindromeTwoDigits # get max value of the list using the max() method     
        print('Palindrome MAX for two 2-digits numbers is :',max(laliste))
	
	# for a multiplication of 2 numbers with three-digit
    elif n == 3:
        print('You choose 3-digit calculation')
        for chiffre in range(900,1000):
            for nombre in range(900,1000):
                resultat = chiffre * nombre
                if resultat > 850000:
                    resultat = str(resultat)
                    listeA.append(resultat)
                    liste1 =set(listeA)
                    # once the data are collected, analyse them to find out any palindrome
                    for donnee in liste1:
                        analyse1 = str(donnee[0])+str(donnee[1])+str(donnee[2])+str(donnee[3])+str(donnee[4])+str(donnee[5])
                        analyse2 = str(donnee[5])+str(donnee[4])+str(donnee[3])+str(donnee[2])+str(donnee[1])+str(donnee[0])
                        if analyse1 == analyse2:
                            listePalindrome.append(analyse1)
                    palindromeTwoDigits =set(listePalindrome)
                    palindromeTwoDigits = sorted(palindromeTwoDigits)
                    print('List palindrome :',palindromeTwoDigits)
                    for item in palindromeTwoDigits: # get max value of the list using a for loop
                        maxValeur = 0
                        item = int(item)
                        if item > maxValeur: maxValeur = item
                    
        print('Palindrome MAX for 3-digit numbers is :', maxValeur)

    else:
    	print('Use number 2 for 2-digit calculation OR 3 for 3-digit calculation as argument')

largestPalindromeProduct(2)
