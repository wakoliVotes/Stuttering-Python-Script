# Writing a function that stutters a word as if someone is struggling to read it
# For example, with any word entered, there is repeating the first tow letters twice, with an ellipsis
#  The final word is then read out
# This program relies on user input
stutterWord = input("Enter the word to stutter: ")
print(stutterWord[:2], ".......", stutterWord[:2], "........", stutterWord)
print(stutterWord,"\n")