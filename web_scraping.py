from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd


def check(driver):
    for i in [
        "[data-value_id='pathogenic_snp']",
        "[data-value_id='probable_pathogenic_snp']",
        "[data-value_id='pathogenic_likely_pathogenic']",
        "[data-value_id='risk_factor']",
        "[data-value_id='snp pubmed']",
        "[data-value_id='snp pubmed_cited']",
    ]:
        try:
            element_xpath = driver.find_element(By.CSS_SELECTOR, i)
            parent_element = element_xpath.find_element(By.XPATH, "..")
            if parent_element.get_attribute("class") != "fil_val selected":
                element_xpath.click()
        except:
            pass
    for i1 in [
        "[data-value_id='inframe_deletion']",
        "[data-value_id='inframe_indel']",
        "[data-value_id='inframe_insertion']",
        "[data-value_id='initiator_codon_variant']",
        "[data-value_id='missense_snp']",
        "[data-value_id='coding_synonymous_snp']",
    ]:
        try:
            element_xpath = driver.find_element(By.CSS_SELECTOR, i1)
            parent_element = element_xpath.find_element(By.XPATH, "..")
            if parent_element.get_attribute("class") != "fil_val selected":
                element_xpath.click()
        except:
            pass


def get_data(response):
    soup = BeautifulSoup(response, "html.parser")

    tables = soup.find_all("table", id="clinical_significance_datatable")
    # print(f"table data len = {len(tables)}")
    table_data = []
    for i1, table in enumerate(tables):
        grand_parent_table = table.parent.parent
        table_text = grand_parent_table.find_all("div", class_="sect_heading")[i1].text
        # print(table_text)
        rows = table.find_all("tr")
        headers = [header.text.strip() for header in rows[0].find_all("th")]
        for row in rows[1:]:
            cells = row.find_all("td")
            row_data = {"table_name": table_text}
            for i, header in enumerate(headers):
                row_data[header] = cells[i].text.strip()
            table_data.append(row_data)
    return table_data


