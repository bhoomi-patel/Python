# The shutil (shell utilities) module provides higher-level file operations, particularly for copying and archiving.
import shutil
# copy file
f = shutil.copy2('sample.txt','new.txt')
print(f)
# Copy a directory and its contents
shutil.copytree('source_dir', 'destination_dir')

# move/rename files or directories
shutil.move('source.txt', 'destination.txt')

# Remove directory and all its contents
shutil.rmtree('directory_to_remove')  # DANGEROUS! No recycle bin 

# Create archives (zip, tar, etc.)
shutil.make_archive('archive_name', 'zip', 'directory_to_archive')

# Unpack an archive
shutil.unpack_archive('archive.zip', 'extract_dir')


# Get disk usage statistics
total, used, free = shutil.disk_usage('/')
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")
