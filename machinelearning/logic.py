import json

with open('dictionary.json', 'r') as f:
    dictionary = json.load(f)

with open('data.json', 'r') as g:
    data = json.load(g)

current_list = data.get('tomas')
final_sum = 0

for x in current_list:
    y = x.split()
    print(y)
    sum = 0
    for word in y:
        value = dictionary.get(word)
        if value is not None:
            sum += value
    average = sum/len(y)
    final_sum += average

final_average = final_sum/len(current_list)

print(final_average)