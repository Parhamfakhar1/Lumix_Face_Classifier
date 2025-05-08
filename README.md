
# Lumix Face Classifier

A Python-based real-time face detection and classification tool that distinguishes between "Human" and "Non-Human" faces using OpenCV and face_recognition. New human faces are automatically saved and reused in future detections.

## Features
- Real-time webcam face detection
- Labels faces as Human or Non-Human
- Automatically saves and remembers new human faces
- Encodings stored in `faces.json`, images in `known_faces/`

## Requirements
```bash
pip install opencv-python face_recognition numpy
```

## Run
```bash
python detect.py
```

## Exit
Press `q` to close webcam window.

## Structure
- `detect.py` – main detection script
- `known_faces/` – folder to store face images
- `faces.json` – stores face encodings

## Author
By Parham Fakhari


---


# طبقه‌بندی چهره لومیکس

یک ابزار شناسایی چهره با پایتون که به صورت زنده چهره‌ها را از طریق دوربین شناسایی کرده و آن‌ها را به دو دسته «انسان» و «غیر انسان» تقسیم می‌کند. چهره‌های انسانی جدید به صورت خودکار ذخیره می‌شوند.

## ویژگی‌ها
- شناسایی زنده چهره از طریق وب‌کم
- برچسب‌گذاری چهره به عنوان انسان یا غیرانسان
- ذخیره و یادآوری خودکار چهره‌های جدید انسانی
- استفاده از `faces.json` و پوشه `known_faces/` برای ذخیره اطلاعات

## نصب پیش‌نیازها
```bash
pip install opencv-python face_recognition numpy
```

## اجرا
```bash
python detect.py
```

## خروج
برای خروج کلید `q` را فشار دهید.

## ساختار پروژه
- `detect.py` – اسکریپت اصلی
- `known_faces/` – پوشه ذخیره تصاویر چهره‌ها
- `faces.json` – فایل ذخیره اطلاعات رمزگذاری‌شده چهره‌ها

## نویسنده
ساخته‌شده توسط پرهام فخاری
