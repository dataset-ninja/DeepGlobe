The authors introduce **DeepGlobe Land Cover Classification Dataset 2018 Challenge**, a comprehensive collection of high-resolution sub-meter satellite imagery focusing on rural areas. This dataset includes 1,146 satellite images of size 2,448x2,448 pixels, split into *train*, *valid*, and *test* sets. The images encompass RGB data with a pixel resolution of 50 cm, sourced from the DigitalGlobe Vivid+ dataset. Pixel-wise segmentation masks were created by professional annotators to represent different land cover classes. The total area size of the dataset is equivalent to 1716.9 km²

It is noted that satellite imagery, a source of rich and structured information, has been less explored in computer vision research compared to everyday images. However, the authors emphasize the potential impact of connecting computer vision with remote sensing data analysis, particularly in areas like global urban planning and climate change research. With this objective in mind, the DeepGlobe initiative is introduced to foster collaboration between researchers from diverse domains and raise awareness of remote sensing within the computer vision community. The goal is to enhance and assess state-of-the-art approaches for understanding satellite images, which could serve as benchmark references for future research in the field.

Highlighting the distinct characteristics of satellite imagery, the authors stress its potential for applications such as map composition, population analysis, precision agriculture, and autonomous driving. The DeepGlobe project defines three tracks to address specific challenges:

1. **Road Extraction Challenge** [(available on DatasetNinja)](https://datasetninja.com/deepglobe-road-extraction): This challenge focuses on automating the extraction of road and street networks from satellite images, particularly in disaster zones and developing countries. The aim is to facilitate automated crisis response and expand map coverage for improved connectivity.
2. **Building Detection Challenge**: With a focus on modelling urban demographics for disaster response and recovery, this challenge involves the automatic detection of buildings from satellite images. This facilitates the remote gathering of urban information and spatial distribution details of urban settlements.
3. **Land Cover Classification Challenge** (current): This challenge revolves around the automatic classification and segmentation of land cover types from satellite images. It is crucial for sustainable development, agriculture, forestry, and urban planning.

Here is the description of the classes:

* *urban_land*: man-made, built up areas with human artifacts (can ignore roads for now which is hard to label).
* *agriculture_land*: farms, any planned (i.e. regular) plantation, cropland, orchards, vineyards, nurseries, and ornamental horticultural areas; confined feeding operations.
* *rangeland*: any non-forest, non-farm, green land, grass.
* *forest_land*: any land with x% tree crown density plus clearcuts.
* *water*: rivers, oceans, lakes, wetland, ponds.
* *barren_land*: mountain, land, rock, dessert, beach, no vegetation.
* *unknown*: clouds and others.

The authors emphasize that the dataset offers significant challenges due to its diversity of land cover types and dense annotations. While they acknowledge that small human errors are inevitable in this exploratory task of pixel-wise classification, the dataset provides a substantial resource for advancing high-resolution satellite image understanding.
