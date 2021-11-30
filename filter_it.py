from genericpath import exists
import cv2
import streamlit as st
import numpy as np 
from PIL import Image
import os

# 6 Filters : Brightness, Negative, Pencil Sketch, Color Extract, Color Focus, Duo-tone


# Brightness Filter : Increase or decrease brightness
def brightness(frame,val):

    h, w = frame.shape[:2]
    # Convert image to HSV(Hue, Saturation, Value) colorspace and store as nupy array with datatype float64 to reduce loss during scaling.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype=np.float64)

    # User provides value between 0 and 150, which must be scaled down to be within range 0 to 1.5 so that pixel values can be appropriately scaled
    val = val/100 
    
    # To change brightness, saturation(Channel 1) and value(Channel 2) of image must be altered
    # Scale pixel values for channel 1 by multiplying with val. For values that exceed 255, change the value to the max, which is 255.
    hsv[:, :, 1] = hsv[:, :, 1] * val
    hsv[:, :, 1][hsv[:, :, 1] > 255] = 255

    # Scale pixel values for channel 2 by multiplying with val. For values that exceed 255, change the value to the max, which is 255.
    hsv[:, :, 2] = hsv[:, :, 2] * val
    hsv[:, :, 2][hsv[:, :, 2] > 255] = 255

    # Convert pixel values datatype back to integer 8 bit, and then convert image from HSV to BGR color space that OpenCV uses.
    hsv = np.array(hsv, dtype=np.uint8)
    bright_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bright_img = cv2.resize(bright_img, (w, h), interpolation= cv2.INTER_LINEAR)
    return bright_img


# Negative Filter : Invert image to create a negative effect
def invert(frame): 
    # To invert the image's pixel values, we must subtract pixel value from 255. This is done using cv2.bitwise_not().
    negative_img = cv2.bitwise_not(frame)
    
    return negative_img


# Pencil Sketch : Pencil sketch of image
def pencilSketch(frame, k_size):   

    # Get the grayscale image of the original image
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Convert the one channelled grayscale image to a three channelled image
    gray_img = np.stack((gray_img,)*3, axis=-1)

    # Invert Image
    invert_img=cv2.bitwise_not(gray_img)

    # Blur image to smoothen, i.e., reduce some noise and amount of detail in final sketch image. Increasing kernel size k_size 
    # creates more thinner lines in the resulting sketch
    blurred_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invert_blurred_img=cv2.bitwise_not(blurred_img)

    # Sketch Image: dividing the image values by the inverted values of the smoothened image which accentuates the most prominent lines
    sketch_img=cv2.divide(gray_img,invert_blurred_img, scale=256.0)
    
    return sketch_img


# Color Extraction : Display all pixels within specific color range and make rest of the image black.
def colorExtract(frame, l, u):
    # Convert image to HSV(Hue, Saturation, Value) colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Save the user-specified lower and upper color bounds as numpy arrays. These will form the hue range for the color to be extracted.
    lower = np.array([l[0], l[1], l[2]])
    upper = np.array([u[0], u[1], u[2]])

    # Create a mask of image for given color range using inRange function, which takes all pixels that fall in the range of (lower, upper)
    mask = cv2.inRange(hsv, lower, upper)

    # Combine the mask and image and blacken all pixels not in color range. This is done by performing cv2.bitwise_and() on the original
    # image using the mask. This keeps the original colors where the mask value isn't 0, and black where the mask value is 0.
    extract_img = cv2.bitwise_and(frame, frame, mask=mask)
    
    return extract_img


# Color Focusing : Display all pixels within specific color range and make rest of the image grayscale.
def colorFocus(frame, l, u):
    # Convert image to HSV(Hue, Saturation, Value) colorspace
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the grayscale image of the original image
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Save the user-specified lower and upper color bounds as numpy arrays. These will form the hue range for the color to be focused.
    lower = np.array([l[0], l[1], l[2]])
    upper = np.array([u[0], u[1], u[2]])

    # Create a mask of image for given color range using inRange function, which takes all pixels that fall in the range of (lower, upper)
    mask = cv2.inRange(hsv,lower, upper)

    #Create inverted mask using bitwise_not(). This is to get all the pixels in the image which does not fall in the required range. This
    # mask is used to filter out the background pixels from the grayscale image
    invert_mask = cv2.bitwise_not(mask)

    #Filter only the specific colour from the original image using the mask(foreground)
    foreground = cv2.bitwise_and(frame, frame, mask=mask)

    #Filter the regions containing colours other than red from the grayscale image(background)
    background = cv2.bitwise_and(gray_img, gray_img, mask = invert_mask)

    #Convert the one channelled grayscale background to a three channelled image
    background = np.stack((background,)*3, axis=-1)

    #Add the foreground and the background
    focus_img = cv2.add(foreground, background)
    
    return focus_img


