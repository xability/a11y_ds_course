# Make pandas DataFrame print more accessible
## Written by JooYoung Seo (jseo1005@illinois.edu)


def custom_display_html(self):
    from great_tables import GT

    gt = GT(self)
    gt.show()
    return ""


def custom_display_str(self):
    from great_tables import GT

    gt = GT(self)
    gt.show()
    return ""


def set_custom_display():
    from pandas import DataFrame

    DataFrame._repr_html_ = custom_display_html
    DataFrame.__repr__ = custom_display_str


set_custom_display()
