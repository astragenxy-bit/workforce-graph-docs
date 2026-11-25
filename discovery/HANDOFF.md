# HANDOFF — Discovery Talent Flow cho BRG và Toho Gas

Tài liệu này giúp một phiên Claude khác (hoặc một thành viên khác trong nhóm) nắm đủ bối cảnh để tiếp tục chỉnh sửa, làm mới tài liệu và bộ slide. Cập nhật lần cuối: 25/11/2026 (bản v3.4).

> Lưu ý về độ tin cậy: số liệu bên dưới lấy từ tài liệu nghiên cứu trong thư mục này. Nội dung có nhãn **[Inference]** là suy luận, chưa kiểm chứng; khi dùng lại phải giữ nhãn. Phần pháp lý là thông tin tham khảo cho thiết kế, không phải tư vấn pháp lý.

---

## 1. Tóm tắt trạng thái

| Hạng mục | Trạng thái | Vị trí |
|---|---|---|
| Nghiên cứu BRG (Doc 1, gửi khách hàng được) | Hoàn thành | PDF trong thư mục này; `docs-md/` có bản Markdown |
| Nghiên cứu Toho Gas | Hoàn thành (bản PDF ngày 19/11/2026) | PDF trong thư mục này |
| So sánh BRG và Toho Gas, khoảng cách năng lực hệ thống (Doc 2, **nội bộ**) | Hoàn thành | PDF trong thư mục này |
| Data flow và tri thức doanh nghiệp (Doc 3) | Hoàn thành | PDF trong thư mục này |
| First principles: nghiên cứu và áp dụng cho hai khách hàng (Doc 4) | Hoàn thành | PDF trong thư mục này |
| Bộ slide BRG, bản v3.2: 25 slide (17 chính gồm bìa và cảm ơn, 8 phụ lục) | Hoàn thành, đã xử lý phản hồi 1–7 | `decks/brg/` |
| Bộ slide Toho Gas, bản v3.2: 26 slide (18 chính gồm bìa và cảm ơn, 8 phụ lục) | Hoàn thành, đã xử lý phản hồi 1–7 | `decks/toho/` |
| Thông tin người liên hệ trên slide cảm ơn | **Chưa điền** (placeholder `[Họ tên · chức danh · email · điện thoại]`) | `slides/thanks.html` của hai bộ |

`text/` chứa bản trích văn bản thuần của các tài liệu nghiên cứu (để tìm kiếm, trích dẫn nhanh). Bản trích từ PDF có thể lỗi dấu ở một số chỗ; khi trích dẫn chính thức, đối chiếu với PDF.

---

## 2. Yêu cầu gốc, phản hồi và các quyết định đã chốt

1. **Mục tiêu bộ slide:** hai bản trình bày với khách hàng (BRG, Toho Gas), tiếng Việt, cho lãnh đạo nhân sự và DX. Ban đầu khoảng 12 slide chính; sau phản hồi 3, phần chính tăng do bổ sung các trang bắt buộc (mục 2.7).
2. **Tên sản phẩm:** gọi chung là **Talent Flow**, gồm tính năng nghiệp vụ, luồng dữ liệu, cơ sở tri thức doanh nghiệp và AI. AINAVI chỉ xuất hiện như nền tảng tích hợp (tuyển nội bộ, thi trực tuyến).
3. **Phong cách:** theo slide *AINAVI Introduction* (navy `#14203C`, cam `#FCA010`, tiêu đề chữ condensed, footer), lấy người dùng làm trung tâm, rõ ràng, sạch.
4. **Phản hồi 1 (văn phong):** bỏ văn nói; viết theo cách diễn đạt của AINAVI Introduction. Quy tắc ở mục 6.
5. **Phản hồi 2 (trực quan):** giảm chữ thuần, bảng và khối chữ dày; dùng mẫu biểu diễn trực quan (thư mục ảnh mẫu của người dùng, slide AINAVI).
6. **Phản hồi 3 (25/11/2026):**
   - Lỗi đường kẻ nằm đè lên component (sơ đồ hub ở `brg-today`, thanh timeline đè lên chấm số). Yêu cầu dùng **đường gấp khúc có bo góc**.
   - Đưa **ảnh demo tính năng** đang có của hệ thống vào các trang phù hợp, không quá nhiều.
   - **Tổng quan hóa** trang chính, bớt diễn giải chi tiết; chi tiết thật sự cần thì đưa vào **phụ lục**.
