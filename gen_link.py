def link_generator(keyword, start_summa, end_summa, end_date_pub, page_number):
    return f"""
    https://zakupki.gov.ru/epz/order/extendedsearch/results.html?
    searchString={keyword}&
    morphology=on&
    pageNumber={str(page_number)}&
    sortDirection=false&
    recordsPerPage=_50&
    showLotsInfoHidden=false&
    sortBy=UPDATE_DATE&fz44=on&
    fz223=on&
    af=on&
    priceFromGeneral={start_summa}&
    priceToGeneral={end_summa}&
    currencyIdGeneral=1&
    applSubmissionCloseDateFrom={end_date_pub}
    """.replace("\n", "").replace("    ", "")
