# Openface of project-21

This is a guide to help you use `Openface` at your own computer.
 

## Environment

The following instructions are for `Linux` and `OSX` only.

* We strongly recommend using the `Docker` container unless you are experienced with building Linux software from source.
* In OSX, you may have to change the hashbangs from `python2` to `python`.
* `OpenFace` has been tested in `Ubuntu` 14.04 and `OSX` 10.10 and may not work well on other distributions.


## Automated Docker Build

The quickest way to getting started is to use our pre-built automated Docker build, which is available from [bamos/openface](https://hub.docker.com/r/bamos/openface/). This does not require or use a locally checked out copy of OpenFace. To use on your images, share a directory between your host and the Docker container.

* Here `local_directory` is the directory which is outside of `Docker container`, where you should put your traing-images in. (for example: /User/training-images)
* And `remote_directory` is the directory which is inside `Docker container` who has the same contents as `local_directory`
	
		docker pull bamos/openface
		docker run -p 9000:9000 -p 8000:8000 -v /local_directory:/remote_directory -t -i bamos/openface /bin/bash
	

## Creating a Classification Model

### 1. Create raw image directory.
Prepare `30` pictures, they must be `2` different persons, the size of the picture does not matter, but it is better to include only faces, `15` pictures for each person, respectively placed in two different directories.

	$ ./local_directory/traing-images
	
	person-1
	├── image-1.jpg
	├── image-2.png
	...
	└── image-15.png

	person-2
	├── image-1.png
	├── image-2.jpg
	...
	└── image-15.png
	
### 2. Face detection

Start automatic detection

	/root/openface/util/align-dlib.py ./training-images align outerEyesAndNose ./aligned-images/ --size 96
	

The purpose of this step is to let the machine automatically trim these 30 photos into `96x96` png files for subsequent processing.

The result of the processing is placed in the `aligned-images` directory. There are two folders below it, that is, the names of the two people you put in, and these two folders include faces of the two persons.

### 3. Generate Representations

	/root/openface/batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/

It produces the classification model which is an SVM saved to disk as a Python pickle. This step will generate 2 csv files in the `generated-embeddings` directory. The `labels.csv` and `reps.csv`, `labels.csv` are relatively simple, it just shows which photo corresponds to which person, and `reps.csv` is a large number of matrix.

### 4. Create the Classification Mode

	/root/openface/demos/classifier.py train ./generated-embeddings
	
The training result will generate a `classifier.pkl` file in the `generated-embeddings` directory. This is what we ultimately want.
	
## Face recognition
Now you can start testing and copy a picture to `/local_directory` that is not in the dataset. This photo can include the background or the entire body, but it is better not to put a photo of several people, or the machine does not know which one you want to identify.

Assuming the photo file is `local_directory/1.jpg`
	
	/root/openface/demos/classifier.py infer ./generated-embeddings/classifier.pkl 1.jpg
	

If the person in the photo is one of the two people identified just now, the recognition accuracy will be more than `90%`. If not, it will be less than `80%`.


