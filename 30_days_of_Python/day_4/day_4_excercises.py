# print('Concatenate Thirty Days Of Python')

# firstword = 'Thirty'
# secondword = 'Days'
# thirdword = 'Of'
# fourthword = 'Python'
# space = ' '
# sentance = firstword + space + secondword + space + thirdword + space + fourthword
# print(sentance)


# print('Concatenate Coding for All')
# firstword = 'Coding'
# secondword = 'For'
# thirdword = 'All'
# space = ' '
# sentance = firstword + space + secondword + space + thirdword
# print(sentance)

company = 'Coding For All'
print(company)

print(len(company))
company_uppercase = company.upper()
company_lowercase = company.lower()

print(company_uppercase)
print(company_lowercase)

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company.strip('Coding'))

print(company.find('Coding'))
print(company.replace('Coding', 'Python'))

original = "Python for Everyone"
print(original.replace('Everyone', 'All'))

print(company.split())

big_tech = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(big_tech.split(','))


first_character = company[0]
print(first_character)
last_character = company[-1]
print(last_character)
tenth_character = company[10]
print(tenth_character)

words = company.split()
acronym = "".join(word[0].upper() for word in words)
print(f"The acronym for '{company}' is: {acronym}")

words = original.split()
acronym = "".join(word[0].upper()for word in words)
print(f"The acronym for '{original} is: {acronym}")

firstocurrence = 'C'
print(company.index(firstocurrence))

firstocurrence = 'F'
print(company.index(firstocurrence))

company1 = 'Coding for All People'
print(company1.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

sentance = 'You cannot end a sentence with because because because is a conjunction'
first_occurance = 'because'
print(sentance.index(first_occurance))

# Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

print(sentance.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'

start_index = sentance.index('because because because')
end_index = start_index + len('because because because')
phrase = sentance[start_index:end_index]
modified_sentance = sentance[:start_index] + sentance[end_index:]
print(f"Original Sentance: {sentance}")
print(f"Sliced phrase: {phrase}")
print(f"Sentence with phrase removed: {modified_sentance}")


# Does ''Coding For All' start with a substring Coding?

print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?

print(company.endswith('Coding'))