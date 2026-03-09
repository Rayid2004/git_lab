st = 'a,b,c.f,g'
result = list ( map( lambda y : y.upper() , ( filter (lambda x : x in [ 'a','e','i','o','u'],st )) ))
print(result)


'''TASK # 1'''

# --- Functions ---
def BMI_calculator (weight, height):
    BMI = weight / (height**2)
    return round ( BMI , 2)
''' CALL FUNCTION'''
result = BMI_calculator(70, 1.75)
print(result)


''' TASK # 02 '''
# def summarise_list ( numbers, show_range = True ):
#     mininum = min (numbers)
#     maximum = max (numbers)
#     average = sum (numbers) / len(numbers) 
#     if show_range:
#         range_min_max = maximum - minimum 
#         return minimum, maximum, average, range_min_max
#     else: 
#         return minimum, maximum, average
#     return round (list , 2)
# ''' call function'''
# result = summarise_list ([4,8,15,16,23,42])
# print(result)

