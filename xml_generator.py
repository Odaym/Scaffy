xml_header = "<?xml version='1.0' encoding='utf-8'?>\n\n"
android_xml_namespace = "xmlns:android='http://schemas.android.com/apk/res/android'"

temporary_closing_tag = ">\n"
closing_tag = "/>\n"

tagDimensions = {"width_match_parent": "\t\tandroid:layout_width='match_parent'\n",
                 "width_wrap_content": "\t\tandroid:layout_width='wrap_content'\n",
                 "height_match_parent": "\t\tandroid:layout_height='match_parent'",
                 "height_wrap_content": "\t\tandroid:layout_height='wrap_content'"}

tagNames = ["RelativeLayout",
            "LinearLayout", "Button",
            "TextView", "EditText", "RadioButton",
            "CheckBox", "ImageView", "ImageButton"]

attrTags = ["id", "text", "orientation", "color"]

orientations = {"orientation_vertical": "\t\tandroid:orientation='vertical'\n",
                "orientation_horizontal": "\t\tandroid:orientation='horizontal'\n"}


def map_attributes(attrs):
    final_attrs = []

    final_attrs.append(tagDimensions["width_match_parent"] + tagDimensions[
        "height_match_parent"])

    if attrs:
        for key, value in attrs.items():
            print("KEY IS {}".format(key))
            # print("key : {} value : {}".format(key, value))
            if key not in attrTags:
                print("")
            else:
                switcher = {
                    "id": "\t\tandroid:id=@+id/{}".format(value),
                    "text": "\t\tandroid:text='{}'".format(value),
                    "orientation": "\t\tandroid:orientation='{}'".format(value),
                    "color": "\t\tandroid:color='{}'".format(value)
                }
                final_attrs.append(switcher.get(key))
                # print("attr_line is {}".format(attr_line))

    return "\n".join(final_attrs)


def textview_node(attrs):
    return '\t<TextView\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def button_node(attrs):
    return '\t<Button\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def imageview_node(attrs):
    start = '\t<ImageView\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')

    return "".join(start)


def imagebutton_node(attrs):
    return '\t<ImageButton\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def edittext_node(attrs):
    return '\t<EditText\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def radiobutton_node(attrs):
    return '\t<RadioButton\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def checkbox_node(attrs):
    return '\t<CheckBox\n{}{}>\n\n'.format(
        map_attributes(attrs),
        '/')


def linearlayout_node(attrs):
    return '<LinearLayout {}{}{}>{}'.format(
        android_xml_namespace, "\n",
        map_attributes(attrs), "\n\n")


def relativelayout_node(attrs):
    return '<RelativeLayout {}{}{}>{}'.format(
        android_xml_namespace, "\n",
        map_attributes(attrs), "\n\n")


def relativelayout_closing_node():
    return "</RelativeLayout>{}".format("\n")


def linearlayout_closing_node():
    return "</LinearLayout>{}".format("\n")


def map_tags(tag, attrs):
    if tag not in tagNames:
        print("")
    else:
        switcher = {
            "relative_layout": relativelayout_node([]),
            "linear_layout": linearlayout_node([]),
            "text_view": textview_node(attrs),
            "button": button_node(attrs),
            "image_button": imagebutton_node(attrs),
            "image_view": imageview_node(attrs),
            "edit_text": edittext_node(attrs),
            "check_box": checkbox_node(attrs),
            "radio_button": radiobutton_node(attrs)
        }

        yield switcher.get(tag)
