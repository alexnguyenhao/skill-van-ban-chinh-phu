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

| Lĩnh vực / loại việc | Người ký | Khối ký (ô 7a + 7b) |
| --- | --- | --- |
| Việc chung, quyết định, quy chế, nhân sự, khen thưởng, kỷ luật, báo cáo năm, chương trình công tác | Nguyễn Thị Xuân Linh - Chủ tịch | `TM. ỦY BAN NHÂN DÂN` + `CHỦ TỊCH` |
| Văn hóa, thể thao, du lịch, giáo dục, y tế, lao động - thương binh và xã hội, dân tộc, tôn giáo, thông tin và truyền thông | Nguyễn Hữu Thương - Phó Chủ tịch | `TM. ỦY BAN NHÂN DÂN` + `PHÓ CHỦ TỊCH` |
| Nông nghiệp, công thương, xây dựng, giao thông, tài chính - kế hoạch, đất đai, môi trường, thuế, hợp tác xã | Trần Thanh Quang - Phó Chủ tịch | `TM. ỦY BAN NHÂN DÂN` + `PHÓ CHỦ TỊCH` |
| Văn bản chuyên môn văn hóa do Phòng Văn hóa chủ trì | Đỗ Văn Duyên - Trưởng phòng Văn hóa | `TL. CHỦ TỊCH` + `TRƯỞNG PHÒNG VĂN HÓA` |
| Văn bản chuyên môn kinh tế do Phòng Kinh tế chủ trì | Tạ Hoàng Dũng - Trưởng phòng Kinh tế | `TL. CHỦ TỊCH` + `TRƯỞNG PHÒNG KINH TẾ` |
| Giấy mời, công văn đôn đốc, thông báo nội bộ, bản sao, văn bản hành chính thường ngày | Tạ Thị Ngọc Dung - Chánh Văn phòng | `TL. CHỦ TỊCH` + `CHÁNH VĂN PHÒNG` |

Ô 7b: chức vụ in hoa đậm 13-14, họ tên in thường đậm ngay dưới, canh giữa; không ghi học hàm, quân hàm.

## 3. Quy ước khối ký của đơn vị

Khối ký gồm **quyền hạn ký (ô 7a) + chức danh (ô 7b) + họ tên**:

- Chủ tịch, Phó Chủ tịch: `TM. ỦY BAN NHÂN DÂN` (ký thay mặt tập thể UBND) + `CHỦ TỊCH` / `PHÓ CHỦ TỊCH`.
- Chánh Văn phòng, Trưởng phòng: `TL. CHỦ TỊCH` (thừa lệnh Chủ tịch) + `CHÁNH VĂN PHÒNG` /
  `TRƯỞNG PHÒNG VĂN HÓA` / `TRƯỞNG PHÒNG KINH TẾ`.
- Không dùng `KT.`, `Q.`, `TUQ.` cho các trường hợp thường ngày; chỉ dùng khi có văn bản giao quyền cụ thể.

```
     TM. ỦY BAN NHÂN DÂN
           CHỦ TỊCH

     Nguyễn Thị Xuân Linh
```

```
     TM. ỦY BAN NHÂN DÂN
         PHÓ CHỦ TỊCH

     Nguyễn Hữu Thương
```

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

```
        TL. CHỦ TỊCH
     TRƯỞNG PHÒNG KINH TẾ

        Tạ Hoàng Dũng
```

- Ô 7a: in hoa, đậm, canh giữa, cỡ 13-14; ô 7b: chức danh in hoa đậm, họ tên in thường đậm ngay dưới.
- Khoảng trống giữa chức danh và họ tên: 2-3 dòng để ký.

## 4. Thứ tự chọn người ký và câu hỏi bắt buộc

**Trước khi viết, luôn hỏi:** *"Anh/chị muốn làm văn bản gì và ai ký?"* - kèm gợi ý nhanh: Chủ tịch, Phó Chủ tịch
(văn hóa - xã hội / kinh tế), Chánh Văn phòng, Trưởng phòng Văn hóa, Trưởng phòng Kinh tế. Chỉ hỏi một lần;
nếu người dùng đã nêu đủ việc và người ký thì vào việc luôn.

Sau khi có câu trả lời:

1. Người dùng nêu tên hoặc chức danh → dùng đúng ý người dùng, không tự "sửa" lại.
2. Người dùng nói "tùy" hoặc chưa rõ → chọn theo lĩnh vực: văn hóa - xã hội → Phó Chủ tịch **Nguyễn Hữu Thương**;
   kinh tế → Phó Chủ tịch **Trần Thanh Quang**.
3. Quyết định, quy chế, nhân sự, khen thưởng, kỷ luật, báo cáo năm, việc liên ngành → Chủ tịch **Nguyễn Thị Xuân Linh**.
4. Văn bản chuyên môn do phòng chủ trì → Trưởng phòng **Đỗ Văn Duyên** (văn hóa) hoặc **Tạ Hoàng Dũng** (kinh tế).
5. Giấy mời, đôn đốc, sao y, thông báo nội bộ, việc thường ngày → Chánh Văn phòng **Tạ Thị Ngọc Dung**.

Không thêm lãnh đạo ngoài danh sách, không đổi chức danh, không ghi "kiêm nhiệm".

## 5. Nơi nhận mặc định

- Văn bản **có `Kính gửi:`** ở đầu → dòng đầu của nơi nhận ghi `Như trên;`.
- Văn bản **không có `Kính gửi:`** (quyết định, kế hoạch, báo cáo...) → bỏ dòng `Như trên`, ghi đối tượng nhận thật.

Mẫu mặc định:

```
Nơi nhận:
- Như trên;
- CT, các P.CT UBND xã;
- Lưu: VT.
```

Có thể thêm đối tượng cụ thể khi cần (các phòng chuyên môn, Trưởng các thôn, đơn vị phối hợp) ngay trước dòng
`Lưu: VT.`.

## 6. Câu mặc định

- `Ủy ban nhân dân xã Lộc Hưng ban hành ...`
- `Chủ tịch Ủy ban nhân dân xã Lộc Hưng quyết định ...`
- `Ủy ban nhân dân xã Lộc Hưng giao Trưởng phòng Văn hóa chủ trì, phối hợp với các phòng chuyên môn ...`
- `Ủy ban nhân dân xã Lộc Hưng đề nghị ...` (ngang cấp) · `... kính đề nghị ...` (cấp trên)
- Kết thúc nội dung bằng `./.`

## 7. Khi làm văn bản cho cơ quan khác

Sao file này thành bản riêng, sửa mục 1-6, hoặc nói rõ "lần này viết cho UBND xã X" - skill sẽ tạm bỏ cấu hình
mặc định và dùng thông tin người dùng cung cấp.
