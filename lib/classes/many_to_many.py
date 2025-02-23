class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

        @property
        def title(self):
            return self.title

        @title.setter
        def title(self,value):
            if isinstance(value,str) and 5 <= len(value) <= 50:
              self.title = value

            else:
                return self.title

        @property
        def author(self):
            return self.author

        @author.setter
        def author(self,author):
            if not isinstance(author,Author):
                raise Exception
                self.author = author
        
class Author:
    def __init__(self, name):
        self.name = name
        if not isinstance(name,str) or name == 0:
            raise ValueError("Author must be an empty string")
    
        @property # used the property to set the name to str and length
        def name(self):
            return self.name

        @name.setter
        def name(self,value):
            if not isinstance(value,str) or len(value) == 0:
                return 
            if self.name != value:
                return

        def articles(self):
            result = []
            for article in Article.all:
                if article.author == self: 
                    result.append(article)
            return result

        def magazines(self):
            unique_magazines = set()
            for article in self.articles(): # loop to return unique articles
                unique_magazines.add(article.magazine) # add magazine which is unique
            return list(unique_magazines)
        
        def add_article(self,magazine,title):
            pass
                




    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,value):
            if isinstance(value,str) and 2 <= len(value) <= 16: 
                self.name = value

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self,value):
                if isinstance(value,str) and len(value) > 0:
                    self.category = value

                

    


    def articles(self):
        result = []
            for article in Article.all:
                if article.magazine == self: 
                    result.append(article)
            return result

    def contributors(self):
        unique_contributors = set()
            for article in self.articles(): # loop to return unique articles
                unique_contributors.add(article.author) # add magazine which is unique
            return list(unique_contributors)

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass