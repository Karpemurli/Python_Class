
def num(nm):
    try:
        result=[]
        for i in range(1,nm,1):
            result.append(i)
        return result
    except Exception as j:
        return j

try:
    nm=int(input("nm="))
    result=num(nm)
    print(result)
except Exception as m:
    print(m)
           
        