7. **Nội dung bắt buộc phải có ở trang chính:** vai trò tham gia; các luồng hoạt động kèm minh họa; kiến trúc cơ sở tri thức dạng architecture; data flow; nguyên tắc hoạt động của AI.
8. **Phản hồi 4 (25/11/2026):** nội dung "Tuân thủ" (yêu cầu pháp lý → chức năng) được đánh giá tốt, phải xuất hiện ở vùng trang chính nhưng **biểu diễn lại**. Đã làm: trang chính `compliance` dạng ba cột theo chủ đề (luật → yêu cầu → chức năng trong Talent Flow, có minh họa nhỏ); bản chi tiết theo điều khoản giữ ở phụ lục A7 (`ap-legal`) của BRG.
9. **Phản hồi 5 (lỗi hiển thị):** số trong các vòng tròn (timeline dọc) lệch lên góc trên trái trong trình xem thật. Nguyên nhân: Slides bỏ qua `display:flex` để căn giữa chữ bên trong `<p>`. Đã đổi các lớp `.num`, `.tl-dot`, `.vt-dot`, `.df-n` sang `text-align:center` + `line-height` bằng chiều cao vòng tròn.
10. **Phản hồi 6:** thêm slide **kiến trúc tổng thể** làm trang đầu phụ lục (A1, `ap-architecture`) ở cả hai bộ; các phụ lục còn lại lùi một số (A2–A8), tham chiếu trong slide và ghi chú đã cập nhật.
11. **Phản hồi 7 (bìa):** nội dung mô tả trên bìa được thể hiện ngay trong hình minh họa, cách biểu diễn tinh tế hơn: bốn dòng chảy (nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp, AI) hội về lõi **Kỹ năng**, rồi tỏa ra hai kết quả (phát triển nghề nghiệp, điều chuyển nhân lực nội bộ); có chuyển động vẽ đường và hiện chữ khi trình chiếu. Đoạn mô tả chữ trên bìa đã bỏ (chuyển vào ghi chú người trình bày).
    - Chỉnh tiếp theo phản hồi: chữ đặt **bên trong các vòng tròn** (bốn vòng thành phần trên quỹ đạo, hai vòng kết quả màu cam bên dưới); tiêu đề bìa chỉ còn "Talent Flow" (bỏ "cho Tập đoàn BRG", "cho Toho Gas"); tên công ty ở chân trang bìa được làm nổi bật (chữ đậm, màu cam).
    - Sáu vòng tròn xếp đều trên **một quỹ đạo** (cách nhau 60°, bán kính 300px quanh lõi): bốn thành phần ở nửa trên (trái, trên trái, trên phải, phải), hai kết quả màu cam ở dưới (dưới trái, dưới phải). Thông số trong `_CV_*` của `gen/blocks.py`.
12. **Không đưa vào slide khách hàng:** khoảng cách năng lực nội bộ (Doc 2), tên khách hàng khác (TPBank, LPBank…).
13. **Ảnh chụp màn hình Talent Flow** lấy từ tài liệu giới thiệu sản phẩm, chứa dữ liệu mẫu của bản thí điểm Toho Gas:
    - Bộ Toho Gas dùng **ảnh rõ**.
    - Bộ BRG chỉ dùng **bản đã làm mờ vùng dữ liệu** (giữ rõ khung, menu, tiêu đề): `decks/brg/assets/brg-*.png`. Không dùng bản rõ cho BRG.
14. **Git:** repo `workforce-graph-docs`, thư mục `discovery/`, nhánh `main`, sau khi được nhắc repo đang **công khai** (có GitHub Pages) và Doc 2 là tài liệu nội bộ.

