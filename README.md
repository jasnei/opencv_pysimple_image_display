# opencv_pysimple_image_display
here is the works using pysimgple gui create a widows &amp; display image, using opencv to process image

Demo program that displays image using OpenCV and applies some very basic image functions

-- functions from top to bottom -

Gray:       change image color to Gray

HSV:        change image color to HSV

LUV:        change image color to LUV

LAB:        change image color to LAB

YUV:        change image color to YUV

Cal_EQ:     Image equalizeHist

threshold:  simple b/w-threshold on the luma channel, slider sets the threshold value

canny:      edge finding with canny, sliders set the two threshold values for the function => edge sensitivity

contour:    contour finding in the frame, slider sets the value of threshold for b/w using threshold to find

            Found objects are drawn with a red contour.
            
blur:       simple Gaussian blur, slider sets the sigma, i.e. the amount of blur smear


