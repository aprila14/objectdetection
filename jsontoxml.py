import json
import xml.etree.ElementTree as ET


imgwidth = 535
imgheight = 414


with open('C:/Users/u380564/OneDrive/Dokumente/objectDetection/Code/objectdetection/tensorflow1/models/research/object_detection/images/train/captures_000.json') as f:
  data = json.load(f)
numberofimages = 0
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

for i in data["captures"]: ##iterate through all the images
    
    numberofimages = numberofimages + 1
    filenamename = i["filename"]
    pathname = "C:/Users/u380564/OneDrive/Dokumente/objectDetection/Artificial Dataset/ea391af9-d56c-458b-bc5e-8ac55cbb47e6"
    pathname = pathname+filenamename
    
    numberofobjects = len(i['annotations'][0]["values"])
    
    # create the file structure
    annotation = ET.Element('annotation')
    
    folder = ET.SubElement(annotation, 'folder')
    folder.set('name','train')
    folder.text=''
    filename = ET.SubElement(annotation,'filename')
    filename.set('name',filenamename)
    filename.text=""
    path = ET.SubElement(annotation, 'path')
    path.set('name',pathname)
    source = ET.SubElement(annotation, 'source')
    source.set('name','source')
    database = ET.SubElement(source, 'database')
    database.set('name','Unknown')
    

    for n in range(numberofobjects):
        ##print((i['annotations'][0]))
        widthvalue = i['annotations'][0]['values'][n]['width']
        heightvalue = i['annotations'][0]['values'][n]['height']

        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        width.set('name', str(imgwidth))
        height = ET.SubElement(size, 'height')
        height.set('name', str(imgheight))
        depth = ET.SubElement(size, 'depth')
        depth.set('name','3')
        segmented = ET.SubElement(annotation, 'segmented')
        segmented.set("name", '0')

        namename = i['annotations'][0]['values'][n]['label_name']
        Xmin = i['annotations'][0]['values'][n]['x']
        Ymin = i['annotations'][0]['values'][n]['y']
        Xmax = Xmin + widthvalue
        Ymax = Ymin + heightvalue


        object = ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name')
        name.set('name',namename)
        pose = ET.SubElement(object, 'pose')
        pose.set('name','Unspecified')
        truncate = ET.SubElement(object, 'truncate')
        truncate.set("name",'0')
        difficult = ET.SubElement(object, 'difficult')
        difficult.set('name','difficult')
        bndbox = ET.SubElement(object, 'bndbox')
        bndbox.set('name',"bndbox")
        xmin = ET.SubElement(bndbox, 'xmin')
        xmin.set('name',str(Xmin))
        ymin = ET.SubElement(bndbox, 'ymin')
        ymin.set('name',str(Ymin))
        xmax = ET.SubElement(bndbox, 'xmax')
        xmax.set('name',str(Xmax))
        ymax = ET.SubElement(bndbox, 'ymax')
        ymax.set('name',str(Ymax))
        
        # create a new XML file with the results
        mydata = ET.tostring(annotation)
        # Save file
        myfile = open("caputures_000.xml", "wb")
        myfile.write(mydata)
        

        
    print("number of images is {}".format(numberofimages))

