s1 = "Уважаемый " + "{:<}".format("Pavel") + "! Ваша работа оценена в " + "{:2}".format(5) + " баллов. Подробности высланы на email: " + "{:^}".format("cherepavell2@gmail.com") + "."
print(s1)
name = "Pavel"
email = "cherepavell2@gmail.com"
value = "5"
s2= "Уважаемый " + f"{name:<}" + "! Ваша работа оценена в " + f"{value:2}" + " баллов. Подробности высланы на email: " + f"{email:^}" + "."
print(s2)