import boto3
import string 
from datetime import datetime
import argparse

conf = 97 #Confianza mínima requerida para proceder

def credenciales():
  
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--awsid', type=str, required=True)
    parser.add_argument('-k', '--awskey', type=str, required=True)

    return parser.parse_args()

def Rekon(photo,creds):
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    textDetections=response['TextDetections']
    lista = list()
    texto = ""
    for text in textDetections:
        confianza = text['Confidence'] #Changeable to try custom confidence
        if (confianza < conf):
            return (False)
        if ('ParentId' in text):
            continue
        else:
            lista.append( text['DetectedText'])
    
    for i in lista:
        texto += i
        texto += " "
    listaa = texto.strip().split()
    listaa = set(listaa)

    return texto.lower()

if __name__ == "__main__":
    arc = open("logs.txt","a")
    now = datetime.now()
    now = str(now)  

    creds = credenciales()
#---------------------------------------------------->
    bucket = "pruebas-rekon" #Nombre bucket
    photo='monday4.jpg' #Foto a testear
    photo2 = "mondaycontrol.png" #Foto de control
#---------------------------------------------------->
    client = boto3.client(
        'rekognition',
        aws_access_key_id=creds.awsid,
        aws_secret_access_key=creds.awskey
    )

    res = Rekon(photo,creds)
    if (res == False):
        res = "Reconocimiento poco confiable de "+ photo + ", no puede proceder"
        print ("Reconocimiento poco confiable de",photo, ", no puede proceder")
    else:
        control = Rekon(photo2,creds)
        res = res.strip().split()
        control = control.strip().split()
        flag = True
        i = 0
        while ((flag == True) and (i != len(control)) ):
            for j in res:
                flag = control[i] in j
                if flag == True:
                    break
            i+=1
        
        if (flag == True):
            res = "True"
            
        else:
            res = "False"
           

    print("Fecha: "+now+"\n"+"Imagen a probar: "+ photo+" Resultado: "+res + "\n")
    arc.write("Fecha: "+now+"\n"+"Imagen a probar: "+ photo+" Resultado: "+res + "\n" + "--------------------------------- \n")

    arc.close()

