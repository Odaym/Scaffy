#!/usr/bin/env python3

from yaml import load as yaml_load
import xml_generator


def parse_yaml(file_path):
    with open(file_path, "r") as stream:
        stream = yaml_load(stream)
        return stream


def traverse_tree(output):
    if isinstance(output, list):
        for element_list in output:
            for element in traverse_tree(element_list):
                yield element

    elif isinstance(output, dict):
        for key in output:
            for value in output[key]:
                yield value


def generate_xml(file_path, yaml_output):
    with open(file_path, "w") as new_file:
        new_file.write(xml_generator.xml_header)

        yaml_activity = yaml_output.get('activity')

        print("ORIGINAL OUTPUT\n----\n{}\n----\n".format(yaml_activity))

        # root element
        for tag in xml_generator.generate_tag(next(iter(yaml_activity[0]))):
            new_file.write(tag)
        # new_file.write(xml_generator.map_tags(next(iter(yaml_activity[0]))))

        for element in traverse_tree(yaml_activity):
            for tag in xml_generator.generate_tag(element):
                new_file.write(tag)

    print("\nYour file is ready at {}!".format(file_path))


def main(file_path):
    yaml_output = parse_yaml(file_path)

    generate_xml("/Users/oday/Desktop/newfile.xml", yaml_output)


if __name__ == '__main__':
    main("/Users/oday/Desktop/stream.yaml")
