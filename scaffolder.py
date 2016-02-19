#!/usr/bin/env python3

from yaml import load as yaml_load
import xml_generator


def parse_yaml(filepath):
    with open(filepath, "r") as stream:
        stream = yaml_load(stream)
        return stream


def yaml_parents(output):
    for parent in output:
        yield output[parent]


def yaml_children(parent):
    for child in iter(parent):
        yield child


def generate_xml(file_path, yaml_output):
    with open(file_path, "w") as new_file:
        new_file.write(xml_generator.xml_header)
        for tag in xml_generator.map_tags(yaml_children(yaml_parents(yaml_output))):
            new_file.write(tag + "\n")


def main(file_path):
    yaml_output = parse_yaml(file_path)

    generate_xml("/Users/oday/Desktop/newfile.xml", yaml_output)


if __name__ == '__main__':
    main("/Users/oday/Desktop/stream.yaml")