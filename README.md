# Movie recommender

A movie recommender created using Cosine Similarity. The engine will recommend 5 movies after the input from the user. It will do it by analysing the text: the description of the movies, the keywords, the cast, the director and the genre.

## Installation

Made using Python, here is a list of necesesarry libraries:
```bash
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
```

## Usage

```python
The data is in this git(two .csv files) , just open a notebook and run the code.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
