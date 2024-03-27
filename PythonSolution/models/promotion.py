from dataclasses import dataclass
from typing import List


@dataclass
class Promotion:
	code: str
	not_combinable_with: List[str]
