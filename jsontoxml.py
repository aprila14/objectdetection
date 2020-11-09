import json
import xml.etree.ElementTree as ET

#define the training image size
imgwidth = 535
imgheight = 414
numberofimages = 0

#open the json file with the data
with open('C:/Users/u380564/OneDrive/Dokumente/objectDetection/Code/objectdetection/tensorflow1/models/research/object_detection/images/train/captures_000.json') as f:
  data = json.load(f)

#iterate through all the images
for i in data["captures"]:
    numberofimages = numberofimages + 1
    filenamename = i["filename"]
    
    #define the the path in which the training images are
    pathname = "C:/Users/u380564/OneDrive/Dokumente/objectDetection/Artificial Dataset/ea391af9-d56c-458b-bc5e-8ac55cbb47e6"
    pathname = pathname+filenamename
    numberofobjects = len(i['annotations'][0]["values"])
    
    # create the file structure
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation, 'folder')
    folder.text='train'
    filename = ET.SubElement(annotation,'filename')
    filename.text=filenamename
    path = ET.SubElement(annotation, 'path')
    path.text = pathname
    source = ET.SubElement(annotation, 'source')
    source.text = 'source'
    database = ET.SubElement(source, 'database')
    database.text = 'Unknown'
    
    #iterate through all the object in 1 image
    for n in range(numberofobjects):
        ##print((i['annotations'][0]))
        widthvalue = i['annotations'][0]['values'][n]['width']
        heightvalue = i['annotations'][0]['values'][n]['height']

        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        width.text = str(imgwidth)
        height = ET.SubElement(size, 'height')
        height.text = str(imgheight)
        depth = ET.SubElement(size, 'depth')
        depth.text = '3'
        segmented = ET.SubElement(annotation, 'segmented')
        segmented.text = '0'

        namename = i['annotations'][0]['values'][n]['label_name']
        Xmin = i['annotations'][0]['values'][n]['x']
        Ymin = i['annotations'][0]['values'][n]['y']
        Xmax = Xmin + widthvalue
        Ymax = Ymin + heightvalue


        object = ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name')
        name.text = namename
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncate = ET.SubElement(object, 'truncate')
        truncate.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = 'difficult'
        bndbox = ET.SubElement(object, 'bndbox')
        bndbox.text = 'bndbox'
        xmin = ET.SubElement(bndbox, 'xmin')
        xmin.text = str(Xmin)
        ymin = ET.SubElement(bndbox, 'ymin')
        ymin.text = str(Ymin)
        xmax = ET.SubElement(bndbox, 'xmax')
        xmax.text = str(Xmax)
        ymax = ET.SubElement(bndbox, 'ymax')
        ymax.text = str(Ymax)
        
        # create a new XML file with the results
        mydata = ET.tostring(annotation)
        
        #create output filename
        imgname = filenamename.split("/")
        imgnameending = imgname[1]
        outputfilename = imgnameending[:-3] + "xml"
        print(outputfilename)
        # Save file
        myfile = open(outputfilename, "wb")
        myfile.write(mydata)
        

        
    print("number of images is {}".format(numberofimages))

