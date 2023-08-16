import cv2

#getting the name of image
file_name=input("Enter the name of the image with extension \t")
#reading the image

src=cv2.imread(file_name,cv2.IMREAD_UNCHANGED)

#specify the size of the image


scale_percent=int(input("enter the size of image you want \t"))

new_width=int(src.shape[1]*scale_percent/100)
new_height=int(src.shape[0]*scale_percent/100)

output=cv2.resize(src,(new_width,new_height))
save_as=input("Enter the name along with extension you want to save the image \t")
cv2.imwrite(save_as,output)
cv2.waitKey(0)