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

class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalPages = max(1, len(items) // self.pageSize + (1 if len(items) % self.pageSize != 0 else 0))
        self.currentPage = 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

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

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems())
p.firstPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.goToPage(3)
print(p.getVisibleItems())
p.goToPage(10)
print(p.getVisibleItems())
p.goToPage(0)
print(p.currentPage)
p.goToPage(-3)
print(p.currentPage)
