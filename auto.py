#I51/JPascual
import os
import base64
import ctypes
import time
from datetime import datetime, timedelta
import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError

def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def cmd(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def detect_captcha(page):
    captcha_keywords = {'captcha', 'CAPTCHA', 'sendo exibido?'}
    body_text = page.query_selector('body').text_content()
    return any(keyword in body_text for keyword in captcha_keywords)

def click_if_visible(page, selectors):
    accept_texts = ["Accept", "I Accept", "Agree", "Save and Close", "Accept additional cookies", "Dismiss", "Yes, these cookies are OK", "Prosseguir", "Accept all cookies", "I understand and I accept the use of cookies", "Accept all", "Aceptar", "Aceptar y continuar", "Accept All Cookies", "Hide this message"]
    for selector in selectors:
        for text in accept_texts:
            elements = page.query_selector_all(selector)
            for element in elements:
                if element.is_visible():
                    element_text = element.evaluate('(el) => el.textContent')
                    if element_text and text in element_text:
                        element.click()
                        return True
    return False

def remove_elements(page):
    selectors_to_remove = ['header',
                           '#header',
                           '.header',
                           '#fixed-top-bar',
                           'body > header',
                           'body > div.o-wrapper--page > header',
                           '#page-header',
                           '#header_refresh',
                           'footer',
                           '.footer',
                           '#footer',
                           '#footerNav',
                           'body > footer',
                           'body > div.o-wrapper--page > footer'
                          ]

    for selector in selectors_to_remove:
        elements = page.query_selector_all(selector)
        if elements:
            for element in elements:
                element.evaluate('(element) => element.remove()')

cmd(decode_base64("STUxIFNjcmlwdA=="))
stringCol = '\033[94m'; print(stringCol + decode_base64("CiAgICAgICAgICAgICAgICAgICAgICAkJFwgICAgICAgICAgICAgICAgICAgJCRJNTEkXCAgICQkSTUxJFwgIAogICAgICAgICAgICAgICAgICAgICAgJCQgfCAgICAgICAgICAgICAgICAgJCQgIF9fJCRcICQkICBfXyQkXCAKICRJNTEkJFwgICQkXCAgICQkXCAkSTUxJCRcICAgICRJNTEkJFwgICAgICQkIC8gIFxfX3wkJCAvICBcX198CiBcX19fXyQkXCAkJCB8ICAkJCB8XF8kJCAgX3wgICQkICBfXyQkXCAgICBcJEk1MSQkXCAgXCRJNTEkJFwgIAogJCQkJCQkJCB8JCQgfCAgJCQgfCAgJCQgfCAgICAkJCAvICAkJCB8ICAgIFxfX19fJCRcICBcX19fXyQkXCAKJCQgIF9fJCQgfCQkIHwgICQkIHwgICQkIHwkJFwgJCQgfCAgJCQgfCAgICQkXCAgICQkIHwkJFwgICAkJCB8ClwkSTUxJCQkIHxcJEk1MSQkICB8ICBcJCQkJCAgfFwkSTUxJCQgIHwkJFxcJCRJNTEkICB8XCQkSTUxJCAgfAogXF9fX19fX198IFxfX19fX18vICAgIFxfX19fLyAgXF9fX19fXy8gXF9ffFxfX19fX18vICBcX19fX19fLyAKCiAgICAgICAgICAgICAgICAgWyAwMTAwMTAwMSAwMDExMDEwMSAwMDExMDAwMSBdCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAK"))

#USER SETTINGS
cycle = 1800 #INTERVAL PER BATCH (1800 = 30MINS || 3200 = 1HR)
interval = 4 #INTERVAL FOR EACH URL

def capture_full_page_screenshot(context, url, row_id, folder, extension):
    page = context.new_page()
    page.goto(url, timeout=120000)
    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        try:
            time.sleep(interval)
            remove_elements(page) #REMOVE HEADER AND FOOTER OF THE PAGE
            selectors = [
                'button',
                'button[type="button"]',
                'a[text="Accept"]',
                'button.accept-cookies',  
                'button#accept-cookies',      
                'button[data-cookie="accept"]',  
                'button[aria-label="Accept Cookies"]'  
            ] 
            click_if_visible(page, selectors)
            
            # CUSTOM NAVIGATION BEFORE CAPTURING OF SCREENSHOT START #

            locators = [
                '#main > div > div:nth-child(1) > div > div > div > div > div.main-col > ul > li:nth-child(1) > a',  #legifrance.fov
                '#filtros > div:nth-child(1) > label',  # boe.es
                '#filtros > div:nth-child(1) > ul > li:nth-child(2) > a',  # boe.es
                'body > div.container > div.contenido > div:nth-child(1) > div.col-xs-12.col-md-8 > div > form > div:nth-child(2) > button' #bcra.gob
            ]

            for locator in locators:
                if page.locator(locator).is_visible():
                    page.locator(locator).click()

            
            # CUSTOM NAVIGATION BEFORE CAPTURING OF SCREENSHOT END #

            page.wait_for_load_state('networkidle')

            if detect_captcha(page):
                print(f"\033[91mCAPTCHA detected! Please perform a manual capture of the screenshot for row ID: {row_id:04}...\033[0m\n")
                break

            timestamp = datetime.now().strftime("Date: %m-%d-%Y || Time: %I:%M:%S %p")
            header_content = f'<div style="position: absolute; top: 0; left: 0; width: 100%; font-weight: bold !important; background-color: black; padding: 10px; z-index: 9999999999; color: white;">{timestamp} || row ID: {row_id:04} || URL: {url}</div>'
            page.evaluate('(headerContent) => { document.body.innerHTML = `${headerContent}${document.body.innerHTML}`; }', header_content)

            folder_path = os.path.join(os.getcwd(), str(folder))
            os.makedirs(folder_path, exist_ok=True)

            if pd.notna(extension) and isinstance(extension, str) and extension.strip():
                filename = f"{row_id:04}_{datetime.now().strftime('%m%d%Y_%H%M')}_{extension}.png"
            else:
                filename = f"{row_id:04}_{datetime.now().strftime('%m%d%Y_%H%M')}.png"

            screenshot_path = os.path.join(folder_path, filename)
            page.screenshot(path=screenshot_path, full_page=True)

            cmdTimestamp = datetime.now().strftime("%I:%M:%S %p")
            print(f"\033[92mScreenshot of row ID {row_id:04} taken at {cmdTimestamp} has been saved.\033[0m\n")
            break

        except Exception as e:
            print(f"\033[91mError capturing screenshot for row ID {row_id:04}: {e}. Attempt {attempt} of {max_attempts}\033[0m")
            attempt += 1
            page.reload()

        except TimeoutError:
            print(f"Timeout exceeded while navigating to row ID: {row_id:04}.")
            attempt += 1
            page.reload()

        except playwright._impl._errors.Error as e:
            if "net::ERR_TIMED_OUT" in str(e):
                print(f"Timeout error occurred. Retrying... (Attempt {attempt} of {max_attempts})")
                attempt += 1
            else:
                print(f"Unexpected error occurred: {e}")
                break

        
    if attempt > max_attempts:
        print(f"\033[91mSkipping URL {url} after {max_attempts} attempts. Moving to next URL.\033[0m")

    if not page.is_closed():
        page.close()
    else:
        print(f"Page for row ID {row_id:04} is closed. It may have been reloaded or closed.")             

def process_excel_data(file_path):
    df = pd.read_excel(file_path)
    with sync_playwright() as p:

        browser = p.chromium.launch_persistent_context (
            user_data_dir="user_dir",
            headless=False,
            accept_downloads=True
        )

        for index, row in df.iterrows():
            url = row['URL']
            row_id = f"{row['Name']:04}"
            folder = f"{row['Folder']:04}".replace(" ", "")
            extension = row['Extension']

            capture_full_page_screenshot(browser, url, row_id, folder, extension)
        browser.close()

def main():
    excel_file_path = "agents.xlsx"
    try:
        cycle_count = 0

        while True:
            cycle_count += 1
            print(f"\n\033[91m[ Starting cycle #{cycle_count} ]")
            process_excel_data(excel_file_path)
            time.sleep(cycle)
    except KeyboardInterrupt:
        print("Script interrupted. Closing browser...")
    finally:
        time.sleep(1)
        print("Exiting...")

if __name__ == "__main__":
    main()
