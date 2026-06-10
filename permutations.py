import os
import random
final=[] 
ShuffledFinal=[]
wins=[[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
numbers=[1,2,3,4,5,6,7,8,9]
winFinal=[]
# x,y=*[0,3] unpacking not allowed in this context
def Permutations(Parent:list,Child:list,Prefrence:str="Both"): #also this works Prefrence:str="Either"
    '''
    Prefrence defines which is the Target player which only playes smart if say Pref = P1 then its the computer so only plays smart move
    '''
    for i in Parent:
        remains=list(set(numbers)-set(Child))
        nextIsWin=[]
        nextLoseSave=[]
        more=True
        nextLose=False
        for nxt in remains:
            yoo=Child.copy()
            yoo.append(nxt)
            smth(yoo)
            if (checker(wins,TargetP1) if (len(Child)%2==0) else checker(wins,TargetP2) if len(Child)%2==1 else ""): # we need to add (checker(wins,TargetP1) if Prefrence=="P1" else checker(wins,TargetP2) if Prefrence=="P2" else "") to BOTH that is why i did a parent if , otherwise IF ((checker(wins,TargetP1) if Prefrence=="P1" else checker(wins,TargetP2) if Prefrence=="P2" else "")) and (checker(TargetP1)) etc shit for both then 
                nextIsWin.append(nxt)
                more=False
            # if more is True:print("uh")
            TargetP2.append(nxt) if (len(Child)%2==0) else TargetP1.append(nxt)
            if (more is True and ((checker(wins,TargetP2) if (len(Child)%2==0) else checker(wins,TargetP1) if (len(Child)%2==1) else ""))): # HERE WAS THE PROBLEM , bro , suppose pref P1 [1,2,3,5,8,7,] # let the case , idk random nums next chance is of P1 , to make sure it dont loses to P2 as P2=[2,5,7] is Target P2 so we need to append nxt to Target P2 NOT P1
                nextLoseSave.append(nxt)
                nextLose=True
        # if (len(Child)%2==0 if Prefrence=="P1" else len(Child)%2==1 if Prefrence=="P2" else "") and ((more is True or (more is False and i in nextIsWin)) or more is True and nextLose is True and i in nextLoseSave): do this or shorter way , bru no u forgot NextLose bool
        # if (len(Child)%2==0 if Prefrence=="P1" else len(Child)%2==1 if Prefrence=="P2" else "") and ((more is True or (more is False and i in nextIsWin)) or ((more is True and nextLose is False) or ( more is True and nextLose is True and i in nextLoseSave))): see how (more is True and NextLose is True) is repeated twice so it can be condensed
        # print(more,nextLose)
        if Prefrence=="Both" and ((more is True and nextLose is False) or ((more is False and i in nextIsWin) or ( more is True and nextLose is True and i in nextLoseSave))):
            copy1=Parent.copy()
            copy2=Child.copy()
            copy2.append(i)
            copy1.remove(i)
            smth(copy2)
            if checker(wins,TargetP1) or checker(wins,TargetP2):
                final.append(copy2)
                winFinal.append(copy2)
                continue
            if copy1==[]:
                final.append(copy2)
                # continue haha continue not req
            else: Permutations(copy1,copy2,Prefrence)
        else:
            continue
def smth(Target:list):
    global TargetP1, TargetP2
    TargetP1=[]
    TargetP2=[]
    if len(Target)%2==0:
        itrs=int(len(Target)/2)
    if len(Target)%2==1:
        itrs=int((len(Target)+1)/2)
    for i in range(itrs):
        value=Target[2*i]
        TargetP1.append(value)
    TargetP2=list(set(Target)-set(TargetP1)) 
def checker(wins:list,marked:list):# or diect issubset()
    global wincase
    for cases in wins:
        k=0
        for i in cases:
            if i in marked:
                k+=1
                if k==3:
                    wincase=cases
                    return True
            else:
                break
def Shuffle(target:list): # also firect by np.permutations
    copyfinal=final.copy()
    for i in range(len(target)):
        ShuffledFinal.append(elem:=copyfinal[random.randint(0,len(copyfinal)-1)])
        copyfinal.remove(elem)
Permutations([1,2,3,4,5,6,7,8,9],[]) #default case is Both so no need
# P1wins,P2wins=0 error ? :c
P1wins=0
P2wins=0
minLen=len(winFinal[0]) # not 0 ig
for i in winFinal:
    if (len(i)%2==1):
        P1wins+=1
    else :(P2wins)+=1
    if minLen>len(i): minLen=len(i)
print("Total Cases are",len(final))
print("Draw -",len(final)-len(winFinal))
print("P1 wins in",P1wins,"cases")
print("P2 wins in",P2wins,"cases")
print("Fastest win is in",minLen,"total moves")

Shuffle(final)
# for i in ShuffledFinal:
#     print(i)
# for case in ShuffledFinal:
#     smth(case)

# def ShuffledGen():
#     for i in ShuffledFinal():
#         yield i
# genF=ShuffledGen()
base=os.path.abspath(__file__)
os.makedirs("ttt_cases",exist_ok=True)
with open("ttt_cases/allCasesNoDumbforWinningAndLosingBOTH.txt","wt") as fileIG:
    # print(fileIG.readlines()) bro this prints with espace characters 
    # print(fileIG.read().splitlines()[1].strip()) # this is shiz since .. rstrip returns right trim version of string and lstrip .... if arg none then strip espace seq characters and white spaces
    for i in ShuffledFinal:
        if i in winFinal:
            fileIG.write("STATE - Win, ")
            if len(i)%2==1:fileIG.write("WINNER - P1, ")
            if len(i)%2==0:fileIG.write("WINNER - P2, ")
        else: fileIG.write("STATE - Draw, WINNER - Nil, ")
        fileIG.write(f"CASE - {str(i)} ") #NOT work , do not take 2args fileIG.write(str(i)," ") as this is not print bur... also then had to do like fileIG.write(str(i)) then fileIG.write(" ")
        # or do by fileIG.write(f"CASE - {str(i)} \n")
        fileIG.write("\n") if i != ShuffledFinal[len(ShuffledFinal)-1] else "" #to avoid the extra blank line at last , also shuffledFinal is - you need to call shuffle first
# print(len(ShuffledFinal),len(final))
print("hi")