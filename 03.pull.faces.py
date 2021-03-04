from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./known/term.jpg')
face_locations = face_recognition.face_locations(image) #this finds the location of the faces, return an arrary for (top, right, bottom, left)

for face in face_locations:
  top,right, bottom, left = face #Here we assign the four attributes to their respectful variables location
  face_image = image[top:bottom, left:right] #then we take the image that we loaded and appply the variable attributes above to get the image of the face
  pil_image = Image.fromarray(face_image) #then the PIL function takes the fromarray to cut the faces out 
  #pil_image.show()
  pil_image.save(f'{top}.png') #saving the file using the location of the top variable as the file name





