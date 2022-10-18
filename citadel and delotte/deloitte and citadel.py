# def solution(A):
#     # write your code in Python 3.6
#     count_dict = {}
#     odd_counter = 0 # Maintains the number of odd valued pairs

#     for i in range(len(A)):
#         if(not count_dict.get(A[i])): # if element not present in dict, then add
#             count_dict[A[i]] = 1
#             odd_counter+=1
#         else:
#             count_dict[A[i]]+=1
#             if(count_dict[A[i]]%2==0):
#                 odd_counter-=1
#             else:
#                 odd_counter+=1

#     print(odd_counter)


# solution([1,2,2,3])


# import heapq
# def get_min_cost(arr):
#     heapq.heapify(arr)
#     while(len(arr) > 1):
#         sum_current = heapq.heappop(arr) + heapq.heappop(arr)
#         heapq.heappush(arr, sum_current)
#         print(arr)


# get_min_cost([700, 100,250,1000])


global d
d = {}

def get_sum_pos(arr, ops, k):
    global d
    temp = []
    # print('help', ops)
    # If minus sign found at first position stop loop
    if(ops[0] == '-'):
        return
        
    # Begin case: if no minus signs found, then start children for the tree by iterating each position change to minus and build on each
    # of those trees
    # if( '-' not in ops):
    #     for i in range(len(ops)):
    #         op_child = ops[:i] + '-' + ops[i+1:]
    #         get_sum_neg(arr, op_child, k)

    else:
        for i in range(len(ops)):
            op_child = ops[:i] + '-' + ops[i+1:]
            if(not d.get(op_child) and (op_child != ops) ):
                get_sum_pos(arr, op_child, k)
        
        # If already computed return
        if( not d.get(ops) ):
            for i in range(len(ops)):
                if(ops[i] == '-'):
                    temp.append( arr[i] - k )
                else:
                    temp.append( arr[i] + k ) 

            d[ops] = abs(max(temp) - min(temp))

            
        # get FIRST FOUND minus index
        if('-' in ops):
            minus_ind = ops.index('-')
            get_sum_pos(arr, ops[:minus_ind-1] + '-' + ops[minus_ind:], k)
        else:
            return




def get_sum_neg(arr, ops, k):
    global d
    temp = []
    # print('help', ops)
    # If minus sign found at first position stop loop
    if(ops[0] == '+'):
        return
        
    # Begin case: if no minus signs found, then start children for the tree by iterating each position change to minus and build on each
    # of those trees
    # if( '+' not in ops):
    #     for i in range(len(ops)):
    #         op_child = ops[:i] + '+' + ops[i+1:]
    #         get_sum_neg(arr, op_child, k)

    else:
        for i in range(len(ops)):
            op_child = ops[:i] + '+' + ops[i+1:]
            if(not d.get(op_child) and (op_child != ops) ):
                get_sum_neg(arr, op_child, k)
        
        # If already computed return
        if( not d.get(ops) ):
            for i in range(len(ops)):
                if(ops[i] == '+'):
                    temp.append( arr[i] + k )
                else:
                    temp.append( arr[i] - k )
            
            d[ops] = abs(max(temp) - min(temp))

            
        # get FIRST FOUND minus index
        if('+' in ops):
            minus_ind = ops.index('+')
            get_sum_neg(arr, ops[:minus_ind-1] + '+' + ops[minus_ind:], k)
        else:
            return

import sys
sys.setrecursionlimit(10000)

ar = [-100000, 100000]
ar = [3,4,7,-7]
ar = [-3,0,1]
k = 3

ops_pos = '+'*len(ar)
ops_neg = '-'*len(ar)


get_sum_pos(ar, ops_pos, k)
get_sum_neg(ar, ops_neg, k)

print(d)
print(len(d), 2**len(ar))
print(min(d.values()))
