import random
li=[[[' __________________'],
 ['|                  |']
,['|']
,['|']
,['|']
,['|']
,['|======================']],
[[' ______________________'],
 ['|                  |']
,['|                ( _ )']
,['|']
,['|']
,['|']
,['|======================']],

[[' _____________________'],
 ['|                  |']
,['|                 (-)']
,['|              _/']
,['|']
,['|'],
 ['|======================']]
 ,[[' ___________________'],
 ['|                  |'],
 ['|                 (-)']
 ,["|               _/| |\_"],
 ['|'],
 ['|'],
 ['|======================']],
 [[' ____________________'],
 ['|                  |']
,['|                 (-)']
,['|               _/| |\_']
,['|               _/ -']
,['|']
,['|']
,['|======================']],
 [[' _____________________'],
 ['|                  |']
,['|                 (-)']
,['|               _/| |\_']
,['|               _/ - \_']
,['|']
,['|']
,['|======================']],
]
def hangam():
    list_of_word=["phone","sun","moon","earth"]
    word=random.choice(list_of_word)
    guess_made=""
    vaild_entery=set("abcdefghijklmnopqrstuvwxyz")
    x=1
    while True:
        main_word=""
        # missed=0
        for letter in word:
            if letter  in guess_made:
                main_word+=letter
            else:
                main_word+='_'
        if main_word== word :
            print(main_word)
            print("you won !!!!")
            break
        print("guese the word ",main_word)
        guess=input()
        if guess in vaild_entery:
            guess_made+=guess
        else:
            print(" enter vaild charcter >>> ")
            guess=input()
        if guess not in word:
            for i in li[x]:
                print(i)
            x+=1
            if len(li)==x:
                print("YOU LOSE THE GAME!!!!")
                print("you let a die good man !!!!")
                break


name=input("ENTER YOU'R NAME  >> ")
print("WELCOME ",name,"!!")
print("------------------------------------------------")
hangam()
