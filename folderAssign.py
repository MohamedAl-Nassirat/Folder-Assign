import os
from random import choice
import shutil
from time import process_time

#
imgs =[]
txt =[]
t1_start = process_time() 

#Initalize Directory Names
scrsPath = 'img' #Main Directory where images and annotations are being stored
imgtrainPath='imgTraining'
traininglabelPath='labelTraining'
valimgPath='imgValidation'
vallabelPath='labelValidation'


#90% will go into training , 10% will go into validation
train_ratio = 0.9
valid_ratio = 0.1


totalImgCount = len(os.listdir(scrsPath))-1


#sorting the files into its corresponding arrays
for (dirname, dirs, files) in os.walk(scrsPath):
    for filename in files:
        if filename.endswith('.txt'):
            txt.append(filename)
        elif filename.endswith('.png'):
            imgs.append(filename)


#Counter for training and validation folders
countForTrain = int(len(imgs)*train_ratio)
countForValid = int(len(imgs)*valid_ratio)
# Create directories to store 
if os.path.isdir(imgtrainPath) == True:
    print("The directories have already been created. Sorting will still continue")
elif os.path.isdir(imgtrainPath) == False:
    
    os.mkdir(imgtrainPath)
    os.mkdir(traininglabelPath)
    os.mkdir(valimgPath)
    os.mkdir(vallabelPath)
    IMGcount = len(os.listdir(imgtrainPath)) + len(os.listdir(traininglabelPath))
    VALcount = len(os.listdir(valimgPath)) + len(os.listdir(vallabelPath))  



#Training Path
for x in range(countForTrain):

    filepng = choice(imgs) # get name of random image from origin dir
    filetxt = filepng[:-4] +'.txt' # get name of corresponding label , ensures 0.png and 0.txt are catagorized together
    
                            # /img --> .png      store in    /training ---> /imgTraining              /imgtraining ----> .png
    shutil.move(os.path.join(scrsPath, filepng), os.path.join(imgtrainPath, filepng))
    shutil.move(os.path.join(scrsPath, filetxt), os.path.join(traininglabelPath, filetxt))

    #remove files from folder once it is sorted
    imgs.remove(filepng)
    txt.remove(filetxt)


#validation directory  
for x in range(countForValid):

    filepng = choice(imgs)
    filetxt = filepng[:-4] +'.txt' 

    #move both files into train directory
    shutil.move(os.path.join(scrsPath, filepng), os.path.join(valimgPath,filepng))
    shutil.move(os.path.join(scrsPath, filetxt), os.path.join(vallabelPath, filetxt))

    #remove files from arrays
    imgs.remove(filepng)
    txt.remove(filetxt)

t1_stop=t1_stop = process_time()

print("Total images in src folder: ", totalImgCount)
print("Training images in folder: ",IMGcount)
print("Validation images in folder: ", VALcount)
print("Total time taken: ", (t1_stop-t1_start))