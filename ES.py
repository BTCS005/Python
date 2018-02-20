#email
import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("anitharathnam.kv@gmail.com","An@12061999")
msg="Hi Annulekha"
s.sendmail("anitharathnam.kv@gmail.com","anulekha2112016@gmail.com",msg)
print("success")
s.quit()
