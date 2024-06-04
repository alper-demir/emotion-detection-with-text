import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Örnek veri seti yükleme
data = pd.read_csv('dataset.csv', on_bad_lines="skip")

# Özellik ve etiketlerin ayrılması
X = data['Text']
y = data['Emotion']

# Eğitim ve test setlerinin oluşturulması
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF Vektörizasyonu
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Lojistik Regresyon Modeli Eğitimi
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Modelin doğruluğunu değerlendirme
y_pred = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Modeli ve vektörizeri kaydet
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
