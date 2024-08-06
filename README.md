In order for Utah to continue to improve its consciousness regarding climate, droughts, and agriculture, it is critical for younger generations to be exposed to the effects of these developing problems and gain awareness. 

Using a Raspberry Pi, along with PlantCV and other image analysis software, lettuce, chinchilla dust bath, and diatomaceous earth, the large-scale effects of dust on agriculture can be simulated for children at public libraries all over the state of Utah. 

The FelsAnalysisInstructions.pdf contains simple instructions on how to use a Raspberry Pi for this project, as well as installing the proper libraries and software, using a virtual environment (venv and Anaconda) on the Pi, using the PiCamera, and how to set up the lettuce trays. 

The LettuceAnalysisCode.ipynb contains the PlantCV code as a Jupyter Notebook that will analyze the lettuce images taken by the Pi.

The LettuceImages folder contains the images of the lettuce taken between 06-25-2024 and 07-17-2024 which were used to test the analysis code.

The LettuceMasks folder contains the corresponding masks to the lettuce images. These masks are created by the first cell in the LettuceAnalysisCode, then used in the second for image segmentation based on the time series of previous masks and images.

The CSVResults folder contains the results of the LettuceAnalysisCode functions `pcv.analyze.color` and `pcv.analyze.size` functions as CSV files.

The Master.CSV file contains all the CSVResults files in one large CSV file. 

The GraphResults folder contains folders for every plant, with a corresponding area over time graph and a plot with a green frequencies curve for every date. These are the final results from the LettuceAnalysisCode!

The photocode.py file contains the code used on the Raspberry Pi to take pictures. It can ONLY be run on a Raspberry Pi. 



