import base64


def get_base64(path):

    with open(path, "rb") as img:
        return base64.b64encode(
            img.read()
        ).decode()


def load_css(path):

    with open(path) as f:
        return f.read()