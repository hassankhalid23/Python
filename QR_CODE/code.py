import qrcode
#  taking upid as input
upid = input("Enter your UPI ID: ")
#  creating a QR code object
phonepe_url = f'upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234'
paytmpe_url = f'upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upid}&pn=Recipient%20Name&mc=1234'

#creating qr code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytmpe_url) 
google_pay_qr = qrcode.make(google_pay_url)

#save qr code as img file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")
#display qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

print("QR codes generated and saved as phonepe_qr.png, paytm_qr.png, and google_pay_qr.png")