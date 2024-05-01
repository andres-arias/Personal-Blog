import datetime
from pathlib import Path

if __name__ == "__main__":
    title: str = input("Article title: ")
    today_date = datetime.date.today()
    article_name = f"{today_date}-{title.lower().replace(' ', '-')}.md"
    category: str = input("Article category: ")
    tags: list = input("Article tags (comma-separated): ").replace(" ", "").split(",")
    front_matter: str = "---\n"\
            f"title: {title}\n"\
            f"date: {today_date}\n"\
            f"category: {category}\n"\
            f"tags: {tags}\n".replace("'", "") +\
            "---\n\n"

    article_path = Path(f"./content/{article_name}")
    if article_path.exists():
        raise FileExistsError(f"File named '{article_name}' already exists!")
    with open(article_path, "w+") as file:
        file.write(front_matter)
    print(f"Article '{article_name}' successfully created!")
