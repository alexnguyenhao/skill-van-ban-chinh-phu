# Skill: Văn bản Chính phủ (chuẩn Nghị định 30/2020/NĐ-CP)

Skill cho AI soạn thảo **văn bản hành chính Việt Nam** đúng thể thức, đúng thẩm quyền, đúng ngôn phong
công vụ. Nội dung được học trực tiếp từ bản signed 76 trang của **Nghị định số 30/2020/NĐ-CP ngày 05/3/2020
của Chính phủ về công tác văn thư** (gồm 6 phụ lục: thể thức, viết hoa, chữ viết tắt và mẫu trình bày).

Dùng được cho: công văn, quyết định, nghị quyết, chỉ thị, tờ trình, báo cáo, kế hoạch, thông báo, biên bản,
giấy mời, giấy giới thiệu, công điện, văn bản quy phạm pháp luật.

**Mặc định của bản này:** cơ quan **Ủy ban nhân dân xã Lộc Hưng**; Chủ tịch **Nguyễn Thị Xuân Linh**;
Phó Chủ tịch **Nguyễn Hữu Thương** (văn hóa - xã hội); Phó Chủ tịch **Trần Thanh Quang** (kinh tế);
Trưởng phòng Văn hóa **Đỗ Văn Duyên**; Trưởng phòng Kinh tế **Tạ Hoàng Dũng**; Chánh Văn phòng
**Tạ Thị Ngọc Dung**. Khối ký chỉ ghi chức danh, không ghi `TM.`/`TL.`. Toàn bộ cấu hình nằm trong
[`van-ban-chinh-phu/assets/co-quan-mac-dinh.md`](van-ban-chinh-phu/assets/co-quan-mac-dinh.md) - đổi cơ quan
chỉ cần sửa file đó.

## Nội dung

```
van-ban-chinh-phu/
├── SKILL.md                          # bài học cốt lõi: 3 câu hỏi, 5 nguyên tắc, 8 bước, sơ đồ 14 ô, 10 lỗi
├── references/
│   ├── the-thuc.md                   # 14 thành phần thể thức + kỹ thuật trình bày + bản sao + chữ ký số
│   ├── the-loai.md                   # khuôn viết 12 nhóm thể loại, câu mở - câu kết - ví dụ
│   ├── ngon-ngu.md                   # động từ ngôn hành, công thức câu, bảng sửa lỗi, số liệu, thời hạn
│   ├── viet-hoa-va-viet-tat.md       # viết hoa (Phụ lục II) + 27 chữ viết tắt loại văn bản (Phụ lục III)
│   ├── quy-trinh.md                  # thẩm quyền ký TM./Q./KT./TL./TUQ., cấp số, phát hành, lưu hồ sơ
│   └── checklist.md                  # 50 mục kiểm tra trước khi trình ký
├── assets/
│   ├── co-quan-mac-dinh.md           # cấu hình: UBND xã Lộc Hưng, người ký theo lĩnh vực, khối ký, nơi nhận
│   ├── mau-cong-van.md               # khung công văn
│   ├── mau-quyet-dinh.md             # khung quyết định
│   ├── mau-to-trinh.md               # khung tờ trình
│   ├── mau-bao-cao.md                # khung báo cáo
│   ├── mau-ke-hoach.md               # khung kế hoạch
│   └── vi-du-cong-van.json           # dữ liệu mẫu cho script sinh .docx
└── scripts/
    └── tao_docx.py                   # sinh file .docx đúng A4, lề, Times New Roman 13-14
```

Ngoài thư mục skill, repo còn có: `chat-prompt.md` (bản dán vào chat, 7,8 nghìn ký tự), `web/` (hướng dẫn
ChatGPT/Claude/Gemini + bản instructions 5.000 và 1.500 ký tự), `dist/van-ban-chinh-phu.zip` (gói upload Claude),
`build-zip.py` (dựng lại ZIP), `install-agy.sh` (cài cho Antigravity CLI), `index.json` (catalog HTTP cho OpenCode).

## Cài đặt

### OpenCode

Cách 1 - cài toàn cục (dùng cho mọi phiên):

```bash
git clone https://github.com/alexnguyenhao/skill-van-ban-chinh-phu.git /tmp/vb-skill
mkdir -p ~/.config/opencode/skills
cp -r /tmp/vb-skill/van-ban-chinh-phu ~/.config/opencode/skills/
```

Cách 2 - trỏ vào thư mục repo trong `opencode.json` (OpenCode tự tìm `SKILL.md` lồng bên trong):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["/duong/dan/toi/skill-van-ban-chinh-phu"]
}
```

Cách 3 - dùng như HTTP catalog (không cần clone):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-chinh-phu/main/"]
}
```

Sau khi cài, gọi bằng `@van-ban-chinh-phu` hoặc nói "viết công văn theo chuẩn Chính phủ".

### Claude Code

```bash
cp -r /tmp/vb-skill/van-ban-chinh-phu ~/.claude/skills/
```

### Antigravity CLI (agy)

Antigravity CLI đọc đúng chuẩn `SKILL.md` như Claude/OpenCode. Cài toàn cục bằng một lệnh:

```bash
curl -fsSL https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-chinh-phu/main/install-agy.sh | bash
```

Script tải ZIP từ Releases, giải nén vào `~/.gemini/antigravity-cli/skills/van-ban-chinh-phu/` và đặt
`name: van-ban-chinh-phu` (agy lấy trường này làm tên slash command). Cài từ bản clone trong máy:

```bash
bash install-agy.sh /duong/dan/toi/skill-van-ban-chinh-phu
```

Trong `agy`: gõ `/skills` để xem skill đã nhận, `/van-ban-chinh-phu` để gọi trực tiếp, hoặc chỉ cần nói
"viết công văn...". Chạy một lần không vào TUI:

