from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "DeepGlobe Land Cover 2018"
PROJECT_NAME_FULL: str = "DeepGlobe Land Cover Classification Dataset 2018 Challenge"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(
    url="http://deepglobe.org/docs/CVPR_InternalUseLicenseAgreement_07-11-18.pdf"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Research.UrbanPlanning(),
    Research.Environmental(),
    Industry.Agricultural(is_used=False),
]
CATEGORY: Category = Category.Aerial(
    extra=[
        Category.Satellite(),
        Category.Environmental(),
        Category.EnergyAndUtilities(),
        Category.Agriculture(),
    ]
)

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2018-06-28"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1459606
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/DeepGlobe"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset/download?datasetVersionNumber=2"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "urban_land": [0, 255, 255],
    "agriculture_land": [255, 255, 0],
    "rangeland": [255, 0, 255],
    "forest_land": [0, 255, 0],
    "water": [0, 0, 255],
    "barren_land": [255, 255, 255],
    "unknown": [0, 0, 0],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/1805.06561"
CITATION_URL: Optional[
    str
] = "https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset"
AUTHORS: Optional[List[str]] = [
    "Ilke Demir",
    "Krzysztof Koperski",
    "David Lindenbaum",
    "Guan Pang",
    "Jing Huang",
    "Saikat Basu",
    "Forest Hughes",
    "Devis Tuia",
    "Ramesh Raskar",
]
AUTHORS_CONTACTS: Optional[List[str]] = None

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "DeepGlobe Satellite Challenge (CVPR 2018)"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "http://deepglobe.org/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = ["train"]

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,        
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
