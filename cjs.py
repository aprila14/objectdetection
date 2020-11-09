import json
import xml.etree.ElementTree as ET

with open('C:/Users/u380564/AppData/LocalLow/UnityTechnologies/SynthDet/cbc6522f-7ab0-4463-997c-7e175bc92614/Datasetdfe1ffc8-a103-4a6a-9dd1-54de932717ec/captures_000.json') as rawfile:
  data = json.load(rawfile)


##print(data['captures'][0])


for i in data['captures']:
    print("id:", i['id'])
    filenametxt = i['filename']
    print("filename:", i['filename'])
    imagepath = "C:/Users/u380564/AppData/LocalLow/UnityTechnologies/SynthDet/cbc6522f-7ab0-4463-997c-7e175bc92614/" + filenametxt
    #define imagename and filename
    imagename = filenametxt.split("/",1)[1]
    imagenameasfilename = imagename.split(".",1)[0]
    print(imagename)
    print(imagepath)
    for j in i['annotations']:
        for k in j['values']:
            print("annotation")
            print("label_id:", k['label_id'])
            print("label_name:", k['label_name'])
            print("x:", k['x'])
            print("y:", k['y'])
            print("width:", k['width'])
            print("height:", k['height'])
            xmin = k['x']
            xmax = k['x']+k['width']
            ymin = k['y']
            ymax = k['y']+k['height']
            print("xmin:", xmin)
            print("xmax:", xmax)
            print("ymin:", ymin)
            print("ymax:", ymax)
            print('\n')
            
            
            
            
            annotation = ET.Element("annotation")
            folder = ET.SubElement(annotation, "folder")
            folder.text = "/resized"
            filename = ET.SubElement(annotation,"filename")
            filename.text = imagename
            #path = path for the images
            path = ET.SubElement(annotation, "path")
            path.text = imagepath
            source = ET.SubElement(annotation, "source")
            database = ET.SubElement(source, "database")
            database.text = "Unknown"
            #size of the images
            size = ET.SubElement(annotation,"size")
            width = ET.SubElement(size, "width")
            width.text = "585"
            height = ET.SubElement(size, "height")
            height.text = "414"
            depth = ET.SubElement(size, "depth")
            depth.text = "3"
            segmented = ET.SubElement(annotation,"segmented")
            segmented.text = "0"
            object = ET.SubElement(annotation,"object")
            name = ET.SubElement(object,"name")
            name.text = k['label_name']
            pose = ET.SubElement(object,"pose")
            pose.text = "Unspecified"
            truncate = ET.SubElement(object,"truncate")
            truncate.text = "0"
            difficult = ET.SubElement(object,"difficult")
            difficult.text = "0"
            bndbox = ET.SubElement(object,"bndbox")
            xmin = ET.SubElement(bndbox,"xmin")
            xmin.text = str(k['x'])
            ymin = ET.SubElement(bndbox,"ymin")
            ymin.text = str(k['y'])
            xmax = ET.SubElement(bndbox,"xmax")
            xmax.text = str(k['x']+k['width'])
            ymax = ET.SubElement(bndbox,"ymax")
            ymax.text = str(k['y']+k['height'])


            tree = ET.ElementTree(annotation)
            filenameout = imagenameasfilename + ".xml"
            tree.write(filenameout) 




