Dataset **DeepGlobe Land Cover 2018** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/M/l/NC/7EhgcxQ5mZZFwBEljZPgardMZSTdxmATd9NxGldXw2wQC9p930gdH4PEjzOxkXzDrtz6Zk5xq0RHLXuOfxmhg2ddF6R5XGxaNc9TpBHzKg79Z51Gc89WazSDwn4B.tar)

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