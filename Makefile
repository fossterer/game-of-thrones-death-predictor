MAKEFLAGS += --silent

run:	preprocess build-model

preprocess:
	echo "\nPerforming Data Preprocessing step"; \
	cd data-preprocessing; \
	python preprocessor.py; \
	echo "Finished successfully..!"
	cd ..; \
		echo "Output written into data-preprocessing/output/"

build-model:
	echo "\nPerforming Model building step"; \
	cd model-building; \
	octave model.m \
	echo "Finished successfully..!"
	cd ..; \
		echo "Scatter plot of training data is saved into model-building/output/"
