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
        self.books.append(Book(title, author))
        print("✅ 책이 추가되었습니다.")

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]
        print("책이 삭제되었습니다. ")

    def search_book(self, title):
        for b in self.books:
            if b.title == title:
                print("🔍 책을 찾았습니다:", b)
                return b
        print("❌ 해당 책이 없습니다.")
        return None

    def list_books(self):
        if not self.books:
            print("📚 등록된 책이 없습니다.")
        for b in self.books:
            print(b)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthLibrary(Library):
    def __init__(self):
        super().__init__()
        self.users = []

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def register_user(self, username, password):
        if self.find_user(username):
            return False
        self.users.append(User(username, password))
        return True

    def login(self, username, password):
        user = self.find_user(username)
        if user and user.password == password:
            return True
        else:
            return False

def main():
    lib = AuthLibrary()
    current_user = None

    while not current_user:
        print("\n1. 로그인  2. 회원가입  3. 종료")
        cmd = input("선택: ")
        if cmd == '1':
            uid = input("아이디: ")
            pw = input("비밀번호: ")
            if lib.login(uid, pw):
                current_user = uid
                print("✅ 로그인 성공")
            else:
                print("❌ 실패")
        elif cmd == '2':
            uid = input("아이디 생성: ")
            pw = input("비번 생성: ")
            if lib.register_user(uid, pw):
                print("✅ 회원가입 완료")
            else:
                print("❌ 이미 존재하는 아이디입니다.")
        else:
            return


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
