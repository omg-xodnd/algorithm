import sys
sys.stdin = open('4358.txt', 'r')

def get_answer():
    tree_dict = {}
    cnt = 0
    while True:
        try:
            tree = input()
            cnt += 1
            if tree not in tree_dict:
                tree_dict[tree] = 1
            else:
                tree_dict[tree] += 1

        except EOFError:
            break

    sorted_dict = sorted(tree_dict.items())

    for key, val in sorted_dict:
        print(key + ' ' + str(round(val*100/cnt, 4)))

get_answer()