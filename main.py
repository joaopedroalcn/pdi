#yolo predict model=yolov8m-pose.pt source='videos/TratamentoFisioVisaoComp3.mp4'

from ultralytics import YOLO

model = YOLO('yolov8m-pose.pt')

results = model(source='newfilterimg.jpg', show=True, conf=0.3, save=True)


