"""
Generating all the possible ip adress from a given string.

Conditions - 
1) Values must range from 0 - 255
2) Values must not start with 0
3) String should have 4 parts -- using for loops

"""
def conditions(part)->bool:
    if part == '':
        return False
    val = int(part)
    if (len(part)>3):
        return False
    elif (part[0] == '0' and len(part)>1):
        return False
    elif (val < 0 or val > 255):
        return False
    else:
        return True

def genIp(s):
    combinations = []
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)-1):
                firstPart = s[0:i+1]
                secondPart = s[i+1:j+1]
                thirdPart = s[j+1:k+1]
                fourthPart = s[k+1:len(s)+1]
                if conditions(firstPart) and conditions(secondPart) and conditions(thirdPart) and conditions(fourthPart):
                    finalIp = firstPart+"."+secondPart+"."+thirdPart+"."+fourthPart
                    print(finalIp)
                    combinations.append(finalIp)
                else:
                    pass
                

                

    return combinations



string = "111123"
ans = genIp(string)
print(ans)