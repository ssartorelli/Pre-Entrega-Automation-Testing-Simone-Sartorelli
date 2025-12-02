from faker import Faker
#Generar datos aleatorios para pruebas
fake = Faker()
def get_login_faker(num_casos=5):
    casos =[]
    #usuarios_validos  =["standart_user", "locked_out_user"]
    #password_valido = "secret_sauce"


    for _ in range(num_casos):
        username = fake.user_name()
        password = fake.password(length=12)
        login_example = fake.boolean(chance_of_getting_true=50)
        


        casos.append((username,password, login_example))
    return casos
