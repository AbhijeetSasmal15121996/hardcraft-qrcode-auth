from email.message import EmailMessage
import imghdr
import smtplib


# img = Image.open(r'test.png')
# d1 = ImageDraw.Draw(img)
# myFont = ImageFont.truetype('font/FreeMono.ttf', 70)
# d1.text((720, 770), pp, font=myFont, fill=(0, 0, 0))
# img.save("pictures/vaccination.png")


Sender_Email = "abhijeetsasmal74@gmail.com"
Reciever_Email = "abhijeetsasmal74@gmail.com"
Password = '6112376BD659748F3E42E62407D92A5D3398'
def send(Reciever_Email, path):
    newMessage = EmailMessage()
    newMessage['Subject'] = "Qr Code for login"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content(' Download the attached QRCode')

    with open(path, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP('smtp.elasticemail.com', 2525) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)