import cv2
import numpy as np
from tensorflow.keras.models import load_model

# carregar o modelo treinado (Keras)
model = load_model('model.keras')

# classes mapeadas (exemplo)
classes = ['A', 'B', 'C', 'L', 'V']

# inicializar a webcam
cap = cv2.VideoCapture(0)

def preprocess(img):
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # exemplo simples: ROI fixa para demo
    x, y, w, h = 100, 100, 300, 300
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    roi = frame[y:y + h, x:x + w]
    processed = preprocess(roi)
    prediction = model.predict(processed)
    predicted_class = classes[np.argmax(prediction)]

    cv2.putText(frame, predicted_class, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Detector de Gestos em Libras', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
