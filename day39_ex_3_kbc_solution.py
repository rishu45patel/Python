quetions=[
  
     [ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

  [ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

  [ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

  [ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

[ "which language was used to create fb?","python","french","javascript","php","none",4],

]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,3200000]
money=0
for i in range(0,len(quetions)):
    quetion=quetions[i]
    print(f"\n\nquestions for Rs.{levels[i]}")
    print(f"a.{quetion[1]}        b.{quetion[2]}   ")
    print(f"c.{quetion[3]}        d.{quetion[4]}   ")

    reply=int(input("enter the answer(1-4)"))
    if(reply==quetion[-1]):
        print(f"correct answer, you have won  Rs.{levels[i]}")

        if(i==4):
            money=10000

        elif(i==9):
            money=320000

        elif(i==14):
            money=10000000
    else:
        print("wrong answer")
        break
print(f"your take home money is {money}")                

































































































