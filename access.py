import json

def accesUser():
  userId=input("Ingresar cedula del paciente")
  date=input(" Ingresar fecha de nacimiento")
  strJson='{"userId":"'+userId+'",'+'"date":"'+date+'"}'
  returnJson=json.dumps(strJson)
  return returnJson
