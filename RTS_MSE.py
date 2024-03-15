# MSEdge
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Target URL
url_MSE = "https://test-zbgis2023.skgeodesy.sk/rts-next/sk/transform"

# Input Variables
Y_coordinate_MSE = "-530212.396"
X_coordinate_MSE = "-1329074.630"

# Webdriver initialization
driver = webdriver.Edge()
driver.get(url_MSE)
driver.maximize_window()
sleep(2)

#ActionChains(self.driver).send_keys(Keys.ENTER).perform()

# Click on "insert_format"
insert_format_selector_MSE = "#mat-select-value-1"
insert_format_MSE = driver.find_element(By.CSS_SELECTOR, insert_format_selector_MSE)
insert_format_MSE.click()
sleep(0.5)

# Click on "transformacia_bodu_jednotlivo"
TBJ_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
TBJ_MSE = driver.find_element(By.XPATH, TBJ_selector_MSE)
TBJ_MSE.click()
sleep(0.5)

# Click on "INPUT_CRS"
input_CRS_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[2]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
input_CRS_MSE = driver.find_element(By.XPATH, input_CRS_selector_MSE)
input_CRS_MSE.click()
sleep(0.5)

# Click on "INPUT_SJTSK-JTSK"
input_SJTSK_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[2]/span"
input_SJTSK_MSE = driver.find_element(By.XPATH, input_SJTSK_selector_MSE)
input_SJTSK_MSE.click()
sleep(0.5)

# Click on "OUTPUT_CRS"
output_CRS_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[3]/mat-form-field[1]/div[1]/div/div[2]/mat-select/div/div[1]/span"
output_CRS_MSE = driver.find_element(By.XPATH, output_CRS_selector_MSE)
output_CRS_MSE.click()
sleep(0.5)

# Click on "OUTPUT_Bessel_JTSK"
output_Bessel_JTSK_selector_MSE = "/html/body/div[2]/div[2]/div/div/mat-option[3]/span"
output_Bessel_JTSK_MSE = driver.find_element(By.XPATH, output_Bessel_JTSK_selector_MSE)
output_Bessel_JTSK_MSE.click()
sleep(0.5)

# Click on "INPUT_Y_coordinates"
#input_Y_coordinates_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
#input_Y_coordinates_MSE = driver.find_element(By.XPATH, input_Y_coordinates_selector_MSE)
#input_Y_coordinates_MSE.click()
#sleep(0.5)

# Y_coordinate_variable
Y_coordinate_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[5]/mat-form-field/div[1]/div/div[2]/input"
Y_coordinate_MSE_field = driver.find_element(By.XPATH, Y_coordinate_MSE_selector)
Y_coordinate_MSE_field.send_keys(Y_coordinate_MSE)
sleep(0.5)

# Click on "INPUT_X_coordinates"
#input_X_coordinates_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
#input_X_coordinates_MSE = driver.find_element(By.XPATH, input_X_coordinates_selector_MSE)
#input_X_coordinates_MSE.click()
#sleep(0.5)

# X_coordinate_variable
X_coordinate_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
X_coordinate_MSE_field = driver.find_element(By.XPATH, X_coordinate_MSE_selector)
X_coordinate_MSE_field.send_keys(X_coordinate_MSE)
sleep(0.5)

# option 1 # Click on "transform" - NEFUNGUJE
#transform_selector_MSE = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[7]/div/button[2]/span[2]"
#transform_MSE = driver.find_element(By.XPATH, transform_selector_MSE)
#transform_MSE.click()
#sleep(10)

# option 2 # Hit Enter - FUNGUJE
transform_MSE_selector = "/html/body/app-layout/mat-drawer-container/mat-drawer-content/app-transform/app-dropzone/div[1]/form/div[6]/mat-form-field/div[1]/div/div[2]/input"
transform_MSE = driver.find_element(By.XPATH, transform_MSE_selector)
transform_MSE.send_keys(Keys.ENTER)
sleep(5)

print("Successfully transformed in Microsoft Edge browser")

driver.quit()
