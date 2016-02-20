xml_header = "<?xml version='1.0' encoding='utf-8'?>\n\n"
android_xml_namespace = "xmlns:android='http://schemas.android.com/apk/res/android'"

temporary_closing_tag = ">\n"
closing_tag = "/>\n"

tagDimensions = {"width_match_parent": "\t\tandroid:layout_width='match_parent'\n",
                 "width_wrap_content": "\t\tandroid:layout_width='wrap_content'\n",
                 "height_match_parent": "\t\tandroid:layout_height='match_parent'",
                 "height_wrap_content": "\t\tandroid:layout_height='wrap_content'"}

tagNames = ["relative_layout",
            "linear_layout", "button",
            "text_view", "edit_text", "radio_button",
            "check_box", "image_view", "image_button"]

attrTags = {"id": "\t\tandroid:id='@+id/{}'\n", "text": "\t\tandroid:text='{}'\n"}

orientations = {"orientation_vertical": "\t\tandroid:orientation='vertical'\n",
                "orientation_horizontal": "\t\tandroid:orientation='horizontal'\n"}


def join_attributes(attrs):
    attrLine = tagDimensions["width_match_parent"] + tagDimensions[
        "height_match_parent"]

    for attr in attrs:
        attrLine += (attrTags[attr]) if attr in attrTags else print("{} attribute is not supported.")

    return attrLine


def textview_node(attrs):
    start = '\t<TextView\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def button_node(attrs):
    start = '\t<Button\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def imageview_node(attrs):
    start = '\t<ImageView\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def imagebutton_node(attrs):
    start = '\t<ImageButton\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def edittext_node(attrs):
    start = '\t<EditText\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def radiobutton_node(attrs):
    start = '\t<RadioButton\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def checkbox_node(attrs):
    start = '\t<CheckBox\n{}{}>\n\n'.format(
        join_attributes(attrs),
        '/')

    return "".join(start)


def linearlayout_node(attrs):
    start = '<LinearLayout {}{}{}>{}'.format(
        android_xml_namespace, "\n",
        join_attributes(attrs), "\n\n")

    return "".join(start)


def relativelayout_node(attrs):
    start = '<RelativeLayout {}{}{}>{}'.format(
        android_xml_namespace, "\n",
        join_attributes(attrs), "\n\n")

    return "".join(start)


def generate_tag(tag):
    if tag not in tagNames:
        print("{} is not supported".format(tag))
    else:
        switcher = {
            "relative_layout": relativelayout_node([]),
            "linear_layout": linearlayout_node([]),
            "text_view": textview_node([]),
            "button": button_node([]),
            "image_button": imagebutton_node([]),
            "image_view": imageview_node([]),
            "edit_text": edittext_node([]),
            "check_box": checkbox_node([]),
            "radio_button": radiobutton_node([])
        }

        yield switcher.get(tag)