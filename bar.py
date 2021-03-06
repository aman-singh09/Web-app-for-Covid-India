import requests
import matplotlib.pyplot as plt
import pandas as pd

result = requests.get(
    "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
content = result.json()
df = pd.DataFrame(content["regionData"])
