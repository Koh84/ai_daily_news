# AI Agents Article - Setup Instructions

## Overview
This directory contains all files needed for an article about AI agents published on April 23, 2026.

## Files Created

1. **Article Content**: `_articles/2026-04-23-ai-agents.md`
   - Complete markdown article with frontmatter
   - Ready to be integrated into your magazine site
   - Features modern AI agent content covering:
     - What AI agents are
     - How they work
     - Real-world applications across industries
     - Future outlook

2. **Image Placeholders**: `assets/images/articles/2026-04-23/placeholders.html`
   - HTML file with CSS-based placeholders for article images
   - Can be opened in a browser and screenshot to create professional-looking images

## How to Complete the Setup

### Step 1: Generate Images (2 methods)

#### Method A: Using Screenshot (Recommended)
1. Open `assets/images/articles/2026-04-23/placeholders.html` in your web browser
2. Take a screenshot of each image placeholder:
   - **Hero Image**: Top section with "AI AGENTS: THE NEW DIGITAL WORKFORCE"
   - **Content Image**: Bottom section showing "HOW AI AGENTS WORK"
3. Save the screenshots as JPEG files in `assets/images/articles/2026-04-23/`:
   - `ai-agents-hero.jpg` (recommended size: 1200x630px)
   - `how-it-works.jpg` (recommended size: 800x500px)

#### Method B: Using Image Generation Script
1. Run the placeholder generation script:
   ```bash
   ./generate_placeholders.sh
   ```
2. Follow the instructions in the output to create images

### Step 2: Verify File Structure
Your directory structure should look like this:

```
magazine-site/
├── _articles/
│   └── 2026-04-23-ai-agents.md
└── assets/
    └── images/
        └── articles/
            └── 2026-04-23/
                ├── placeholders.html
                ├── ai-agents-hero.jpg (after you add it)
                └── how-it-works.jpg (after you add it)
```

### Step 3: Integrate into Your Site
1. Copy the article file to your site's articles directory if needed
2. Ensure the image paths in the article frontmatter match your setup:
   ```yaml
   featured_image: /assets/images/articles/2026-04-23/ai-agents-hero.jpg
   ```

### Step 4: Push to GitHub
1. Add all files to git:
   ```bash
   git add .
   ```
2. Commit with a descriptive message:
   ```bash
   git commit -m "Add AI Agents article (April 23, 2026)"
   ```
3. Push to your repository:
   ```bash
   git push origin main
   ```

## Article Content Highlights

The article covers:

- **Definition**: What exactly constitutes an AI agent vs traditional chatbots
- **Architecture**: How modern AI agents work with perception, planning, and action cycles
- **Applications**: Real-world use cases across industries (healthcare, manufacturing, legal, etc.)
- **Future Outlook**: Trends in AI agent development through 2026 and beyond

## Troubleshooting

If you encounter any issues:
1. Check that all file paths match between the article content and your directory structure
2. Ensure image files are in the correct location with proper names
3. Verify the frontmatter in the markdown file matches your site's requirements

## Next Steps

Once images are added and pushed to GitHub, your article will be ready to publish on your magazine site!