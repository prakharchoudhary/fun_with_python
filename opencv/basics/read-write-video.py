import cv2

videoCapture = cv2.VideoCapture(raw_input('Enter the path to file: '))
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('Output.avi',
                              cv2.VideoWriter_fourcc('I','4','2','0'),
                              fps, size)
success, frame = videoCapture.read()
# print success
while success:	# Loop until there are no more frames
	videoWriter.write(frame)
	success, frame = videoCapture.read()
