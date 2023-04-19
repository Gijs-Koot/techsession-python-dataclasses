import pytest
from pathlib import Path
from boxes import Box, read_csv, group_by_building

def test_box():

    b = Box("asef", 23., 23., 24., 24., "Deur")
    assert b.area() == pytest.approx(1)


def test_read_csv():

    box_list = read_csv(Path(__file__).parent / "data" / "boxes.csv")
    assert len(box_list) == 284


def test_groupby():

    box_list = read_csv(Path(__file__).parent / "data" / "boxes.csv")
    grouped = group_by_building(box_list)

    assert grouped["733100000003603"] == pytest.approx(-2970.999094158411)
    assert len(grouped) == 11
