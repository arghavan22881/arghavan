#indor_voice
Data = input('enter you data:\n')
data=Data.lower()
print(data)

#play_back_speed
texts = input("please enter a sentense:\n ")
print(texts.replace(" ", "..."))

#making_Faces
text_2 = input("please input a text with smile or frown emojies:\n")
text_2 = text_2.replace(":)", "🙂")
text_2 = text_2.replace(":(", "🙁")
print(text_2)

#Einstein
m = int(input("enter your desrire mass in kilogram: \n "))
c = 300000000 
E = m * c * c
print(f'{E: ,}')

#Tip_calculater
dollars = float(input("How much was the meal? "))
percent = float(input("What percentage would you like to tip? "))
tip = dollars * percent / 100
print(tip)