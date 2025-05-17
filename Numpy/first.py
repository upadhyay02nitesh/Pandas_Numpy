import numpy as np

# a=np.array([10,20,30])
# b=np.array([20,30,40])
# print(a*b)
# # print(type(a))

# c=np.array([[10,20],[30,40]])
# for i in range(len(c)):
#     for j in range(len(c[i])):
#         print(i,j,c[i][j])

a=np.array([5,7,10,20,30])
# n=len(a)
# print(a[-2:])
# print(a[-3:-1])
# print(a[::-1])
# print(a[-4:-2])

c=np.array([[10,20,30],[30,40,50],[60,70,70]])
# print(c[0])
# print(c[0:2,0:2])
# print(c[0,1:3])
# print(c[2,1:3])
# for i in range(len(c)):
#     for j in range(len(c[i])):
#         print(i,j,c[i][j])
#     print()

# print(c[1,2:3])
# print(c[2,0:2])


# print(np.shape(c))
# print(np.size(c))
# print(np.ndim(c))
# print(c.dtype)
# print(c.astype(str))


# a=np.array([10,20,30])
# b=np.array([20,30,40])
# print(a*b)
# print(a-b)
# print(a+b)
# print(a/b)
# print(a%b)
# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.multiply(a,b))

# # a=np.array([10,20,30])
# # b=np.array([2])
# # print(np.power(a,b))
# # print(np.sqrt(a))

# a=np.array([10,20,30])
# b=np.array([40,50,60])
# c=np.concatenate([a,b])
# print(c)

a=np.array([[10,20],[30,40],[10,20],[30,40]])
b=np.array([[40,50],[60,70],[10,20],[30,40]])
# c=np.concatenate([a,b],axis=1)
# print(c)
# # c=np.concatenate([a,b],axis=1)
# # print(c)

# print(np.hstack([a,b]))
# print(np.vstack([a,b]))



# arr=np.array([11,22,44,55,66,77,88,99])
# s=np.array_split(arr,3)
# print(s)
# print(np.append(arr,90))
# print(np.insert(arr,0,100))


a=np.array([[100,20],[30,40]])
# print(np.insert(a,1,[50,60]))
# print(np.insert(a,1,[50,60],axis=1))
# # print(np.insert(a,1,[50],axis=0))

# # print(a)
# print(np.delete(a,1))
# print(np.delete(a,1,axis=1))


# print(np.sort(a))

a=np.array([10,20,30])
# print(np.where(a==20))
# print(np.where(a%2==0))

# print(np.searchsorted(a,20))

# a=np.array([10,20,30,47,50,63,70])
# fa=[True,False,True,True,True,True,True]
# new=a[fa]
# print(new)

# fa=a>15
# new=a[fa]
# print(new)

# fa=a%2==0
# new=a[fa]
# print(new)


# a=np.array([10,20,30,47,50,63,70])
# print(np.sum(a))
# print(np.min(a))
# print(np.max(a))
# print(np.size(a))
# print(np.mean(a))
# print(np.cumsum(a))
# print(np.cumprod(a))


# # price=np.array([10,20,30,47,50,63,70])
# # quantity=np.array([1,2,3,4,5,6,7])

# # s=np.cumprod([price,quantity],axis=0)
# # print("Price :",price)
# # print("Quantity :",quantity)
# # print("Per Product Sell :",s[1])
# # print("Total Sell :",s[1].sum())
# 
import statistics as st
price=np.array([10,20,30,47,20,30,50,63,70])
print(np.mean(price))
print(np.median(price))
print(st.mode(price))
print(np.std(price))
print(np.std(price)**2)
print(np.var(price))


# price=[300,100,350,150,200]
# sales=[10,20,7,17,3]
# print(np.corrcoef(price,sales))