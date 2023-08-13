
#####################################  Step 1 (Don't need)  #####################################
# import os

# folders = ['train', 'test', 'valid']

# # Check if any of the folders already exist
# existing_folders = [folder for folder in folders if os.path.exists(folder)]

# if existing_folders:
#     print("Error: The following folders already exist:", ', '.join(existing_folders))
# else:
#     # Create the folders
#     for folder in folders:
#         os.makedirs(folder)
#     print("The folders 'train,' 'test,' and 'valid' have been created successfully.")

#####################################  Step 2  #####################################

import os

folders = ['train', 'test', 'valid']

# Check if any of the folders already exist
existing_folders = [folder for folder in folders if os.path.exists(folder)]

if existing_folders:
    print("Error: The following folders already exist:", ', '.join(existing_folders))
else:
    # Create the folders
    for folder in folders:
        os.makedirs(os.path.join(folder, 'images'))
        os.makedirs(os.path.join(folder, 'labels'))
    print("The folders 'train,' 'test,' and 'valid' have been created successfully, along with 'images' and 'labels' folders.")


#####################################  Step 3  #####################################

import os
import shutil

source_folders = ['WIDER_test', 'WIDER_train', 'WIDER_val']
destination_folders = ['test', 'train', 'valid']

for source_folder, destination_folder in zip(source_folders, destination_folders):
    if not os.path.exists(source_folder):
        print(f"Error: {source_folder} does not exist.")
        continue

    if not os.path.exists(destination_folder):
        print(f"Error: {destination_folder} does not exist. Make sure you have created the train, test, and valid folders first.")
        continue

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, 'images', file)
                shutil.copy(source_path, destination_path)

print("Photos have been successfully copied to the train, test, and valid folders.")


#####################################  Step 4 (Don't need)  #####################################
# import os
# import shutil

# split_folder = 'wider_face_split'
# annotation_file = 'wider_face_train_bbx_gt.txt'

# # Check if the split folder exists
# if not os.path.exists(split_folder):
#     print(f"Error: {split_folder} does not exist.")
#     exit()

# # Check if the annotation file exists
# annotation_path = os.path.join(split_folder, annotation_file)
# if not os.path.exists(annotation_path):
#     print(f"Error: {annotation_file} does not exist in {split_folder}.")
#     exit()

# # Function to process the annotation file
# def process_annotation_file(annotation_path):
#     train_folder = 'train'
#     labels_folder = 'labels'

#     with open(annotation_path, 'r') as file:
#         current_filename = None
#         current_file = None

#         for line in file:
#             line = line.strip()

#             if line.startswith('#'):
#                 continue

#             if line[0].isdigit() and '/' in line:
#                 if current_file is not None:
#                     current_file.close()

#                 parts = line.split('/')
#                 filename = parts[-1].replace('.jpg', '')
#                 current_filename = filename + '.txt'
#                 current_file = open(os.path.join(train_folder, labels_folder, current_filename), 'w')
#                 continue

#             if current_file is None:
#                 continue

#             numbers = line.split(' ')
#             if len(numbers) == 10:
#                 last_6_numbers = numbers[4:]
#                 if all(num == '0' for num in last_6_numbers):
#                     continue

#                 first_4_numbers = numbers[:4]
#                 current_file.write(' '.join(first_4_numbers) + '\n')

#         if current_file is not None:
#             current_file.close()

# # Process the annotation file
# process_annotation_file(annotation_path)

# print("Annotation files have been created and saved in the train/labels folder successfully.")

#####################################  Step 5  #####################################

import os
import shutil

split_folder = 'wider_face_split'
train_annotation_file = 'wider_face_train_bbx_gt.txt'
valid_annotation_file = 'wider_face_val_bbx_gt.txt'

# Check if the split folder exists
if not os.path.exists(split_folder):
    print(f"Error: {split_folder} does not exist.")
    exit()

# Check if the train annotation file exists
train_annotation_path = os.path.join(split_folder, train_annotation_file)
if not os.path.exists(train_annotation_path):
    print(f"Error: {train_annotation_file} does not exist in {split_folder}.")
    exit()

