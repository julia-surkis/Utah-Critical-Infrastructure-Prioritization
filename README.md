# BatchResizeImages README:

This script is used to retroactively reduce the size of images/attachments by a specific factor to control the space that the feature layer takes up in AGOL. Image/Attachment size can also be controlled at collection point by methods here: https://community.esri.com/t5/education-blog/configure-photo-size-for-data-collection/ba-p/1238938. Currently, the script does not auto-delete the local image files, but that is something to add in the future.
<br><br>
## Resources used to create this script:
* Pillow/Image reference: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail
* Loop through attachments AGOL community post: https://community.esri.com/t5/arcgis-api-for-python-questions/loop-to-all-items-of-a-feature-layer-using-arcpy/td-p/1136526
* API for Python manager reference: https://developers.arcgis.com/python/api-reference/arcgis.features.managers.html


# Jurisdictional View Layer Creation/Update README:

This script is used to automatically create jurisdicitonal view layers that are geographically constrained based on an AGOL boundary view layer (in this case, a combined city/county view layer). This process pulls all the fields from the master feature layer to the view layers, as well as the symbology, pop-up info and form info which are saved to the master hosted feature layer JSON. This allows updates to be made solely to the master feature layer, and then this script can be run to update the rest of the ~350 view layers automatically.
<br><br>
## Resources used to create this script:
