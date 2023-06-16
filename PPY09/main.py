import wikipedia

def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def get_article(title):
    w_api = wikipedia.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""

def calculate_average_letter_count(articles_generator):
    total_letter_count = 0
    article_count = 0
    for title in articles_generator:
        article = get_article(title)
        letter_count = len(set(article.lower()))
        total_letter_count += letter_count
        article_count += 1
    if article_count > 0:
        average_letter_count = total_letter_count / article_count
        return average_letter_count
    else:
        return 0

title_generator = read_titles("small.txt")
average_letter_count = calculate_average_letter_count(title_generator)
print("Average letter count per article:", average_letter_count)
