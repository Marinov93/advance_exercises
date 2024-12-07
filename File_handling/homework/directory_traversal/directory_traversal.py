import os


def save_extenstions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            my_dict[extension] = my_dict.get(extension, []) + [filename]
        elif os.path.isdir(file):
            save_extenstions(file)


directory = input()
my_dict = {}
save_extenstions(directory)

