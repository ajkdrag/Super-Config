import os

from superconfig.superconf import SuperConfig

os.environ.setdefault("STORAGE_EMULATOR_HOST", "http://localhost:4443")

path = "gs://sample-bucket/some_file.yaml"


SuperConfig.setup(path_default="configs/default.ini", path_custom=path)

print(SuperConfig.get("spec.containers"))
