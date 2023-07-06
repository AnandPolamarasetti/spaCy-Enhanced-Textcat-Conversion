from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from ..tokens import Doc, Span
from ..vocab import Vocab
from .alignment import Alignment

def annotations_to_doc(
    vocab: Vocab,
    tok_annot: Dict[str, Any],
    doc_annot: Dict[str, Any],
) -> Doc: ...
def validate_examples(
    examples: Iterable[Example],
    method: str,
) -> None: ...
def validate_get_examples(
    get_examples: Callable[[], Iterable[Example]],
    method: str,
): ...

class Example:
    x: Doc
    y: Doc

    def __init__(
        self,
        predicted: Doc,
        reference: Doc,
        *,
        alignment: Optional[Alignment] = None,
    ): ...
    def __len__(self) -> int: ...
    @property
    def predicted(self) -> Doc: ...
    @predicted.setter
    def predicted(self, doc: Doc) -> None: ...
    @property
    def reference(self) -> Doc: ...
    @reference.setter
    def reference(self, doc: Doc) -> None: ...
    def copy(self) -> Example: ...
    @classmethod
    def from_dict(cls, predicted: Doc, example_dict: Dict[str, Any]) -> Example: ...
    @property
    def alignment(self) -> Alignment: ...
    def get_aligned(self, field: str, as_string=False): ...
    def get_aligned_parse(self, projectivize=True): ...
    def get_aligned_sent_starts(self): ...
    def get_aligned_spans_x2y(self, x_spans: Sequence[Span], allow_overlap=False) -> List[Span]: ...
    def get_aligned_spans_y2x(self, y_spans: Sequence[Span], allow_overlap=False) -> List[Span]: ...
    def get_aligned_ents_and_ner(self) -> Tuple[List[Span], List[str]]: ...
    def get_aligned_ner(self) -> List[str]: ...
    def get_matching_ents(self, check_label: bool = True) -> List[Span]: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def split_sents(self) -> List[Example]: ...
    @property
    def text(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
