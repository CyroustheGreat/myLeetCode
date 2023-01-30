# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Answer:

def twoSum (num:list[int], target:int):
    index1=0;
    while index1<len(num):
        for index2 in range(index1+1, len(num)):
            if num[index1] == (target - num[index2]):
                print('index: ',index1, ': ', num[index1], '&' ,'index: ', index2, ': ', num[index2]);
        index1+=1;
           
twoSum([1,2,6,3,7], 8);
