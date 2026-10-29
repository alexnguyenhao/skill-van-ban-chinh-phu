# Dùng skill trên web (ChatGPT, Claude, Gemini)

Repo này không chỉ dành cho OpenCode/Claude Code. Dưới đây là cách đưa cùng một bộ quy tắc vào các chat web,
kèm đúng file cần dùng cho từng nơi.

## Chọn nhanh

| Nơi dùng | Cách làm | File |
|---|---|---|
| **Claude web** (claude.ai) | Upload skill dạng ZIP | [`../dist/van-ban-chinh-phu.zip`](../dist/van-ban-chinh-phu.zip) |
| **Claude Projects** | Instructions + knowledge files | `chat-prompt.md` + `van-ban-chinh-phu/references/` |
| **ChatGPT Plus/Pro** - Custom Instructions | Dán vào 2 ô: giới thiệu (ô 1) + quy tắc (ô 2) | [`chatgpt-about-you.txt`](chatgpt-about-you.txt) + [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) |
| **ChatGPT free** - Custom Instructions | Dán bản rút gọn (giới hạn 1.500 ký tự/ô) | [`chatgpt-about-you.txt`](chatgpt-about-you.txt) + [`chatgpt-instructions-1500.txt`](chatgpt-instructions-1500.txt) |
| **ChatGPT Projects** | Instructions + upload file | `chat-prompt.md` + references |
| **ChatGPT Custom GPT** | Configure + Knowledge | `chat-prompt.md` + references |
| **Gemini Gems** | Instructions + file | `chatgpt-instructions-5000.txt` hoặc `chat-prompt.md` |
| **Bất kỳ chat nào** | Dán đầu cuộc trò chuyện | [`../chat-prompt.md`](../chat-prompt.md) |

Giới hạn đã kiểm tra (2026): Custom Instructions của ChatGPT là **5.000 ký tự** với gói trả phí, **1.500** với gói free;
Projects nhận instructions dài hơn và tối đa ~25 file.

## Link tải nhanh (mở là thấy nội dung, không cần clone)

- ZIP cho Claude: <https://github.com/alexnguyenhao/skill-van-ban-chinh-phu/releases/latest/download/van-ban-chinh-phu.zip>
- Instructions 5.000 ký tự: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-chinh-phu/main/web/chatgpt-instructions-5000.txt>
- Instructions 1.500 ký tự: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-chinh-phu/main/web/chatgpt-instructions-1500.txt>
- Bản đầy đủ dán vào chat: <https://raw.githubusercontent.com/alexnguyenhao/skill-van-ban-chinh-phu/main/chat-prompt.md>

---

## 1. Claude trên web (claude.ai) - cách tốt nhất

Claude đọc được cả bộ skill, tự gọi khi thấy việc soạn văn bản, không cần dán prompt mỗi lần.

1. Mở **claude.ai** → đăng nhập.
2. **Settings** (bánh răng góc dưới trái) → **Capabilities** → bật **Code execution and file creation**.
   Không bật mục này thì phần Skills không dùng được (skill cần đọc file và chạy script).
