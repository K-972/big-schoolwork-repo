# Stuttering Function
#Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.

def stutter(word):
    two_letetrs = word[0] + word[1]
    print(f'{two_letetrs}... {two_letetrs}... {word}')




word = input('word: ')
stutter(word)