# Check if the valid annotation file exists
valid_annotation_path = os.path.join(split_folder, valid_annotation_file)
if not os.path.exists(valid_annotation_path):
    print(f"Error: {valid_annotation_file} does not exist in {split_folder}.")
    exit()

# Function to process the annotation file and copy files to the labels folder
def process_annotation_file(annotation_path, labels_folder):
    with open(annotation_path, 'r') as file:
        current_filename = None
        current_file = None

        for line in file:
            line = line.strip()

            if line.startswith('#'):
                continue

            if line[0].isdigit() and '/' in line:
                if current_file is not None:
                    current_file.close()

                parts = line.split('/')
                filename = parts[-1].replace('.jpg', '')
                current_filename = filename + '.txt'
                current_file = open(os.path.join(labels_folder, current_filename), 'w')
                continue

            if current_file is None:
                continue

            numbers = line.split(' ')
            if len(numbers) == 10:
                # last_6_numbers = numbers[4:]
                # if all(num == '0' for num in last_6_numbers):
                #     continue

                first_4_numbers = numbers[:4]
                current_file.write(' '.join(first_4_numbers) + '\n')

        if current_file is not None:
            current_file.close()

# Process the train annotation file and copy files to train/labels folder
train_labels_folder = os.path.join('train', 'labels')
if not os.path.exists(train_labels_folder):
    os.makedirs(train_labels_folder)
process_annotation_file(train_annotation_path, train_labels_folder)

# Process the valid annotation file and copy files to valid/labels folder
valid_labels_folder = os.path.join('valid', 'labels')
if not os.path.exists(valid_labels_folder):
    os.makedirs(valid_labels_folder)
process_annotation_file(valid_annotation_path, valid_labels_folder)

print("Annotation files have been created and saved in the train/labels and valid/labels folders successfully.")


#####################################  Step 6  #####################################

import os

train_labels_folder = 'train/labels'
valid_labels_folder = 'valid/labels'

# Function to process the text files in a folder
def process_text_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)  # Move the file pointer to the beginning
                file.truncate()  # Clear the file content

                for line in lines:
                    modified_line = '0 ' + line
                    file.write(modified_line)

# Process the train/labels folder
if os.path.exists(train_labels_folder):
    process_text_files(train_labels_folder)
else:
    print(f"Error: {train_labels_folder} does not exist.")

# Process the valid/labels folder
if os.path.exists(valid_labels_folder):
    process_text_files(valid_labels_folder)
else:
    print(f"Error: {valid_labels_folder} does not exist.")

print("Prefix '0' has been added to each line in the text files successfully.")

#####################################  Step 7 (Don't need) #####################################
# import os

# train_folder = 'train'
# images_folder = 'images'
# labels_folder = 'labels'

# # Function to check filenames without extensions
# def check_filenames():
#     images_path = os.path.join(train_folder, images_folder)
#     labels_path = os.path.join(train_folder, labels_folder)

#     image_files = set(os.path.splitext(filename)[0] for filename in os.listdir(images_path))
#     label_files = set(os.path.splitext(filename)[0] for filename in os.listdir(labels_path))

#     common_files = image_files.intersection(label_files)

#     total_files = len(common_files)
#     checked_files = 0

#     for filename in common_files:
#         print(f"Matching filename: {filename}")
#         checked_files += 1

#     success_rate = 100 * checked_files / total_files if total_files != 0 else 100
#     print(f"File checking completed. Checked {checked_files} files out of {total_files} ({success_rate:.2f}% success rate).")

# # Check the filenames in train/images and train/labels folders
# if os.path.exists(train_folder):
#     check_filenames()
# else:
#     print(f"Error: {train_folder} folder does not exist.")


#####################################  Step 8  #####################################

import os

train_folder = 'train'
valid_folder = 'valid'
images_folder = 'images'
labels_folder = 'labels'

