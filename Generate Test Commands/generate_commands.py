#Masked images are in the masked_images folder
#Masks are in the masks folder
#Output of the inpainting results are in the outputs folder

for count in range(1,6):
    f = open("test_command.cmd", "a")
    f.write("python test.py --image masked_images/"+str(count)+".png --mask masks/"+str(count)+".png --output outputs/output_"+str(count)+".png --checkpoint_dir logs/full_model_celeba_hq_256\n")
    f.close()
