#accessing files from test folders 
#IN THIS PROJECT 
#Topic  - file handling , loops , conditional statement , exception handling 

'''
-counted the length of the files in the folders using listdir() functions 
-accessing the text , json , excel file 
-updating or adding text in textfiles and json files.
-used if-else statement for conditions 
-used try - except for error handling 
-file handling to -read - write/append data 
-list to append the input data
-json to convert the data into json format and inputed in json file
'''

import json ,jsonify
import os 
# from flask import jsonify

#counting the length of the files in the folders 
folder_path = "test" #name of the folder
folder = os.listdir(folder_path)        
print("total files in test folder:",len(folder))
print("List of files :\n",folder,"\n")

#taking the input from the user to access the file they want 
files_input = input("enter the file you want from test folder:")
      
try:
    with open(rf"test\{files_input}",'r') as file:
            data = file.read() 
            if files_input:
                print(data)     #getting all the data from the text file
            for_inputting = int(input('enter 1 to input or 0 to end:'))   
            if for_inputting == 1:          
                if files_input=="test_demo.txt":
                    new_text = input('enter the additional text you want:')
                    with open(rf"test\{files_input}",'a') as file:
                        data = file.write("\n"+new_text)         #adding a new text in text file #"\n" for new line
                        if data :
                            print("data inserted successfully!!")



#adding data in json file
                elif files_input == "newfile.json":
                    for_inputting = int(input('enter 1 to input or 0 to end:'))
                    with open(rf"test\{files_input}",'r') as file:
                                    data = json.load(file) 

                    if for_inputting == 1:
                        user_input =input("enter the data in json format:")  
                        json_text = json.loads(user_input)          #converting the text input into json format 
                        # print(json_text)

                        if user_input:  
                            try: 
                                with open(rf"test\{files_input}",'r') as file:
                                        data = json.load(file)              #reading the existing data 

                            except(FileNotFoundError,json.JSONDecodeError):
                                        data = []

                            data.append(json_text)      

                            with open(rf"test\{files_input}",'w') as file:
                                    json.dump(data,file)                        #adding the data in json format 
                                    print("data inserted successfully")
                    
                    
                          
except Exception as e :
    print(f"Error: {e}")
                    

                             
                             
                            
               
                  
                        

                      