# Function to check filenames without extensions in the train folder
def check_train_filenames():
    train_images_path = os.path.join(train_folder, images_folder)
    train_labels_path = os.path.join(train_folder, labels_folder)

    train_image_files = set(os.path.splitext(filename)[0] for filename in os.listdir(train_images_path))
    train_label_files = set(os.path.splitext(filename)[0] for filename in os.listdir(train_labels_path))

    train_common_files = train_image_files.intersection(train_label_files)

    train_total_files = len(train_common_files)
    train_checked_files = 0

    for filename in train_common_files:
        print(f"Matching filename in train folder: {filename}")
        train_checked_files += 1

    train_success_rate = 100 * train_checked_files / train_total_files if train_total_files != 0 else 100
    print(f"Train file checking completed. Checked {train_checked_files} files out of {train_total_files} ({train_success_rate:.2f}% success rate).")

    return train_success_rate

# Function to check filenames without extensions in the valid folder
def check_valid_filenames():
    valid_images_path = os.path.join(valid_folder, images_folder)
    valid_labels_path = os.path.join(valid_folder, labels_folder)

    valid_image_files = set(os.path.splitext(filename)[0] for filename in os.listdir(valid_images_path))
    valid_label_files = set(os.path.splitext(filename)[0] for filename in os.listdir(valid_labels_path))

    valid_common_files = valid_image_files.intersection(valid_label_files)

    valid_total_files = len(valid_common_files)
    valid_checked_files = 0

    for filename in valid_common_files:
        print(f"Matching filename in valid folder: {filename}")
        valid_checked_files += 1

    valid_success_rate = 100 * valid_checked_files / valid_total_files if valid_total_files != 0 else 100
    print(f"Valid file checking completed. Checked {valid_checked_files} files out of {valid_total_files} ({valid_success_rate:.2f}% success rate).")

    return valid_success_rate

# Check the filenames in train/images and train/labels folders
if os.path.exists(train_folder):
    print("Checking filenames in train/images and train/labels folders...")
    train_success_rate = check_train_filenames()
else:
    print(f"Error: {train_folder} folder does not exist.")
    train_success_rate = 0

print()

# Check the filenames in valid/images and valid/labels folders
if os.path.exists(valid_folder):
    print("Checking filenames in valid/images and valid/labels folders...")
    valid_success_rate = check_valid_filenames()
else:
    print(f"Error: {valid_folder} folder does not exist.")
    valid_success_rate = 0

print()
print(f"Final success rate for train folder: {train_success_rate:.2f}%")
print(f"Final success rate for valid folder: {valid_success_rate:.2f}%")

#####################################  Step 9 (Run only once)  #####################################
import os
import cv2

train_folder = 'train'
valid_folder = 'valid'
images_folder = 'images'
labels_folder = 'labels'

# Function to get image shape
def get_image_shape(image_path):
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    return width, height

# Function to process label files
def process_labels(folder):
    images_path = os.path.join(folder, images_folder)
    labels_path = os.path.join(folder, labels_folder)

    image_files = os.listdir(images_path)
    label_files = os.listdir(labels_path)

    for image_file in image_files:
        image_name, _ = os.path.splitext(image_file)
        image_path = os.path.join(images_path, image_file)
        width, height = get_image_shape(image_path)

        label_file = f"{image_name}.txt"
        label_file_path = os.path.join(labels_path, label_file)

        if os.path.exists(label_file_path):
            with open(label_file_path, 'r') as label_file:
                lines = label_file.readlines()

            with open(label_file_path, 'w') as label_file:
                for line in lines:
                    values = line.strip().split()
                    if len(values) == 5:
                        class_id, x, y, w, h = map(float, values)
                        center_x = (x + (w / 2)) / width
                        center_y = (y + (h / 2)) / height
                        w /= width 
                        h /= height
                        label_file.write(f"{class_id} {center_x} {center_y} {w} {h}\n")
                    else:
                        label_file.write(line)

# Process the label files in train folder
if os.path.exists(train_folder):
    print("Processing label files in train folder...")
    process_labels(train_folder)
    print("Label files in train folder processed successfully.")
else:
    print(f"Error: {train_folder} folder does not exist.")

print()

# Process the label files in valid folder
if os.path.exists(valid_folder):
    print("Processing label files in valid folder...")
    process_labels(valid_folder)
    print("Label files in valid folder processed successfully.")
else:
    print(f"Error: {valid_folder} folder does not exist.")

#####################################  Step 10  #####################################

