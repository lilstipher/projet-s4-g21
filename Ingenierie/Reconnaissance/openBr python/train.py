from brpy import init_brpy
#this is the script use for transform a image gallery into gallery of vector

train_dir = 'pictures'
br = init_brpy()
br.br_initialize_default()

br.br_set_property('algorithm', 'FaceRecognition')
br.br_set_property('enrollAll', 'true')
#we save the transforme gallery here
br.br_enroll(train_dir, 'train_gallery.gal')
