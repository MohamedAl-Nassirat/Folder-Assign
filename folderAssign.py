import os
from random import choice
import shutil
from time import process_time


t1_start = process_time() 
imgs =[]
txt =[]

#Initalize Directory Names
scrsPath = 'img' #Main Directory where images and annotations are being stored
imgtrainPath='imgTraining'
traininglabelPath='labelTraining'
valimgPath='imgValidation'
vallabelPath='labelValidation'

while (True): 
    trainRatio=float(input("What percentage of your data would you like to go to training? (decimal): "))
    validRatio=float(input("What percentage of your data would you like to go to validation? (decimal): "))
    if trainRatio + validRatio == 1:
        train_ratio = trainRatio
        valid_ratio = validRatio
        break
    else:
        print("Your percentages don't add up to 100%, please retry")
        
        


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
# 
#Check every case





if not os.path.exists(imgtrainPath):
        os.makedirs(imgtrainPath)
if not os.path.exists(traininglabelPath):
        os.makedirs(traininglabelPath)
if not os.path.exists(valimgPath):
        os.makedirs(valimgPath)
if not os.path.exists(vallabelPath):
        os.makedirs(vallabelPath)
else:
    print("Directories have already been created, sorting will still continue")
        




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

IMGcount = len(os.listdir(imgtrainPath)) 
imgLABELcount= len(os.listdir(traininglabelPath)) #fix later
VALcount = len(os.listdir(valimgPath)) 
valLABELcount=len(os.listdir(vallabelPath))  # fix later

print("Total images in src folder: ", totalImgCount)
print("Training images in folder: ",IMGcount)
print("Training labels in folder:",imgLABELcount)
print("Validation images in folder: ", VALcount)
print("Validation training in folder:", valLABELcount)
print("Total time taken CPU runtime taken: ", (t1_stop-t1_start),"s")