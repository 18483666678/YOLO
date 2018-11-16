import xml.etree.ElementTree as ET
import os

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["raccoon"]


def convert_annotation(image_id, list_file):
    in_file = open('./dataset/raccoon/annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


images = os.listdir('./dataset/raccoon/images/')
list_file = open('train.txt', 'w')

for image in images:
    list_file.write(os.path.join('raccoon/images', image))
    convert_annotation(image.split('.')[0], list_file)
    list_file.write('\n')
list_file.close()

