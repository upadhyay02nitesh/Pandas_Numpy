
def sort_by_parity(num_str):
    evens=[i for i in num_str if int(i)%2==0]
    evens=sorted(evens,reverse=True)
    
    odds=[i for i in num_str if int(i)%2!=0]
    odds=sorted(odds,reverse=True)
    print(evens)
    print(odds)

    result=[]
    even,odd=0,0
    for num in num_str:
        if int(num)%2==0:
            result.append(evens[even])
            even+=1
        else:
            result.append(odds[odd])
            odd+=1
    return "".join(result)




num_str="6841793268"
print(num_str)
print(sort_by_parity(num_str))