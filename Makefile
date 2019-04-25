MAKEFLAGS += --silent

run:	preprocess build-model

preprocess:
	echo "Performing Data Preprocessing step"; \
	cd data-preprocessing; \
	python preprocessor.py; \
	echo "Finished successfully..!"
	cd ..; \
		echo "Output written into data-preprocessing/output/"

build-model:
	echo "Performing Data Preprocessing step"; \
	cd data-preprocessing; \
	python preprocessor.py; \
	echo "Finished successfully..!"
	cd ..; \
		echo "Output written into data-preprocessing/output/"