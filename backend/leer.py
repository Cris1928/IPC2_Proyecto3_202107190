import collections
from xml.etree import ElementTree as ET
import xmltodict
from collections import OrderedDict
from datetime import datetime

def leerXML(xml,encoding="utf-8"):
    doc = xmltodict.parse(xml,encoding="utf-8")

    file = open('BaseDatos.xml','w', encoding="utf-8")
    file.write(str(xml).replace('\n', '')) ##---> base de datos
    file.close()
