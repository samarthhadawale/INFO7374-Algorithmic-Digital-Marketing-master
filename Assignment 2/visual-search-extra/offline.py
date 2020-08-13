from PIL import Image
from get_image_feature_vectors import get_image_feature_vectors
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    fe = get_image_feature_vectors()

    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        print(img_path) 
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
        np.save(feature_path, feature)
