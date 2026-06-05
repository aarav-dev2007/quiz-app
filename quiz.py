import random

gk={'Capital of India?': ['New Delhi','Jammu','Jaipur','Kerala','A'],
    'Which is the only continent on Earth that has land located in all four hemispheres?':['Asia','Africa','South America','Antarctica','B'],
    'Which planet is known as the Red Planet':['Earth','Mars','Jupiter','Pluto','B'],
    'Who wrote Indian National Anthem?':['Mahatma Gandhi','Rabindranath Tagore','Jawaharlal Nehru','Bhagat Singh','B'],
    'What is the capital of Australia?':['Sydney','Melbourne','Canberra','Perth','C']}

while True:
    print('1. Admin')
    print('2. User')
    print('3. Exit')

    try:
        a=int(input("Enter choice number: "))
    except:
        print("Inavlid input! Enter a number.")
        continue

    if a==3:
        break

    elif a==1:
        print('***Admin Passcode= 123***')
        b=int(input("Enter Passcode: ")) 
        if b!=123:
            print("Invalid Passcode")
        else:
            print('*'*20)
            print("Welcome")
            print('*'*20)

            while True:
                print('')
                print('1. Add Questions')
                print('2. Delete Questions')
                print('3. Print')
                print('4. Update Options')
                print('5. Search')
                print('6. Number of Questions')
                print('7. Exit')
                print('')
            
                c=int(input("Enter choice number: "))
                if c==7:
                    break
                    
                elif c==1:
                    e=int(input("Enter Number of Questions to add: "))
                    ans=[]
                    queno=1

                    for i in range(e):
                        print('Question',queno)
                        que=input('Enter Question: ')
                        queno+=1

                        ans=[]
                        
                        h=65
                        for i in range(4):
                            print('Option', chr(h),':',end=' ')
                            h=h+1
                            g=input()
                            ans.append(g)

                        while True:
                            correct=input('Enter correct option (A/B/C/D):' ).upper()
                            if correct in ['A','B','C','D']:
                                break
                            else:
                                print("Invalid input! Please enter A/B/C/D")

                        ans.append(correct)

                        gk[que]=ans

                elif c==2:
                    print(gk.keys())
                    e=input("Enter Question to Delete: ").lower()
                    for i in gk:
                        if i.lower()==e:
                            del gk[i]
                            print('Question deleted successfully!')
                            break
                    else:
                        print("Question Unavailable")

                elif c==3:
                    print(gk)
                    z=1
                    for i in gk:
                        print('Question',z,i)
                        z+=1

                        print('\tA:',gk[i][0])
                        print('\tB:',gk[i][1])
                        print('\tC:',gk[i][2])
                        print('\tD:',gk[i][3])
                        print('\tCorrect Option:',gk[i][4])

                elif c==4:
                    qu=input('Enter Question to Update: ')
                    if qu in gk:
                        ans=[]
                        h=65
                        for i in range(4):
                            print('Option',chr(h),':',end=' ')
                            h+=1
                            newans=input()
                            ans.append(newans)
                        while True:
                            correct=input("Enter correct option (A/B/C/D): ").upper()
                            if correct in ['A','B','C','D']:
                                break
                            else:
                                print("Invalid input! Please enter A/B/C/D")
                        ans.append(correct)
                        gk[qu]=ans
                    else:
                        print("Question does not exist")

                elif c==5:
                    qu=input("Enter Question to Search: ").lower()
                    for i in gk:
                        if i.lower()==qu:
                            print("Found: ",gk[i])
                            break
                    else:
                        print("Not Found")

                elif c==6:
                    print("Number of Questions: ", len(gk))

    elif a==2:
        print('*'*20)
        print('Welcome')
        print('*'*20)

        q=1
        score=0

        print('')
        print('*'*20)
        print('\t GK Quiz')
        print('*'*20)

        name=input("Enter Your Name: ")
        print('*'*20)
        print('Each Question Carries 10 Marks')
        print("No Negative Marking")
        print('Number of Questions: ',len(gk))
        print('*'*20)

        h=65

        questions=list(gk.keys())
        random.shuffle(questions)

        for i in questions:
            print('Q',q)
            q+=1
            print(i)

            print('\tOption',chr(h),gk[i][0])
            h+=1
            print('\tOption',chr(h),gk[i][1])
            h+=1
            print('\tOption',chr(h),gk[i][2])
            h+=1
            print('\tOption',chr(h),gk[i][3])
            h+=1

            print('')
            h=65

            while True:
                answer=input('Enter Answer (A/B/C/D): ').upper()
                if answer in ['A','B','C','D']:
                    break
                else:
                    print('Invalid input! Please enter A/B/C/D')
                

            if answer==gk[i][4]:
                print('***Congrats! Your Answer is Correct!***')
                score +=10
            else:
                print('***Your Answer is Incorrect***')
                correct_letter=gk[i][4]
                correct_text=gk[i][ord(correct_letter) - 65]
                print('Correct Answer: ','('+str(correct_letter)+')', correct_text)
                print('')

        input('Press enter to continue...')
        print('*'*20)
        print("Your Name: ",name)
        print('Your Score: ', score)
        print('Out of', len(gk)*10)
        print('Percentage= ',str((score/(len(gk)*10))*100)+'%')
        print()
        if score == len(gk)*10:
            print('Excellent Performance!')
        elif score >= (len(gk)*10)//2:
            print('Good job!')
        else:
            print('Keep practicing!')
        print('*'*20)


    else:
        print('Invalid choice')