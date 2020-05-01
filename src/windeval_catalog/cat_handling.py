import intake
import os
from pathlib import Path


def get_windeval_catalog_paths(rel_path=None):
    """Wrap data dir discovery."""
    # FIXME: Instead of __file__, find a better way to retrieve the package dir
    potential_path = Path(__file__).parent / rel_path
    if potential_path.exists():
        return potential_path
    else:
        raise ValueError(f"{potential_path} does not exist.")


def set_env_vars():
    """Ensure env vars point to data dir.

    Background: The test data catalog uses `{{env({"WINDEVAL_DATA_DIR"})}}/...` to point to data files. 
    """
    os.environ["WINDEVAL_DATA_DIR"] = str(
        get_windeval_catalog_paths("windeval_data_dir")
    )


def get_catalog():
    """Return Intake catalog with test data."""
    catalog_path = get_windeval_catalog_paths(
        "windeval_catalogs/windeval_test_data.yaml"
    )
    return intake.open_catalog(catalog_path.as_posix())
