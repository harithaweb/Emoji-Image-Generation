import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
from fontTools import ttLib

# Define the Unicode character to generate an image from
#unicode_character = u"\U0001F605"  # Slightly Smiling Face emoji

#####
csv_file = 'C:/Users/91782/Desktop/EmojiSheet.csv'
df = pd.read_csv(csv_file, encoding='utf-8', delimiter='/t')
print(df.columns)
####

####
    # Access the desired columns from the row
for index, row in df.iterrows():
    try:
        unicode_text = row['Unicode']
        unicode_value = int(unicode_text[2:], 16) #converts hexa decimal to decimal
        unicode_character = chr(unicode_value) #converts decimal code to character

        #font_path = 'C:\\Users\\91782\\Documents\\seguiemj.ttf'  # Replace with the path to your font file  
        font_path = "C:\\Users\\91782\\Desktop\\image generation\\font\\NotoEmoji-VariableFont_wght.ttf"
        
        #output_path = 'C:\\Users\\91782\\Desktop\\image generation.ttf'
        

        #font_file = os.listdir(font_path)[0] #assumes there is only one font
        #font_path = os.path.join(font_path, font_file)
        
        #with open(font_path, 'rb') as f:
            #font_data = io.BytesIO(f.read().decode('utf-8', errors='ignore'))

        #font = ttLib.TTFont(font_path, encoding = 'utf-8')
        #font.save(output_path)
        font_size = 620
        #font = ImageFont.truetype("arial",font_size)
        font = ImageFont.truetype(font_path, font_size)
        #font = ImageFont.truetype(font_path, font_size, layout_engine=ImageFont.LAYOUT_BASIC, fontext='ttf')

        text_width, text_height = font.getsize(unicode_character)
        image_width = text_width + 100
        image_height = text_height + 100

        # Create a new image
        image = Image.new("RGB", (800, 800), "white") #(image_width , image_height)
        draw = ImageDraw.Draw(image)

    # Draw the text onto the image
        draw.text((10, 10), unicode_character, font=font, fill="black")

    # Save the image with a unique filename
        image_filename = f"image_{index}.png"
        image.save(image_filename) 
        #font = ImageFont.truetype(font_path, font_size)

    # Determine the size of the image based on the text
        #text_width, text_height = font.getsize(unicode_text)
        #image_width = text_width + 20
    except KeyError:
        print(f"Error:Missing column 'Unicode' in row {index}")
        continue

####



# Define the image size and font properties
#image_width, image_height = 200, 200
#font_size = 148
#font_path = "C:\\Users\\91782\\Documents\\seguiemj.ttf"  # Replace with the path to your desired font file

# Create a blank image with a white background
#image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
#draw = ImageDraw.Draw(image)

# Load the font
#font = ImageFont.truetype(font_path, font_size)

# Calculate the position to center the character on the image
#char_width, char_height = draw.textsize(unicode_character, font=font)
#x = (image_width - char_width) // 2
#y = (image_height - char_height) // 2

# Create a new image for the filled shape
#fill_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
#fill_draw = ImageDraw.Draw(fill_image)


# Draw a yellow-colored circle
#circle_center = (image_width // 2.9, image_height // 3.5)
#circle_radius = min(image_width, image_height) // 2.9
#fill_color = (255, 255, 0, 255)  # Yellow color (R, G, B, A)
#circle_box = [(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
   #           (circle_center[0] + circle_radius, circle_center[1] + circle_radius)]
#fill_draw.ellipse(circle_box, fill=fill_color)

# Paste the emoji onto the main image with transparency
#image.paste(fill_image , (x, y), fill_image)


#########
# Create a new image for the filled shape
#fill_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
#fill_draw = ImageDraw.Draw(fill_image)


# Draw the filled shape with the fill color (yellow)
#fill_color = "#ffcc22"
#fill_draw.rectangle([(x,y),(x + image_width, y + image_height)],fill="#fff5ee")
#fill_draw.text((x, y), unicode_character, font=font, fill="#fff5ee")

# Create a new image for the outline shape
#outline_image = Image.new("RGBA", (image_width, image_height), "black")
#outline_draw = ImageDraw.Draw(outline_image)

# Draw the outline shape with the outline color (black)
#outline_color = "#000000"
#outline_draw.text((x, y), unicode_character, font=font, fill=outline_color)

# Paste the filled shape onto the main image
#image.paste(fill_image, (0, 0), fill_image)

# Paste the outline shape onto the main image
#image.paste(outline_image, (0, 0), outline_image)

########

#create new image foe filled shape -h
#shape_image = Image.new("RGBA", (image_width, image_height), (255, 255, 0, 255))
#shape_draw = ImageDraw.Draw(shape_image)

# Draw a filled shape that matches the emoji outline
#outline_color = "black"
#fill_color = "yellow"
#shape_draw.text((x, y), unicode_character, font=font, fill=outline_color)
#shape_draw.text((x, y), unicode_character, font=font, fill=fill_color)

# Paste the filled shape onto the main image
#image.paste(shape_image, (0, 0), shape_image)

# Draw the character on the image
#draw.text((x, y), unicode_character, font=font, fill="black")

# Save the image
#image.save("emoji_image.png")