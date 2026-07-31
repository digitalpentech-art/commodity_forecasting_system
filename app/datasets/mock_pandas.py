# Mocking pandas
class MockDataFrame:
    def __init__(self, data=None): self.data = data
    def head(self): return self
    def to_html(self): return "<table></table>"
    def groupby(self, col): return self
    def mean(self): return self
    def to_dict(self): return {}

class MockPandas:
    DataFrame = MockDataFrame
    def read_csv(self, path): return MockDataFrame()
    def to_datetime(self, col): return col

pd = MockPandas()
