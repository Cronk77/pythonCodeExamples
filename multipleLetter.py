def get_input():
    user_input = input("Enter in a word to check if it has multiples of the same letters: ")
    while len(user_input) == 0:
        user_input = input("Error, Enter in a word to check if it has multiples of the same letters: ")
    return user_input

def check_if_multiple(user_input):
    letter_count = 0 # carries the highest letter count
    input_list = list(user_input) 
    #print(input_list)
    count_dic = {}
    for i in input_list:
        if i == ' ': # ignores ' ' as part of the check
            break
        if i not in count_dic:
            count_dic[i] = 1
        else:
            count_dic[i] = count_dic.get(i) + 1
        if letter_count < count_dic.get(i):
            letter_count = count_dic.get(i)

    if letter_count > 1:
        return True
    else:
        return False

user_input = get_input()
result = check_if_multiple(user_input)
if result is True:
    print(f"The String '{user_input}' has multiple of the same letters.")
else:
    print(f"The String '{user_input}' does NOT have multiple of the same letters.")
