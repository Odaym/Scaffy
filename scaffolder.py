#!/usr/bin/env python3

from yaml import safe_load as yaml_safe_load
from lxml import etree as ET
import xml_generator
import stack


def parse_yaml(file_path):
    with open(file_path, "r") as stream:
        stream = yaml_safe_load(stream)
        return stream


def traverse(output, file, root_element, last_element):
    if isinstance(output, list):
        for item in output:
            traverse(item, file, root_element, last_element)
    elif isinstance(output, dict):
        for key, value in output.items():
            if isinstance(value, dict):
                # element with attrs
                sub_element = ET.SubElement(last_element, key)
                for attr_name, attr_value in value.items():
                    sub_element.set(attr_name, attr_value)
            elif isinstance(value, list):
                # layout element
                last_element = ET.Element(key)
                root_element.append(last_element)

            traverse(output[key], file, root_element, last_element)

    elif isinstance(output, str) and output in xml_generator.tagNames:
        ET.SubElement(last_element, output)

    return root_element


def main(source, target):
    with open(target, "w") as target_file:
        target_file.write(xml_generator.xml_header)

        yaml_output = parse_yaml(source)

        yaml_activity = yaml_output.get('activity')

        root_element = ET.Element(next(iter(yaml_activity)))

        print(yaml_activity)
        element_stack = stack.Stack()

        tree = ET.ElementTree(traverse(yaml_activity, target_file, root_element, None))
        tree.write("trial.xml", pretty_print=True)


if __name__ == '__main__':
    main("stream.yaml", "newfile.xml")
