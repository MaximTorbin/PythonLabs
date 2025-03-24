import os

def create_missing_files(directory='.', missing_files_path='missing_files.txt'):
    if not os.path.exists(missing_files_path):
        print(f"File '{missing_files_path}' not found")
        return
    
    with open(missing_files_path, 'r') as f:
        missing_files = [line.strip() for line in f.readlines() if line.strip()]
    
    if not missing_files:
        print("No missing files to create")
        return
    
    os.makedirs(directory, exist_ok=True)
    
    created_count = 0
    for file in missing_files:
        file_path = os.path.join(directory, file)
        try:
            with open(file_path, 'w') as f:
                pass  # Just create empty file
            created_count += 1
        except OSError as e:
            print(f"Error creating file '{file}': {e}")
    
    print(f"Created {created_count} out of {len(missing_files)} missing files in '{directory}'")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', default='.', help='Directory to create files in')
    parser.add_argument('--missing_files', default='missing_files.txt', help='Path to missing files list')
    args = parser.parse_args()
    
    create_missing_files(args.dirpath, args.missing_files)
