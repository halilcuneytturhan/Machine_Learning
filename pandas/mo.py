import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r"C:\Users\cavus\Desktop\Titanic-Dataset")
