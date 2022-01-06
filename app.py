from Tokopedia import TokopediaScrape


if __name__ == '__main__':
    ts = TokopediaScrape(keyword = 'laptop asus', sort=2, totalPages=1, stars4=False, offStore=False, merchantPro=False, merchant=False, minPrice=None, maxPrice=None)
    data = ts.run()
    ts.to_excel(data)
