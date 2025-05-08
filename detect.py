
import cv2
import face_recognition
import os
import json
import numpy as np

known_faces_dir = 'known_faces'
faces_json = 'faces.json'

# لود اطلاعات ذخیره‌شده
if os.path.exists(faces_json):
    with open(faces_json, 'r') as f:
        face_data = json.load(f)
else:
    face_data = {"encodings": [], "names": []}

# تبدیل داده‌های json به numpy array
known_encodings = [np.array(enc) for enc in face_data["encodings"]]
known_names = face_data["names"]

# فعال کردن دوربین
video = cv2.VideoCapture(0)

human_counter = len(known_names)

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.45)
        label = "Non-Human"

        if True in matches:
            label = "Human"
        else:
            # چون چهره جدید ولی انسانه، ذخیره‌اش کن
            human_counter += 1
            label = "Human"
            name = f"Human_{human_counter:02}"
            known_encodings.append(face_encoding)
            known_names.append(name)

            # ذخیره چهره به صورت تصویر
            face_image = frame[top:bottom, left:right]
            cv2.imwrite(f"{known_faces_dir}/{name}.jpg", face_image)

            # آپدیت faces.json
            face_data["encodings"].append(face_encoding.tolist())
            face_data["names"].append(name)
            with open(faces_json, 'w') as f:
                json.dump(face_data, f)

        # نمایش مستطیل و برچسب
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Lumix - Face Classifier", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
