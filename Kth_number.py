Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(array, commands):
    returns = []

    for num_coms in range(len(commands)):
        cur_com = commands[num_coms]
        arr_tmp = array[cur_com[0]-1:cur_com[1]]
        arr_val_wanted = sorted(arr_tmp)[cur_com[2]-1]
        returns.append(arr_val_wanted)

    return returns