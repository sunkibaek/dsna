import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    dirs = os.listdir(path)
    match_file_paths = []

    for dir in dirs:
        dir_path = os.path.join(path, dir)

        if os.path.isfile(dir_path) and dir.endswith(suffix):
            match_file_paths.append(dir_path)

        if os.path.isdir(dir_path):
            match_file_paths = match_file_paths + find_files(suffix, dir_path)

    return match_file_paths


def main():
    print(find_files(".c", "./testdir"))


main()
