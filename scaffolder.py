#!/usr/bin/env python3

from yaml import safe_load as yaml_safe_load
import xml_generator


def parse_yaml(file_path):
    with open(file_path, "r") as stream:
        stream = yaml_safe_load(stream)
        return stream


def traverse(output, file):
    if isinstance(output, list):
        for item in output:
            traverse(item, file)
    elif isinstance(output, dict):
        for key, value in output.items():
            if isinstance(value, dict):
                # element with attrs
                print("{} with {}".format(key, value))
                for tag in xml_generator.map_tags(key, []):
                    file.write(tag)
            elif isinstance(value, list):
                # another layout
                print("root : {}".format(key))
                for tag in xml_generator.map_tags(key, []):
                    file.write(tag)

            traverse(output[key], file)
    elif isinstance(output, str) and output in xml_generator.tagNames:
        # normal element
        for tag in xml_generator.map_tags(output, []):
            file.write(tag)


def generate_xml(file_path, yaml_output):
    with open(file_path, "w") as new_file:
        new_file.write(xml_generator.xml_header)

        yaml_activity = yaml_output.get('activity')

        traverse(yaml_activity, new_file)

    print("\nYour file is ready at {}!".format(file_path))


def main(file_path):
    yaml_output = parse_yaml(file_path)

    generate_xml("newfile.xml", yaml_output)


if __name__ == '__main__':
    main("stream.yaml")
