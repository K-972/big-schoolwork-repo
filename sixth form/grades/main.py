import pandas as pd

import warnings

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)



df = pd.DataFrame(columns=['Name', 'Mark', 'Max Marks', 'Grade', 'Percentage'])