import random
def phone_a_friend(correct_answer):
  possible_options = ['A','B','C','D']
  possible_options.remove(correct_answer)
  percentage_poss = random.randint(0,100)
  wrong_answer = possible_options[random.randint(0,2)]

  if(percentage_poss > 85):
    return wrong_answer
  else:
    return correct_answer
  
user_name = input("Welcome to Millionaire! What is your name? ")
 
print("Currently you have made $0.")
amount_1 = "$" + str(500) + '.'
amount_2 = "$" + str(1000) + '.'
amount_3 = "$" + str(5000) + '.'
amount_4 = "$" + str(20000) + '.'
amount_5 = "$" + str(50000) + '.'
amount_6 = "$" + str(250000) + '.'
amount_7 = "$" + str(500000) + '.'
amount_8 = "$" + str(1000000) + '.'
got_q8 = False
  
Question_1 = "Which BTS member released the song 'Promise'? "
print(Question_1)
print("A.Jimin")
print("B.Jungkook")
print("C.SoekJin")
print("D.Rap_monster")
print("E.Phone a friend")
answer = input(">> ").upper()
if(answer == 'E'):
    print("Your friend suggests " + phone_a_friend('A'))
    answer = input(">> ").upper()
if(answer == 'A'):
    
    print("Correct!")
    print("Currently you have made " + str(amount_1))
    Question_2 = "Who is the inventor of the pseudo-money 'bitcoin'? "
    print(Question_2)
    print("A.Steven Hawking")
    print("B.Ibunkunoluwa Esan")
    print("C.Satoshi Nakamoto")
    print("D. Sasuke Shoto")
    print("E. Phone a friend")
    answer_2 = input(">> ").upper()
    if(answer_2 == 'E'):
        print("Your friend suggests " + phone_a_friend('C'))
        answer_2 = input(">> ").upper()
    if(answer_2 == 'C'):
        print("Correct!")
        print("Currently you have made " + str(amount_2))
        Question_3 = "Who is the main vocalist in the british band 'Bastille'? "
        print(Question_3)
        print("A.Dan Smith ")
        print("B.Samuel Calmday ")
        print("C.Amy Winehouse ")
        print("D.Eric Williams ")
        print("E. Phone a friend")
        answer_3 = input(">> ").upper()
        if(answer_3 == 'E'):
            print("Your friend suggests " + phone_a_friend('A'))
            answer_3 = input(">> ").upper()
        if(answer_3 == 'A'):
            print("Correct!")
            print("Currently you have made " + str(amount_3))
            Question_4 = "What is the favorite color of Princess Sochi "
            print(Question_4)
            print("A.Pink")
            print("B.Silver")
            print("C.Purple")
            print("D.Green")
            print("E. Phone a friend")
            answer_4 = input(">> ").upper()
            if(answer_4 == 'E'):
                print("Your friend suggests " + phone_a_friend('D'))
                answer_4 = input(">> ").upper()
            if(answer_4 == 'D'):
                print("Correct!")
                print("Currently you have made " + str(amount_4))
                Question_5 = "What is the hottest planet in the universe? "
                print(Question_5)
                print("A.Venus ")
                print("B.Jupiter ")
                print("C.Mercury ")
                print("D.Neptune")
                print("E. Phone a friend")
                answer_5 = input(">> ").upper()
                if(answer_5 == 'E'):
                    print("Your friend suggests " + phone_a_friend('C'))
                    answer_5 = input(">> ").upper()
                if(answer_5 == 'C'):
                    print("Correct!")
                    print("Currently you have made " + str(amount_5))
                    Question_6 = "Which of the following is a conditional statement in python? "
                    print(Question_6)
                    print("A.else")
                    print("B.and")
                    print("C.or")
                    print("D.elef")
                    print("E. Phone a friend")
                    answer_6 = input(">> ").upper()
                    if(answer_6 == 'E'):
                        print("Your friend suggests " + phone_a_friend('A'))
                        answer_6 = input(">> ").upper()
                    if(answer_6 == 'A'):
                        print("Correct!")
                        print("Currently you have made " + str(amount_6))
                        Question_7 = "What is the name of the seventh dwarf in Snow White? "
                        print(Question_7)
                        print("A.Sad ")
                        print("B.Bashful")
                        print("C.Dupey")
                        print("D.Clumsy")
                        print("E. Phone a friend")
                        answer_7 = input(">> ").upper()
                        if(answer_7 == 'E'):
                            print("Your friend suggests " + phone_a_friend('B'))
                            answer_7 = input(">> ").upper()
                        if(answer_7 == 'B'):
                            print("Correct!")
                            print("Currently you have made " + str(amount_7))
                            Question_8 = "What is the name of Bastille's last album? "
                            print(Question_8)
                            print("A.Wild World")
                            print("B.Bad blood")
                            print("C.Dooms day")
                            print("D.Previously on other peoples' heartache")
                            print("E. Phone a friend")
                            answer_8 = input(">> ").upper()
                            if(answer_8 == 'E'):
                                print("Your friend suggests " + phone_a_friend('C'))
                                answer_8 = input(">> ").upper()
                            if(answer_8 == 'C'):
                                print("Correct!")
                                print("Currently you have made " + str(amount_8))
                                print("You are a millionaire")
                                got_q8 = True

if not got_q8:
  print("I'm sorry, that is incorrect")
