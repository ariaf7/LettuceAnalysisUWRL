# Import all important libraries
from picamera2 import Picamera2, Preview
from datetime import datetime, timedelta
import time
import schedule
# Create a function that takes the photo, so it can be called once a day
def photo():
# Get current date and time
    current_datetime = datetime.now()
# Round up the hour if the minute is greater than 30
    if current_datetime.minute >= 30:
        current_datetime += timedelta(hours=1)
# Turn the time into a H:0:0 time, which just represents the hours, because minutes and seconds don't matter
    current_datetime = current_datetime.replace(minute =0, second = 0, microsecond =0)
# How we are representing the date and time
    current_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")

# Convert datetime to a string to be used as the file name
    str_current_datetime = str(current_datetime)

# Create a file object along with extension
    file_name = str_current_datetime+".jpg"

# Initialize object picam2
    with Picamera2() as picam2:

# Configure the camera settings to encompass the most area possible
        camera_config = picam2.create_still_configuration(main={"size":(3280,2464)})
        picam2.configure(camera_config)
        picam2.resolution= (3280, 2464)
        picam2.framerate =15

# Opens camera preview window
        picam2.start_preview(Preview.QTGL)
        picam2.start()
        time.sleep(2)

# Take the picture and save it to the lettucePhoto directory
        picam2.capture_file(f'/home/ciroh-uwrlphoto/Desktop/lettucePhoto/{file_name}')
# Close window
        picam2.stop_preview()
# Takes a photo every minute, can be used to test the schedule library and the code
#schedule.every(1).minute.do(photo)
# Take a picture at 2:00 pm every day. (Calls photo function when the date-time is 2:00pm)
schedule.every().day.at("14:00").do(photo)

# Put the code to sleep for 24 hrs, to save RAM
while True:
    schedule.run_pending()
    time.sleep(3600)
    # Use time.sleep(1) if testing with schedule.every(1).minute.do(photo)
                                                                                                                                                                                            