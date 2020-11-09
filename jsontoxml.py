import json
import xml.etree.ElementTree as ET

#define the training image size
imgwidth = 535
imgheight = 414
numberofimages = 0

for i in range(33):
    i = str(i)
    print(len(i))
    if len(i) == 1:
        i = str(0) + i
    
    jsonname = 'C:/Users/Kevin/Documents/objectDetection/Artificial Dataset/ea391af9-d56c-458b-bc5e-8ac55cbb47e6/RGB6230a11d-6b66-4c43-8a18-b200653e6f33/' + 'captures_0' + str(i) + '.json'
    print(i)
    print(jsonname)
    
    #open the json file with the data
    with open(jsonname) as f:
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
        
        #iterate through all the object in 1 image
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
            
            #create output filename
            imgname = filenamename.split("/")
            imgnameending = imgname[1]
            outputfilename = imgnameending[:-3] + "xml"
            print(outputfilename)
            # Save file
            myfile = open(outputfilename, "wb")
            myfile.write(mydata)
            

            
        print("number of images is {}".format(numberofimages))

