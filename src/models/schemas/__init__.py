"""Schemas module."""
from typing import Dict
from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base schema class for all schemas."""
    def to_dict(self) -> Dict:
        """Convert schema to dict."""
        return self.__dict__
    @classmethod
    def from_dict(cls, data: Dict) -> 'BaseSchema':
        """Convert dict to schema."""
        return cls(**data)