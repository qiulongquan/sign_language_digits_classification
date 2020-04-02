import os, shutil

original_dataset_dir = '/home/qiulongquan/Tensorflow_js/sign_language_digits_classification/python/Dataset'
folder_name = ["0","1","2","3","4","5","6","7","8","9"]

for j in range(0, len(folder_name)):
    print(folder_name[j])

    files = os.listdir(original_dataset_dir + "/" + folder_name[j] + "/")
    print(type(files))

    # Pythonでパス文字列からファイル名・フォルダ名・拡張子を取得、結合
    # https: // note.nkmk.me / python - os - basename - dirname - split - splitext /
    for i in range(0, len(files)):
        print(files[i])
        root, extension = os.path.splitext(files[i])
        if files[i] == ".DS_Store":
            print("This is no image.")
        elif extension == ".png" or ".jpeg" or ".jpg":
            # shutil.copy()  文件复制（源文件保留，新目录文件创建）
            # shutil.move()  文件移动（源文件删掉，新目录文件创建）
            if os.path.exists(original_dataset_dir + "/" + folder_name[j] + "/rename_folder/"):
                shutil.copy(original_dataset_dir + "/" + folder_name[j] + "/" + files[i], original_dataset_dir + "/" + folder_name[j] + "/rename_folder/" + folder_name[j] + "_" + str(i + 1) + ".jpg")
            else:
                os.mkdir(original_dataset_dir + "/" + folder_name[j] + "/rename_folder/")
                shutil.copy(original_dataset_dir + "/" + folder_name[j] + "/" + files[i], original_dataset_dir + "/" + folder_name[j] + "/rename_folder/" + folder_name[j] + "_" + str(i + 1) + ".jpg")

print("Rename Done.")
