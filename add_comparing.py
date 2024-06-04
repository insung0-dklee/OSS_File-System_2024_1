import filecmp
import os

def compare_directories(dir1, dir2):

    dircmp = filecmp.dircmp(dir1, dir2)

    print("dir1에만 존재하는 파일:", dircmp.left_only)
    print("dir2에만 존재하는 파일:", dircmp.right_only)

    for common_file in dircmp.common_files:
        path1 = os.path.join(dir1, common_file)
        path2 = os.path.join(dir2, common_file)
        if filecmp.cmp(path1, path2):
            print(f"동일한 파일: {common_file}")
        else:
            print(f"다른 파일: {common_file}")

    for common_dir in dircmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        compare_directories(new_dir1, new_dir2)