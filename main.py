"""
GOAL:
Can you name all of the 54 countries of Africa?

In this challenge we will write a Python script to create 
a quiz where we ask the user to guess as many African countries as possible. 
The player will score one point per correct country. 
"""

countries = ["Algeria", 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 
             'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 
             'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini, Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau',
             'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique',
             'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome & Principe', 'Senegal', 'Seychelles', 'Sierra Leone',
             'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

numb = 1
go_on = True
ls = []

play_on = True
guessed_score = 0

while play_on:
    user_play = input('Would you like to play? Type yes or no ')
    if user_play == 'yes' or user_play == 'Yes':
        print('Type as many countries as you know. To exit just leave line blank')
        while go_on:
            user = input(f'{numb}: ')
            if len(user) != 0 and user != ' ':
                ls.append(user)
                numb += 1
            else:
                go_on = False  
                numb = 1
        if len(ls) != 0:
            for guessed_country in ls:
                if guessed_country in countries:
                    guessed_score += 1         
    else:
        play_on = False
        print(f'You have guessed {guessed_score} countries')


