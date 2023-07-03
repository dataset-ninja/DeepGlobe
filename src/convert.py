import os
from urllib.parse import unquote, urlparse

import numpy as np
import pandas as pd
import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name, get_file_name_with_ext
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    cls_names = [
        "urban_land",
        "agriculture_land",
        "rangeland",
        "forest_land",
        "water",
        "barren_land",
        "unknown",
    ]
    objclasses = [sly.ObjClass(clsname, sly.Bitmap) for clsname in cls_names]
    cls_to_objclasses = {cls_name: obj_cls for cls_name, obj_cls in zip(cls_names, objclasses)}

    img_ext = "_sat.jpg"
    ann_ext = "_mask.png"
    dataset_path = "./APP_DATA"
    ds_names = [
        "valid",
        "test",
        "train",
    ]

    def create_ann(image_path: str):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_width = image_np.shape[1]

        tmp_path = image_path.split(img_ext)[0]
        mask_path = os.path.join(os.path.dirname(tmp_path), os.path.basename(tmp_path) + ann_ext)

        if os.path.exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)
            for cls, rgb in s.CLASS2COLOR.items():
                obj_mask = np.all(mask_np == rgb, axis=2)

                if np.any(obj_mask):
                    curr_bitmap = sly.Bitmap(obj_mask)
                    curr_obj_class = cls_to_objclasses[cls]
                    if curr_bitmap.area > 100:
                        curr_label = sly.Label(curr_bitmap, curr_obj_class)
                        labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_width), labels=labels)

    meta = sly.ProjectMeta(
        obj_classes=objclasses,
    )

    df = pd.read_csv(f"{dataset_path}/metadata.csv")
    df["sat_image_path"] = df["sat_image_path"].apply(lambda x: os.path.join(dataset_path, x))
    all_images_path = df["sat_image_path"].values.tolist()

    project = api.project.create(workspace_id, project_name)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ds_names:
        dataset = api.dataset.create(project.id, ds_name)

        ds_img_paths = [
            path for path in all_images_path if os.path.basename(os.path.dirname(path)) == ds_name
        ]

        pbar = tqdm(desc=f"Processing '{ds_name}' dataset", total=len(ds_img_paths))
        for batch in sly.batched(ds_img_paths, batch_size=30):
            images_names = [os.path.basename(image_path) for image_path in batch]
            img_infos = api.image.upload_paths(dataset.id, images_names, batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns_batch = [create_ann(image_path) for image_path in batch]
            api.annotation.upload_anns(img_ids, anns_batch)

            pbar.update(len(batch))

    return project
