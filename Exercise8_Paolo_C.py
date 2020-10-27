InputUsername = input("กรุณาใส่ Username : ")
InputPassword = input("กรุณาใส่ Password : ")
if InputUsername == "1234" and InputPassword == "1234":
    print("รหัสผ่านถูกต้อง")
    print(".")
    print(".")
    print("----- PShop -----")
    print("1.กาแฟ ราคา 10 บาท")
    print("2.น้ำส้ม ราคา 15 บาท")
    InputDrink = int(input("กรุณาเลือกเครื่องดื่ม : "))
    InputQuantity = int(input("กรุณาเลือกจำนวนที่ต้องการ : "))
    price1 = 10
    price2 = 15
    if InputDrink == 1:
        print("คุณได้เลือกเครื่องดื่มกาแฟ", "จำนวน", InputQuantity, "กระป๋อง")
        print("กระป๋องละ 10 บาท รวมเป็นเงิน", price1 * InputQuantity, "บาท")
    if InputDrink == 2:
        print("คุณได้เลือกเครื่องดื่มน้ำส้ม", "จำนวน", InputQuantity, "แก้ว")
        print("แก้วละ 15 บาท รวมเป็นเงิน", price2 * InputQuantity, "บาท")
    else:
        print("คุณทำรายการไม่ถูกต้อง")
else:
    print("รหัสผ่านผิดพลาด")