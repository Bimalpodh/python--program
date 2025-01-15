# def mxmPermutationValue(input1,input2):
#   def fact(num):
#     if num<=1:
#       return 1
#     else:
#       return num*fact(num-1)
  
  
#   v="aeiou"
#   li=[]
#   for i in input2:
#     s=0
#     lc=i.lower()
#     for j in range(len(i)):
#       if lc[j] not in v:
#         s=s+1
#     li.append(s)
#   max=max(li)
#   ans=fact(max)
#   return ans
 
# input2=3     
# input=['hello','ccbc','aeiou']
# print(mxmPermutationValue(input2,input))


def mxmPermutationValue(num_strings, strings):
    # Corrected factorial function
    def fact(num):
        if num <= 1:
            return 1
        else:
            return num * fact(num - 1)  # Recursive factorial calculation

    vowels = "aeiou"
    consonant_counts = []

    for string in strings:
        consonant_count = 0
        for char in string.lower():
            if char not in vowels:
                consonant_count += 1
        consonant_counts.append(consonant_count)

    max_consonants = max(consonant_counts)
    result = fact(max_consonants)
    return result, consonant_counts

# Test with example input
num_strings = 3
strings = ['hello', 'ccbc', 'aeiou']
print(mxmPermutationValue(num_strings, strings))
