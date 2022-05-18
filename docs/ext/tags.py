"""Script to create index, date and tag pages.
"""
import os
from docutils.parsers.rst import Directive
from docutils import nodes


# TAGLINK is used to generate the link from within each narrative page
TAGLINK = "tags/%s.html"
TAGSTART = ".. tags::"

class TagLinks(Directive):
    """Custom directive for adding tags to Sphinx-generated files.

    Loosely based on https://stackoverflow.com/questions/18146107/how-to-add-blog-style-tags-in-restructuredtext-with-sphinx

    See also https://docutils.sourceforge.io/docs/howto/rst-directives.html

    """
    # Sphinx directive class attributes
    required_arguments = 1
    optional_arguments = 200  # Arbitrary.
    has_content = False

    # Custom attributes
    separator = ","
    taglink = TAGLINK
    intro_text = "Tags: "

    def run(self):
        tags = [arg.replace(self.separator, "") for arg in self.arguments]
        result = nodes.paragraph()
        result["classes"] = ["tags"]
        result += nodes.inline(text=self.intro_text)
        count = 0
        for tag in tags:
            count += 1
            link = self.taglink % tag
            tag_node = nodes.reference(refuri=link, text=tag)
            result += tag_node
            if not count == len(tags):
                result += nodes.inline(text=f"{self.separator} ")
        return [result]


class Tag:
    """A tag contains entries"""

    def __init__(self, name):
        self.name = name
        self.items = []
        self.filename = os.path.join(".", f"tags/{self.name}.rst")

    def create_file(self, items):
        """Create rst file with list of documents associated with a given tag.

        This file is reached as a link from the tag name.

        """
        content = []
        content.append(self.name)
        content.append("#" * len(self.name))
        content.append("")
        #  Return link block at the start of the page"""
        content.append(".. toctree::")
        content.append("    :maxdepth: 1")
        content.append("")
        #  items is a list of files associated with this tag
        for item in items:
            link = item.filename.replace("./", "")
            content.append(f"    {item.title} <../{link}>")
        content.append("")
        with open(self.filename, "w", encoding="utf8") as f:
            f.write("\n".join(content))


class Entry:
    """Extracted info from *.rst file.

    We need the path, the title and the tags.

    """
    def __init__(self, filepath):
        self.filename = filepath
        with open(filepath, "r", encoding="utf8") as f:
            self.lines = f.read().split("\n")
        self.title = self.lines[0].strip()
        tagline = [line for line in self.lines if TAGSTART in line]
        self.tags = []
        if tagline:
            tagline = tagline[0].replace(TAGSTART, "")
            self.tags = tagline.split(",")
            self.tags = [tag.strip() for tag in self.tags]

    def assign_to_tags(self, tag_dict):
        """Append ourself to tags"""
        for tag in self.tags:
            if tag not in tag_dict:
                tag_dict[tag] = Tag(tag)
            tag_dict[tag].items.append(self)


def tagpage(tags):
    """Creates Tag overview page.

    This page contains a list of all available tags.

    """
    content = []
    title = "Tag overview"
    content.append(title)
    content.append("#" * len(title))
    content.append("")
    content.append(".. toctree::")
    content.append("    :maxdepth: 1")
    content.append("")
    tags = list(tags.values())
    for tag in tags:
        content.append(f"    {tag.name} <{tag.name}.rst>")
    content.append("")
    filename = os.path.join(".", "tags/index.rst")
    with open(filename, "w", encoding="utf8") as f:
        f.write("\n".join(content))


def assign_entries():
    """Assign all found entries to their tag."""
    pages = []
    tags = {}
    for entryname in os.listdir("."):
        if entryname.endswith(".rst"):
            path = os.path.join(".", entryname)
            entry = Entry(path)
            entry.assign_to_tags(tags)
            pages.append(entry)
    return tags, pages


def setup(app):
    """Setup for Sphinx."""
    app.add_directive("tags", TagLinks)
    # directives.register_directive("tags", TagLinks)
    tags, pages = assign_entries()
    for tag in tags.values():
        tag.create_file([item for item in pages if tag.name in item.tags])
    tagpage(tags)
