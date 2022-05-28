first_list= [1, 2, 3, 4, 5, 6]

second_list = [11, 22, 33, 44, 55, 66]

final_list = []
def unite_list(first_list,second_list):
    for i in range(0, len(first_list)):
        final_list.append(first_list[i])
        final_list.append(second_list[i])
    return final_list


print(unite_list(first_list,second_list))