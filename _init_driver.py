import time, os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def coop(driver: webdriver):
    # stora_coop_sodertalje_url = "https://www.coop.se/butiker-erbjudanden/stora-coop/stora-coop-sodertalje/"
    # coop_sodertalje_c_url = "https://www.coop.se/butiker-erbjudanden/coop/coop-sodertalje-c/"

    stora_coop_sodertalje_url = "https://dr.coop.se/Butik/?store=250800"
    coop_sodertalje_c_url = "https://dr.coop.se/Butik/?store=016140"

    the_coops = [stora_coop_sodertalje_url, coop_sodertalje_c_url]
    cookieAccepted = True
    
    for coop_url in the_coops:
        driver.get(coop_url)
        
        # # Accept cookies
        # if not cookieAccepted:
        #     ac_btn_xpath = '//*[@id="cmpwelcomebtnyes"]/a'
        #     driver.find_element(By.XPATH, ac_btn_xpath).click()
        #     cookieAccepted = True

        # # Flyer button click
        # flyer_btn_xpath = '//*[@id="reactMicroApp"]/div[2]/div[1]/div/div/div[2]/div[2]/button[1]'
        # driver.find_element(By.XPATH, flyer_btn_xpath).click()

        time.sleep(2)


def hemkop(driver: webdriver):
    pdf_url = "https://hemkop.eo.se/hkp/4640.pdf"
    driver.get(pdf_url)
    time.sleep(5)


def ica(driver: webdriver):
    ica_maxi_vasa = "https://www.e-magin.se/latestpaper/68j2dh4h/paper"
    ica_supermarket_kringlan = "https://www.e-magin.se/latestpaper/p5d63fb8/paper"
    the_icas = (ica_maxi_vasa, ica_supermarket_kringlan)

    for ica in the_icas:
        driver.get(ica)
        time.sleep(2)
        # scroll_out(driver)

        # # Cookie handler button
        # ach_btn_btn = '//*[@id="onetrust-accept-btn-handler"]'
        # driver.find_element(By.XPATH, ach_btn_btn).click()
        # time.sleep(2)

        # # Flyer button url extraction
        # ads_btn_xpath = '/html/body/div[1]/section/div[2]/div/div[5]/div[1]/div[2]/a'
        # ads_btn = driver.find_element(By.XPATH, ads_btn_xpath)
        # ads_btn.click()
        # ads_btn.location_once_scrolled_into_view
        # flyer_url = ads_btn.get_attribute("href")
        # driver.get(flyer_url)
        # time.sleep(2)

        # Download PDF
        pdf_btn_xpath = '//*[@id="toolbarContainer"]/div[3]/div/button[3]/div[1]'
        driver.find_element(By.XPATH, pdf_btn_xpath).click()

        time.sleep(2)


def lidl(driver: webdriver):
    lidl_weda_url = "https://www.lidl.se/s/sv-SE/butiker/soedertaelje/bergaholmsvaegen-7/"
    driver.get(lidl_weda_url)

    ac_handler_btn_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    driver.find_element(By.XPATH, ac_handler_btn_xpath).click()

    flyer_btn_xpath = "/html/body/div/main/div/aside/div/ol/li/div/ol/li[1]"
    driver.find_element(By.XPATH, flyer_btn_xpath).click()

    pdf_dl_xpath = '//*[@id="targetbe7864da-6d56-11e8-8e93-005056ab0fb6"]/div[1]/div/a'
    pdf_url = driver.find_element(By.XPATH, pdf_dl_xpath).get_attribute("href")

    driver.get(pdf_url)
    time.sleep(20)


def oob(driver: webdriver):
    url = "https://ipaper.ipapercms.dk/oob/"
    driver.get(url)

    dl_btn_xpath = '//*[@id="modDownloadPdfBtn"]/div'
    driver.find_element(By.XPATH, dl_btn_xpath).click()

    time.sleep(2)


def rusta(driver: webdriver):
    rusta_url = "https://view.publitas.com/rusta-bladet"
    driver.get(rusta_url)

    dl_pdf_xpath = '//*[@id="downloadAsPdf"]'
    driver.find_element(By.XPATH, dl_pdf_xpath).click()

    time.sleep(2)


def snabbgross(driver: webdriver):
    snabbgross_sodertalje_url = "https://www.snabbgross.se/butik/6029"
    driver.get(snabbgross_sodertalje_url)

    ac_handler_xpath = '//*[@id="onetrust-accept-btn-handler"]'
    driver.find_element(By.XPATH, ac_handler_xpath).click()

    age_confirm_xpath = '//*[@id="agree"]'
    driver.find_element(By.XPATH, age_confirm_xpath).click()

    try:
        campaign_store_xpath = '//*[@id="currentCampaignRefresh"]/div/div[3]/div'
    except:
        print("Second campaign element seems not to exist")
    else:
        campaign_store_xpath = '//*[@id="currentCampaignRefresh"]/div/div[2]/div'
    
    driver.find_element(By.XPATH, campaign_store_xpath).click()

    time.sleep(3)


def willys(driver: webdriver):
    willys_url = "https://viewer.ipaper.io/willys/2284/"
    driver.get(willys_url)

    pdf_dl_xpath = '//*[@id="modDownloadPdfBtn"]'
    driver.find_element(By.XPATH, pdf_dl_xpath).click()

    time.sleep(5)


def scroll_out(driver: webdriver):
    win = driver.find_element(By.TAG_NAME, "html")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")


today = datetime.date.today()
this_week = today.isocalendar().week

project_path = os.path.dirname(os.path.abspath(__file__))

download_dir = "pdfs"
download_path = os.path.join(project_path, download_dir)
if not os.path.exists(download_path):
    os.mkdir(download_path)

download_year_path = os.path.join(download_path, str(today.year))
if not os.path.exists(download_year_path):
    os.mkdir(download_year_path)

download_week_path = os.path.join(download_year_path, str(this_week))
if not os.path.exists(download_week_path):
    os.mkdir(download_week_path)

profile = {
    'download.prompt_for_download': False,
    'download.default_directory': download_week_path,
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
}

prefs = {"download.default_directory":download_week_path}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('prefs', profile)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(0.5)
driver.execute_script("document.body.style.zoom='50%'")

scroll_out(driver)
