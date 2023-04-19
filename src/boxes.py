from typing import List, Dict
from pathlib import Path

class Box:
    pass

def read_csv(fn: Path) -> List[Box]:
    """
    Parses the file and returns a box for every line in the csv.
    """
    pass

def group_by_building(boxes: List[Box], cat: str) -> Dict[str, float]:
    """
    Returns the total area of a category grouped by building id.

    {
        '0518100000342075': {
            1234.324324
        }
    }
    """
    pass
