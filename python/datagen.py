import os
import shutil

# 三部分的sum必须等于1，否则会报错误
train_ratio = 0.8
test_ratio = 0.2
validation_ratio = 0

if train_ratio+test_ratio+validation_ratio != 1.0:
    raise Exception("train_ratio + test_ratio + validation_ratio != 1.0 三部分的sum必须等于1，否则无法分配图片!")

original_dataset_dir = 'Dataset'
base_dir = 'hand_sign_digit_data'
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

folder_name = ["0","1","2","3","4","5","6","7","8","9"]


def distribution_ratio(path):
    files_len = len(os.listdir(path))
    train_end = int(files_len*train_ratio)
    test_end = int((train_ratio+test_ratio)*files_len)
    print(files_len, train_end, test_end)
    return files_len, train_end, test_end


for j in range(0, len(folder_name)):
    os.mkdir(os.path.join(train_dir, folder_name[j]))
    os.mkdir(os.path.join(validation_dir, folder_name[j]))
    os.mkdir(os.path.join(test_dir, folder_name[j]))

    files_len, train_end, test_end = distribution_ratio(os.path.join(original_dataset_dir, folder_name[j], "rename_folder"))
    fnames = [folder_name[j] + '_{}.jpg'.format(i) for i in range(1, train_end+1)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], "rename_folder", fname)
        dst = os.path.join(train_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

    fnames = [folder_name[j] +'_{}.jpg'.format(i) for i in range(train_end+1, test_end+1)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], "rename_folder", fname)
        dst = os.path.join(test_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

    fnames = [folder_name[j] +'_{}.jpg'.format(i) for i in range(test_end+1, files_len+1)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], "rename_folder", fname)
        dst = os.path.join(validation_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

print("Data generate Done.")
