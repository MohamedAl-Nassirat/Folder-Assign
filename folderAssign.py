import os
from random import choice
import shutil

#Empty Arrays to store
imgs =[]
txt =[]

#Initalize Directory Names
scrsPath = 'img' #Main Directory where images and annotations are being stored
#scrsAnnotationPath='annotations'
#scrsImagesPath='images' <sub directories, no longer in use>

trainPath = 'training'
imgtrainPath='imgTraining'
traininglabelPath='labelTraining'

valPath = 'validation'
valimgPath='imgValidation'
vallabelPath='labelValidation'


#90% will go into training , 10% will go into validation
train_ratio = 0.9
valid_ratio = 0.1



totalImgCount = len(os.listdir(scrsPath))/2

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

#Create directories we need an training directory --- > /img training, /labelTraining
#                              validation directory ---- > /img Validation, /label Validation
#                    Creates and stores it in src 

# trainPath imgtrainPath traininglabelPath
# valPath valimgPath vallabelPath



os.mkdir(imgtrainPath)
os.mkdir(traininglabelPath)

os.mkdir(valimgPath)
os.mkdir(vallabelPath)

#Training Path
for x in range(countForTrain):

    filepng = choice(imgs) # get name of random image from origin dir
    filetxt = filepng[:-4] +'.txt' # get name of corresponding label 
    
                            # /img --> .png      store in    /training ---> /imgTraining              /imgtraining ----> .png
    x=shutil.move(os.path.join(scrsPath, filepng), os.path.join(trainPath, imgtrainPath), os.path.join(imgtrainPath, filepng))
    y=shutil.move(os.path.join(scrsPath, filetxt), os.path.join(trainPath, traininglabelPath), os.path.join(traininglabelPath, filetxt))

    #remove files from folder once it is sorted
    imgs.remove(filepng)
    txt.remove(filetxt)



#validation directory  
for x in range(countForValid):

    filepng = choice(imgs)
    filetxt = filepng[:-4] +'.txt' 

    #move both files into train directory
    z=shutil.move(os.path.join(scrsPath, filepng), os.path.join(valPath, valimgPath), os.path.join(valimgPath,filepng))
    j=shutil.move(os.path.join(scrsPath, filetxt), os.path.join(valPath, vallabelPath), os.path.join(vallabelPath, filetxt))

    #remove files from arrays
    imgs.remove(filepng)
    txt.remove(filetxt)



print("Total images in folder: ", totalImgCount)

 