# new_df = pd.DataFrame(
#     columns=["Gene", "rsId", "Clinical_Significant", "condition", "reference"]
# )
# output_file_name = "output_10_19.csv"
# all_gene_txt = "ABRAXAS1, AIP, ALK, ANKRD26, APC, ARMC5, ATM, ATR, AXIN2, BAP1, BARD1, BLM, BMPR1A, BRAF, BRCA1, BRCA2, BRIP1, BUB1B, CASR, CBL, CD70, CDC73, CDH1, CDK4, CDKN1B, CDKN1C, CDKN2A, CEBPA, CEP57, CHEK1, CHEK2, CTC1, CTNNA1, CYLD, DDB2, DDX41, DICER1, DIS3L2, DKC1, DLST, DROSHA, EFL1, EGFR, EGLN1, ELANE, EPCAM, ERCC1, ERCC2, ERCC3, ERCC4, ERCC5, ETV6, EXO1, EXT1, EXT2, EZH2, FAM111B, FAN1, FANCA, FANCB, FANCC, FANCD2, FANCE, FANCF, FANCG, FANCI, FANCL, FANCM, FH, FLCN, FOCAD, GALNT12, GATA2, GPC3, GPR101, GREM1, HAVCR2, HNF1A, HNF1B, HOXB13, HRAS, IKZF1, KIF1B, KIT, KITLG, KRAS, LZTR1, MAP2K1, MAP2K2, MAX, MC1R, MEN1, MET, MITF, MLH1, MLH3, MRE11, MRE11A, MSH2, MSH3, MSH6, MUTYH, NBN, NF1, NF2, NHP2, NOP10, NRAS, NSD1, NSUN2, NTHL1, PALB2, PALLD, PAX5, PDGFRA, PHOX2B, PIK3CA, PMS1, PMS2, POLD1, POLE, POLH, POT1, PPM1D, PRF1, PRKAR1A, PRSS1, PTCH1, PTCH2, PTEN, PTPN11, RAB43, RABL3, RAD1, RAD50, RAD51C, RAD51D, RAF1, RASA2, RB1, RECQL, RECQL4, RECQL5, REST, RET, RHBDF2, RIT1, RNF43, RPS20, RRAS, RUNX1, SAMD9, SAMD9L, SBDS, SDHA, SDHAF2, SDHB, SDHC, SDHD, SHOC2, SLX4, SMAD4, SMARCA4, SMARCB1, SMARCE1, SOS1, SOS2, SPRED1, SRP72, STK11, SUFU, TERC, TERT, TGFBR2, TINF2, TMEM127, TP53, TP53I3, TRIP13, TSC1, TSC2, TYR, VHL, WRAP53, WRN, WT1, XPA, XPC, XRCC2, XRCC3"
# all_gene_txt = "ABRAXAS1, AIP, ALK, ANKRD26, APC, ARMC5, ATM, ATR, AXIN2, BAP1, BARD1, BLM, BMPR1A, BRAF, BRCA1, BRCA2, BRIP1, BUB1B, CASR, CBL, CD70, CDC73, CDH1, CDK4, CDKN1B, CDKN1C, CDKN2A, CEBPA, CEP57, CHEK1, CHEK2, CTC1, CTNNA1, CYLD, DDB2, DDX41, DICER1, DIS3L2, DKC1, DLST, DROSHA, EFL1, EGFR, EGLN1, ELANE, EPCAM, ERCC1, ERCC2, ERCC3, ERCC4, ERCC5, ETV6, EXO1, EXT1, EXT2, EZH2, FAM111B, FAN1, FANCA, FANCB, FANCC, FANCD2, FANCE, FANCF, FANCG, FANCI, FANCL, FANCM, FH, FLCN, FOCAD, GALNT12, GATA2, GPC3, GPR101, GREM1, HAVCR2, HNF1A, HNF1B, HOXB13, HRAS, IKZF1, KIF1B, KIT, KITLG, KRAS, LZTR1"
# all_gene_list = [x.strip() for x in all_gene_txt.split(",")]
all_gene_list = ["ABRAXAS1", "AIP"]
for round in range(((len(all_gene_list) - 1) // 10) + 1):
    output_file_name = f"output_{round*10+1}_{(round+1)*10}.csv"
    new_df = pd.DataFrame(
        columns=[
            "Gene",
            "rsId",
            "Ref",
            "Alt",
            "Variant type",
            "Functional Consequence",
            "condition",
            "Clinical_Significant",
            "reference",
        ]
    )
    for gene_name in all_gene_list[round * 10 : (round + 1) * 10]:
        print(f"gene {gene_name}")
        driver = webdriver.Chrome()
        driver.get("https://www.ncbi.nlm.nih.gov/snp")
        element_xpath = driver.find_element(By.CLASS_NAME, "search_form")
        # print(element_xpath.text)
        new_element_xpath = element_xpath.find_element(By.ID, "term")
        new_element_xpath.send_keys(gene_name)
        new_element_xpath.send_keys(Keys.RETURN)
        # a = driver.find_element(By.XPATH, f'//*[@id="display_settings_menu"]/button')
        # a.check()
        a = driver.find_element(
            By.XPATH,
            f'//*[@id="EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.Display"]',
        )
        a.click()
        ps200_radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ps200"))
        )
        ps200_radio_button.click()
        check(driver=driver)
        list_rs_id = []
        try:
            a = driver.find_element(
                By.XPATH, f'//*[@id="maincontent"]/div/div[3]/div/h3'
            )
            n = int(a.text.split(":")[1].strip())
        except:
            print("error find number check case number = 1")
            n = 0
            try:
                element_xpath = driver.find_element(
                    By.XPATH,
                    f'//*[@id="maincontent"]/div/div[5]/div/div[2]/div[1]/span/a',
                )
                list_rs_id.append(element_xpath.text)
            except:
                print("error skip gene")
                new_row = {
                    "Gene": gene_name,
                    "rsId": "ERROR FIND N",
                    "Clinical_Significant": "ERROR FIND N",
                }
                df_dictionary = pd.DataFrame([new_row])
                new_df = pd.concat([new_df, df_dictionary], ignore_index=True)
                continue
        for i in range(n):
            element_xpath = driver.find_element(
                By.XPATH,
                f'//*[@id="maincontent"]/div/div[5]/div[{i+1}]/div[2]/div[1]/span/a',
            )
            list_rs_id.append(element_xpath.text)
            # <a href="/snp/rs121434642">rs121434642</a>
        print(f"list_rs_id = {list_rs_id}")
        for index, rs_id in enumerate(list_rs_id):
            check(driver=driver)
            try:
                element_xpath = driver.find_element(
                    By.CSS_SELECTOR, f'[href="/snp/{rs_id}"]'
                )
            except:
                print(f"error find {rs_id}")
                new_row = {
                    "Gene": gene_name,
                    "rsId": rs_id,
                    "Clinical_Significant": "no exist",
                }
                df_dictionary = pd.DataFrame([new_row])
                new_df = pd.concat([new_df, df_dictionary], ignore_index=True)
                continue
            # parent = element_xpath.find_element(By.XPATH, "..")
            # grand_parent = parent.find_element(By.XPATH, "..")
            element_xpath_type = driver.find_element(
                By.XPATH,
                f'//*[@id="maincontent"]/div/div[5]/div[{index+1}]/div[2]/div[1]/dl/dd[1]',
            )
            variant_type = element_xpath_type.text
            element_xpath_alleles = driver.find_element(
                By.XPATH,
                f'//*[@id="maincontent"]/div/div[5]/div[{index+1}]/div[2]/div[1]/dl/dd[2]/span[1]',
            )
            alleles = element_xpath_alleles.text
            element_xpath_functional_consequence = driver.find_element(
                By.XPATH,
                f'//*[@id="maincontent"]/div/div[5]/div[{index+1}]/div[2]/div[1]/dl/dd[6]',
            )
            functional_consequence = element_xpath_functional_consequence.text
            element_xpath.click()
            element_xpath = driver.find_element(By.XPATH, f'//*[@id="label_id_second"]')
            element_xpath.click()
            should_have_tabel_list = []
            have_table = []
            alleles_list_split = alleles.split(">")
            if len(alleles_list_split) > 1 and (
                variant_type == "SNV" or variant_type == "MNV"
            ):
                consider = alleles_list_split[1]
                for x in consider.split(","):
                    should_have_tabel_list.append(x.strip())
            for data in get_data(driver.page_source):
                table_name = data["table_name"].split()[1]
                if "dup" in table_name:
                    ref = "duplication"
                    alt = table_name[3:]
                elif "del" in table_name:
                    ref = "deletion"
                    alt = table_name[3:]
                elif "ins" in table_name:
                    ref = "Insertion"
                    alt = table_name[3:]
                else:
                    ref = alleles_list_split[0]
                    alt = table_name
                    if alt not in have_table:
                        have_table.append(alt)
                new_row = {
                    "Gene": gene_name,
                    "rsId": rs_id,
                    "Ref": ref,
                    "Alt": alt,
                    "Variant type": variant_type,
                    "Functional Consequence": functional_consequence,
                    "condition": data["Clinical Significance"],
                    "Clinical_Significant": data["Disease Names"],
                    "reference": f'https://www.ncbi.nlm.nih.gov/clinvar/{data["ClinVar Accession"]}/',
                }
                df_dictionary = pd.DataFrame([new_row])
                new_df = pd.concat([new_df, df_dictionary], ignore_index=True)
            if not len(should_have_tabel_list) == len(have_table):
                for table_name2 in should_have_tabel_list:
                    if table_name2 not in have_table:
                        new_row = {
                            "Gene": gene_name,
                            "rsId": rs_id,
                            "Ref": alleles_list_split[0],
                            "Alt": table_name2,
                            "Variant type": variant_type,
                            "Functional Consequence": functional_consequence,
                            "condition": "NOT report",
                            "Clinical_Significant": "NOT report",
                            "reference": "NOT report",
                        }
                        df_dictionary = pd.DataFrame([new_row])
                        new_df = pd.concat([new_df, df_dictionary], ignore_index=True)
            driver.back()
            driver.back()
        driver.close()
    new_df.to_csv(output_file_name, index=False)
