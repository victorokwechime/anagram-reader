anagrams = ['stable', 'dog', 'tar', 'god', 'pat', 'rat', 'fried', 'tables']
grouped_anagrams = {}
for string in anagrams:
    sorted_string = str(sorted(string))
    if sorted_string in grouped_anagrams:
        grouped_anagrams[sorted_string].append(string)
    else:
        grouped_anagrams[sorted_string] = [string]
print(list(grouped_anagrams.values()))
      

are_anagrams = lambda x, y: str(sorted(x.lower())) == str(sorted(y.lower()))
print(are_anagrams('stable', 'tables'))
print(are_anagrams('god', 'dog'))
print(are_anagrams('rat', 'tar'))
print(are_anagrams('fried', 'pat'))
