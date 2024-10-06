import random
import string
from captcha.image import ImageCaptcha
import PIL.Image
import IPython.display as display

def generate_Captcha():
    # Generate random string
    random_string = string.digits + string.ascii_lowercase
    captcha_text = ''.join(random.choice(random_string) for _ in range(5))
    
    # Generate Captcha from text
    image = ImageCaptcha(width=400, height=200)
    image.generate(captcha_text)
    
    # Save Captcha image and display it
    image.write(captcha_text, "captcha.png")
    img = PIL.Image.open("captcha.png")
    display.display(img)
    img.show()
    
    return captcha_text

def verify_Captcha():
    flag = False
    while flag != True:
        captcha_text = generate_Captcha()
        # print(captcha_text)
        user_input = input("Enter CAPTCHA Text \n")
        if user_input == captcha_text:
            print("\nCaptcha Verified Successfully")
            flag = True
        else:
            print("\nInvalid Captcha Entry!!!!!!!!!!!!!!!!!!")

def main():
    verify_Captcha()

if __name__ == "__main__":
    main()
