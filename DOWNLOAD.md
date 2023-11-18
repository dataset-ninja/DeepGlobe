Dataset **DeepGlobe Land Cover 2018** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/h/B3/K0z2Jjg32ViBij8X6WQ7sSYNADOy7aLZk1eQdK2HeYoX9SeI6kgpZglhe7ywO3mthLhcNPPPvGtbXiUc6voDTupMxCbwPqG227vO2kJaik2dWi13bBH5Sk78RsT2.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DeepGlobe Land Cover 2018', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset/download?datasetVersionNumber=2).