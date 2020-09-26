def vowelcount(str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        for letter in str:
            if (vowel == letter):
                count = count+1

    print(count)


vowelcount("consonants and vowels")
vowelcount("a")
vowelcount("aeiouaeiou")