---

## 3. Hai khách hàng: số liệu và luận điểm chính

### BRG (Việt Nam)
- Hệ sinh thái tư nhân đa ngành, gần **22.000** nhân viên (phạm vi có gồm SeABank hay không cần xác nhận), hàng chục công ty thành viên và liên doanh. Lĩnh vực: tài chính – ngân hàng (SeABank, hơn 5.300 nhân viên), bán lẻ – thương mại (BRGMart, FujiMart, Hapro, Intimex), bất động sản – đô thị (Thành phố thông minh Bắc Hà Nội: 4,2 tỷ USD, gần 272 ha, khởi công 19/8/2025, liên doanh Sumitomo), golf, khách sạn – nghỉ dưỡng, vui chơi giải trí (BRIGHTPARK).
- FujiMart: mục tiêu thêm 50 cửa hàng đến 2028. Học viện SeABank: 1.541 khóa học năm 2025, trung bình 62 giờ mỗi người. Tiền lệ Hapro (2018): toàn bộ nhân viên tiếp tục làm việc.
- Tín hiệu thị trường: hơn 21% ngân hàng tiếp tục giảm nhân sự (khảo sát NHNN quý I/2025); bán buôn – bán lẻ thuộc nhóm chịu tác động AI cao nhất (ILO); khách sạn cần khoảng 60.000 lao động mỗi năm, đào tạo đáp ứng khoảng 20.000 (Hoteljob.vn).
- Ràng buộc pháp lý: Bộ luật Lao động 2019 Điều 29, 33 (điều chuyển tạm thời tối đa 60 ngày làm việc/năm khi không có đồng ý), Điều 42, 44 (ưu tiên đào tạo lại); Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 1/1/2026), Điều 25; Nghị định 356/2025/NĐ-CP (hồ sơ đánh giá tác động gửi A05); Luật Trí tuệ nhân tạo (hiệu lực 1/3/2026).
- Bài toán: dịch chuyển nhân sự từ vị trí thu hẹp (ngân hàng, bán lẻ) sang vị trí thiếu hoặc mới (khách sạn – golf, đô thị thông minh) qua nhiều pháp nhân, có đồng ý.
- Ba luồng hoạt động trong bộ BRG: (1) Phát triển cá nhân, (2) Dịch chuyển nội bộ, (3) Chiến lược nhân lực. Bảy vai trò: nhân viên, quản lý trực tiếp, người đăng tuyển, nhân sự pháp nhân, nhân sự tập đoàn, Ban Tổng giám đốc, quản trị hệ thống.
- PoC 12 tuần: 200–300 nhân viên, 20–30 vị trí đích, 2–3 công ty tại Hà Nội; SeABank tham gia giai đoạn 2; 4 tuần đầu dùng dữ liệu ẩn danh; hai điểm quyết định.

### Toho Gas (Nhật Bản)
- 6.131 nhân viên hợp nhất (3/2026): gas 3.391; LPG và năng lượng khác 1.284; điện 196 (~3%); khác 1.260. Công ty mẹ khoảng 970 người, thâm niên bình quân 14,7 năm, tỷ lệ nghỉ việc 1,93% (FY2024).
- Kế hoạch trung hạn 2025–2027: đầu tư mảng chiến lược khoảng 130 tỷ yên, mảng lõi khoảng 110 tỷ yên. 224 DX人材 (mục tiêu 200). Chế độ nhân sự mới từ 4/2026. Graffer AI Studio cho khoảng 1.500 người ở khoảng 30 công ty nhóm.
- Bối cảnh ngành: tự động hóa (smart meter, drone), điện và năng lượng tái tạo, trung hòa carbon (e-methane, hydrogen), dịch vụ khách hàng số; thiếu 保安人材 (METI). WEF: 39% kỹ năng cốt lõi thay đổi đến 2030; IPA: 85,1% doanh nghiệp Nhật thiếu nhân lực DX.
- 5 Whys (giả thuyết, nay ở phụ lục A5): vì sao mảng điện mới có 196 người → gốc: [Inference] thiếu dữ liệu công việc – kỹ năng và quy tắc bàn giao khi điều chuyển.
- Tuân thủ: 個人情報保護法 Điều 27 (共同利用: thông báo trước) và Điều 28 (cung cấp cho bên ở nước ngoài; đội Việt Nam dùng dữ liệu ẩn danh); mức tối thiểu nhân lực 保安 theo quy định và chuẩn nội bộ.
- Bốn luồng theo hai phase: Phase 1 (1) Lộ trình phát triển, (2) An toàn và kế thừa; Phase 2 (3) Tuyển dụng nội bộ 社内公募, (4) Chiến lược nhân lực (danh mục nhân sự). Tám vai trò: nhân viên, cấp trên, người đăng tuyển, nhân sự công ty, nhân sự tập đoàn, ban giám đốc, Văn phòng DX, quản trị.

