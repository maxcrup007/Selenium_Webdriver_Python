
import os

# os.chdir('C:/Users/voraw/Desktop/Working/Gaming & Hobby/Ma11/miKu-Doujin/Chane name')
# print(os.getcwd())
# COUNT = 1
# pop = int(input())

def source_population():
    global pop

# for p in os.listdir():
#     p_name, p_ext = os.path.splitext(p)
#     if pop >= 100:
#         f_name = str(pop)
#
#     elif pop >= 10 and pop < 100:
#         p_name = "0" + str(pop)
#
#     else:
#         p_name = "00" + str(pop)
#     change_name()
#
#     new_name = '{} {}'.format(p_name, p_ext)
#     os.rename(p, new_name)

    population = int(input())
    area_base = int(input())

    pop_value = population // area_base

    print(pop_value)



source_population()