q1='''is python is an case sensitive programming language ?
a.) yes
b.) no
c.) machine dependent
d.) none'''
q2='''which of the following is floor division operator ?
a.) /
b.) //
c.) %
d.) &'''
q3='''which of the following is not an keyword in python programming ?
a.) eval
b.) assert
c.) if
d.) elif'''
q4='''what is the output of 3*1**3 ?
a.) 27
b.) 9
c.) 3
d.) 0'''
questions={q1:'a',q2:'b',q3:'a',q4:'c'}
name=input("enter your name:")
print("hey friend ",name," ! welcome to the quiz")
score=0
for i,j in questions.items():
    print(i)
    option=input("do you want to skip this question..(yes/no):")
    if option=="yes":
        continue
    ans=input("enter your answer(a/b/c/d):")
    if ans==questions[i]:
        print("correct answer ! you got a point well done !")
        score=score+1
        print("your'e present score is:",score)
    else:
        print("bad luck! you entered a wrong answer !")
        score=score-1
        print("your'e present score is:",score)
print("your final score is:",score)
if score<=0:
    print("don't worry ! stay focused and understand each topic !")
elif score ==1:
    print("well done friend! try to make more efforts for your goal")
elif score ==2:
    print("well done friend! try to make more efforts for your goal")
elif score ==3:
    print("well done friend! try to make more efforts for your goal")
else:
    print("excellent champ ! you nailed this")
    
