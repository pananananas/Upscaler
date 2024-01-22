# Upscaler

Upscaler is a project that uses machine learning algorithms to upscale images. It consists of a Vue.js frontend and a Django backend.

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