import json

with open('..\dictionary\cat_dictionary.json', 'r') as f:
    cat_dictionary = json.load(f)

with open('..\dictionary\dog_dictionary.json', 'r') as h:
    dog_dictionary = json.load(h)

with open('..\machinelearning\data.json', 'r') as g:
    # global data
    data = json.load(g)

# current_list = data.get('tomas')

def calculate_person_type(handle):
    if not handle:
        return 'notfound'
    global data
    current_list = data.get(handle)
    if not current_list:
        return 'notfound'

    cat_final_sum = 0
    dog_final_sum = 0

    for x in current_list:
        y = x.split()
        #print(y)
        cat_sum = 0
        dog_sum = 0
        for word in y:
            cat_value = cat_dictionary.get(word)
            dog_value = dog_dictionary.get(word)
            #print (value)
            if cat_value is not None:
                cat_sum += cat_value
            if dog_value is not None:
                dog_sum += dog_value
        cat_average = cat_sum/len(y)
        dog_average = dog_sum/len(y)
        cat_final_sum += cat_average
        dog_final_sum += dog_average

    cat_final_average = cat_final_sum/len(current_list)
    dog_final_average = dog_final_sum/len(current_list)

    if cat_final_average > dog_final_average:
        return 'cat'
    elif dog_final_average > cat_final_average:
        return 'dog'
    elif dog_final_average == cat_final_average:
        return 'dogcat'
    else:
        return 'notfound'

# print("cat {}".format(cat_final_average))
# print("dog {}".format(dog_final_average))