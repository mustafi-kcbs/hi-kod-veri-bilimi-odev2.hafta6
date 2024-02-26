
#1

import numpy as np
a=np.array([7,5,3,1,9],dtype="int")
print(a)
print(a.ndim)
print(a.size)

#2

import numpy as np
iki_b= np.array([[1,2,6,7],[4,3,9,5]])
uc_b= np.array([[[7,5,14],[21,8,11]],[[8,6,20],[14,3,9]]])
print(iki_b)
print(uc_b)

print(iki_b.ndim)
print(uc_b.ndim)
print(iki_b.size)
print(uc_b.size)
print(np.shape(iki_b))
print(np.shape(uc_b))


#3
import numpy as np
iki_b= np.array([[1,2,6,7],[4,3,9,5]])
uc_b= np.array([[[7,5,14],[21,8,11]],[[8,6,20],[14,3,9]]])

print(iki_b[0,1])
print(iki_b[0,3])
print(uc_b[1,1,2])
print(uc_b[0,0,1])


#4

import numpy as np
iki_b= np.array([[1,2,6,7],[4,3,9,5]])
uc_b= np.array([[[7,5,14],[21,8,11]],[[8,6,20],[14,3,9]]])

print(iki_b[0,1:3])
print(iki_b[1,1:4])
print(uc_b[0,1:])
print(uc_b[1,0,1:3])


#5
import numpy as np
a0=np.zeros((5,3))
a1=np.ones((5,3))
print(a0)
print(a1)
b=np.concatenate([a0,a1],axis=0)
c=np.concatenate([a0,a1],axis=1)
print(b)
print(c)
