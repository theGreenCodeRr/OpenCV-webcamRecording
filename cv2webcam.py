# for webcam reading and writing
cap = cv2.VideoCapture(0)                    # Load webcam into cap
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')     # Define codec
out = cv2.VideoWriter('cam_output.mp4',fourcc, 20.0, (640,480)) # Define output
while(cap.isOpened()):                       # Check if cap is opened
    ret, frame = cap.read()                  # Read frame from cap
    if ret == True:                          # Check if frame is read
        out.write(frame)                     # Write frame to output
        cv2.imshow("Video", frame)           # Output a frame
        if cv2.waitKey(30) == 27:            # Wait for key input
            break
    else:
        break
cap.release()                               # Release cap
out.release()                               # Release output
cv2.destroyAllWindows()                     # Destroy all windows