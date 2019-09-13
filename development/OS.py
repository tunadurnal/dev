import os
from time import sleep
from datetime import datetime

print(os.getcwd())
os.chdir('C:/Users/Tuna Durnal/Downloads/Python Projects/opencv_py/')
print(os.getcwd())
print(os.listdir())
if not os.path.exists('neg-2'):
    os.makedirs('neg-2/Sub_Dir-2')
    #os.rename('neg-2', 'neg-3')

print(os.listdir('neg-2/'))
print(os.stat('neg-2'))
print(os.environ.get('HOME'))
print(dir(os.path))
print(os.path.join(os.getcwd(), 'test.txt'))
print(os.path.isdir('test.txt'))
print(os.path.isfile('test.txt'))

##for dirpath, dirnames, filenames in os.walk(os.getcwd()):
##    print('Current Path:', dirpath)
##    print('Directories:', dirnames)
##    print('Files:', filenames)
    
#os.rmdir('neg-3/Sub_Dir-2') sadece 'Sub_Dir-2' silinir.
#os.removedirs('neg-3/Sub_Dir-2') iki dosya da silinir.

