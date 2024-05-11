import json 

data = '{"firstName":"murat","lastName":"asik"}'

y = json.load(data)

print(y["firstName"])
print(y["lastName"])

customer = {
    "firstName":"murat",
    "email":"muratasik@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)