### Kiến trúc và luồng dữ liệu (dùng chung, nguồn: Doc 1, Doc 3, nghiên cứu Toho Gas)
- **Workforce Graph 7 lớp:** bối cảnh kinh doanh, năng lực, tổ chức và vị trí, từ điển kỹ năng, con người và bằng chứng, mạng lưới, phát triển tương lai. BRG thêm lớp pháp nhân và đồng ý; Toho Gas thêm lớp công ty trong nhóm (出向) và nhãn vị trí 保安. Graph chỉ lưu mã ẩn danh; dữ liệu định danh lưu riêng, có mã hóa (BRG: tách theo pháp nhân).
- **Lớp AI:** trích xuất kỹ năng từ văn bản, chuẩn hóa về từ điển, ghép nối có giải thích, gợi ý lộ trình; mọi gợi ý có người xác nhận và được ghi vết.
- **Data flow 8 chặng:** nguồn → cổng pháp lý ◆ → chuẩn hóa → AI trích xuất kỹ năng → người xác nhận ◆ → Workforce Graph → suy luận, mô phỏng → người quyết định ◆; phản hồi sau 90 ngày và 12 tháng cập nhật graph.
- **Năm nguyên tắc AI:** con người quyết định; giải thích được; không chấm điểm trừ; bảo vệ dữ liệu; truy vết được.

### Phương pháp first principles (nay ở phụ lục của cả hai bộ)
Năm yếu tố nền tảng: **Nhu cầu** (giờ công việc), **Nguồn lực** (kỹ năng có bằng chứng), **Lộ trình** (kỹ năng kề cận), **Ràng buộc** (điều kiện cứng chạy trước khi xếp hạng), **Động lực**. Workshop nửa ngày (khoảng 3,5 giờ), 5 phiên: Kết quả cần đạt 30' · Giả định 45' · Ràng buộc thực tế 60' · Xây dựng phương án 45' · Kiểm chứng, phạm vi PoC 30'.

---

## 4. Tài liệu và artifact trên claude.ai

Các liên kết dưới đây **riêng tư theo tài khoản chủ sở hữu**; tài khoản khác chỉ mở được khi chủ sở hữu chia sẻ. Nếu không mở được, dùng bản PDF và mã nguồn trong repo.

