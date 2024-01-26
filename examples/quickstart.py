import superconfig as sc
from superconfig.superconf import SuperConfig


def main():
    SuperConfig.setup(
        path_default="configs/default.ini", path_custom="configs/dev.yaml"
    )

    print(SuperConfig.get("LOCAL_PATHS.path"))
    print(SuperConfig.get("CLOUD_PATHS.path"))
    print(SuperConfig.get("ENVIRONMENT_NAME"))
    val = SuperConfig.get("ENVIRONMENT_ID", dtype=sc.INT)
    print(val, type(val))


if __name__ == "__main__":
    main()
