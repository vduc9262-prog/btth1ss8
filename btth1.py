while True:
    print()
    choice = input("""===== HỆ THỐNG QUẢN LÝ VIDEO TIKTOK =====
1. Nhập dữ liệu và xem báo cáo
2. Chuẩn hóa tên tài khoản
3. Kiểm tra hashtag
4. Tìm và thay thế từ
5. Thoát
Nhập lựa chọn: """).strip()

    if choice == "1":
        username = input("Tên tài khoản: ").strip()
        title = input("Tiêu đề: ").strip()
        description = input("Mô tả: ").strip()
        hashtag_str = input("Hashtag (cách nhau dấu phẩy): ").strip()
        
        if username == "":
            print("Tên tài khoản không được rỗng!")
            continue
        if description == "":
            print("Mô tả không được rỗng!")
            continue
            
        hashtags = []

        for i in hashtag_str.split(","):
            i = i.strip()   # xóa khoảng trắng đầu cuối
            
            if i != "":     # nếu không rỗng thì thêm vào list
                hashtags.append(i)
                
        print("\n--- BAO CAO ---")
        print("Tai khoan:", username)
        print("Tieu de:", title.title())
        print("Mo ta:", description)
        print("Do dai mo ta:", len(description))
        print("So tu:", len(description.split()))
        print("Hashtag:", ", ".join(hashtags))
        print("So hashtag:", len(hashtags))
        print("Mo ta thuong:", description.lower())
        print("Mo ta HOA:", description.upper())
        
    elif choice == "2":
        username = input("Nhap ten tai khoan: ").strip()
        if username == "":
            print("Ten tai khoan khong duoc rong!")
        else:
            print("Ten goc:", username)
            print("Ten chuan hoa:", "@" + username.lower())
        
    elif choice == "3":
        tag = input("Nhap hashtag: ").strip()
        if tag == "":
            print("Hashtag khong duoc rong")
        elif not tag.startswith("#"):
            print("Hashtag phai bat dau bang #")
        elif " " in tag:
            print("Hashtag khong duoc chua khoang trang")
        elif len(tag) < 2:
            print("Hashtag phai co it nhat 2 ky tu")
        else:
            print("Hashtag hop le")
        
    elif choice == "4":
        description = input("Nhap mo ta: ").strip()
        if description == "":
            print("Mo ta khong duoc rong!")
        else:
            keyword = input("Tu khoa can tim: ").strip()
            replace_word = input("Thay the bang: ").strip()
            if keyword in description:
                count = description.count(keyword)
                new_desc = description.replace(keyword, replace_word)
                print("Sau thay the:", new_desc)
                print("So lan tim thay:", count)
            else:
                print("Khong tim thay tu khoa!")
        
    elif choice == "5":
        print("Thoat chuong trinh")
        break
        
    else:
        print("Lua chon khong hop le!")


        
# replace() dùng để làm gì?

# Tác dụng: Thay thế một chuỗi con bằng một chuỗi khác.


# isdigit() dùng để làm gì?

# Tác dụng: Kiểm tra xem chuỗi có phải toàn bộ là chữ số hay không.
