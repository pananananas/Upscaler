# Upscaler

Upscaler is a project that uses machine learning algorithms to upscale images. It consists of a Vue.js frontend and a Django backend.

![Image](https://github.com/user-attachments/assets/93710b92-3b8e-4ce5-9785-1ed277c1beca)

![Image](https://github.com/user-attachments/assets/13af5b67-35e4-44b0-b5f7-d18d8e87e12c)

![Image](https://github.com/user-attachments/assets/f5fd3eef-a712-4945-9705-d9bd21e1c672)

![Image](https://github.com/user-attachments/assets/782d5191-0090-4b8d-bcb6-6eeaac159939)


## Algorithms

In this project I utilized two different algorithms to upscale images:

- [ESRGAN](https://github.com/xinntao/ESRGAN) - Enhanced Super-Resolution Generative Adversarial Network

- [DWSR](https://github.com/tT0NG/DWSRx4) - Deep Wavelet Super-Resolution


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Running the project

#### Frontend

Navigate to the `upscaler_vue_frontend` directory and install the necessary packages:

```sh
cd upscaler_vue_frontend
npm install
npm run serve
```

#### Backend 

To run backend server you need to create a virtual environment and install the necessary packages:

```sh
source environment_3_8_2/bin/activate
cd upscaler_django_backend
python manage.py runserver
```
