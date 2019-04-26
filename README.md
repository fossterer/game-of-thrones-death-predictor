# Purpose
A logistic regression model that predicts whether a given character from the popular TV series "Game of Thrones" is likely to die.

# Design
Please see [Design documentation](docs/DESIGN.md)

# Tested on
Ubuntu 18.04 LTS(x64) system

# System Requirements
1. GNU Make tool
2. Python 2.7+
3. GNU Octave
4. fig2dev tool (optional, may show warnings if not installed)

# Development

# Build/Run Instructions
This project comes with a Makefile.

 - Just use

 		make run

to run all the steps in line.

Alternatively, 
 - Use

		make preprocess

to run just the *Data Pre-processing* step

 - Use

		make build-model

to only *build the model* for prediction, provided the training dataset is available (from the preprocessing step)

# Production
**Note:** This may not be production ready. Please see 'Issues' in the Github UI

# Build/Run Instructions
This project comes with a Makefile.

 - Just use

 		make run

to run all the steps in line.

Alternatively, 
 - Use

		make preprocess

to run just the *Data Pre-processing* step

 - Use

		make build-model

to only *build the model* for prediction, provided the training dataset is available (from the preprocessing step)