| Tài liệu | Liên kết | ID nội bộ |
|---|---|---|
| Doc 1 · BRG — Career Development trong bối cảnh AI | https://claude.ai/artifact/LFnxPaaTz6GyNxnNjEruf1 | project `9bee5e3a-f7a9-441f-8f72-1af6216f0864`, tab `1f31ce92-6381` |
| Doc 2 · BRG và Toho Gas — khác biệt bài toán và khoảng cách năng lực (nội bộ) | https://claude.ai/artifact/3y3XDFzwjNjYiCNRYh7xSE | project `18057b63-c008-4a65-bd5b-13fc2f2541c3`, tab `fa90a7a9-eaef` |
| Doc 3 · Data flow và tri thức doanh nghiệp | https://claude.ai/artifact/PnXs8NL381BYBXLUd5Rc8K | project `b8848a7b-6395-4b71-a37d-c0a04e389e54`, tab `f67a94fb-b24d` |
| Doc 4 · First principles | https://claude.ai/artifact/J6vs8y4uVA9bBbFmZeUXgB | project `8a7f456d-ee81-4c0a-b4c2-2e4561f850a0`, tab `46d51631-b64d` |
| Tài liệu "BRG và Toho Gas — phân tích giải pháp: phần dùng chung và phần đặc thù" | https://claude.ai/artifact/Uteqea6diUDjBmHyRcq2pL | slug `e1dcfebb-a609-439d-af85-3e64bcbbbd8d` (có trên tài khoản; nội dung chưa được đối chiếu trong phiên cập nhật này) |
| Slide BRG | https://claude.ai/artifact/WNZocWXGjQCUHFyWnRT19B | slug `eddbdb35-5a5b-4b2b-a6c7-51c35a3993ca`, bản v3.4: `1795566682-0a48` |
| Slide Toho Gas | https://claude.ai/artifact/MzfgagwLnMp4KcZfksb5Uy | slug `aa0401c9-a65c-4ed4-b87c-61f333d53bb6`, bản v3.4: `1795566684-75f3` |

- Kiểu artifact Slides: slug `3e9dc3d6-8a10-4143-ac0b-5af4f2b03a61`.
- Ảnh đã tải lên (URL nằm trong `decks/<deck>/blobs.json`, bản gốc trong `decks/<deck>/assets/`):
  - BRG (bản làm mờ): `brg-menu` `/_blob/ec88d7060eddc75f5912b8fd32a9f21f` · `brg-idp` `/_blob/2c8007c71773679a0519958a0cc3ac9f` · `brg-match` `/_blob/0c77d0e0c2f7fd2cdb4a9d88d2999795` · `brg-context` `/_blob/3a56386a332a8a08012c0b644b15d3ba`.
  - Toho Gas: `my-path` `/_blob/00c6a13404590bb8093cbf52a18cb676` · `portfolio` `/_blob/5252daa08947e1689d35526ff366a1ac` · `safety` `/_blob/ab5dbd4857bca9c5a59a60b000b45285` · `tf-match` `/_blob/e63daeb707cb4f93161b75f7bd2514c4` · `tf-menu` `/_blob/3e7df7313fb75db4907a6f2b087e9e36`.
- Phiên bản ghi ở trên là bản đăng cuối của phiên này; trước khi đăng lại, lấy phiên bản hiện hành bằng `get_artifact` hoặc `list_files` (người dùng có thể đã sửa trong trình chỉnh sửa).

---

## 5. Cấu trúc bộ slide và hệ thống thiết kế

### Thứ tự slide (v3.2)
- **BRG** (`decks/brg/project/deck.json`)
  - Chính: `cover`, `context`, `brg-today`, `problem`, `talent-flow`, `roles`, `flow-dev`, `flow-mobility`, `flow-strategy`, `architecture`, `data-flow`, `ai`, `compliance`, `poc`, `kpi`, `next-steps`, `thanks`.
  - Phụ lục: `ap-architecture` (A1 kiến trúc tổng thể), `ap-problems` (A2 bảy vấn đề), `ap-principles` (A3 first principles), `ap-matrix` (A4 ma trận nguồn – đích), `ap-roles` (A5 phân quyền), `ap-mobility` (A6 dịch chuyển nội bộ: 75%/56%, ràng buộc), `ap-legal` (A7 pháp lý theo điều khoản), `ap-sources` (A8 nguồn).
- **Toho Gas** (`decks/toho/project/deck.json`)
  - Chính: `cover`, `context`, `toho-today`, `problem`, `talent-flow`, `roles`, `flow-dev`, `flow-safety`, `flow-mobility`, `flow-strategy`, `architecture`, `data-flow`, `ai`, `compliance`, `roadmap`, `kpi`, `next-steps`, `thanks`.
  - Phụ lục: `ap-architecture` (A1 kiến trúc tổng thể), `ap-usecases` (A2), `ap-roles` (A3), `ap-matrix` (A4), `ap-five-whys` (A5), `ap-principles` (A6), `ap-problems` (A7), `ap-sources` (A8).
