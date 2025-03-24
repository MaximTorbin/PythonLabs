import os
import argparse

def check_files(directory='.', files=None):
    if files is None:
        files = []
    
    if not files:
        total_size = 0
        file_count = 0
        
        for root, dirs, files_in_dir in os.walk(directory):
            for file in files_in_dir:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        print(f"Directory info for '{directory}':")
        print(f"Total files: {file_count}")
        print(f"Total size: {total_size} bytes")
        return
    
    existing_files = []
    missing_files = []
    
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.exists(file_path):
            existing_files.append(file)
        else:
            missing_files.append(file)
    with open('existing_files.txt', 'w') as f:
        f.write('\n'.join(existing_files))
    
    with open('missing_files.txt', 'w') as f:
        f.write('\n'.join(missing_files))
    print("Existing files:")
    print('\n'.join(existing_files) if existing_files else "None")
    print("\nMissing files:")
    print('\n'.join(missing_files) if missing_files else "None")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', default='.', help='Directory path to check')
    parser.add_argument('--files', nargs='*', default=[], help='Files to check')
    args = parser.parse_args()
    
    check_files(args.dirpath, args.files)
