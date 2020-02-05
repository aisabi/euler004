def largestPalindromeProduct(n):
	# calculate palindrome numbers example : The largest palindrome made from the product of
	#  two 2-digits numbers is 9009 = 91 × 99
    print('please wait during calculation')
    listeA =[]
    listePalindrome = []
    # for a multiplication of 2 numbers with two-digit
    if  n == 2:
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
                    laliste = palindromeTwoDigits         
        print('Palindrome MAX for two 2-digits numbers is :',max(laliste))
	
	# for a multiplication of 2 numbers with two-digit
    elif n == 3:
    	print('to do')

    else:
    	print('Use number 2 or 3 as argument')

largestPalindromeProduct(2)