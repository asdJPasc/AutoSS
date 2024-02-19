import os
import base64
import ctypes
import time
from datetime import datetime, timedelta
import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError

def get_screen_size():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return width, height

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

def click_if_visible(page, selector):
    if page.locator(selector).is_visible():
        page.locator(selector).click()
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
cycle = 600 #INTERVAL PER BATCH (1800 = 30MINS || 3200 = 1HR)
interval = 3 #INTERVAL FOR EACH URL

def capture_full_page_screenshot(context, url, row_id, folder, extension):
    page = context.new_page()
    page.goto(url, timeout=60000)
    max_attempts = 3
    attempt = 1

    while attempt <= max_attempts:
        try:
            time.sleep(interval)
            remove_elements(page)
            # CUSTOM NAVIGATION BEFORE CAPTURING OF SCREENSHOT START #
            
            if click_if_visible(page, 'div.initial:nth-child(3) > a:nth-child(1)'): #BANKINGSUPERVISION.EUROPA
                pass
            elif click_if_visible(page, 'a[alt="year/2024"]'): #rowid 219
                pass
            elif click_if_visible(page, 'button.cky-btn-accept:nth-child(2)'): #M-X.CA
                pass
            elif click_if_visible(page, '#ccc-recommended-settings > span:nth-child(1)'): #PSR.GOV
                pass
            elif click_if_visible(page, '#close'): #SFO.GOV.UK
                pass
            elif click_if_visible(page, 'body > div.animated.fadeIn.position-relative.ng-scope > div > div:nth-child(3) > div.col-lg-3 > div.card.mb-4 > div.card-body > div:nth-child(6) > label'): #BOLSA SANTIAGO CIRCULARES
                pass
            elif click_if_visible(page, '//*[@id="main"]/div/div[1]/div/div/div/div/div[1]/ul/li[1]/a'): #JORF WEBSITE 
                pass
            elif click_if_visible(page, '#filtros > div:nth-child(1) > label'): #BOE.es WEBSITE  
                pass
            elif click_if_visible(page, '//*[@id="cn-accept-cookie"]'): #Takeoverpanel WEBSITE
                pass
            elif click_if_visible(page, '#onetrust-accept-btn-handler'): #IRISHISTATUTEBOOK WEBSITE
                pass
            elif click_if_visible(page, '#popup-buttons > button.agree-button.eu-cookie-compliance-secondary-button.button.button--small'): #BANREP WEBSITE
                pass
            elif click_if_visible(page, 'body > app-root > bcb-cookies > div > div > div > div > button.btn.btn-primary.btn-accept'): #BCB.GOV WEBSITE
                pass
            elif click_if_visible(page, '#cookie-consent-banner > div > div > div.cck-actions.wt-noconflict > a.wt-link.wt-ecl-button.wt-ecl-button--primary.cck-actions-button.ea_ignore'): #EUR.LEX WEBSITE
                pass
            elif click_if_visible(page, '.wt-ecl-button__label'):
                pass
            elif click_if_visible(page, '#content > div.home-articles.news-wrap > div > div.all-news-link-wrap > button'):
                pass
            elif click_if_visible(page, 'text=Prosseguir'):
                pass  
            
            # CUSTOM NAVIGATION BEFORE CAPTURING OF SCREENSHOT END #

            page.wait_for_load_state('networkidle')

            if detect_captcha(page):
                print(f"\033[91mCAPTCHA detected! Skipping URL of row ID: {row_id:04}...\033[0m\n")
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
        
    if attempt > max_attempts:
        print(f"\033[91mSkipping URL {url} after {max_attempts} attempts. Moving to next URL.\033[0m")

    if not page.is_closed():
        page.close()
    else:
        print(f"Page for row ID {row_id:04} is closed. It may have been reloaded or closed.")             

def process_excel_data(file_path):
    df = pd.read_excel(file_path)

    with sync_playwright() as p:

        width, height = get_screen_size()
        browser = p.chromium.launch_persistent_context (
            user_data_dir="user_data",
            headless=True,
            accept_downloads=True,
            viewport={"width": width, "height": height}
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
