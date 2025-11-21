import shutil
folder_name = input("Enter folder name: ")
shutil.make_archive(folder_name, 'zip', folder_name)
print("Folder zipped successfully")
