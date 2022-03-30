# Folder Assign 

Folder assign is an automated sorting system meant to prepare your machine learning training sets and sort them accordingly. 
In this specific script you will get the optino of assigning the percentage amount of files you want to be split. Files will be safely split into a selection of Training and Validation folders, and ensures the corresponding annotations don't get lost in the splitting. 

<img width="777" alt="Screen Shot 2022-03-29 at 10 52 10 PM" src="https://user-images.githubusercontent.com/96555957/160754625-e62219e1-614b-4923-9961-6c17b770759e.png">


<img width="772" alt="Screen Shot 2022-03-29 at 10 57 04 PM" src="https://user-images.githubusercontent.com/96555957/160754650-fd71ffb9-300e-4ec3-aadb-a2c023313853.png">


## Input Prompt

<img width="730" alt="Screen Shot 2022-03-29 at 10 54 57 PM" src="https://user-images.githubusercontent.com/96555957/160754668-aaffc339-72a6-47f2-b76e-a8b337af2472.png">




## How it works
  1. Load your .png and .txt files into the main img folder
  2. Run the script `python3 folderassign.py`
  3. Files will be sorted accordingly into Training and Validation folders and can be easily accessed in `imgTraining` `imgValidation` `labelValidation` `labelTraining`
##

Mohamed Al-Nassirat