3. Vào **Customize** → **Skills** → **Upload skill**.
4. Chọn file `dist/van-ban-chinh-phu.zip` trong repo này (hoặc tải từ
   [Releases](https://github.com/alexnguyenhao/skill-van-ban-chinh-phu/releases)).
5. Claude hiện thông tin skill; gạt công tắc sang **On**.
6. Mở chat mới, gõ việc cần làm - Claude tự nạp skill:

   > Viết công văn đề nghị Sở Văn hóa và Thể thao báo cáo kết quả công tác văn thư trước ngày 20/6/2026,
   > căn cứ Nghị định 30/2020/NĐ-CP, người ký là Phó Chủ tịch UBND tỉnh.

**Lưu ý về ZIP:** gốc ZIP phải là thư mục skill (`van-ban-chinh-phu/`), tên thư mục trùng trường `name` trong
`SKILL.md` và phải là chữ thường có gạch nối. Trong repo, `SKILL.md` ghi `name: Văn bản Chính phủ` để OpenCode
hiển thị đẹp; vì vậy **đừng nén thư mục bằng tay** - chạy:

```bash
python build-zip.py     # tạo dist/van-ban-chinh-phu.zip với name: van-ban-chinh-phu
```

Claude không chạy được script Python nếu chưa bật code execution, nên khi cần file Word hãy yêu cầu thẳng:
*"Xuất văn bản trên thành file .docx theo đúng lề và phông của Nghị định 30"*.

## 2. Claude Projects (bản free cũng có)

1. **Projects** → **New project** → đặt tên "Văn bản hành chính".
2. **Set project instructions** → dán toàn bộ [`../chat-prompt.md`](../chat-prompt.md) (7,8 nghìn ký tự, dưới giới hạn 8.000).
3. **Add content / Files** → upload các file trong `van-ban-chinh-phu/references/`
   (`the-thuc.md`, `the-loai.md`, `ngon-ngu.md`, `viet-hoa-va-viet-tat.md`, `quy-trinh.md`, `checklist.md`)
   và 5 file trong `van-ban-chinh-phu/assets/`.
4. Trong project, yêu cầu viết văn bản. Claude đọc file đã upload và trả lời theo đúng quy tắc.

## 3. ChatGPT - Custom Instructions (nhanh nhất)

Bản trong repo đã cấu hình sẵn cho **UBND xã Lộc Hưng** (Chủ tịch Nguyễn Thị Xuân Linh; Phó Chủ tịch
Nguyễn Hữu Thương - văn hóa - xã hội; Phó Chủ tịch Trần Thanh Quang - kinh tế; Trưởng phòng Văn hóa
Đỗ Văn Duyên; Chánh Văn phòng Tạ Thị Ngọc Dung).

1. **Settings** → **Personalization** → **Custom instructions**.
2. Ô thứ nhất ("What should ChatGPT know about you?"): dán [`chatgpt-about-you.txt`](chatgpt-about-you.txt).
3. Ô thứ hai ("How should ChatGPT respond?"):
   - gói Plus/Pro/Team/Enterprise: dán [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) (4.937 ký tự)
   - gói free: dán [`chatgpt-instructions-1500.txt`](chatgpt-instructions-1500.txt) (1.479 ký tự)
4. **Save** → mở chat mới. Custom Instructions áp cho mọi cuộc trò chuyện.

Bản 5.000 ký tự đủ 8 nhóm quy tắc: cấu hình mặc định, hỏi trước khi viết, chọn thể loại, 14 thành phần thể thức,
bố cục, câu mẫu, viết hoa, 10 lỗi cần tránh, định dạng câu trả lời.

## 4. ChatGPT Projects (giữ được cả bộ tài liệu)

1. **ChatGPT** → **Projects** → **New project**.
2. **Project instructions** → dán [`../chat-prompt.md`](../chat-prompt.md) (7,8 nghìn ký tự, dưới giới hạn 8.000).
3. **Add files** → upload `references/*.md` + `assets/*.md` (tối đa ~25 file).
4. Chat trong project. Nếu cần file Word: bật **Code interpreter/Canvas** rồi yêu cầu xuất `.docx`.

## 5. ChatGPT Custom GPT (dùng chung cho cả nhóm)

1. **Explore GPTs** → **Create** → tab **Configure**.
2. **Instructions**: dán [`../chat-prompt.md`](../chat-prompt.md).
3. **Knowledge**: upload `references/*.md` và `assets/*.md`.
4. **Capabilities**: bật **Code Interpreter & Data Analysis** để sinh được `.docx`.
5. **Create** → chọn "Only me" hoặc "Anyone with a link".

## 6. Gemini Gems

1. **Gemini** → **Gems** → **New Gem**.
2. Dán [`chatgpt-instructions-5000.txt`](chatgpt-instructions-5000.txt) (hoặc `chat-prompt.md` nếu ô cho phép dài).
3. **Add files** → upload `references/*.md` để Gem tra cứu chi tiết.
4. **Save**.

## 7. Không có công cụ nào ở trên - dán trực tiếp

Mở chat bất kỳ (Grok, Copilot, DeepSeek, Qwen...), dán [`../chat-prompt.md`](../chat-prompt.md) làm tin nhắn đầu,
sau đó nêu yêu cầu. Cách này tốn token mỗi cuộc nhưng dùng được ở mọi nơi, kể cả app điện thoại.

## Câu lệnh mẫu

```
Viết Quyết định ban hành Quy chế công tác văn thư của UBND tỉnh, người ký là Chủ tịch UBND tỉnh.
```

```
Kiểm tra thể thức công văn sau và sửa lỗi: [dán văn bản]
```

```
Chuyển tờ trình này thành file .docx đúng lề 30/20/20/15 mm, Times New Roman 13, giãn dòng 1,5.
```

## Khác biệt so với bản cài trong máy

| | Bản cài (OpenCode / Claude Code) | Bản web |
|---|---|---|
| Nạp skill | Tự động theo mô tả | Upload ZIP (Claude) hoặc dán instructions |
| Chạy `tao_docx.py` | Có, tạo file thật | Chỉ khi bật code execution / code interpreter |
| Đọc toàn bộ references | Có | Có (Claude ZIP) hoặc chỉ phần đã upload |

Nếu chỉ cần một việc gấp mà không muốn cấu hình: dán `chat-prompt.md` là đủ 90% chất lượng.
