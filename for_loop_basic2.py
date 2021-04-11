# To see output for each section un-comment each section.

# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def Biggie_Size(x):
#     for i in range(len(x)):
#         if x[i] > 0:
#             x[i] = "Big"
#     return x
#     print (x)
# print(Biggie_Size([-1,3,5,-5]))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number 
# of positive values. (Note that zero is not considered to be a positive number).  
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def Count_Positives(x):
#     var = 0
#     for i in x:
#         if i > 0:
#             var += 1
#         x[len(x) - 1] = var
            
#     return x
    
# print(Count_Positives([-1,1,1,1]))
# print(Count_Positives([1,6,5,-4,-2,-7,-2]))


# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def Sum_Total(answer):
#     result = {
#         'sumtotal': None,
#     }
#     if len(answer) == 0:
#         return result
#     else:
#         result['sumtotal'] = 0
#     for value in answer:

#         result['sumtotal'] += value
#     return result
# print(Sum_Total([1, 2, 3, 4]))
# print(Sum_Total([6,3,-2]))



# 4. Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def Ave(answer):
#     result = {
#         'average': None,
#     }
#     if len(answer) == 0:
#         return result
#     else:
#         sumtotal = 0    
#     for value in answer:
#         sumtotal += value
#     result['average'] = sumtotal / len(answer)

#     return result
# print(Ave([1, 2, 3, 4]))

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0 

# def Length(answer):
#     result = len(answer)
#     return result
# print(Length([37, 2, 1, -9]))
# print(Length([]))


# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def Minimum(answer):
    # if len(answer) == 0:
    #     return False
#     result = answer[0]
#     for val in answer:
#         if val < result:
#             result = val
#     return result
    
# print(Minimum([37, 2, 1, -9]))
# print(Minimum([]))


#  7.Maximum - Create a function that takes a list and returns the maximum value in the array.
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def Maximum(answer):
#     if len(answer) == 0:
#         return False
#     result = {        
#         'maximum': None,     
#     }
#     if len(answer) == 0:
#         return result
#     else:        
#         result['maximum'] = answer[0]        
    
#     for val in answer:
#         if val > result['maximum']:
#             result['maximum'] = val
#     return result
# print(Maximum([37, 2, 1, -9,]))
# print(Maximum([]))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has 
# the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(answer):
#     result = {
#         'sumtotal': None,
#         'average': None,
#         'length': 0,
#         'minimum': None,
#         'maximum': None,
#     }
#     if len(answer) == 0:
#         return result
#     else:
#         result['sumtotal'] = 0
#         result['maximum'] = answer[0]
#         result['minimum'] = answer[0]
    
#     for value in answer:
#         if value > result['maximum']:
#             result['maximum'] = value
#         elif value < result['minimum']:
#             result['minmum'] = value

#         result['sumtotal'] += value
#         result['length'] += 1
#     result['average'] = result['sumtotal'] / len(answer)

#     return result
# print(ultimate_analysis([37, 2, 1, -9]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37, 2, 1, -9]) should return [-9, 1, 2, 37]
def Reverse_List(x):
    value = int(len(x) / 2)
    for i in range(value):
        x[i] , x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
    return x

print(Reverse_List([37, 2, 1, -9]))


