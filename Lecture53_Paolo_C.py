def vatcal(total):
    result = total+(total*7/100)
    return  result

InputTotla = int(input("ใส่ราคาสินค้า : "))
print(vatcal(InputTotla))