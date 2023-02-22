# reate a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
# The Pagination class will accept 2 parameters:
# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:
# alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')
# p = Pagination(alphabetList, 4)
# The Pagination class will have a few methods:
# getVisibleItems() : returns a list of items visible depending on the pageSize
# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

from typing import List

class Pagination:
    def __init__(self, items: List, pageSize: int = 10):
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = self.calculateTotalPages()

    def getVisibleItems(self) -> List:
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum: int):
        pageNum = int(pageNum)
        if pageNum <= 0:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self

    def calculateTotalPages(self):
        return (len(self.items) + self.pageSize - 1) // self.pageSize


alphabetList = "abcdefghijklmnopqrstuvwxyz".split("")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems()) # ["a", "b", "c", "d"]
p.nextPage().nextPage()
print(p.getVisibleItems()) # ["i", "j", "k", "l"]
p.lastPage()
print(p.getVisibleItems()) # ["y", "z"]
p.goToPage(10)
print(p.getVisibleItems()) # ["w", "x", "y", "z"]