- Kiến trúc tổng thể (phụ lục A1): người dùng → Talent Flow (6 module nghiệp vụ M1–M6, dịch vụ AI, dữ liệu, tích hợp) → hệ thống hiện có; kèm dải quản trị và hạ tầng.
- Ánh xạ trang bắt buộc: vai trò = `roles`; luồng kèm minh họa = `flow-*` (mỗi trang một ảnh màn hình + timeline dọc); kiến trúc tri thức = `architecture`; data flow = `data-flow`; nguyên tắc AI = `ai`; tuân thủ = `compliance`.

### Định dạng file (kiểu Slides)
- `project/deck.json` (v5, `lists: "css"`, `format.shared: ["project/deck.css"]`, `order`, `sections`, `faces`).
- `project/deck.css`: phần quy tắc nền + khối `Visual components (v3)` sinh từ `decks/gen/visual.css`.
- `project/slides/<id>.html`: mỗi file đúng một `<section id="<id>">`, ghi chú người trình bày trong `<aside>` cuối section (≤ 4.000 ký tự).
- Khung 1920×1080; lề 128px (dưới 160px cho footer); không đặt nội dung dưới y = 920 ngoài footer; chữ tối thiểu 24px; ≤ 200 phần tử, ≤ 15 tầng `div` mỗi slide.
- Phông: Barlow Semi Condensed (tiêu đề, số), Be Vietnam Pro (nội dung), Noto Sans JP (chữ Nhật, bộ Toho Gas).

### Quy tắc đường nối (quan trọng, rút ra từ lỗi phản hồi 3)
- Trình xem Slides vẽ phần tử `position:absolute` nằm trong một `div` có `position:relative` **đè lên** nội dung flow của div đó, kể cả khi đặt trước trong mã. Vì vậy **không ghim đường nối** trên các khối.
- Mọi đường nối là **phần tử flow nằm giữa** các khối, không giao nhau với khối nào:
  - Timeline ngang `timeline()`: mỗi bước có đoạn kẻ trái/phải (`.tl-ln`) nằm cạnh chấm, không chạy dưới chấm.
  - Timeline dọc `vtimeline()`: đoạn kẻ (`.vt-ln`) nằm dưới chấm, trong cùng hàng.
  - Sơ đồ hub `rounded_bus()`: SVG flow đặt trong ô lưới riêng giữa thẻ và vòng tròn, đường gấp khúc bo góc (bán kính 12px). Thẻ có chiều cao cố định 104px để điểm giữa cạnh trùng đầu đường.
  - Data flow `_bend_svg()`: dải SVG flow giữa hai hàng (nối chặng 4 → 5) và dưới hàng hai (phản hồi chặng 8 → 6), góc bo.
  - Mũi tên giữa thẻ: `<x-shape kind="arrow-right|arrow-down|arrow-up">` trong flow.
  - Bìa `cover_slide()`: một `<svg>` nền (ghim, đặt đầu tiên) vẽ dòng chảy; nhãn là `<p>` ghim đặt ở vùng trống cạnh đầu mỗi dòng, không đè lên nét vẽ.
- **Căn giữa chữ trong `<p>`:** không dùng `display:flex` (Slides bỏ qua); dùng `text-align:center` và `line-height` bằng chiều cao hộp. Căn giữa bằng flex chỉ dùng cho `<div>`.

### Màu và thành phần
- Navy `#14203C`, navy phụ `#22325A`, nền `#F3F4F7`, thẻ `#FCFCFD`, viền `#DDE2EA`, chữ phụ `#4A5568`/`#5B6478`, cam `#FCA010` (hình, nền), cam đậm `#A85A00` (chữ trên nền sáng), nền cam nhạt `#FFF3DF`.
- Thành phần v3.2 (trong `visual.css`, thêm `.sa-*` kiến trúc tổng thể, `.cv-*` bìa): `.ic` icon tròn; `.num`, `.stat`, `.cap`, `.lbl`, `.pill`, `.band`; `.tl*` timeline ngang; `.vt*` timeline dọc; `.roles/.role` ô vai trò; `.ly/.ly-t/.ly-n/.nd/.gov/.lyc` kiến trúc lớp; `.df*` data flow; `.law/.lawtag/.feat/.meter/.mini` tuân thủ; `.hbar`, `.share`, `.maprow`, `.gantt`, `.shot`.
- Dấu **◆** đánh dấu bước có người có thẩm quyền phê duyệt; chấm cam trên timeline = bước phê duyệt.

