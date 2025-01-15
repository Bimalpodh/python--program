dictionary={
  9:"sita",
  8:"laxmi",
  7:'PRIYATAMA' 
}

# print(dictionary[9])
# print(dictionary.get("radha")) # it gives none if the element does not present in dict
# print(dictionary.keys())
# print(dictionary.values())
# for key in dictionary.keys():
# print(f"the value corresponding to the {key} is {dictionary[key]}")

print(dictionary.items())
for key,value in dictionary.items():
  print(f"{key} :: {value}")
 