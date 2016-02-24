#!/usr/bin/env python3

from yaml import load as yaml_load
from lxml import etree as ET

NSMAP = {"android": "http://schemas.android.com/apk/res/android"}
tagDimensions = {"layout_width": "wrap_content",
                 "layout_height": "wrap_content"}


def parse_yaml(file_path):
    with open(file_path, "r") as stream:
        stream = yaml_load(stream)
        return stream


def traverse(node, parent_element):
    try:
        name = list(node.keys())[0]
        sub_element = ET.SubElement(parent_element, name)
    except AttributeError:
        ET.SubElement(parent_element, node)
    else:
        for child in node.get(name, []):
            if 'attrs' in child:
                config = child['attrs']

                for key, value in config.items():
                    sub_element.attrib[ET.QName(NSMAP['android'], key)] = value
            else:
                traverse(child, sub_element)
    return parent_element


def main(source, target):
    with open(target, "w") as target_file:

        yaml_output = parse_yaml(source)

        yaml_activity = yaml_output.get('activity')

        top_element = ET.Element(next(iter(yaml_activity)), nsmap=NSMAP)

        tree = ET.ElementTree(traverse(yaml_activity, top_element))

        for i, tag in enumerate(tree.getiterator()):
            if i == 1:
                tree._setroot(tag)
            for key, value in tagDimensions.items():
                tag.attrib[ET.QName(NSMAP['android'], key)] = value

        tree.write(target_file.name, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    main("/Users/oday/Code/stream.yaml", "trial.xml")
