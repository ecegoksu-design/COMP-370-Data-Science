from bs4 imort BeautifulSoup

# grep 'CEO' index.html
def main():

    with open("index.html", "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    panel = soup.select_one(".newsLineupContainer-qVPFg")

    news_elements = panel.select(".headline-s55xx") 

    for el in news_elements:
        print(el.text)

if __name__ == "__main__":
    main()