# Duo-tone
def duotone(img, exp, c, l_d):
    # Convert exponential factor to range between 1 to 2
    exp = 1 + exp/100

    # Convert the tone parameters to their appropriate channel numbers. Blue for channel 0, green for channel 1, and so on.
    colors={'blue':0,'green':1,'red':2,'none':3}
    for i in range(len(c)):
        c[i]=colors[c[i]]

    # Iterate through each channel value and if the user selected the specific channel, increase the pixel values in the channel
    # using the exponential function.
    for i in range(3):
        # If the user selected this channel, increase the values of the pixels exponentially for that channel. This highlights the specific color. 
        # If the values are too high, they perform clipping to ensure the values do not go above 255.
        if i in c: 
            table = np.array([min((i**exp), 255) for i in np.arange(0, 256)]).astype("uint8")
            img[:, :, i] =cv2.LUT(img[:, :, i], table) 

        #If the user has not selected this channel, this channel is not part of the 2 tones and so we must lighten the color's appearance or darken it to black.
        else:
            if l_d=='light': 
                # For light option, make these unselected channels lighter by using an exponential value in the range of 0 to 1 with the exponential function. 
                table = np.array([min((i**(2-exp)), 255) for i in np.arange(0, 256)]).astype("uint8")
                img[:, :, i] =cv2.LUT(img[:, :, i], table)
                
            else: 
                # For dark option, the unselected channel is darkened all the way down to 0(black).
                img[:, :, i] = 0
    return img


# Upon selecting filter to apply, user is given option to select parameter values. After clicking Submit, 
# check the type of file: image or video. If file is an image, read it and call the appropriate function for the filter and 
# provide user selected parameters as input. If file is video, use VideoCapture and apply filter on each frame, then write
# output into file using VideoWriter. 
def applyFilter(option, input_format, file):
    form = st.sidebar.form(key='my_form')
    #According to filter user selected, appropriate sliders for filter parameters are displayed.
    with form:
        if option =="Brightness":
            value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0, 150, 100)
        
        elif option == "Pencil Sketch":
            kernel = st.sidebar.slider('Select kernel size', 3, 101, 3, step =2)
        
        elif option =="Color Extract":
            l_r = st.sidebar.slider('Lower bound red', 0, 255, 50)
            l_g = st.sidebar.slider('Lower bound green', 0, 255, 50)
            l_b = st.sidebar.slider('Lower bound blue', 0, 255, 50)
            
            u_r = st.sidebar.slider('Upper bound red', 0, 255, 150)
            u_g = st.sidebar.slider('Upper bound green', 0, 255, 150)
            u_b = st.sidebar.slider('Upper bound blue', 0, 255, 150)
        
        elif option =="Color Focus":
            l_r = st.sidebar.slider('Lower bound red', 0, 255, 50)
            l_g = st.sidebar.slider('Lower bound green', 0, 255, 50)
            l_b = st.sidebar.slider('Lower bound blue', 0, 255, 50)
            
            u_r = st.sidebar.slider('Upper bound red', 0, 255, 150)
            u_g = st.sidebar.slider('Upper bound green', 0, 255, 150)
            u_b = st.sidebar.slider('Upper bound blue', 0, 255, 150)

        elif option=="Duo-tone":
            exp = st.sidebar.slider('Exponent factor',0,10,5)
            s1= st.sidebar.select_slider('Channel', ['blue', 'green', 'red'])
            s2= st.sidebar.select_slider('Channel', ['blue', 'green', 'red', 'none'])
            l_d = st.sidebar.select_slider('Light or Dark', ['light', 'dark'])

        submit = st.form_submit_button(label='Submit')
    
    # Images
    if submit:
        if input_format=="image":
            #Read file using imread. If user submitted parameters, call function for filter selected and save output in out.png
            img = cv2.imread("input.png")

            if submit:
                if option=="Brightness":
                    img=brightness(img,value)
                elif option=="Pencil Sketch":
                    img=pencilSketch(img,kernel)
                elif option=="Negative":
                    img=invert(img)
                elif option=="Color Extract":
                    img=colorExtract(img, [l_r, l_g, l_b], [u_r, u_g, u_b])
                elif option=="Color Focus":
                    img=colorFocus(img, [l_r, l_g, l_b], [u_r, u_g, u_b])
                elif option =="Duo-tone":
                    img=duotone(img,exp, [s1,s2], l_d)
                cv2.imwrite("out.png", img)
        
        # Videos
        else:
            # Create VideoCapture object for video file
            cap = cv2.VideoCapture(file.name)
            if (cap.isOpened() == False):
                print('Error while trying to open video. Plese check again...')
            
            # Get the frame width and height
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            
            # Define codec and create VideoWriter object for saving output
            out = cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width, frame_height))

            #Start reading video file
            while(cap.isOpened()):
                # Capture each frame of the video and apply selected filter on the frame
                ret, frame = cap.read()
                if ret == True:
                    if option=="Brightness":
                        frame=brightness(frame,value)
                    elif option=="Pencil Sketch":
                        frame=pencilSketch(frame,kernel)
                    elif option=="Negative":
                        frame=invert(frame)
                    elif option=="Color Extract":
                        frame=colorExtract(frame, [l_r, l_g, l_b], [u_r, u_g, u_b])
                    elif option=="Color Focus":
                        frame=colorFocus(frame, [l_r, l_g, l_b], [u_r, u_g, u_b])
                    elif option=="Duo-tone":
                        frame=duotone(frame, exp, [s1,s2], l_d)
                    
                    # Save altered video frame into output file
                    out.write(frame)

                    if cv2.waitKey(27) & 0xFF == ord('q'):
                        break
                
                # If no frame is found, exit 
                else:
                    break
            
            # Release VideoCapture()
            cap.release()