```bash
agy -p "Viết công văn đề nghị Sở Văn hóa và Thể thao báo cáo kết quả công tác văn thư trước 20/6/2026"
```

Muốn skill chỉ áp cho một dự án: chép thư mục vào `<workspace>/.agents/skills/` (agy ưu tiên vị trí này).
Trên Windows, dùng PowerShell:

```powershell
Invoke-WebRequest https://github.com/alexnguyenhao/skill-van-ban-chinh-phu/releases/latest/download/van-ban-chinh-phu.zip -OutFile $env:TEMP\vb.zip
Expand-Archive $env:TEMP\vb.zip -DestinationPath "$env:USERPROFILE\.gemini\antigravity-cli\skills" -Force
```

Cần xuất file `.docx` thì cài thêm `pip install python-docx` (script `scripts/tao_docx.py` nằm trong thư mục skill).

### Cursor, Codex, Windsurf, Cline và các agent khác

- Clone repo, trỏ agent đọc `van-ban-chinh-phu/SKILL.md` khi làm văn bản; hoặc
- Chép nội dung `van-ban-chinh-phu/SKILL.md` vào `AGENTS.md` / `.cursor/rules` / system prompt của agent.

### Dùng trên web (ChatGPT, Claude, Gemini)

- **Claude web**: upload [`dist/van-ban-chinh-phu.zip`](dist/van-ban-chinh-phu.zip) ở Settings → Customize → Skills
  (nhớ bật Settings → Capabilities → *Code execution and file creation*).
- **ChatGPT**: dán [`web/chatgpt-about-you.txt`](web/chatgpt-about-you.txt) vào ô 1 và
  [`web/chatgpt-instructions-5000.txt`](web/chatgpt-instructions-5000.txt) vào ô 2 của Custom Instructions
  (bản free dùng [`web/chatgpt-instructions-1500.txt`](web/chatgpt-instructions-1500.txt)); hoặc tạo Project rồi
  upload `chat-prompt.md` + `references/`.
- **Gemini Gems**: dán cùng file instructions, upload thêm `references/`.

Hướng dẫn từng bước, kèm giới hạn ký tự và cách xử lý khi cần file `.docx`: xem [`web/README.md`](web/README.md).
Muốn dựng lại file ZIP sau khi sửa skill: `python build-zip.py`.

Nếu chỉ muốn dùng ngay trong một cuộc trò chuyện: dán toàn bộ [`chat-prompt.md`](chat-prompt.md) làm tin nhắn đầu, rồi yêu cầu:
*"Viết công văn đề nghị Sở Văn hóa và Thể thao báo cáo kết quả công tác văn thư trước 20/6/2026"*.

## Ví dụ sử dụng

```
@van-ban-chinh-phu viết Kế hoạch triển khai công tác văn thư năm 2026 của UBND xã,
căn cứ Nghị định 30/2020/NĐ-CP, phân công 4 nhiệm vụ có chủ trì - thời hạn - sản phẩm.
```

Skill sẽ: chọn thể loại và ký hiệu → dựng khối đầu (quốc hiệu, số, địa danh ngày tháng) → viết căn cứ, nội dung,
tổ chức thực hiện → ráp nơi nhận, thẩm quyền ký → tự chạy checklist thể thức.

## Sinh file Word

```bash
pip install python-docx
python van-ban-chinh-phu/scripts/tao_docx.py \
    van-ban-chinh-phu/assets/vi-du-cong-van.json \
    -o "Cong-van-125.docx"
```

Script tự đặt: A4 dọc, lề trên/dưới 20 mm - trái 30 mm - phải 15 mm, Times New Roman 13-14, khối đầu 2 cột
(quốc hiệu - tên cơ quan), số trang canh giữa ẩn trang 1, khối `Nơi nhận` - chữ ký, ô địa chỉ - điện thoại.
Xem hướng dẫn JSON đầy đủ ở đầu file script.

## Cập nhật

```bash
cd skill-van-ban-chinh-phu && git pull
cp -r van-ban-chinh-phu/SKILL.md van-ban-chinh-phu/references van-ban-chinh-phu/assets \
      van-ban-chinh-phu/scripts ~/.config/opencode/skills/van-ban-chinh-phu/
```

## Nguồn và giới hạn

- Nội dung pháp lý tóm lược từ Nghị định 30/2020/NĐ-CP và 6 phụ lục. Nghị định này vẫn là văn bản đang áp dụng
  cho thể thức, kỹ thuật trình bày văn bản hành chính (đã kiểm chứng năm 2026).
- Trước khi ban hành văn bản có hiệu lực pháp lý, luôn đối chiếu lại văn bản gốc trên `vanban.chinhphu.vn`
  và quy chế công tác văn thư của cơ quan.
- Skill hỗ trợ soạn thảo, không thay thế trách nhiệm của người kiểm tra thể thức và người ký văn bản.

## English

A reusable AI skill for drafting Vietnamese government administrative documents according to
Decree 30/2020/NĐ-CP: document types, 14 mandatory layout components, typography (A4, Times New Roman 13-14 pt),
capitalisation rules, number/symbol formats, signing authority, drafting style, review checklist, and a
python-docx generator. Install by copying `van-ban-chinh-phu/` into your agent's skills directory
(`~/.config/opencode/skills`, `~/.claude/skills`, ...) or paste `chat-prompt.md` into any chat model.
For web chat: upload `dist/van-ban-chinh-phu.zip` as a Claude skill, or paste the file in `web/` into ChatGPT
Custom Instructions / Projects; see `web/README.md`.

## Giấy phép

MIT - xem [LICENSE](LICENSE).
