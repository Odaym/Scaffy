xml_header = "<?xml version='1.0' encoding='utf-8'?>\n\n"
android_xml_namespace = "\n\txmlns:android='http://schemas.android.com/apk/res/android'\n"

temporary_closing_tag = ">\n"
closing_tag = "/>\n"

tagDimensions = {"width_match_parent": "\t\tandroid:layout_width='match_parent'\n",
                 "width_wrap_content": "\t\tandroid:layout_width='wrap_content'\n",
                 "height_match_parent": "\t\tandroid:layout_height='match_parent'",
                 "height_wrap_content": "\t\tandroid:layout_height='wrap_content'"}

tagNames = {"relative_layout_open": "<RelativeLayout", "relative_layout_close": "</RelativeLayout>",
            "linear_layout_open": "<LinearLayout", "linear_layout_close": "<LinearLayout", "button": "\t<Button\n",
            "text_view": "\t<TextView\n", "edit_text": "\t<EditText\n", "radio_button": "\t<RadioButton\n",
            "check_box": "\t<CheckBox\n", "image_view": "\t<ImageView\n", "image_button": "\t<ImageButton\n"}

orientations = {"orientation_vertical": "\t\tandroid:orientation='vertical'\n",
                "orientation_horizontal": "\t\tandroid:orientation='horizontal'\n"}


def map_tags(yaml_elements):
    for yelement_list in yaml_elements:
        for i, yelement in enumerate(yelement_list):
            if yelement not in tagNames:
                print("{} is not supported".format(yelement))
            elif i == 0:
                # first tag (root element open)
                yield tagNames[yelement] + " " + android_xml_namespace + tagDimensions["width_match_parent"] + \
                      tagDimensions[
                          "height_match_parent"] + temporary_closing_tag
            elif i == len(yelement_list) - 1:
                # final tag (root element close)
                yield tagNames[yelement] + "\n"
            else:
                # all other tags
                yield tagNames[yelement] + tagDimensions["width_match_parent"] + tagDimensions[
                    "height_match_parent"] + closing_tag
