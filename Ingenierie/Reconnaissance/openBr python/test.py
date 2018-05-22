from brpy import init_brpy
samples_dir = 'test'
pictures_dir = 'pictures'

br = init_brpy()
br.br_initialize_default()

br.br_set_property('algorithm', 'FaceRecognition')
br.br_set_property('enrollAll', 'true')

br.br_enroll(samples_dir, 'gallery.gal')
br.br_enroll(pictures_dir, 'pictures.gal')
#scoresmat = br.br_compare_template_lists(samples_dir, pictures_dir)
br.br_compare('gallery.gal', 'pictures.gal', 'scores.csv')
br.br_make_mask(samples_dir, pictures_dir, 'result.mask')

#br.br_eval(scoresmat, result_mask, 'results.csv')
