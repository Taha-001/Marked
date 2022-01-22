import face_recognition
from base64_to_image import convert_base64_to_string

known_face_encodings = []
known_face_names = []

def input(name, img_string):
    
    img = convert_base64_to_string(name, img_string)

    # Load a sample picture and learn how to recognize it.
    user_image = face_recognition.load_image_file(img)
    user_face_encoding = face_recognition.face_encodings(user_image)[0]
    
    # add data to arrays of known face encodings and their names
    known_face_encodings.append(user_face_encoding)
    known_face_names.append(name)

    # declare and intialize a dict to store names as key and encodings as its value
    input_dict={}

    for i in range(0,len(known_face_encodings)):
        input_dict[known_face_names[i]]=known_face_encodings[i]

    return input_dict

def exportkfe():
    return known_face_encodings

def exportkfn():
    return known_face_names