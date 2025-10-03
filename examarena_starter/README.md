# Exam Arena — MVP1 Starter Kit (Python + FastAPI)

Đây là bộ khung **cực đơn giản** để bạn chạy MVP1 trên **Google Colab** (hoặc máy cá nhân) và sau này mở rộng thành sản phẩm.

## 🚀 Bạn sẽ làm gì (phiên bản siêu dễ)
1) Tạo một **GitHub repo** trống (Private).
2) **Tải file ZIP** starter kit (file bạn đang đọc), giải nén, **upload toàn bộ** lên repo (kéo-thả qua web GitHub).
3) Mở **Google Colab** → chạy các lệnh ở mục **Colab Quickstart** bên dưới.
4) Nhận **public URL (ngrok)** và gửi cho máy thứ hai → cả hai thấy trang `Setup OK`.

Sau bước này, chúng ta sẽ lần lượt bổ sung: Lobby → Match → Socket.IO.

---

## ✅ Yêu cầu tối thiểu
- Tài khoản Google & GitHub.
- (Tuỳ chọn) **Ngrok Authtoken** miễn phí: đăng ký tại ngrok.com, copy token.

---

## 🧭 Tạo GitHub Repo (cách nhanh)
1. Vào https://github.com → **New** → Repository name: `examarena` → **Private** → Create.
2. Trên trang repo, bấm **Add file → Upload files**.
3. Kéo-thả tất cả file/thư mục trong ZIP này vào → **Commit changes**.

> Không cần dùng Git/Git CLI. Dùng giao diện web là đủ.

---

## 🟡 Colab Quickstart (copy/paste từng ô)
> Mẹo: mở https://colab.new để tạo Notebook trống. Chạy từng ô một.

**Ô 1 — Cài đặt & clone repo**
```python
!pip -q install fastapi==0.115.0 "uvicorn[standard]==0.30.6" "python-socketio[asyncio]==5.11.3" Jinja2==3.1.4 python-dotenv==1.0.1 pyngrok==7.2.0

# THAY đường dẫn dưới bằng repo của bạn (HTTPS).
REPO_URL = "https://github.com/<YOUR_USERNAME>/examarena.git"
!rm -rf examarena
!git clone {REPO_URL}
%cd examarena
```

**Ô 2 — Chạy server FastAPI (nền)**
```python
# Chạy uvicorn ở background (không chiếm notebook)
import os, subprocess, sys, time
if os.path.exists("uvicorn.pid"):
    !kill -9 $(cat uvicorn.pid) || true
    !rm -f uvicorn.pid

p = subprocess.Popen(["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"])
with open("uvicorn.pid","w") as f:
    f.write(str(p.pid))
time.sleep(2)
print("✅ Uvicorn started on port 8000 (PID:", p.pid, ")")
```

**Ô 3 — Tạo public URL với ngrok**
```python
import os
from pyngrok import ngrok

# DÁN token của bạn vào đây (hoặc bỏ qua nếu đã add trên tài khoản Colab)
NGROK_AUTHTOKEN = os.environ.get("NGROK_AUTHTOKEN", "")
if NGROK_AUTHTOKEN:
    ngrok.set_auth_token(NGROK_AUTHTOKEN)

# Tạo tunnel tới cổng 8000
public_url = ngrok.connect(8000, "http")
print("🌍 Public URL:", public_url)
```

Mở đường link **Public URL** → bạn sẽ thấy trang **“Setup OK”**. Gửi link cho máy thứ hai để kiểm tra cả 2 truy cập được.

**Dừng server (khi cần)**
```python
!kill -9 $(cat uvicorn.pid) || true
!rm -f uvicorn.pid
```

---

## 📁 Cấu trúc thư mục
```
app/
  __init__.py
  main.py            # FastAPI mount static/ (index.html)
  static/
    index.html       # Trang "Setup OK"
    css/style.css
    js/app.js
data/
  word_bank.json     # Mẫu 5 từ (test)
tests/
  test_room_flow.py  # Test placeholder
.env.example
requirements.txt
README.md
```

---

## 🔜 Tiếp theo (kế hoạch code từng bước)
1. Thêm các trang: `home.html` (nickname + room), `lobby.html`, `match.html`, `result.html`.
2. Tích hợp **Socket.IO**: server (python-socketio) & client (CDN).
3. Module **rooms** giữ state trận (in-memory).
4. Sự kiện: `create_room`, `join_room`, `start_match`, `question_start`, `answer_lock`, `question_reveal`, `match_end`.
5. Timer: server gửi `deadline_ts`, client hiển thị đồng hồ.
6. Test 2 máy qua **ngrok URL**.

Bạn đã sẵn sàng nền tảng để tiếp tục từng bước với mình. ✌️
