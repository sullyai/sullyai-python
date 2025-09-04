# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import Section as Section, HeadingSection as HeadingSection
from .delete_response import DeleteResponse as DeleteResponse
from .note_create_params import NoteCreateParams as NoteCreateParams
from .note_create_response import NoteCreateResponse as NoteCreateResponse
from .note_retrieve_response import NoteRetrieveResponse as NoteRetrieveResponse
from .note_style_create_params import NoteStyleCreateParams as NoteStyleCreateParams
from .note_style_create_response import NoteStyleCreateResponse as NoteStyleCreateResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.heading_section.HeadingSection.update_forward_refs()  # type: ignore
else:
    shared.heading_section.HeadingSection.model_rebuild(_parent_namespace_depth=0)
