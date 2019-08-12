#Question : https://leetcode.com/problems/two-sum/
#Python 3 script
#Given nums = [2, 7, 11, 15], target = 9,

import numpy as np

def  my_(nums, target):
  s=np.intersect1d(nums,target-nums)
  k=[]
  for i in range(len(s)) :
    k.append(np.where(nums == s[i])[0][0])
  return(s,k)

nums = np.array([4,2, 12, 11,6,3,7,6, 15])

target = 9

my_(nums,target)

#question: how can I write this without for ... loop?
