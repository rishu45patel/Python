"ritesh is a good boy and i am very handsome"

st=input("enter the massage")
words=st.split(" ")
coding=input("1 for coding or 0 for decoding")
coding=True if(coding=="1") else False
if(coding):
    nwords=[ ]
    for word in words:
        if(len(word)>=3):
             r1="rit"
             r2="aku"
             stnew=r1+word[1: ]+word[0]+r2
             nwords.append(stnew)
        else:
            nwords.append(word[: :-1])
    print(" ".join(nwords))        


else:
    nwords=[]






















































