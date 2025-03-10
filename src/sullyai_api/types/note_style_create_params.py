# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NoteStyleCreateParams"]


class NoteStyleCreateParams(TypedDict, total=False):
    instructions: List[str]
    """Optional instructions for note generation"""

    sample_note: Annotated[str, PropertyInfo(alias="sampleNote")]
    """Sample note text to base the style on"""
