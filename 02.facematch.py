import face_recognition

image_of_jpressly = face_recognition.load_image_file('./known/j.pressly.jpg')

#Face encoding to get facial feature to compare faces
kate_face_encoding = face_recognition.face_encodings(image_of_jpressly)[0] #taking only the first array

#image to copare it to
unknown_image = face_recognition.load_image_file('./unknown/m.robbie.unknown.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0] #taking only the first array

#Compare images
results = face_recognition.compare_faces([kate_face_encoding],unknown_face_encoding) #For the first argument you can use a list

if results[0]:
  print('The faces are a match')
else:
  print('The faces do not match')







