# Cấu hình cơ quan mặc định - UBND xã Lộc Hưng

Đây là phần "cấu hình" của skill: mọi văn bản mặc định lấy thông tin trong file này, **không hỏi lại** những gì
đã có ở đây. Khi chuyển sang cơ quan khác, chỉ cần sửa file này (và giữ nguyên các file quy tắc).

## 1. Cơ quan ban hành

| Trường | Giá trị |
| --- | --- |
| Ô 2 (dòng dưới) | `ỦY BAN NHÂN DÂN XÃ LỘC HƯNG` |
| Ô 2 (dòng trên) | không có - xã trực thuộc tỉnh, chính quyền 2 cấp, không còn cấp huyện |
| Ô 4 | `Lộc Hưng, ngày ... tháng ... năm ...` |
| Ký hiệu | `QĐ-UBND`, `BC-UBND`, `KH-UBND`, `TB-UBND`, `TTr-UBND`, `BB-UBND`, `GM-UBND`; công văn: `.../UBND-VP` |
| Ô 13 | Địa chỉ: [...] - Điện thoại: [...] - Email: [...] - Website: [...] |

- Số văn bản lấy theo sổ văn bản đi của Văn phòng; số nhỏ hơn 10 phải thêm `0` (`Số: 05/QĐ-UBND`).
  Chưa biết số thì ghi `Số: .../QĐ-UBND`, **không tự bịa số**.
- Tên cơ quan trong ô 2 viết đúng chính tả, không viết tắt; không ghi "UBND xã Lộc Hưng" trong ô 2.
- Văn bản gửi cấp trên dùng `Kính gửi: Ủy ban nhân dân tỉnh [tên tỉnh]`; gửi trong xã dùng `Kính gửi:` hoặc
  `Nơi nhận:` theo quy định tại `references/the-thuc.md`.

## 2. Người ký mặc định

| Lĩnh vực / loại việc | Người ký | Ô 7a | Ô 7b |
| --- | --- | --- | --- |
| Việc chung, quyết định, quy chế, nhân sự, khen thưởng, kỷ luật, báo cáo năm, chương trình công tác | Nguyễn Thị Xuân Linh - Chủ tịch | `TM. ỦY BAN NHÂN DÂN` | `CHỦ TỊCH` |
| Văn hóa, thể thao, du lịch, giáo dục, y tế, lao động - thương binh và xã hội, dân tộc, tôn giáo, thông tin và truyền thông | Nguyễn Hữu Thương - Phó Chủ tịch | `TM. ỦY BAN NHÂN DÂN` | `PHÓ CHỦ TỊCH` |
| Nông nghiệp, công thương, xây dựng, giao thông, tài chính - kế hoạch, đất đai, môi trường, thuế, hợp tác xã | Trần Thanh Quang - Phó Chủ tịch | `TM. ỦY BAN NHÂN DÂN` | `PHÓ CHỦ TỊCH` |
| Văn bản chuyên môn văn hóa do Phòng Văn hóa chủ trì, khi được giao ký | Đỗ Văn Duyên - Trưởng phòng Văn hóa | `TL. CHỦ TỊCH` | `TRƯỞNG PHÒNG VĂN HÓA` |
| Giấy mời, công văn đôn đốc, thông báo nội bộ, bản sao, văn bản hành chính thường ngày khi được giao | Tạ Thị Ngọc Dung - Chánh Văn phòng | `TL. CHỦ TỊCH` | `CHÁNH VĂN PHÒNG` |

Ô 7b: chức vụ in hoa đậm 13-14, họ tên in thường đậm ngay dưới, canh giữa; không ghi học hàm, quân hàm.

## 3. Thứ tự chọn người ký

1. Người dùng nêu tên hoặc chức danh → dùng đúng ý người dùng, không tự "sửa" lại.
2. Có từ khóa văn hóa - xã hội (văn hóa, thể thao, du lịch, giáo dục, y tế, LĐTBXH, dân tộc, tôn giáo, TT&TT)
   → Phó Chủ tịch **Nguyễn Hữu Thương**.
