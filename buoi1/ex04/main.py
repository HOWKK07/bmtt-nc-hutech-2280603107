from QLSV import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("***************MENU**************************")
    print("* 1. Them sinh vien.")
    print("* 2. Cap nhat thong tin sinh vien boi ID")
    print("* 3. Xoa sinh vien boi Id")
    print("* 4. Tim kiem sinh vien theo ten")
    print("* 5. Sap xep sinh vien theo diem trung binh.")
    print("* 6. Sap xep sinh vien theo chuyen nganh.")
    print("* 7. Hien thi danh sach sinh vien.")
    print("* 0. Thoat")
    print("**********************************************")

    key = int(input("nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien. ")
        qlsv.nhapSinhVien
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nSanh sách sinh viên trống!")
        
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có id = ", ID, " đã bị xóa.")
            else:
                print("\nSinh viên có id = ", ID, " không tồn tại.")
        else:
            print("\nSanh sách sinh viên trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nSanh sách sinh viên trống!")

    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sách sinh viên trống!")

    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sách sinh viên trống!")

    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sách sinh viên trống!")

    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình!")
        break

    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng trong hợp menu.")
        
