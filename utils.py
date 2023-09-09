import os
import json
import torch
import torchvision
from pathlib import Path
import cv2
import itertools


def count_images(directory):
    counts = {}
    for root, dirs, files in os.walk(directory):
        count = sum(fname.endswith((".png", ".jpg", ".jpeg")) for fname in files)

        counts[root] = count
    return counts

def main_func(base_path):
    model = torch.jit.load("/Users/gwonsmpro/Desktop/SDK_semilabeling/yolox_model_cpu.jit")
    patterns = ["*.png", "*.jpg", "*.jpeg"]

    img_list = list(itertools.chain.from_iterable(Path(base_path).glob(pattern) for pattern in patterns))

    def output_to_labelme(img_path, output, img_height, img_width):
        class_mapping = {
        0: "ab",
        1: "bd",
        2: "hb",
        3: "hc",
        4: "sc",
        5: "sn",
        6: "ul",
        }

        def tensor_to_labelme(tensor, class_mapping):
            shapes = []
            for row in tensor:
                xmin, ymin, xmax, ymax, _, _, class_idx = row
                class_label = class_mapping.get(int(class_idx), "unknown")
                points = [[float(xmin), float(ymin)], [float(xmax), float(ymax)]]
                shape_data = {
                    "label": class_label,
                    "points": points,
                    "group_id": None,
                    "shape_type": "rectangle",
                    "flags": {}
                }
                shapes.append(shape_data)

            return shapes

        # tensor에서 shape 데이터 추출
        shapes = tensor_to_labelme(output, class_mapping)

        # 사용자가 제공할 imagePath, imageWidth, imageHeight
        image_path = img_path.name

        # 최종 labelme JSON 포맷
        labelme_json = {
            "version": "4.5.7",
            "flags": {},
            "shapes": shapes,
            "imagePath": image_path,
            "imageData": None,
            "imageWidth": img_width,
            "imageHeight": img_height
        }

        # JSON 파일로 저장 (옵션)
        with open(f"{img_path.with_suffix('.json')}", "w") as f:
            json.dump(labelme_json, f, indent=4)
            
    for img in img_list:
        tensor_img = torch.tensor(cv2.imread(str(img)))
        img_height, img_width = tensor_img.shape[:2]
        output = model(tensor_img)

        output_to_labelme(img, output, img_height, img_width)

    
