def calculate_vat(price, vat=0.23):
    default_vat = 0.23

    if isinstance(vat, float) and isinstance(price, (float, int)):
        if vat < 0.0:
            vat = default_vat
        return price * vat