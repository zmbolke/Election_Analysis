#What is your score?
score = int(input('What is you test score?'))
#If above 90 than A
if score >= 90:
    print('Your grade is an A.')
else: 
    #If above 80 than B...
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your score is a D.')
            else:
                print('Your grade is an F.') 
                   
