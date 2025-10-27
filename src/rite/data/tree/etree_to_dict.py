from collections import defaultdict
from typing import Any, Dict, Union
from xml.etree.ElementTree import Element


def etree_to_dict(t: Element) -> Dict[str, Any]:
    """
    Convert an XML ElementTree node into a nested Python dictionary.

    Args:
        t (Element): The root XML element to convert.

    Returns:
        Dict[str, Any]: A dictionary representation of the XML element.
    """
    tag_dict: Dict[str, Union[dict, str, None]] = {
        t.tag: {} if t.attrib else None
    }
    children = list(t)

    if children:
        child_dict = defaultdict(list)
        for child in children:
            for key, value in etree_to_dict(child).items():
                child_dict[key].append(value)
        tag_dict[t.tag] = {
            key: value[0] if len(value) == 1 else value
            for key, value in child_dict.items()
        }

    if t.attrib:
        tag_dict.setdefault(t.tag, {})
        tag_dict[t.tag].update({f"@{k}": v for k, v in t.attrib.items()})

    text = (t.text or "").strip()
    if text:
        if children or t.attrib:
            tag_dict[t.tag]["#text"] = text
        else:
            tag_dict[t.tag] = text

    return tag_dict


# =============================================================================
# Exports
# =============================================================================

__all__ = [
    "etree_to_dict",
]

# =============================================================================
# Example Usage
# =============================================================================


from xml.etree.ElementTree import fromstring

xml_str = "<book id='123'><title>Python</title><author>Lars</author></book>"
root = fromstring(xml_str)
result = etree_to_dict(root)

print(result)
# ➜ {'book': {'@id': '123', 'title': 'Python', 'author': 'Lars'}}
