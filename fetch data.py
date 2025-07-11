import requests
from bs4 import BeautifulSoup as BS


def main():
    """
    Main function to scrape laptops across multiple price ranges and save results.
    Scrapes laptops in price increments of 5,000,000 Toman across 26 ranges.
    """
    final_dict = {}
    
    # Scrape laptops across multiple price ranges
    for i in range(26):
        min_price = 14_000_000 + i * 5_000_000
        max_price = 20_000_000 + i * 5_000_000
        temp = get_laptop_dict(min_price, max_price)
        print(temp)  # Display progress
        final_dict.update(temp)
    
    # Save final results to file
    save_file(final_dict)


def get_laptop_dict(minprice, maxprice):
    """
    Scrape laptop data from Zoomit.ir for a specific price range.
    
    Args:
        minprice (int): Minimum price in Toman
        maxprice (int): Maximum price in Toman
        
    Returns:
        dict: Dictionary of laptops with specs and prices (converted to USD)
    """
    # Fetch HTML content
    url = f"https://www.zoomit.ir/product/list/laptop/?minPrice={minprice}&maxPrice={maxprice}&onlyInStock=true"
    html = requests.get(url).text
    soup = BS(html, 'html5lib')
    
    # Extract laptop names and specifications
    name = []
    spec = []
    name_text_list = soup.find_all(class_="sc-68673876-0 rmiQX sc-ad0a6d77-1 cjHLzn")
    for word in name_text_list:
        name.append(word.get_text().split(" - ")[0])
        spec.append(word.get_text().split(" - ")[1])
    
    # Extract and convert prices (Toman to USD)
    price = []
    price_text_list = soup.find_all(class_="sc-68673876-0 eouUcl fa")
    for word in price_text_list:
        price_toman = int(word.get_text().replace(",", ""))
        price_dollar = int(price_toman / 88000)  # Conversion rate to USD
        price.append(price_dollar)
    
    # Create dictionary of results
    result = {}
    for i in range(len(name)):
        result[name[i]] = [spec[i], price[i]]
    
    return result


def save_file(mydict):
    """
    Save dictionary data to a text file.
    
    Args:
        mydict (dict): Dictionary containing laptop data
    """
    with open('fetch_data.txt', 'w', encoding="utf-8") as data:
        data.write(str(mydict))


if __name__ == "__main__":
    main()
