# слово по буквам
# Демонстрирует применение цикла for  к строке
word = input("VVedite slovo: ")
print("\nVot vse bukvi po poradku:")
for letter in word:
    print(letter)
input("\n\nPress Enter to Exit")
#Считалка
# Демонстрирует использование функции range()
print('Poschitaem:')
for i in range(10):
    print(i, end= " ")
print('\n\nPerechislim kratnie 5:')
for i in range(0,50,5):
    print(i, end= " ")
print('\n\nPoshitaem v obratnom poradke:')
for i in range(10,0,-1):
    print(i, end= " ")
input("\n\nPress Enter to Exit")
# Анализатор текста
# Демонстрирует работу функции len и оператор in
message = input("Vvedite text: ")
print("\nDlina texta sostavlyet:", len(message))
print("\nSamya chastay soglasnya, 't', ")
if 't' in message:
    print("vstrechaetsya v vashem texte")
else:
    print("ne vstrechaetsya")
input("\n\nPress Enter to Exit")
#Случайные буквы
#Демонстрирует индексацию строк
import random
word = "индекс"
print("V peremennoy word hranitsya: ", word, "/n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low,high)
    print("word[", position, "]\t", word[position])
input("\n\nPress Enter to Exit")



