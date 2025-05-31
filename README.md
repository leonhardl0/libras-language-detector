# Detector de Gestos em Libras

Este projeto tem como objetivo ajudar a comunidade surda através da detecção e reconhecimento de gestos em Libras a partir de imagens.

## Sobre o Projeto

Usamos uma abordagem baseada em Visão Computacional para:
- Detectar a mão na imagem (YOLO)
- Classificar o gesto em Libras (Keras)

**Base de Dados:**
- [Alfabeto em Libras - Roboflow](https://universe.roboflow.com/elainesilva/alfabeto-em-libras-qrvnw) (~5.000 imagens)

## Estrutura

- `main.py` - Código principal que detecta e classifica gestos
- `model/` - Diretório para armazenar o modelo treinado (`model.keras`)
- `requirements.txt` - Dependências do projeto

## Tecnologias usadas

- YOLO (para detecção de mãos)
- Keras/TensorFlow (para classificação dos gestos)
- OpenCV
- Numpy

## Melhorias Futuras

- Melhor recorte da mão
- Treinamento em vídeos
- Mais classes de gestos

## Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/Libras-Detector.git
cd Libras-Detector
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute:
```bash
python main.py
```