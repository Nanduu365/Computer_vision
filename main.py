# Main file 
from detection import model, detect
from LLM import get_output


def check_invalid_inputs(img_path):
    extension = img_path.split('.')[-1]
    image_extension = ['jpg', 'jpeg','png']  #common extensions

    if extension not in image_extension:
        print("Enter  a Valid image path")

#Get the user input

img_path = input('Give the Image Path : ')
check_invalid_inputs(img_path)
user_text = input("Give your Prompt : ")

#Dummy user_text
user_text = "Describe the things in the given image"


#Detceting objects in the image
results = model(img_path)

name_score_dict = detect(results)

PROMPT = '''
You are an expert image analyzer and you should be able to describe about the objects that are given in the image.
The list of objects that are present in the image would be given to you and you should describe about the objects.

Example:
Describe the things in the given image 'bicycle', 'car'

Response:

Bicycle --Bicycle is a two wheeled vehicle that uses no fuel and is more eco friendly than the others

Car --  Car is a type of car designed to run on a flat surface. It is usually a standard, low mileage car, but includes a large number of other types of vehicles such as motorcycles. 
The concept of a car is about the use of a vehicle to make an informed decision about what is best for your car's needs.
'''



final_prompt = PROMPT + user_text
for key in name_score_dict.keys():
    final_prompt += key 


output = get_output(final_prompt)

print("--------------Objects and Confidence Scores--------")
print(name_score_dict)
print("--------------LLM Response--------------------------")
print(output)



