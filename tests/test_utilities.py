import os

from ptl_bolts import PACKAGE_ROOT


def test_paths():
    assert os.path.isdir(PACKAGE_ROOT)
