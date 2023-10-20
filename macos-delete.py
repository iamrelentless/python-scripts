import os


cwd = os.getcwd()
ctr = 0
# walk through cwd and subdirectories
for root, dirs, files in os.walk(cwd): 
    # root = current directory
    # dirs = subdirectories
    # files = files in current directory
    # increase counter if __MACOSX folder exists and delete it
    if '__MACOSX' in dirs:
        # delete __MACOSX folder even if it has files in it
        os.system('rm -rf ' + os.path.join(root, '__MACOSX'))
        ctr += 1
        

print('Deleted __MACOSX folder in ' + root)
# print number of folders deleted
print('Deleted ' + str(ctr) + ' __MACOSX folders')


