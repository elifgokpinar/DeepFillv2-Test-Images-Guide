import cv2
import numpy as np

for count in range(1,6):

    mask_path = 'masks/' +str(count) +'.png'
    image_path = 'original_images/' +str(count) +'.jpg'
    print("Mask Path : "+mask_path)
    print("Image Path : " + image_path)

    original_image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    #--- Resizing the mask to the shape of original image ---
    resizedMask = cv2.resize(mask , (original_image.shape[1], original_image.shape[0]))

    #--- Apply Otsu threshold---
    ret, image_mask = cv2.threshold(resizedMask[:,:,0], 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

    #Show the resized mask
    #cv2.imshow('image_mask', image_mask)

    #Save the mask image
    #cv2.imwrite('masks_resized/mask_'+str(count)+'.png', image_mask)

    original_image_copy = original_image.copy()

    #--- Copy pixel values 
    original_image_copy[np.where(image_mask == 255)] = resizedMask[np.where(image_mask == 255)]

    #Show the masked image
    #cv2.imshow('result', original_image_copy)

    #Save the masked image
    cv2.imwrite('masked_images/masked_image_'+str(count)+'.png', original_image_copy)
    print("Masked image is generated succesfully.\n" + image_path)
    cv2.waitKey()
    cv2.destroyAllWindows()

