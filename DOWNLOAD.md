Dataset **DeepGlobe Land Cover 2018** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEyOTJfRGVlcEdsb2JlIExhbmQgQ292ZXIgMjAxOC9kZWVwZ2xvYmUtbGFuZC1jb3Zlci0yMDE4LURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIm1MZEZINjNaaW9pd24veHJmMWFISjRtb1FXT3loR1JXZ1NaK3M2cWR2ZmM9In0=)

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