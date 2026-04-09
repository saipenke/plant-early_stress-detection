!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="LGIjzq0DgTAcFqkre1WW")
project = rf.workspace("palm-oil-leaf-nutrient-detection").project("leaf-nutrient-detection")
version = project.version(678)
dataset = version.download("yolov8")
                