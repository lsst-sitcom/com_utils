"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documenation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.com.utils


_g = globals()
_g.update(build_package_configs(
    project_name='com_utils',
    version=lsst.com.utils.version.__version__))
