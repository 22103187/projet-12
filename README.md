# Master-mind_12
projet master mind 
bonjour 
#Interphase



print("-----------------------------------------")
print("\t\tMenu")
print("-----------------------------------------")
print("Enter code using numbers.")
print("1 - rouge, 2 - vert, 3 - jaune, 4 - bleu, 5 - blanc, 6 - orange, 7 - violet, 8 - rose")
print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
print("-----------------------------------------")
print_ mastermind_board(show_passcode, guess_codes, guess_flags)
couleurs = ['rouge', 'rose', 'bleu', 'vert', 'jaune', 'orange', 'violet', 'blanc']
essais = 10    # nbr d'essai pour trouver le code secret
