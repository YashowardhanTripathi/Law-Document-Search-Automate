import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def generate_captcha():
    # Generate a random string (captcha text)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Create an image with white background
    image = Image.new('RGB', (150, 50), color=(255, 255, 255))
    font = ImageFont.load_default()

    draw = ImageDraw.Draw(image)
    # Draw the text on the image
    draw.text((20, 10), captcha_text, font=font, fill=(0, 0, 0))

    # Save the image to a byte buffer
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)

    return captcha_text, buffer
