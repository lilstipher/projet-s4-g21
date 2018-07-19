from PIL import Image, ImageDraw
import os
import os.path
import time
import face_recognition
import matplotlib.pyplot as plt

all_list=[]
pixel=[]
timeT=[]
#informations=[]
def show_rectangle_on_faces(img_path):
    time_start = time.time()
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(img_path)
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    #t1=time.time()
    face_locations = face_recognition.face_locations(image)
    #t2=time.time()
    #print('time for face_location',t2-t1)
    information = [filename]
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))
    pil_image = Image.fromarray(image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

    for face_location in face_locations:

        top, right, bottom, left = face_location
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
        information.append((left,top,right,bottom))
        #print(information)
    #pil_image.show()
    all_list.append(information)
    time_end = time.time()
    #print('Time cost is ', time_end - time_start,'s')
    Width, Height = pil_image.size
    pixel.append(Width*Height)
    timeT.append(time_end - time_start)

    return information
for image_file in os.listdir("E:\PycharmProject\Test"):
    filename = os.path.basename(image_file)
    #print(filename)
    #all_list.append(show_rectangle_on_faces(os.path.join("E:\PycharmProject\Test", image_file)))

    #print(information)

    show_rectangle_on_faces(os.path.join("E:\PycharmProject\Test", image_file))
#print(time_pixel)
plt.plot(pixel,timeT, 'bo')
plt.show()
