import os
import pytsk3

def recover_files(image_path, output_path):
    # Open the disk image using pytsk3
    image = pytsk3.Img_Info(image_path)
    filesystem = pytsk3.FS_Info(image)
    
    recovered_files = []

    # Iterate over all entries in the filesystem
    for directory_entry in filesystem.recurse():
        # Check if the entry is a regular file and its size is greater than 0
        if (directory_entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_REG and
            directory_entry.info.meta.size > 0):
            
            # Check if the file is marked as allocated (not deleted)
            if directory_entry.info.meta.flags == pytsk3.TSK_FS_META_FLAG_ALLOC:
                
                # Recover the file data
                file_data = directory_entry.read_random(0, directory_entry.info.meta.size)
                
                # Create the output file path
                output_file_name = directory_entry.info.name.name.decode()
                output_file_path = os.path.join(output_path, output_file_name)
                
                # Save the recovered file to the output path
                with open(output_file_path, "wb") as output_file:
                    output_file.write(file_data)
                
                # Add the recovered file to the list
                recovered_files.append(output_file_path)
    
    return recovered_files

def main():
    # Get the disk image path and output directory from user input
    image_path = input("Enter the path to the disk image: ")
    output_path = input("Enter the output directory to save recovered files: ")
    
    # Ensure the output directory exists, create it if necessary
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Recover files from the disk image
    recovered_files = recover_files(image_path, output_path)
    
    # Output results
    if recovered_files:
        print("Files recovered successfully:")
        for file_path in recovered_files:
            print(file_path)
    else:
        print("No files recovered.")

if __name__ == "__main__":
    main()
