Dataset **DeepGlobe 2018** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/K/yW/sxF7knXsw9GubnMuXn2w8IHrjruG4S54KtWYvGWouYZq4Pwa0L5ltVhH5p4ej6owzD8Y26IxE7XKc3xrveLrM0MzfnBSUmVh85PtygvyTvBF258YKQ4eZk84niog.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DeepGlobe 2018', dst_path='~/dtools/datasets/DeepGlobe 2018.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset/download?datasetVersionNumber=2)