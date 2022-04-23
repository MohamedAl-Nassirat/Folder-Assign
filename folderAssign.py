import os
from random import choice
import shutil
from time import process_time

t1_start = process_time() 
imgs =[]
txt =[]

#Initalize Directory Names
scrsPath = 'main' #Main Directory where images and annotations are being stored
xPath='imgs'
yPath='label'
imgtrainPath='imgTraining' # /imgTraining 
traininglabelPath='labelTraining' # /labelTraining
valimgPath='imgValidation' # /imgValidation 
vallabelPath='labelValidation' #labelValidation

while (True): 
    trainRatio=float(input("What percentage of your data would you like to go to training? (decimal): "))
    validRatio=float(input("What percentage of your data would you like to go to validation? (decimal): "))
    if trainRatio + validRatio == 1:
        train_ratio = trainRatio #store ratio to go into training
        valid_ratio = validRatio #store ratio to go into validation
        break
    else:
        print("Your percentages don't add up to 100%, please retry")
        
        


totalImgCount = (len(os.listdir(scrsPath))-1)/2 # takes the total img count found in /img


#sorting the files into its corresponding arrays, ensures that .txt or .png (can add more room for xml etc)
for (dirname, dirs, files) in os.walk(scrsPath,topdown=True): #possible solution ?? os.walk(scrs patos.walk())
    for filename in files:
        if filename.endswith('.txt'):
            txt.append(filename)
        elif filename.endswith('.png'):
            imgs.append(filename)


#Counter for training and validation folders 
countForTrain = int(len(imgs)*train_ratio)
countForValid = int(len(imgs)*valid_ratio)

#Error handling system for creating the folders
if not os.path.exists(imgtrainPath):
        os.makedirs(imgtrainPath) # creates /imgtraining folder
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

    filetxt = filepng[:-4] + '.txt' # get name of corresponding label , ensures 0.png and 0.txt are catagorized together

                            # /img --> .png      store in    /training ---> /imgTraining              /imgtraining ----> .png
    shutil.move(os.path.join(scrsPath, os.path.join(xPath,filepng)), os.path.join(imgtrainPath, filepng))
    shutil.move(os.path.join(scrsPath, os.path.join(yPath,filetxt)), os.path.join(traininglabelPath, filetxt))

    #remove files from folder once it is sorted
    imgs.remove(filepng)
    txt.remove(filetxt)


#validation directory  
for x in range(countForValid):

    filepng = choice(imgs)
    filetxt = filepng[:-4] +'.txt' 

    #move both files into train directory
    shutil.move(os.path.join(scrsPath, os.path.join(xPath,filepng)), os.path.join(valimgPath,filepng))
    shutil.move(os.path.join(scrsPath, os.path.join(yPath,filetxt)), os.path.join(vallabelPath, filetxt))

    #remove files from arrays
    imgs.remove(filepng)
    txt.remove(filetxt)


IMGcount = len(os.listdir(imgtrainPath)) 
imgLABELcount= len(os.listdir(traininglabelPath)) 
VALcount = len(os.listdir(valimgPath)) 
valLABELcount=len(os.listdir(vallabelPath))  

t1_stop=t1_stop = process_time() #End CPU runtime time

print("Total images in src folder: ", totalImgCount)
print("Training images in folder: ",IMGcount)
print("Training labels in folder:",imgLABELcount)
print("Validation images in folder: ", VALcount)
print("Validation training in folder:", valLABELcount)
print("Total time taken CPU runtime taken: ", (t1_stop-t1_start),"s")