### Mã sinh slide (`decks/gen/`)
- `lib.py`: icon, header, section, `timeline`, `vtimeline`, `shot`, `rounded_bus`.
- `blocks.py`: builder dùng chung cho hai bộ: `overview_slide`, `roles_slide`, `flow_slide`, `arch_slide`, `dataflow_slide`, `ai_slide`, `compliance_slide`, `problems_slide`, `system_arch_slide` (kiến trúc tổng thể), `cover_slide` (bìa).
- `brg.py`, `toho.py`: nội dung từng bộ; đọc URL ảnh từ `../<deck>/blobs.json`. Không ghi đè: `thanks` và các phụ lục chuyển từ bản cũ (BRG: `ap-principles`, `ap-matrix`, `ap-roles`, `ap-legal`, `ap-sources`; Toho Gas: `ap-usecases`, `ap-roles`, `ap-matrix`, `ap-five-whys`, `ap-principles`, `ap-sources`). Các slide này sửa trực tiếp HTML.
- Chạy từ thư mục `decks/`:
  - `python3 gen/brg.py` · `python3 gen/toho.py` (ghi vào `<deck>/project/slides/`).
  - `python3 gen/build_css.py brg toho` (dựng lại `deck.css` sau khi sửa `visual.css`).
  - `python3 render/render.py brg out/brg [id ...]` (cần Playwright, Pillow): in `maxBottom` từng slide, phải ≤ 920; tạo `out/brg-sheet.png`. `blobmap.json` ánh xạ URL ảnh sang file trong `assets/`. Bản xem trước vẽ `x-icon`, `x-shape` thành ô màu; trình xem thật vẽ đúng hình.

### Đăng lên artifact
- Chủ sở hữu hiện tại: `publish_files` với `slug`, `base_version` (phiên bản hiện hành), `mode: "patch"`, danh sách `{as: "project/...", path: <đường dẫn cục bộ>}`; xóa slide cũ bằng `remove`.
- Tài khoản khác: `create_from_type` với slug kiểu Slides; `upload_asset` các ảnh trong `assets/`; cập nhật URL mới vào `blobs.json` và `blobmap.json`; chạy lại `gen/*.py`; đăng `deck.json`, `deck.css` và toàn bộ slide.

---

## 6. Quy tắc văn phong và trình bày (bắt buộc)

Theo cách diễn đạt của AINAVI Introduction:
- Tiêu đề là mệnh đề hoàn chỉnh hoặc mẫu "Từ … đến …"; nhãn mục viết hoa (`VAI TRÒ THAM GIA`, `TRONG TALENT FLOW`…); gạch đầu dòng là cụm từ ngắn, đủ nghĩa.
- **Không dùng từ văn nói:** "ở cả", "rồi", "thì", "mà", "thấy", "chuyển người", "đúng việc", "ra sao". Không dùng ẩn dụ khó hiểu: "hội tụ một lõi", "nguyên tố", "cửa quyết định".
- Thuật ngữ chuẩn: **vị trí** (không dùng "job" trong câu tiếng Việt), dịch chuyển / bố trí / điều chuyển nhân sự nội bộ, khoảng trống kỹ năng, hồ sơ kỹ năng, khung năng lực, lộ trình phát triển, người có thẩm quyền phê duyệt, ghi nhật ký.
- Giữ nguyên bốn câu hỏi của Talent Flow ("Tổ chức cần gì? Hiện có gì? Còn thiếu gì? Cần làm gì?").
- **Trang chính tổng quan; chi tiết vào phụ lục** và ghi chú người trình bày. Mỗi trang một ý chính, ưu tiên sơ đồ, số liệu lớn, ảnh màn hình thay cho khối chữ.
- Suy luận ghi nhãn **[Inference]** ở đầu câu; không trình bày suy luận như sự thật. Các từ như "đảm bảo", "loại bỏ hoàn toàn", "không bao giờ" chỉ dùng khi có nguồn. Con số minh họa giao diện (ví dụ 45/60 ngày ở trang tuân thủ BRG) phải ghi "Ví dụ".
- Ghi nguồn số liệu ở slide (dòng ghi chú) hoặc trong ghi chú người trình bày.

