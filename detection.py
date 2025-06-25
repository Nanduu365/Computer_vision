from ultralytics import YOLO


model = YOLO("yolov3u.pt")


# model.info()


results = model(r"C:\Users\alwin\OneDrive\Desktop\test\sample_img_2.jpg")

# print(results[0])



def detect(results):
    name_score_dict = {}
    for box in results[0].boxes:
        class_id = int(box.cls[0].item())  
        name = model.names[class_id]  
        confidence = float(box.conf[0].item()) 

        name_score_dict[name] =confidence

    return name_score_dict


# print(detect(results))



