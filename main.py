# Main file 
import os

from detection import model, detect
from LLM import get_output
from prompts import PROMPT



# Necessary functions
def check_invalid_inputs(img_path):
    extension = img_path.split('.')[-1]
    image_extension = ['jpg', 'jpeg','png']  #common extensions


    if extension not in image_extension:
        print("Enter  a Valid image path")
        return True
    elif not os.path.isfile(img_path):
        print("Image path does not exist!")
        return True
    else:
        return False

def print_output(name_score_dict,output):
    print("--------------Objects and Confidence Scores--------")
    print(name_score_dict)
    print()
    print("--------------LLM Response--------------------------")
    print(output)


#Get the user input
img_path = input('Give the Image Path : ')

while check_invalid_inputs(img_path):
    img_path = input('Give the Image Path : ')

user_text = input("Give your Prompt : ")
    

#Dummy user_text for testing
# user_text = "Describe the things in the given image"


#Detceting objects in the image
results = model(img_path, verbose = False)   #object detection
name_score_dict = detect(results)




final_prompt = PROMPT + user_text + str(list(name_score_dict.keys()))
output = get_output(final_prompt)


print_output(name_score_dict, output)



