-- ==============================================================================
-- BÀI TẬP: TẠO BẢNG TRONG CƠ SỞ DỮ LIỆU BẰNG CÂU LỆNH SQL
-- Cơ sở dữ liệu: QuanLyDiemThi
-- Sinh viên / Tác giả: DTC245200413
-- Repository: https://github.com/dtc245200413-cmyk/jwbd-2023-sql-create-table
-- Tham khảo: https://github.com/codegym-vn/jwbd-2023-sql-create-table (branch dev)
-- ==============================================================================

-- Bước 1: Tạo cơ sở dữ liệu có tên là QuanLyDiemThi
CREATE DATABASE IF NOT EXISTS QuanLyDiemThi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Bước 2: Chọn Database QuanLyDiemThi để thao tác với cơ sở dữ liệu này
USE QuanLyDiemThi;

-- Bước 3: Sử dụng câu lệnh CREATE TABLE để tạo bảng HocSinh
CREATE TABLE HocSinh(
    MaHS VARCHAR(20) PRIMARY KEY,
    TenHS VARCHAR(50),
    NgaySinh DATETIME,
    Lop VARCHAR(20),
    GT VARCHAR(20)
);

-- Bước 4: Tạo bảng MonHoc
CREATE TABLE MonHoc(
    MaMH VARCHAR(20) PRIMARY KEY,
    TenMH VARCHAR(50),
    MaGV VARCHAR(20)
);

-- Bước 5: Tạo bảng BangDiem là bảng trung gian của mối quan hệ n - n giữa 2 thực thể HocSinh và MonHoc
CREATE TABLE BangDiem(
    MaHS VARCHAR(20),
    MaMH VARCHAR(20),
    DiemThi INT,
    NgayKT DATETIME,
    PRIMARY KEY (MaHS, MaMH),
    FOREIGN KEY (MaHS) REFERENCES HocSinh(MaHS),
    FOREIGN KEY (MaMH) REFERENCES MonHoc(MaMH)
);

-- Bước 6: Tạo bảng GiaoVien
CREATE TABLE GiaoVien(
    MaGV VARCHAR(20) PRIMARY KEY,
    TenGV VARCHAR(50),
    SDT VARCHAR(10)
);

-- Bước 7: Chỉnh sửa lại bảng MonHoc bổ sung thêm khóa ngoại của bảng MonHoc tham chiếu đến bảng GiaoVien
ALTER TABLE MonHoc ADD CONSTRAINT FK_MaGV FOREIGN KEY (MaGV) REFERENCES GiaoVien(MaGV);

-- ==============================================================================
-- DỮ LIỆU MẪU KIỂM CHỨNG (SEED DATA TEST)
-- ==============================================================================

-- 1. Thêm dữ liệu mẫu vào bảng GiaoVien
INSERT INTO GiaoVien (MaGV, TenGV, SDT) VALUES
('GV01', N'Nguyễn Văn Tuấn', '0912345678'),
('GV02', N'Trần Thị Thu Thảo', '0987654321');

-- 2. Thêm dữ liệu mẫu vào bảng MonHoc
INSERT INTO MonHoc (MaMH, TenMH, MaGV) VALUES
('MH01', N'Toán Đại Số', 'GV01'),
('MH02', N'Lập Trình Web Backend', 'GV02');

-- 3. Thêm dữ liệu mẫu vào bảng HocSinh
INSERT INTO HocSinh (MaHS, TenHS, NgaySinh, Lop, GT) VALUES
('HS01', N'Lê Minh Khang', '2005-04-12 00:00:00', '12A1', N'Nam'),
('HS02', N'Phạm Phương Linh', '2005-08-25 00:00:00', '12A1', N'Nữ');

-- 4. Thêm dữ liệu mẫu vào bảng BangDiem
INSERT INTO BangDiem (MaHS, MaMH, DiemThi, NgayKT) VALUES
('HS01', 'MH01', 9, '2026-10-15 08:00:00'),
('HS01', 'MH02', 10, '2026-10-18 09:30:00'),
('HS02', 'MH01', 8, '2026-10-15 08:00:00');
