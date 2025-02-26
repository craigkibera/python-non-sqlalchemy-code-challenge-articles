class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)


    @property # used the property to set the title to str and length
    def title(self):
        return self._title

    @title.setter  # used to set the conditions needed
    def title(self, title):
        def is_valid_title(title):
            return isinstance(title, str) and 5 <= len(title) <= 50
        
        if title != self._title and is_valid_title(title):
            self._title = title
        
        else:
            return self._title


     


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        Author.all.append(self)
        self.author_articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            return
        if self._name != value:
            return

    def articles(self):
        result = []
        for article in Article.all:
            if article.author == self:
                result.append(article)
        return result

    def magazines(self):
       unique_magazines = set()
       for article in self.articles():
           unique_magazines.add(article.magazine)
       return list(unique_magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception
        self.author_articles.append(magazine)
        return Article(self, magazine, title)

    def topic_areas(self):
        if [magazine.category for magazine in self.author_articles] == []:
            return None
        category_set = set([magazine.category for magazine in self.author_articles])
        return list(category_set)

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        result = []
        for article in Article.all:
            if article.magazine == self:
                result.append(article)
        return result

    def contributors(self):
        unique_contributors = set()
        for article in self.articles():
            unique_contributors.add(article.author)
        return list(unique_contributors)

    def article_titles(self):
        if [article.title for article in self.articles()] == []:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if len([article.author for article in self.articles()]) <= 2:
            return None
        return [article.author for article in self.articles()]