class DecoratorDiv:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, func):
        def wrap(names_list):
            return "<div class=*{0}*>\n{1}</div>".format(self.style_class, func(names_list))

        return wrap


def decorator_body(func):
    def wrap(names_list):
        return "<body>\n{}\n</body>\n".format(func(names_list))

    return wrap


class DecoratorHead:
    def __init__(self, title):
        self.title = title

    def __call__(self, func):
        def wrap(names_list):
            return "<head>\n<title>*{0}*</title>\n</head>\n{1}".format(self.title, func(names_list))
        return wrap


def decorator_html(func):
    def wrap(names_list):
        return "<html>\n{}</html>\n".format(func(names_list))
    return wrap


@decorator_html
@DecoratorHead("title")
@decorator_body
@DecoratorDiv('my_class')
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>\n"
    template = "<p> {} </p>"
    output = ""
    for name in names_list:
        output += template.format(name) + "\n"
    return template_head + output


print(get_names_page(["Misha", "Olya", "Vitaliy", "Vita"]))
