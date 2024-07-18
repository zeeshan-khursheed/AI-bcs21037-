def reverse_word(x):
  return x[::-1]

word = str(input("Enter a Word to reverse:   "))
text = reverse_word(word)
print(text)