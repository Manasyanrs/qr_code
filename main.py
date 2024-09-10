import os

import qrcode

path_to_qr_code = os.path.abspath(os.path.dirname(__file__)) + "/qr_codes"
if not os.path.exists(path_to_qr_code):
    os.makedirs(path_to_qr_code)


def generate_qr_code(company_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(company_name)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white",
    )
    file_path = os.path.join(path_to_qr_code, company_name.removeprefix("https://") + '.png')
    img.save(file_path)


if __name__ == "__main__":
    name = "https://yerevan-city.am"
    generate_qr_code(name)
