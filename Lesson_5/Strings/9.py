word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")

common_letters = ""

for i in word1:
    if i in word2 and i not in common_letters:
        common_letters+=i

print(common_letters)
print(len(common_letters))