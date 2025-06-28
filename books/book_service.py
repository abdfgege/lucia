class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("책이 추가되었습니다. ")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remov(book)
                print("책이 삭제되었습니다. ")
                return
        print("✅ 책이 추가되었습니다.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("🔍 책을 찾았습니다:")
                print(book)
                return
        print("❌ 해당 책이 없습니다.")

    def list_books(self):
        if not self.books:
            print("📚 등록된 책이 없습니다.")
        else:
            print("📚 도서 목록:")
            for book in self.books:
                print(book)


def main():
    lib = Library()

    while True:
        print("\n📘 도서관 관리 프로그램")
        print("1. 책 추가")
        print("2. 책 삭제")
        print("3. 책 검색")
        print("4. 책 목록 보기")
        print("5. 종료")

        choice = input("원하는 작업을 선택하세요 (1-5): ")

        if choice == '1':
            title = input("책 제목: ")
            author = input("책 저자: ")
            lib.add_book(title, author)

        elif choice == '2':
            title = input("삭제할 책 제목: ")
            lib.remove_book(title)

        elif choice == '3':
           title = input("검색할 책 제목: ")
           lib.search_book(title)

        elif choice == '4':
            lib.list_books()

        elif choice == '5':
            print("👋 프로그램을 종료합니다.")
            break
        
        else:
            print("❗ 유효하지 않은 입력입니다. 1~5 중 선택해주세요.")