3. Có từ khóa kinh tế (nông nghiệp, công thương, xây dựng, giao thông, tài chính, đất đai, môi trường, thuế,
   hợp tác xã, chợ, giảm nghèo phần kinh tế) → Phó Chủ tịch **Trần Thanh Quang**.
4. Quyết định, quy chế, nhân sự, khen thưởng, kỷ luật, báo cáo năm, chương trình công tác, việc liên ngành
   hoặc văn bản quan trọng → Chủ tịch **Nguyễn Thị Xuân Linh**.
5. Giấy mời, đôn đốc, sao y, thông báo nội bộ, văn bản hành chính thường ngày → Chánh Văn phòng
   **Tạ Thị Ngọc Dung** (`TL. CHỦ TỊCH`).
6. Văn bản chuyên môn văn hóa do Phòng Văn hóa chủ trì → Trưởng phòng **Đỗ Văn Duyên** (`TL. CHỦ TỊCH`).
7. Không xác định được lĩnh vực → hỏi đúng một câu: *"Văn bản này thuộc lĩnh vực văn hóa - xã hội, kinh tế hay
   do Chủ tịch ký?"* rồi mới viết.

Không thêm lãnh đạo ngoài danh sách, không đổi chức danh, không ghi "kiêm nhiệm", không suy ra người ký từ
chức vụ của cơ quan khác.

## 4. Khối ký - bản mẫu

Chủ tịch:

```
TM. ỦY BAN NHÂN DÂN
       CHỦ TỊCH

  Nguyễn Thị Xuân Linh
```

Phó Chủ tịch (văn hóa - xã hội):

```
TM. ỦY BAN NHÂN DÂN
     PHÓ CHỦ TỊCH

  Nguyễn Hữu Thương
```

Phó Chủ tịch (kinh tế): giống trên, thay tên **Trần Thanh Quang**.

Thừa lệnh:

```
TL. CHỦ TỊCH
CHÁNH VĂN PHÒNG

 Tạ Thị Ngọc Dung
```

```
TL. CHỦ TỊCH
TRƯỞNG PHÒNG VĂN HÓA

   Đỗ Văn Duyên
```

- `TM.` chỉ dùng khi ký thay mặt tập thể UBND (Chủ tịch, Phó Chủ tịch được phân công).
- `TL.` dùng khi Chủ tịch giao ký thay (Chánh Văn phòng, Trưởng phòng).
- Không dùng `KT.` cho Phó Chủ tịch ký văn bản thuộc lĩnh vực được phân công; `KT.` chỉ dùng khi ký thay
  người đứng đầu trong trường hợp được giao cụ thể và ghi rõ chức vụ thay.

## 5. Nơi nhận mặc định

Văn bản chỉ đạo, triển khai trong xã:

```
Nơi nhận:
- TT. HĐND xã;
- Chủ tịch, các Phó Chủ tịch UBND xã;
- Các phòng chuyên môn thuộc UBND xã;
- Lưu: VT, VP (02).
```

Văn bản gửi cấp trên: dòng đầu `Kính gửi: Ủy ban nhân dân tỉnh [tên tỉnh]`, cuối vẫn có `Lưu: VT, VP (02).`

## 6. Câu mặc định

- `Ủy ban nhân dân xã Lộc Hưng ban hành ...`
- `Chủ tịch Ủy ban nhân dân xã Lộc Hưng quyết định ...`
- `Ủy ban nhân dân xã Lộc Hưng giao Trưởng phòng Văn hóa chủ trì, phối hợp với các phòng chuyên môn ...`
- `Ủy ban nhân dân xã Lộc Hưng đề nghị ...` (ngang cấp) · `... kính đề nghị ...` (cấp trên)
- Kết thúc nội dung bằng `./.`

## 7. Khi làm văn bản cho cơ quan khác

Sao file này thành bản riêng, sửa mục 1-6, hoặc nói rõ "lần này viết cho UBND xã X" - skill sẽ tạm bỏ cấu hình
mặc định và dùng thông tin người dùng cung cấp.
