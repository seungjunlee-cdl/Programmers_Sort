def solution(array, commands):
    returns = []

    for num_coms in range(len(commands)):
        cur_com = commands[num_coms]
        arr_tmp = array[cur_com[0]-1:cur_com[1]]
        arr_val_wanted = sorted(arr_tmp)[cur_com[2]-1]
        returns.append(arr_val_wanted)

    return returns
