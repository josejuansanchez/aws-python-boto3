# aws-python-boto3

## Primeros pasos

Creamos un entorno virtual.

```
python3 -m venv .venv
```

Activamos el entorno virtual.

```
. .venv/bin/activate
```

Instalamos el paquete boto3.

```
python3 -m pip install boto3
```

## Configuramos las credenciales de AWS


Editamos el archivo de credenciales de AWS que está en la ruta:

```
~/.aws/credentials
```

Copiamos nuestras credenciales, sustituyendo los valores de `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` y `AWS_SESSION_TOKEN`, por nuestros valores.

```
[default]
aws_access_key_id=AWS_ACCESS_KEY_ID
aws_secret_access_key=AWS_SECRET_ACCESS_KEY
aws_session_token=AWS_SESSION_TOKEN
```

Editamos el archivo de configuración de AWS, para indicar la región y el formato de salida de los comandos de AWS CLI.

~/.aws/config

```
[default]
region = us-east-1
output = json
```

## Referencias

- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#securitygroup
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance