from PIL import Image

# 1. Load your original QR code and convert it to grayscale
qr = Image.open("qr.png").convert("L")

# 2. Create a new blank RGB image of the exact same size
out = Image.new("RGB", qr.size)

# 3. Loop through every single pixel
width, height = qr.size
for x in range(width):
    for y in range(height):
        pixel = qr.getpixel((x, y))
        
        # If the QR code pixel is white...
        if pixel > 128:
            # Make the output pixel pure black
            out.putpixel((x, y), (0, 0, 0))
        # If the QR code pixel is black...
        else:
            # Make the output pixel almost black (invisible to the eye)
            out.putpixel((x, y), (2, 2, 2))

# 4. Save the new "blank" image
out.save("level_challenge.png")
print("Challenge generated! Open level_challenge.png and check the levels.")
