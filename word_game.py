import random
def get_randomword(min_w_len):
 fl=open('text.txt','r')
 str=""
 s=0
 for f in fl :
  str=str+" "+f
 lst=str.split()
 nos={'0','1','2','3','4','5','6','7','8','9'}
 n=len(lst)
 while True :
     w=random.choice(lst)
     
     for a in w:
         if a in nos:
          s=a
          break
     if s in nos:
         continue
     if len(w)<min_w_len : 
         continue
     break
    
    
 word=w.strip().lower()
 return word   
    
   
   

nos=range(4,11)
alf="abcdefghijklmnopqrstuvwxyz"
def min_w_len():
 
 while True:
   a=input("enter minimum word length between 4 & 10  ")
   a=int(a)
   if a in nos:
    break
    
   else:
     print("not a number between 4 & 10")
     continue
 return a


def get_char():
 while True:
  c=input("guess the letter  ")
  c=c.lower()
  if (len(c)==1) & (c in alf):
    break
  else :
    print("wrong input! enter only one letter")
    continue
 return c 




def chr_pstn(c,wrd):
 
   
 p=-1
 pos=set()
 for i in wrd:
   p=p+1
   if c==i:
     pos.add(p)
 return pos



while True:
 rst=""
 str=""
 a=min_w_len()
 word=get_randomword(a)
 ast=[]

 for i in range(0,len(word)):
   ast.append("*")

 noa=int(len(word)*2+4)
 print("the no of attempts is %d"%noa)
 print("the word is :")
 for h in ast:
   rst=rst+h
 print(rst)
 while noa!=0:
   ch=get_char()
   noa-=1
  
   if str==word:
      print("congratulations!! the word is ")
      print(word)
      break
   if ch in word:
     print("correct guess!!! %d chances left"%noa)
     
     pos=chr_pstn(ch,word)
     for k in pos:
      ast[k]=ch
     
     for i in ast:
      str=str+i
     print(str)
     if str==word:
      print("congratulations!! the word is ")
      print(word)
      break
     str=""
   else:
      print("letter not present  %d  chances left"%noa)

 if noa==0:
   print("no chances left, the word is ")
   print(word)
 a=input(" press 1 to try another word or 0 to quit ")
 if a=='1':
   continue
 else:
   break

print("Thank you!!!!")
