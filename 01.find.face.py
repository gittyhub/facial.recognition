import face_recognition

image = face_recognition.load_image_file('./unknown/alison.brie.community.cast.png') #load image as numpy arrary

face_location = face_recognition.face_locations(image) #Array of coordinates of each face

print('Locations of faces are at \n' + str(face_location))

print(f'Number of faces in photo, {len(face_location)}') #Simple count of the array to count how many people





