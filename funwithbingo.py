# Python program to play Bingo Gmae
# import pandas as pd
import pandas as pd
import numpy as np
import random
import time
def namefun(Name1,Age1,Name2,Age2):
# Calling DataFrame constructor
    data1 = {'B':[1,3,12,17,22], 'I':[6,13,18,23,25],"N":[7,11,14,21,24],"G":[4,10,9,20,15],"O":[2,5,8,16,19]}
    df1 = pd.DataFrame(data1)
    data2 = {'B':[13,9,11,22,25], 'I':[8,16,21,15,24],"N":[7,14,2,23,5],"G":[6,12,17,18,20],"O":[1,10,3,4,19]}
    df2 = pd.DataFrame(data2)
    print("First Bingo:",Name1)
    print(df1)
    print("Second Bingo:" ,Name2)
    print(df2)
    return df1,df2
def firstplayer(rand1):                                           #First Player 
     count1=0
     B1=[False,False,False,False,False]
     B2=[False,False,False,False,False]
     C1=False
     C2=False
     first=rand1
     a = df1.where(df1==first).dropna(how='all').dropna(axis=1)
     a1=a.index.tolist()
     a2=a.columns.tolist()
     df1.at[a1[0],a2[0]]=None
     print("First Player Bingo:\n",df1)
     b= df2.where(df2==first).dropna(how='all').dropna(axis=1)
     b1=b.index.tolist()
     b2=b.columns.tolist()
     df2.at[b1[0],b2[0]]=None
     print("\nSecond Player Bingo:\n",df2)
     Firstdig=pd.Series(np.diag(df1), index=[df1.index, df1.columns]).tolist()
     for i in range(len(Firstdig)):
        if(str(Firstdig[i])=="nan"):
             Firstdig[i]=0
     lastdig=pd.Series(np.diag(np.fliplr(df1)), index=[df1.index, df1.columns]).tolist()
     for i in range(len(lastdig)):
        if(str(lastdig[i])=="nan"):
             lastdig[i]=0
     if(len(set(Firstdig))==1 and C1==False):
         count1=count1+1
         C1=True
     if(len(set(lastdig))==1 and C2==False):
        count1=count1+1
        C2=True
     d1=df1.count(axis=0).tolist()
     for i in range(len(d1)):
        if(d1[i]==0 and B1[i]==False):
           count1=count1+1
           B1[i]=True
     d2=df1.count(axis=1).tolist()
     for i in range(len(d2)):
       if(d2[i]==0 and B2[i]==False):
           count1=count1+1
           B2[i]=True
     return count1
def secondplayer(rand2):
     count2=0
     B3=[False,False,False,False,False]
     B4=[False,False,False,False,False]
     C3=False
     C4=False
     second=rand2
     a = df1.where(df1==second).dropna(how='all').dropna(axis=1)
     a1=a.index.tolist()
     a2=a.columns.tolist()
     df1.at[a1[0],a2[0]]=None
     print("First Player Bingo:\n",df1)
     b= df2.where(df2==second).dropna(how='all').dropna(axis=1)
     b1=b.index.tolist()
     b2=b.columns.tolist()
     df2.at[b1[0],b2[0]]=None
     print("\nSecond Player Bingo:\n",df2)
     lastd=pd.Series(np.diag(np.fliplr(df2)), index=[df2.index, df2.columns]).tolist()
     for i in range(len(lastd)):
        if(str(lastd[i])=="nan"):
             lastd[i]=0
     Seconddig=pd.Series(np.diag(df2), index=[df2.index, df2.columns]).tolist()
     for i in range(len(Seconddig)):
        if(str(Seconddig[i])=="nan"):
             Seconddig[i]=0
     if(len(set(Seconddig))==1 and C3==False): 
       count2=count2+1
       C3=True
     if(len(set(lastd))==1 and C4==False): 
         count2=count2+1
         C4=True
     d3=df2.count(axis=0).tolist()
     for i in range(len(d3)):
       if(d3[i]==0 and B3[i]==False):
           count2=count2+1
           B3[i]=True
     d4=df2.count(axis=1).tolist()
     for i in range(len(d4)):
       if(d4[i]==0 and B4[i]==False):
           count2=count2+1
           B4[i]=True
     return count2
def First(df1,df2,rand):
   count1=0
   count2=0
   while(count1<=5 or count2<=5):
    for i in range(0,24,2):
     rand1=rand[i]
     print("Wait First Player Choose Random Number:")
     time.sleep(2)
     print("First Player Choose:",rand1)
     time.sleep(2)
     count1=firstplayer(rand1)
     if(count1>=5):
         print("First Winner")
         quit()
     elif(count2>=5):
         print("Second Winner")
         quit()
     rand2=rand[i+1]
     print("Wait Second Player Choose Random Number:")
     time.sleep(2)
     print("Second Player Choose:",rand2)
     time.sleep(2)
     count2=secondplayer(rand2)
     if(count1>=5):
         print("First Winner")
         quit()
     elif(count2>=5):
         print("Second Winner")
         quit()
     
    
def randomgenerator(df1,df2):
     rand=[i for i in range(1,26)]
     random.shuffle(rand)
     First(df1,df2,rand)
if __name__=="__main__":
  Name1="Upendra"               #input("Enter 1st Player Name:")
  Age1=12                  #int(input("Enter Your Age:"))
  Name2="Kamal"              #input("Enter 2nd Player Name:")
  Age2=21                  #int(input("Enter Your Age:"))
  df1,df2=namefun(Name1,Age1,Name2,Age2)   #Calling namefun Function  
  randomgenerator(df1,df2)                 #Calling Random Function
  


# This code is contributed by Upendra Charasiya
# Contact upendrachaurasiya1998@gmail.com
