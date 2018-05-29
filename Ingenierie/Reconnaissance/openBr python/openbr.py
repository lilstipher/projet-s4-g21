from brpy import init_brpy
from PIL import Image
from os import listdir,walk,path
from os.path import isfile, join
imageFiles=[]
mypath="./pictures/"
for path, subdirs, files in walk(mypath):
    for name in files:
        f= join(path, name)
        if isfile(f) and (f.endswith("G") or f.endswith("g")):
            #print(f)
            imageFiles.append(f)

#subdirectories=[x for x in walk(mypath)]
#imageFiles = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
#print(subdirectories[0]) 
# br_loc is /usr/local/lib by default,
# you may change this by passing a different path to the shared objects
print(imageFiles)
br = init_brpy()
br.br_initialize_default()
br.br_set_property('algorithm', 'FaceRecognition') # also made up
br.br_set_property('enrollAll','true')
mycatsimg = open('messi3.jpg', 'rb').read() # cat picture not provided =^..^=
mycatstmpl = br.br_load_img(mycatsimg, len(mycatsimg))
query = br.br_enroll_template(mycatstmpl)
nqueries = br.br_num_templates(query)
print(query)
scores = []
for imurl in imageFiles:
    # load and enroll image from path
    img = open(imurl, 'rb').read()
    tmpl = br.br_load_img(img, len(img))
    targets = br.br_enroll_template(tmpl)
    ntargets = br.br_num_templates(targets)# compare and collect scores
    scoresmat = br.br_compare_template_lists(targets, query)
    for r in range(ntargets):
        for c in range(nqueries):
            scores.append((imurl, abs(br.br_get_matrix_output_at(scoresmat, r, c))))
                # clean up - no memory leaks
    br.br_free_template(tmpl)
    br.br_free_template_list(targets)
print(scores)
scores.sort(key=lambda s: s[1])
for s in scores[:10]:
    print(s[0], s[1])
a=max([f[1] for f in scores])
print(a)
for s in scores:
    if abs(s[1])>=a:
        person=s[0].split("/")
        print("I think it's :",person[2]) 
#print(min(scores[1]))


# clean up - no memory leaks
br.br_free_template(mycatstmpl)
br.br_free_template_list(query)
br.br_finalize()
