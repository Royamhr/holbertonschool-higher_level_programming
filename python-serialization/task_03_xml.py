import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Root elementi yarat
    root = ET.Element("data")

    # Dictionary-dən elementləri əlavə et
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # key adı ilə element
        child.text = str(value)           # dəyəri text olaraq saxla

    # XML tree-i fayla yaz
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    # XML faylını parse et
    tree = ET.parse(filename)
    root = tree.getroot()

    # XML elementlərini dictionary-yə çevir
    result = {}
    for child in root:
        result[child.tag] = child.text  # tag = key, text = value

    return result
