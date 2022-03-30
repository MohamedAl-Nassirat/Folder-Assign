# Folder Assign 


Folder assign is an automated sorting system meant to prepare your machine learning training sets and sort them accordingly. 
In this specific script, 90% of the .png and .txt files will be sorted at random into Training and 10% will
go to Validation. 


<img width="768" alt="Screen Shot 2022-03-26 at 1 22 32 AM" src="https://user-images.githubusercontent.com/96555957/160230459-56027c60-15df-4b1b-b531-4bd8924a024f.png">
<img width="770" alt="Screen Shot 2022-03-26 at 1 28 03 AM" src="https://user-images.githubusercontent.com/96555957/160230469-6813dcdc-b23d-4383-a641-0eb379812932.png">


In this example, the script would sort 32,088 images with a performing runtime of `1.533304214477539 s` 




## How it works
  1. Load your .png and .txt files into the main img folder
  2. CD into directory saved and run  `python3 folderassign.py` in terminal
  3. Files will be sorted at random into Training and Validation according to your percentages and the sets and can be easily accessed in `imgTraining` `imgValidation` `labelValidation` `labelTraining`
  
## To-Do
  1. Accept all data types (.xml, .csv, .jpeg etc)
  

##

Mohamed Al-Nassirat
