import os


def find_files(suffix, path):
    dirs = os.listdir(path)
    match_file_paths = []

    for dir in dirs:
        dir_path = os.path.join(path, dir)

        if os.path.isfile(dir_path) and dir.endswith(suffix):
            match_file_paths.append(dir_path)

        if os.path.isdir(dir_path):
            match_file_paths = match_file_paths + find_files(suffix, dir_path)

    return match_file_paths


print(find_files(".c", "./testdir"))
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(".h", "./testdir"))
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']

print(find_files(".py", "./"))
# ['./find_files.py']