---

## 7. Việc tiếp theo đề xuất

1. Điền thông tin người liên hệ trên slide cảm ơn của hai bộ.
2. Mở hai bộ slide trong trình xem Slides, rà các trang mới (bìa, hub `brg-today`, `flow-*`, `architecture`, `data-flow`, `compliance`, `ap-architecture`) để xác nhận đường nối, số trong vòng tròn, icon và mũi tên hiển thị như bản xem trước.
3. Xác nhận với khách hàng các câu hỏi mở (mục 8) trước workshop; cập nhật số liệu nếu có dữ liệu nội bộ.
4. Tùy nhu cầu: xuất PDF/PPTX từ menu của artifact để gửi khách hàng; chuyển các phụ lục dạng bảng sang dạng trực quan.
5. Khi làm mới nội dung: sửa nguồn trong `gen/*.py` (hoặc HTML với slide sửa tay), chạy xem trước, rồi đăng lại.

## 8. Câu hỏi mở với khách hàng

- **BRG:** nhu cầu nhân sự của dự án mới 2027–2028; nơi lưu dữ liệu nhân sự, đào tạo và mức độ sẵn có của mô tả công việc; quyền dữ liệu và quyết định nhân sự tại khách sạn do hãng quốc tế quản lý; chính sách hợp đồng, thâm niên khi chuyển công ty trong tập đoàn; đơn vị đầu tư và người quyết định; con số 22.000 có gồm SeABank hay không; danh sách hệ thống cần tích hợp.
- **Toho Gas:** nhu cầu nhân sự mảng điện, nước ngoài, giải pháp đến 2027 và giữa thập niên 2030; vị trí thu hẹp do smart meter, RPA (mục tiêu 700 quy trình), AI tạo sinh; hệ thống nhân sự lõi và tiến độ chuyển SAP S/4HANA Cloud (theo báo chí, cần xác nhận); phạm vi dữ liệu (công ty mẹ hay toàn nhóm); thông báo 共同利用 hiện có; danh sách vị trí 保安 bắt buộc và số người đủ điều kiện; thời điểm tham vấn công đoàn; khả năng dùng Graffer AI Studio làm giao diện hỏi đáp.

## 9. Git và lưu ý bảo mật

- Repo: `https://github.com/astragenxy-bit/workforce-graph-docs`, nhánh `main`, thư mục `discovery/`. Repo **công khai** và có GitHub Pages: mọi file trong thư mục này có thể được người ngoài đọc.
- Doc 2 (PDF và `text/brg-toho-comparison.txt`) là tài liệu **nội bộ**, nêu tên khách hàng khác và khoảng cách năng lực; người dùng đã chọn đưa vào repo sau khi được nhắc. Cân nhắc chuyển repo sang riêng tư hoặc gỡ file này nếu cần.
- `decks/*/assets/` chứa ảnh màn hình Talent Flow (dữ liệu mẫu bản thí điểm Toho Gas; bản BRG đã làm mờ) để tài khoản khác dựng lại bộ slide. Cùng lưu ý repo công khai.
- Không đưa vào repo: file gốc AINAVI Introduction và Giới thiệu Talent Flow (do người dùng cung cấp, có thông tin thương mại); ảnh mẫu tham khảo trong thư mục ảnh của người dùng.
- Môi trường Cowork không cho phép `git push`; commit được tạo trên máy người dùng, người dùng tự chạy `git push`.
