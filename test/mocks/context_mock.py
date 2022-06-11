"""Mock Context"""
from src.commons.context import Context
from test.mocks.config_mock import MockConfig


class MockContext(Context):
    """Class"""

    def __init__(self):
        self.config = MockConfig()
        super().__init__(self.config)
