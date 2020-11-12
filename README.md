# tarea2-inf331
En esta tarea se utilizará AWS Rekognition en conjunto con S3 (buckets) para comparar si dos imagenes tienen el mismo texto.

# Dependencias
Se utilizó python 3.8.6 y boto3

# Instalación dependencias

``` pip install boto3 ```

# Uso
Para correr el programa usar \n
``` $python app.py -i awsid -k awskey``` \n
En donde **awsid** es la aws_access_key_id y **awskey** es aws_secret_access_key

Luego, para poder testear las fotos, cambiar las lineas 45, 46 y 47 del código según corresponda, ingresando el nombre del bucket a utilizar, el nombre de la imagen a testear y el nombre de la imagen de control.
