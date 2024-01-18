# BatchResizeImages README:

This script is used to retroactively reduce the size of images/attachments by a specific factor to control the space that the feature layer takes up in AGOL. Image/Attachment size can also be controlled at collection point by methods here: https://community.esri.com/t5/education-blog/configure-photo-size-for-data-collection/ba-p/1238938. 
Resources used to create this script:
* Pillow/Image reference: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail
* Loop through attachments AGOL community post: https://community.esri.com/t5/arcgis-api-for-python-questions/loop-to-all-items-of-a-feature-layer-using-arcpy/td-p/1136526
* API for Python manager reference: https://developers.arcgis.com/python/api-reference/arcgis.features.managers.html