st.set_page_config(layout='wide')
# Opening of Streamlit page
st.write("""
          # Filter-It!
          """
          )

st.write("An app to apply filters on your videos or images!")

# Option for user to upload image or video file
file = st.sidebar.file_uploader("Please upload an image or video file", type=["jpg", "png", "jpeg","mp4"])
path = os.path.dirname(__file__)
# my_file = path+str(file.name)
col1, col2= st.columns(2)

if file is None:
    st.text("You haven't uploaded a file")
else:
    
    #User selects filter to apply
    option = st.sidebar.selectbox(
        'Which filter would you like to apply to your image?',
        ('Brightness','Pencil Sketch','Negative', 'Color Extract', 'Color Focus', 'Duo-tone'))
    
    # If file is an image, open and display the image, call applyFilter on it, and display output image.
    if file.name.split(".")[1]!="mp4":
        image = Image.open(file)
        img = np.array(image)
        cv2.imwrite("input.png",cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))
        with col1:
            st.text("Your original image")
            st.image(image, use_column_width=True)
        
        if os.path.isfile("out.png"):
            os.remove("out.png")
        applyFilter(option, 'image', file)
        if os.path.isfile("out.png"):
            with col2:
                st.text("Your final image")
                img = Image.open('out.png')
                st.image(img, use_column_width=True)
    
    # If file is a video, open and display the video, call applyFilter on it, convert output .avi file to .mp4 file and display it.
    elif file.name.split(".")[1]=='mp4':
        if os.path.isfile(file.name)==False:
            with open(file.name,"wb") as f:
                f.write(file.getbuffer())
        with col1:
            video = open(file.name, "rb") 
            st.text("Your original video")
            st.video(video)
        if os.path.isfile("out.avi"):
            os.remove("out.avi")
        applyFilter(option, 'video', file)
        os.popen("ffmpeg -analyzeduration 2147483647 -probesize 2147483647 -y -i out.avi -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 out.mp4".format(input = 'out', output = 'out')).read()
        if os.path.isfile("out.mp4") and os.path.isfile("out.avi"):
            with col2:
                st.text("Your edited video")
                out = open("out.mp4", "rb")
                st.video(out) 
