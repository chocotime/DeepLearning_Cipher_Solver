from dic import *

print("암호문을 입력하세요")
question = input() #암호문

def decoding(encode_str, n):
    
    decode_str=""
    
    for i in encode_str:              
        if (ord(i)>=65 and ord(i)<=90):     
            if(ord(i)-n < 65):      
                x=chr(ord(i)+(26-n))
            else:
                x=chr(ord(i)-n)                  
            decode_str+=x
        elif (ord(i)>= 97 and ord(i) <= 122): 
            if(ord(i)-n < 97):
                x=chr(ord(i)+(26-n)) 
            else:
                x=chr(ord(i)-n)                 
            decode_str+=x            
        elif i==' ':        
            decode_str+=i
    return decode_str

def deeplearning():
    blank = [-1]
    strtmp = possible[end][0]
    for i in range(len(strtmp)):
        if strtmp[i] == ' ':
            blank.append(i)
            
    f = open("dic.py", 'a')
    for i in range(len(blank)-1):
        if strtmp[blank[i]+1:blank[i+1]] not in lists:
            lists.append(strtmp[blank[i]+1:blank[i+1]])
            f.write("lists.append(\"%s\")\n" % strtmp[blank[i]+1:blank[i+1]])
    f.close()
    print("학습에 성공하였습니다.")

possible = [[]for i in range(26)]

for i in range(26):
    poss = 0
    tmp = decoding(question,i)
    for j in lists:
        if j in tmp:
            poss +=1
    possible[i] = [tmp, poss]
tmp = 0
for i in range(26):
    if possible[i][1] > tmp:
        tmp = possible[i][1]
        end = i



print(possible[end][0])
print("단어를 학습시킬까요? (Y/N)")
ans = input()
if ans == 'y' or ans == 'Y':
    deeplearning()
else: 
    exit(1)
