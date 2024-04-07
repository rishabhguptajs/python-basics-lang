# excercise 1

exp = [2200, 2350, 2325, 3200]
print("Q1: In Feb, how many dollars you spent extra compare to Jan?")
print(exp[1] - exp[0])

print("Q2: Find out your total expense in first quarter (first three months) of the year.")
print(sum(exp[:3]))

print("Q3: Find out if you spent exactly 2000 dollars in any month")
print(2000 in exp)

print("Q4: June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list")
exp.append(1980)

print("Q5: You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this")
exp[2] -= 200
print(exp)

# excercise 2

heros=['spider man','thor','hulk','iron man','captain america']

print("Q1: Length of the list")
print(len(heros))

print("Q2: Add 'black panther' at the end of this list")
heros.append('black panther')
print(heros)

print("Q3: You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'")
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

print("Q4: Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.")
heros[1:3] = ['doctor strange']
print(heros)

print("Q5: Sort the list in alphabetical order")
heros.sort()
print(heros)