from PIL import Image
import glob, os, sys
from arcgis import GIS
from arcgis.features import FeatureLayerCollection
import Image
from PIL import Image

# Login to ArcGIS Online
user = "********"
gis = GIS("https://www.arcgis.com",user,"*********")


# Set path for temporarily saving images locally
path = "C:/Users/18602/Desktop"

# Access existing AGOL layer (replace w/ layer ID)
num = gis.content.get("5b90172d5b1b40199c5c5e5752f6318c")
fl = num.layers[0]
fs = fl.query(where="1=1")
oidFieldName = "OBJECTID"
oids = [f.attributes[oidFieldName] for f in fs.features]

# Loop through each feature/ObjectID to get all the associated attachments
for oid in oids:
    attachments = fl.attachments.get_list(oid=oid)
    print(attachments)
  
    # Check if the feature has attachments, will be a blank list if not
    if len(attachments)>0:
        print(oid)

        # Loop through each attachment associated with OID
        for i in range(len(attachments)):
            i_id = str(attachments[i]["id"])
            print(i_id)
            i_name = str(attachments[i]["name"])
            print(i_name)

            # The image_path is how the attachments.download (below) saves the image file
            image_path = path+"/"+str(oid)+"/"+i_id+"/"+i_name
            print(image_path)

            # Download the attachment to local path
            fl.attachments.download(save_path=path,oid=oid)

            # Access the downloaded attachment and reduce size by 3, save with new name
            im = Image.open(image_path)
            print(im)
            imrd = im.reduce(3)
            new_path= path+"/"+str(oid)+"/"+i_id+"/SMALL_"+i_name
            imrd.save(new_path)
            print("New Saved")

            # Replace existing attachment with reduced image size attachment
            fl.attachments.update(oid,i_id,new_path)
            print("UPDATED OBJECTID:"+str(oid))
