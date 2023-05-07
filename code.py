import time

now = time.ctime()
qna = {
       "hi":"hey",
       "how are you":"I am fine",
       "what is your name":"my name is ishu",
       "How old are you":"I am 20 years old",
       "what is the time now" : now,
       "Who is the winner of 2022 F1 championship?":"Max Versattpen",
       "Who created this bot?":"Ahmed Tarek who is an intern at sync intern"
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])
