from PIL import Image, ImageDraw
import os

# Create directories for today's date (April 23, 2026)
os.makedirs('assets/images/articles/2026-04-23', exist_ok=True)

def create_simple_hero_image():
    """Create a simple hero image with gradient background and text"""
    width, height = 1200, 630
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Create a modern gradient background
    for y in range(height):
        r = int(44 + (52 - 44) * y / height)
        g = int(152 + (59 - 152) * y / height)
        b = int(235 + (147 - 235) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Add title text
    text = "AI AGENTS: THE NEW DIGITAL WORKFORCE"
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    except:
        font = None
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((width - text_width) // 2, (height - text_height) // 2 - 50)
    draw.text(position, text, font=font, fill="white", align="center")
    
    # Add subtitle
    subtitle = "Revolutionizing Our Future"
    try:
        subfont = ImageFont.truetype("DejaVuSans.ttf", 32)
    except:
        subfont = None
        
    bbox2 = draw.textbbox((0, 0), subtitle, font=subfont)
    sub_width = bbox2[2] - bbox2[0]
    sub_position = ((width - sub_width) // 2, position[1] + text_height + 20)
    draw.text(sub_position, subtitle, font=subfont, fill="#ecf0f1", align="center")
    
    # Add date
    date_text = "April 23, 2026"
    bbox3 = draw.textbbox((0, 0), date_text, font=subfont)
    date_width = bbox3[2] - bbox3[0]
    date_position = ((width - date_width) // 2, sub_position[1] + 60)
    draw.text(date_position, date_text, font=subfont, fill="#bdc3c7", align="center")
    
    # Save image
    img.save('assets/images/articles/2026-04-23/ai-agents-hero.jpg', 'JPEG', quality=85)

def create_simple_content_image1():
    """Create a simple content image showing AI agent architecture"""
    width, height = 800, 500
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Modern tech background pattern
    for x in range(0, width, 40):
        for y in range(0, height, 40):
            if (x // 40 + y // 40) % 2 == 0:
                draw.rectangle([x, y, x+38, y+38], fill="#2c3e50")
            else:
                draw.rectangle([x, y, x+38, y+38], fill="#34495e")
    
    # Add text
    text = "HOW AI AGENTS WORK"
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 50)
        subfont = ImageFont.truetype("DejaVuSans.ttf", 28)
    except:
        font = None
        subfont = None
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    position = ((width - text_width) // 2, height // 2 - 80)
    draw.text(position, text, font=font, fill="white", align="center")
    
    # Save image
    img.save('assets/images/articles/2026-04-23/how-it-works.jpg', 'JPEG', quality=85)

def create_simple_content_image2():
    """Create a simple content image showing industry applications"""
    width, height = 800, 500
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Create a background with colored circles representing industries
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c"]
    for i in range(6):
        x = 100 + (i % 3) * 250
        y = 100 + (i // 3) * 150
        
        # Draw circle with industry letter
        draw.ellipse([x, y, x+180, y+130], fill=colors[i])
    
    # Add title
    try:
        from PIL import ImageFont
        big_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 48)
        subfont = ImageFont.truetype("DejaVuSans.ttf", 28)
    except:
        big_font = None
        subfont = None
    
    text = "INDUSTRIES TRANSFORMED"
    bbox = draw.textbbox((0, 0), text, font=big_font)
    text_width = bbox[2] - bbox[0]
    position = ((width - text_width) // 2, 35)
    draw.text(position, text, font=big_font, fill="#2c3e50", align="center")
    
    # Save image
    img.save('assets/images/articles/2026-04-23/industries.jpg', 'JPEG', quality=85)

if __name__ == "__main__":
    print("Generating magazine images...")
    create_simple_hero_image()
    print("✓ Created hero image: ai-agents-hero.jpg")
    create_simple_content_image1()
    print("✓ Created content image 1: how-it-works.jpg")
    create_simple_content_image2()
    print("✓ Created content image 2: industries.jpg")
    print("\nAll images generated successfully!")