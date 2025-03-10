from functools import singledispatch

from typing import List, Dict, Any

@singledispatch
def formatter_content(content: Any, *, role: str) -> List[Dict]:
    return [{
        "role": role,
        "content": str(content)
    }]

@formatter_content.register(list)
def formatter_content_list(content: List, *, role: str) -> List[Dict]:
    return [{
        "role": role,
        "content": str(data)
    } for data in content]
