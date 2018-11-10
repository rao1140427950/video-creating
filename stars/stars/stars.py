import cv2 as cv
import numpy as np

PATH = 'resource/'

#img = cv.imread(PATH+'IMG_0001.JPG')
#img = img[250:3626,:,:]
#img = cv.resize(img,(1920,1080),interpolation=cv.INTER_LINEAR)
#img = cv.resize(img,(960,540),interpolation=cv.INTER_LINEAR)

#print(np.shape(img))

#cv.imshow('image',img)
#cv.waitKey(8000)

fourcc = cv.VideoWriter_fourcc(*'XVID')
video = cv.VideoWriter('moving_stars.avi',fourcc,15,(1920,1080))

print('Creating video...')
for i in range(1,100):
    image_path = PATH+'IMG_00'
    if i<10:
        image_path += '0'+str(i)+'.JPG'
    else:
        image_path += str(i)+'.JPG'
    image = cv.imread(image_path)
    image = image[250:3626,:,:]
    video.write(cv.resize(image,(1920,1080),interpolation=cv.INTER_LINEAR))
    cv.imshow('moving_stars',cv.resize(image,(960,540),interpolation=cv.INTER_LINEAR))
    cv.waitKey(20)
    print('frame',i,'added')

video.release()
cv.destroyAllWindows()
print('VideoWriter released')