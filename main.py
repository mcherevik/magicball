from random import *

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Yes', 'Reply hazy, try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


def answer_check():
    while True:
        answer = input()
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        else:
            print('I do not understand your reply. Please answer again')
            continue


print('Hi, I am a Magic Ball, and I know the answer for any of your questions')
print('What is your name?')
name = input()
print('Hi,', name)
while True:
    print('Please, ask a question')
    question = input()
    print('The answer for your question: {} is: {}'.format(question, choice(answers)))
    print('Do you want to know more? Y / N')
    if answer_check():
        continue
    else:
        print('See you again!')
        break
