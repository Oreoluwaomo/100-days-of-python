import smtplib
my_email = "oreoluwaomojuwa@gmail.com"
password = "kugq tlga nqif jsze"


with smtplib.SMTP("smtp.gmail.com",587) as connection :
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="florenceomojuwa25@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email")




