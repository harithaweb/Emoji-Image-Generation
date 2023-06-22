from PIL import Image, ImageDraw, ImageFont

# Define the Unicode character to generate an image from
unicode_character = u"\U0001F604"  # Slightly Smiling Face emoji

# Define the image size and font properties
image_width, image_height = 200, 200
font_size = 148
font_path = "C:\\Users\\91782\\Documents\\seguiemj.ttf"  # Replace with the path to your desired font file

# Create a blank image with a white background
image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Calculate the position to center the character on the image
char_width, char_height = draw.textsize(unicode_character, font=font)
x = (image_width - char_width) // 2
y = (image_height - char_height) // 2

# Create a new image for the filled shape
fill_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
fill_draw = ImageDraw.Draw(fill_image)


# Draw a yellow-colored circle
circle_center = (image_width // 2.9, image_height // 3.5)
circle_radius = min(image_width, image_height) // 2.9
fill_color = (255, 255, 0, 255)  # Yellow color (R, G, B, A)
circle_box = [(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
              (circle_center[0] + circle_radius, circle_center[1] + circle_radius)]
fill_draw.ellipse(circle_box, fill=fill_color)

# Paste the emoji onto the main image with transparency
image.paste(fill_image , (x, y), fill_image)


#########
# Create a new image for the filled shape
#fill_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
#fill_draw = ImageDraw.Draw(fill_image)


# Draw the filled shape with the fill color (yellow)
fill_color = "#ffcc22"
fill_draw.rectangle([(x,y),(x + image_width, y + image_height)],fill="#fff5ee")
fill_draw.text((x, y), unicode_character, font=font, fill="#fff5ee")

# Create a new image for the outline shape
outline_image = Image.new("RGBA", (image_width, image_height), "black")
outline_draw = ImageDraw.Draw(outline_image)

# Draw the outline shape with the outline color (black)
outline_color = "#0b0200"
outline_draw.text((x, y), unicode_character, font=font, fill=outline_color)

# Paste the filled shape onto the main image
#image.paste(fill_image, (0, 0), fill_image)

# Paste the outline shape onto the main image
#image.paste(outline_image, (0, 0), outline_image)

########

#create new image foe filled shape -h
shape_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
shape_draw = ImageDraw.Draw(shape_image)

# Draw a filled shape that matches the emoji outline
outline_color = "black"
fill_color = "yellow"
shape_draw.text((x, y), unicode_character, font=font, fill=outline_color)
shape_draw.text((x, y), unicode_character, font=font, fill=fill_color)

# Paste the filled shape onto the main image
image.paste(shape_image, (0, 0), shape_image)

# Draw the character on the image
draw.text((x, y), unicode_character, font=font, fill="black")

# Save the image
image.save("coloured_emoji_image.png")