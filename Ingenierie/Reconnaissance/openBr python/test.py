from brpy import init_brpy
from PIL import Image
from os import listdir,walk,path
from os.path import isfile, join

people_to_recognize_dir = 'test'

br = init_brpy()
br.br_initialize_default()

br.br_set_property('algorithm', 'FaceRecognition')
br.br_set_property('enrollAll', 'true')
br.br_enroll(people_to_recognize_dir, 'people_to_recognize.gal')
#scoresmat = br.br_compare_template_lists(samples_dir, pictures_dir)
br.br_compare('train_gallery.gal', 'people_to_recognize.gal', 'scores.csv')

