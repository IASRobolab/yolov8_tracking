from setuptools import setup, find_packages

package_name = 'yolov8_tracking'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[],
    install_requires=[easydict, ultralytics==8.0.20],
    zip_safe=True,
    description='This package contains functions useful for ML algorithm use. It creates simple interface between some used AI algorithms.',
    license='GNU GENERAL PUBLIC LICENSE v3',
    entry_points={},
)
