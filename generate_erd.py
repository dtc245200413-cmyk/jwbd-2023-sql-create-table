import os
import shutil
import subprocess
import tempfile

svg_content = """<svg width="1280" height="780" viewBox="0 0 1280 780" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <style>
    .tbl-title { font-size: 14px; font-weight: 800; fill: #ffffff; }
    .col-pk { font-size: 12.5px; font-weight: 800; fill: #b91c1c; }
    .col-fk { font-size: 12.5px; font-weight: 700; fill: #2563eb; }
    .col-norm { font-size: 12.5px; fill: #1e293b; }
    .col-type { font-size: 11.5px; fill: #64748b; text-anchor: end; font-family: monospace; }
  </style>

  <!-- Title Banner -->
  <rect x="30" y="20" width="1220" height="48" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5" />
  <text x="640" y="50" font-size="16" font-weight="800" fill="#166534" text-anchor="middle">
    SƠ ĐỒ CƠ SỞ DỮ LIỆU QUẢN LÝ ĐIỂM THI (DATABASE: QuanLyDiemThi)
  </text>

  <!-- TABLE 1: HocSinh -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="280" height="215" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 272,0 Q 280,0 280,8 L 280,36 L 0,36 Z" fill="#1e40af" />
    <text x="18" y="24" class="tbl-title">👨‍🎓 HocSinh</text>
    
    <text x="18" y="62" class="col-pk">🔑 MaHS (PK)</text>
    <text x="262" y="62" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="74" x2="268" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-norm">TenHS</text>
    <text x="262" y="98" class="col-type">VARCHAR(50)</text>
    <line x1="12" y1="110" x2="268" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-norm">NgaySinh</text>
    <text x="262" y="134" class="col-type">DATETIME</text>
    <line x1="12" y1="146" x2="268" y2="146" stroke="#f1f5f9" />

    <text x="18" y="170" class="col-norm">Lop</text>
    <text x="262" y="170" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="182" x2="268" y2="182" stroke="#f1f5f9" />

    <text x="18" y="202" class="col-norm">GT</text>
    <text x="262" y="202" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 2: GiaoVien -->
  <g transform="translate(940, 110)" filter="url(#shadow)">
    <rect width="280" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 272,0 Q 280,0 280,8 L 280,36 L 0,36 Z" fill="#0f766e" />
    <text x="18" y="24" class="tbl-title">👩‍🏫 GiaoVien</text>
    
    <text x="18" y="62" class="col-pk">🔑 MaGV (PK)</text>
    <text x="262" y="62" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="74" x2="268" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-norm">TenGV</text>
    <text x="262" y="98" class="col-type">VARCHAR(50)</text>
    <line x1="12" y1="110" x2="268" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-norm">SDT</text>
    <text x="262" y="134" class="col-type">VARCHAR(10)</text>
  </g>

  <!-- TABLE 3: MonHoc -->
  <g transform="translate(940, 360)" filter="url(#shadow)">
    <rect width="280" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 272,0 Q 280,0 280,8 L 280,36 L 0,36 Z" fill="#4338ca" />
    <text x="18" y="24" class="tbl-title">📚 MonHoc</text>
    
    <text x="18" y="62" class="col-pk">🔑 MaMH (PK)</text>
    <text x="262" y="62" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="74" x2="268" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-norm">TenMH</text>
    <text x="262" y="98" class="col-type">VARCHAR(50)</text>
    <line x1="12" y1="110" x2="268" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-fk">🔗 MaGV (FK)</text>
    <text x="262" y="134" class="col-type">VARCHAR(20)</text>
  </g>

  <!-- TABLE 4: BangDiem (Junction Table) -->
  <g transform="translate(500, 230)" filter="url(#shadow)">
    <rect width="280" height="185" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 272,0 Q 280,0 280,8 L 280,36 L 0,36 Z" fill="#b45309" />
    <text x="18" y="24" class="tbl-title">📝 BangDiem (N - N)</text>
    
    <text x="18" y="62" class="col-pk">🔑 MaHS (PK, FK)</text>
    <text x="262" y="62" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="74" x2="268" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-pk">🔑 MaMH (PK, FK)</text>
    <text x="262" y="98" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="110" x2="268" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-norm">DiemThi</text>
    <text x="262" y="134" class="col-type">INT</text>
    <line x1="12" y1="146" x2="268" y2="146" stroke="#f1f5f9" />

    <text x="18" y="170" class="col-norm">NgayKT</text>
    <text x="262" y="170" class="col-type">DATETIME</text>
  </g>

  <!-- RELATIONSHIP CONNECTORS -->
  <!-- HocSinh.MaHS -> BangDiem.MaHS -->
  <path d="M 340,172 L 420,172 L 420,292 L 500,292" fill="none" stroke="#2563eb" stroke-width="2.5" />
  <circle cx="340" cy="172" r="4" fill="#2563eb" />
  <polygon points="495,287 505,292 495,297" fill="#2563eb" />

  <!-- MonHoc.MaMH -> BangDiem.MaMH -->
  <path d="M 940,422 L 860,422 L 860,328 L 780,328" fill="none" stroke="#4338ca" stroke-width="2.5" />
  <circle cx="940" cy="422" r="4" fill="#4338ca" />
  <polygon points="785,323 775,328 785,333" fill="#4338ca" />

  <!-- GiaoVien.MaGV -> MonHoc.MaGV -->
  <path d="M 1080,260 L 1080,360" fill="none" stroke="#0f766e" stroke-width="2.5" />
  <circle cx="1080,260" r="4" fill="#0f766e" />
  <polygon points="1075,355 1080,365 1085,355" fill="#0f766e" />

  <!-- SUMMARY INFO CARD -->
  <g transform="translate(60, 560)">
    <rect width="1160" height="185" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="25" y="32" font-size="14.5" font-weight="800" fill="#0f172a">CHI TIẾT RÀNG BUỘC KHÓA CHÍNH (PK) VÀ KHÓA NGOẠI (FK):</text>
    <text x="35" y="65" font-size="12.5" fill="#334155">• Bảng HocSinh: Khóa chính là MaHS. Lưu trữ thông tin cá nhân của từng học sinh.</text>
    <text x="35" y="92" font-size="12.5" fill="#334155">• Bảng GiaoVien: Khóa chính là MaGV. Lưu trữ danh mục giáo viên bộ môn.</text>
    <text x="35" y="119" font-size="12.5" fill="#334155">• Bảng MonHoc: Khóa chính là MaMH. Khóa ngoại MaGV tham chiếu đến GiaoVien(MaGV) (1 giáo viên phụ trách môn).</text>
    <text x="35" y="146" font-size="12.5" fill="#334155">• Bảng BangDiem: Khóa chính phức hợp (MaHS, MaMH). Là bảng trung gian giải quyết quan hệ Nhiều - Nhiều (N - N) giữa Học sinh và Môn học.</text>
    <text x="35" y="170" font-size="12.5" font-weight="700" fill="#16a34a">✓ Bảng đã được cấu hình toàn vẹn dữ liệu chuẩn theo đúng yêu cầu đề bài.</text>
  </g>
</svg>
"""

base_dir = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\jwbd-2023-sql-create-table"
assets_dir = os.path.join(base_dir, "assets")

svg_path = os.path.join(assets_dir, "erd_quan_ly_diem_thi.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Sơ đồ CSDL QuanLyDiemThi</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 30px;
    }}
    .card {{
      background: #ffffff;
      border-radius: 20px;
      padding: 24px 28px 32px 28px;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08);
      border: 1px solid #cbd5e1;
    }}
  </style>
</head>
<body>
  <div class="card">
    {svg_content}
  </div>
</body>
</html>
"""

html_path = os.path.join(assets_dir, "index.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = tempfile.gettempdir()
temp_png = os.path.join(temp_dir, "erd_quan_ly_diem_thi.png")
dest_png = os.path.join(assets_dir, "erd_quan_ly_diem_thi.png")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1400,950",
    f"--screenshot={temp_png}",
    "file:///" + html_path.replace("\\", "/")
]

subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(temp_png):
    shutil.copy2(temp_png, dest_png)
    print("PNG rendered successfully to", dest_png)
else:
    print("Error rendering PNG")
