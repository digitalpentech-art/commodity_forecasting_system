try:
    import pandas as pd
    print("Pandas version:", pd.__version__)
except ImportError:
    print("Pandas not found")
