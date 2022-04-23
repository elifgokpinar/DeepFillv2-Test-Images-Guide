#Masked images are in the masked_images folder
#Masks are in the masks folder
#Output of the inpainting results are in the outputs folder

#Format 
#python test.py --image MASKED_IMAGE_PATH --masks MASK_IMAGE_PATH --output INPAINTING_RESULT_PATH --checkpoint_dir PRETRAINED_MODEL_PATH


#If you are going to run on windows you can generate the file .cmd format
for count in range(1,6):
    f = open("test_command.cmd", "a")
    f.write("python test.py --image masked_images/"+str(count)+".png --mask masks/"+str(count)+".png --output outputs/masked_image_"+str(count)+".png --checkpoint_dir logs/full_model_celeba_hq_256\n")
    f.close()
#In order to run test_command.cmd on windows, you can write in cmd => test_command.cmd

    
#If you are going to run on ubuntu you can generate the file .sh format. 
#for count in range(1,6):
    #f = open("test_command.sh", "a")
    #f.write("python test.py --image masked_images/"+str(count)+".png --mask masks/"+str(count)+".png --output outputs/masked_image_"+str(count)+".png --checkpoint_dir logs/full_model_celeba_hq_256")
    #f.write(" \ \n")
    #f.close()
#In order to run test_command.sh on ubuntu, you can write in terminal  => sh test_command.sh
