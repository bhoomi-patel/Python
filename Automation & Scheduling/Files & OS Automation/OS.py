# os --> os module provides a portable way to use operating system-dependent functionality.
import os 
# current working directory 
current_dir = os.getcwd()
print("current dir is :-" , current_dir)

# change directory 
os.chdir('/path/to/directory')

#  list contents of directory
files = os.listdir('.') #   ['./<file/folder name>'] ,, ['.'  <- this means all]
print(f"list contents :- {files}")

# create / remove directories
os.mkdir('new_folder')
os.makedirs('/nested/folders/created',exist_ok=True) # create parent dirs too
os.rmdir('folders_to_remove') # remove  directory

# join paths correctly for any os
full_path = os.path.join('folder','subfolder','file.txt')

# check if file/directory exists
exists = os.path.exists('OS.py') # [os.path.exists<filename>]
print("exists or not ? ", exists)
is_file = os.path.isfile('sample.txt')
print("is file or not ? ", is_file)
is_dir = os.path.isdir('numpy')
print("is directory or not ?",is_dir)

# get file information
size = os.path.getsize('sample.txt')
print(f"size of sample.txt is :- {size}")

mod_time = os.path.getmtime('sample.txt')
# returns the timestamp indicating when the file named 'sample.txt' was last modified , This number is a Unix Timestamp (also known as Epoch time).
print(f"mod time is : {mod_time}") 

# Access environment variables
home_dir = os.environ.get('HOME')
print(f"home directory is :- {home_dir}")
# Set environment variable
os.environ['MY_VAR'] = 'value' 

# run a command
exit_code = os.system('echo Hello, World!')
print(f"exit code is :- {exit_code}")
