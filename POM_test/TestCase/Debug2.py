
import os

os.chdir('C:/Users/voraw/Desktop/Working/Gaming & Hobby/Ma11/miKu-Doujin/Chane name')
print(os.getcwd())
COUNT = 1


def change_name():
    global COUNT
    COUNT = COUNT + 1


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if COUNT >= 100:
        f_name = str(COUNT)

    elif COUNT >= 10 and COUNT < 100:
        f_name = "0" + str(COUNT)

    else:
        f_name = "00" + str(COUNT)
    change_name()

    new_name = '{} {}'.format(f_name, f_ext)
    os.rename(f, new_name)




#### Source Code


# import os
#
# os.chdir('D://Geeksforgeeks')
# print(os.getcwd())
# COUNT = 1
#
#
# # Function to increment count
# # to make the files sorted.
# def increment():
#     global COUNT
#     COUNT = COUNT + 1
#
#
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)
#     f_name = "geek" + str(COUNT)
#     increment()
#
#     new_name = '{} {}'.format(f_name, f_ext)
#     os.rename(f, new_name)









