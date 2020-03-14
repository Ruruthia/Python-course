VAT = 0.23

def vat_faktura(lista):
    return round(sum(lista) * VAT, 2)

def vat_paragon(lista):
    z_vat = [round(item * VAT, 2) for item in lista]
    return sum(z_vat)
