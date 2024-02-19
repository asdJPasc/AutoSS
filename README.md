
# Automatic Full-Page Screenshot Capturer

This script automates the task of capturing full-page screenshots of multiple web pages listed in an Excel file. It utilizes the power of Python and the Playwright library to navigate through websites, remove unwanted elements, and capture comprehensive screenshots, providing users with a visual snapshot of each webpage.


## Features

- Effortless Automation: Say goodbye to manual screenshot capturing. The script handles everything automatically, saving you time and effort.
- Customizable Configuration: Easily customize the interval between screenshot captures, ensuring flexibility to meet specific needs.
- Dynamic Element Removal: Unwanted elements like headers, footers, or pop-ups are automatically removed before capturing screenshots, ensuring clean and focused images.
- Captcha Detection: The script intelligently detects and skips web pages with CAPTCHA challenges, preventing interruptions in the automation process.
- Persistent Browser Context: With a persistent browser context, the script efficiently manages resources, optimizing performance and reliability.
- Interrupt Handling: The script gracefully handles interruptions such as keyboard interrupts, ensuring a smooth exit while maintaining browser integrity.
- Easy Setup: Simply provide the URLs in an Excel file, specify the capture settings, and let the script do the rest.


## Ideal Use Cases:
- Monitoring website changes for competitive analysis.

- Tracking online content for compliance or regulatory purposes.

- Collecting visual data for research or trend analysis.

- Automating periodic website snapshots for archival or historical records.

## Current Limitation and Ongoing Development:
- Captcha Puzzle Handling: The script currently lacks the capability to bypass captcha puzzles automatically. Development is ongoing to implement captcha solving mechanisms.

- Partial Website Configuration: Not all websites listed in the Excel file may be fully configured to navigate and capture screenshots seamlessly. Additional configuration may be required for specific websites to handle unique elements or interactions effectively.

These limitations are being actively addressed by the developer to enhance the script's functionality and user experience. Your feedback and suggestions are invaluable in driving future improvements.
## Usage/Examples
1. Create a new folder on your desktop called "autoss".
2. Download auto.py (the Python script) and agents.xlsx (the Excel file with URLs).
3. Move both downloaded files into the "autoss" folder.
4. Run Script:

For Windows 10, navigate to the 'autoss' folder and press and hold the Shift key, then right-click anywhere inside the folder. In the context menu that appears, select 'Open command window here'.

![App Screenshot](https://www.groovypost.com/wp-content/uploads/2018/11/02-Open-command-window-here-option-added.png)

For Windows 11, navigate to the 'autoss' folder, right-click anywhere inside the folder, and choose 'Open in Windows Terminal' from the context menu.

![App Screenshot](https://allthings.how/content/images/wordpress/2021/11/allthings.how-how-to-open-command-prompt-window-inside-a-directory-on-windows-11-image-8.png)

Once open type auto.py and press Enter to run the script.
```bash
Microsoft Windows [Version 10.0.22631.3155]
(c) Microsoft Corporation. All rights reserved.

C:\Users\whoAmI\OneDrive\Desktop\autoss>auto.py
```

5. Monitor Progress:

- The script will start capturing screenshots automatically.
Sit back and let it run. It will capture screenshots at set intervals.
Review Screenshots:

- Once done, find the screenshots in the "autoss" folder.
Open the folder to view the captured screenshots.

## Requirements:
- Python 3.x

- Playwright library (pip install playwright)

- Excel file containing URLs (Agents.xlsx)


## Author

- [@asdJPasc / I51](https://github.com/asdJPasc)

