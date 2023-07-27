def read_markdown(file: str) -> str:
    with open(file=file, mode="r") as markdown:
        content = markdown.read()

    return content
