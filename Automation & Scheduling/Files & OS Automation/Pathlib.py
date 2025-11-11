# pathlib is a more modern, object-oriented approach to file system paths. It was introduced in Python 3.4 and provides a cleaner interface than os.path.
from pathlib import Path
# Create a Path objects
home = Path.home()
file_path = Path('New-Python/sample.txt')
print ("file path is : ",file_path)

# Join paths (no need for os.path.join)
full_path = home / 'New-Python' / 'sample.txt'
print("full path is : ",full_path)

#---- Path Information ----
# path components
file_path = Path('New-Python/sample.txt')
name = file_path.name
print(f"File name is : {name}")
stem = file_path.stem
print(f"stemming for file is : {stem}")
suffix = file_path.suffix
print(f"suffix of file is : {suffix}")
parent = file_path.parent
print(f"parent of file is : {parent}")

# check path properties
exists = file_path.exists()
print(f"file path is exists or not ? {exists}")
is_file=file_path.is_file()
print(f"file is exists or not > {is_file}")
is_dir=file_path.is_dir()
print(f"directory is exists or not ? {is_dir}")

# file operations
file_path = Path('New-Python/sample.txt')
content = file_path.read_text()
file_path.write_text('Hello World!')

# Read/write binary
data = file_path.read_bytes()
file_path.write_bytes(b'Binary data')

# list directory contents
for item in Path('.').iterdir():
    print(item)
# Find files matching a pattern
python_files = list(Path('.').glob('*.py'))
print(python_files)
all_python_files = list(Path('.').rglob('*.py'))  # Recursive
print(all_python_files)