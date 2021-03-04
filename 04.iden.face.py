import face_recognition
from PIL import Image, ImageDraw

#Identify faces and draw a box around known faces
#Unknown around unknown faces
#https://www.youtube.com/watch?v=QSTnwsZj2yc

image_of_alison = face_recognition.load_image_file('./known/alison.brie.jpg') #load image as numpy arrary
alison_face_encoding = face_recognition.face_encodings(image_of_alison)[0] #taking only the first array

#Create arry of encoding and names
known_face_encoding = [
  alison_face_encoding]

known_face_names = [
  "Alison.Bri"
]


#Load test image to find faces in
test_image = face_recognition.load_image_file('./unknown/alison.brie.community.cast.png') #load image as numpy arrary

#Find faces in test image
face_location = face_recognition.face_locations(test_image)
face_encoding = face_recognition.face_encodings(test_image, face_location)

#Convert to PIL format
pil_image = Image.fromarray(test_image)

#Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

#Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_location, face_encoding):
  matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
  name = "Unknon Person"

  #If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  #Draw the box, another small rectangle, then a name in the small rectangle
  draw.rectangle(((left,top), (right,bottom)), outline=(0,0,0))

  #Draw label
  tex_width, text_height = draw.textsize(name)
  draw.rectangle(((left, bottom - text_height -10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
  draw.text((left + 6, bottom-text_height - 5), name, fill=(255,255,255,255))

del draw

pil_image.show()



