letter="hey my name is {} and i'm from {}"
country="india"
name="harry"
print(letter.format(name,country))
print(f"hey iam {name} from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))