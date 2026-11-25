# BRG — Career Development trong bối cảnh AI: nghiên cứu và giải pháp

Nov 24, 2026 · @Thu Phan Thi

## 0. Tóm tắt điều hành

**Bài toán:** AI đổi task trong job nhanh hơn xóa job. Ở Việt Nam khoảng 11,5 triệu lao động (1/5 việc làm) có task chịu tác động của AI tạo sinh, nặng nhất ở tài chính, bán lẻ và văn phòng (ILO, 4/2026). Hệ sinh thái BRG có cả ba mảng này, đồng thời có khách sạn – golf thiếu người và các dự án mới cần người. \[Inference\] Cách nhanh và ít rủi ro nhất để có đúng người là **chuyển đổi người đang có** trong hệ sinh thái.

**BRG đang ở đâu:**

- **Quy mô và đa dạng:** gần 22.000 nhân viên, hàng chục công ty thành viên và liên doanh; golf, khách sạn, bán lẻ, bất động sản, giải trí; SeABank trong hệ sinh thái. Nhiều đơn vị từng có vốn nhà nước (Hapro, Thăng Long GTC, Intimex) và liên doanh với Sumitomo.
- **Có nền móng:** khi nhận Hapro (2018), BRG cam kết giữ toàn bộ nhân viên và sắp xếp lại theo năng lực. SeABank có học viện riêng, trung bình 62 giờ đào tạo/người, 90,5% nhân viên muốn gắn bó ít nhất 2 năm. BRG, SeABank và ĐHQG Hà Nội đã ký hợp tác khoa học công nghệ.
- **Điểm còn thiếu:** \[Unverified\] nguồn công khai không cho thấy kế hoạch nhân lực hay chiến lược AI cấp tập đoàn, không có số liệu nhân sự ngoài SeABank, không rõ cơ chế chuyển người giữa công ty thành viên. Tháng 9/2026, Chủ tịch Quốc hội đề nghị BRG và SeABank đẩy mạnh chuyển đổi số và ứng dụng AI.

**Nhận định:** \[Inference\] BRG không thiếu chương trình đào tạo. BRG thiếu một **vòng khép kín cấp hệ sinh thái** nối kế hoạch kinh doanh với job nội bộ, skill của từng người, lộ trình học và cơ hội được bố trí, qua ranh giới các pháp nhân. Khác Nhật, luật Việt Nam không cho đổi hẳn công việc một chiều và người giỏi dễ nhảy việc, nên dịch chuyển phải tự nguyện, minh bạch và đủ hấp dẫn.

**Đề xuất:** xây **thị trường nhân lực nội bộ dựa trên skill** cho hệ sinh thái BRG, chạy trên nền Workforce Graph (module Career Development của AINAVI): (1) kiến trúc job và từ điển skill theo khung Việt Nam và quốc tế (Khung năng lực số TT 02/2025, VTOS/ACCSTP, SFIA 9); (2) hồ sơ skill có bằng chứng; (3) danh mục nhân sự động theo kịch bản kinh doanh; (4) định hướng nghề nghiệp cá nhân; (5) ghép nối nội bộ qua tuyển nội bộ, dự án và chuyển công ty có thỏa thuận; (6) đo kết quả và lưu hồ sơ ưu tiên đào tạo lại. AI chỉ đề xuất, con người quyết định, theo Bộ luật Lao động, Luật Bảo vệ dữ liệu cá nhân và Luật Trí tuệ nhân tạo.

**Bước đầu:** PoC 12 tuần trên một cặp "nguồn – đích" ở khu vực Hà Nội (ví dụ thu ngân và văn phòng khối bán lẻ sang FujiMart mới, khách sạn – golf và job số), khoảng 200–300 nhân viên, 2–3 công ty thành viên; lập hồ sơ đánh giá tác động dữ liệu ngay tuần đầu.

## 1. Bối cảnh 1: AI và tự động hóa tạo job mới, đổi skill của job cũ

Ở Việt Nam, AI chủ yếu đổi task bên trong job, ít xóa hẳn job. Nhóm chịu tác động mạnh nhất là tài chính, bán lẻ và văn phòng, tức là các mảng lớn trong hệ sinh thái BRG. \[Inference\]

### 1.1 Toàn cầu

- Theo [WEF Future of Jobs Report 2025](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/) (hơn 1.000 nhà tuyển dụng, hơn 14 triệu lao động, 55 nền kinh tế): giai đoạn 2025–2030 có **170 triệu job mới** và **92 triệu job bị thay thế**, ròng tăng 78 triệu.
- Trung bình **39% skill hiện có** sẽ thay đổi hoặc lỗi thời đến 2030. 63% nhà tuyển dụng coi khoảng trống skill là rào cản lớn nhất; 85% ưu tiên nâng cấp skill.
- Về AI: 50% nhà tuyển dụng định hướng lại kinh doanh, 2/3 tuyển người có skill AI, 40% dự kiến giảm người ở nơi AI tự động hóa được.
- Job giảm nhanh nhất: giao dịch viên ngân hàng, nhập liệu, nhân viên bưu chính. Giảm nhiều nhất về số lượng: văn thư – thư ký, thu ngân, bán vé, trợ lý hành chính.

Ý nghĩa: danh sách job giảm của WEF gần như là các vị trí tuyến đầu của quầy giao dịch, siêu thị, lễ tân khách sạn và sân golf. \[Inference\] Bài toán chính là **người đang làm job cũ cần skill mới**.

### 1.2 Việt Nam

- [ILO (16/4/2026)](https://www.ilo.org/resource/news/generative-ai-could-transform-millions-jobs-viet-nam-new-ilo-brief-shows): khoảng **11,5 triệu lao động (1/5 việc làm)** ở nghề có task chịu tác động của AI tạo sinh. Rủi ro tự động hóa toàn phần dưới 2% lực lượng lao động. Kịch bản chính là **đổi task**, không phải mất job hàng loạt.
- Phơi nhiễm cao nhất: tài chính – bảo hiểm, bán buôn – bán lẻ, thông tin – truyền thông. Gần 2/3 lao động văn phòng – hỗ trợ làm nghề dễ bị tự động hóa task nhất. Nữ 24,1%, nam 17,8%. Hà Nội, TP.HCM, Đà Nẵng chiếm hơn 1/3 số job chịu tác động.
- ILO khuyến nghị đối thoại xã hội tại nơi làm việc khi đưa AI vào, và đầu tư skill cho nhóm chịu tác động nhiều nhất.
- &#91;Unverified\] [VnEconomy (7/4/2026)](https://vneconomy.vn/ai-dang-thay-doi-luat-choi-trong-quan-tri-nhan-luc.htm) viết: Việt Nam xếp thứ 38 thế giới về tỷ lệ người dùng AI; ứng dụng AI của doanh nghiệp tăng 39% năm 2025. Bài không nêu nguồn số liệu.
- Khung pháp lý mới: [Luật Trí tuệ nhân tạo](https://daibieunhandan.vn/quoc-hoi-thong-qua-luat-tri-tue-nhan-tao-10399959.html) (8 chương, 35 điều) thông qua 10/12/2025, hiệu lực 1/3/2026. Luật phân loại hệ thống AI theo rủi ro; rủi ro cao là hệ thống có thể gây thiệt hại đáng kể đến quyền và lợi ích hợp pháp của con người. Luật Bảo vệ dữ liệu cá nhân hiệu lực 1/1/2026 (xem 5.3).

**Ngôn ngữ skill chung.** \[Unverified\] Chưa tìm thấy một chuẩn skill số cho doanh nghiệp được dùng rộng rãi như DSS ở Nhật. Các khung đang có để ghép lại:

- [Khung năng lực số cho người học](https://vneconomy.vn/bo-giao-duc-va-dao-tao-ban-hanh-khung-nang-luc-so-cho-nguoi-hoc.htm) (Thông tư 02/2025/TT-BGDĐT, hiệu lực 11/3/2025): 6 miền, 24 năng lực thành phần, 8 bậc; miền thứ 6 là **ứng dụng trí tuệ nhân tạo**.
- Du lịch – khách sạn: VTOS (Việt Nam) và [ACCSTP của ASEAN](https://doanhnghiephoinhap.vn/tp-ho-chi-minh-muon-chuan-hoa-nhan-luc-khach-san-theo-chuan-asean-148551.html) với 242 đơn vị năng lực, 32 chức danh; cùng tiêu chuẩn kỹ năng nghề quốc gia.
- Skill số và AI chuyên sâu: [SFIA 9](https://sfia-online.org/en/sfia-9/sfia-9-release-notes) (công bố 30/10/2024), có nhóm skill AI và dữ liệu.

### 1.3 Các ngành của BRG

Job đang đổi theo bốn mảng. Cột skill mới là suy luận từ nguồn ngành. \[Inference\]

| Mảng | Job đang đổi | Skill mới cần | Tín hiệu thị trường |
| --- | --- | --- | --- |
| Ngân hàng (SeABank) | Giao dịch viên, nhập liệu, hỗ trợ gián tiếp → kênh số, callbot | Tư vấn dựa trên dữ liệu, vận hành kênh số, quản trị rủi ro dữ liệu | [Khảo sát NHNN quý I/2025](https://vietnamfinance.vn/ngan-hang-chuyen-doi-so-bao-gio-moi-dung-sa-thai-nhan-su-d128861.html): hơn 21% ngân hàng tiếp tục giảm người. [Sacombank 18.088 → 16.816 người, VIB 11.736 → 10.278 người](https://www.dnse.com.vn/senses/tin-tuc/ngan-hang-o-at-cat-giam-hang-ngan-nhan-su-ai-co-phai-la-thu-pham-chinh-35224497) (cuối 2024 → cuối 2025) |
| Bán lẻ (BRGMart, FujiMart, Hapro) | Thu ngân, nhập liệu kho, đặt hàng thủ công | Vận hành đa kênh, dự báo nhu cầu, quản lý hàng tươi bằng dữ liệu | ILO: bán buôn – bán lẻ thuộc nhóm phơi nhiễm cao nhất; WEF: thu ngân giảm nhiều nhất về số lượng |
| Khách sạn – golf – giải trí | Lễ tân, đặt phòng và tee time, tổng đài → đặt chỗ online, chatbot | Quản trị doanh thu, CRM, ngoại ngữ, dịch vụ cá nhân hóa | [Cần khoảng 60.000 lao động/năm, đào tạo cung cấp khoảng 20.000](https://theleader.vn/diem-nghen-lon-nhat-cua-nganh-du-lich--khach-san-da-nang-trong-giai-doan-tang-truong-moi-d47481.html) (Hoteljob.vn). [Khách sạn từ khoảng 780.000 lao động trước dịch còn khoảng 300.000 năm 2024](https://baodautu.vn/cong-bo-top-10-noi-lam-viec-tot-nhat-viet-nam-nganh-du-lich---khach-san---resort-d437620.html) |
| Bất động sản – đô thị thông minh | Kinh doanh và vận hành tòa nhà truyền thống | Năng lượng thông minh, quản trị đô thị số, đo phát thải và ESG | [Thành phố thông minh Bắc Hà Nội](https://viettimes.vn/chinh-thuc-khoi-cong-du-an-thanh-pho-thong-minh-bac-ha-noi-post188719.html): 6 nhóm giải pháp thông minh, mục tiêu trung hòa carbon |

BRG vì vậy vừa có job thu hẹp (quầy, thu ngân, văn phòng), vừa có job thiếu người (khách sạn, golf, dự án mới). \[Inference\] Đây là điều kiện để chuyển người trong nội bộ thay vì vừa cắt vừa tuyển.

## 2. Bối cảnh 2: doanh nghiệp Việt Nam tuyển, phát triển và tái cơ cấu nhân sự thế nào

Khác Nhật, doanh nghiệp Việt Nam được cho thôi việc khi đổi công nghệ, nhưng luật buộc ưu tiên đào tạo lại. Mọi thay đổi công việc lâu dài cần người lao động đồng ý. Vì vậy dịch chuyển nội bộ ở Việt Nam phải là lựa chọn tự nguyện và đủ hấp dẫn. \[Inference\]

### 2.1 Khác mô hình Nhật ở đâu

| Khía cạnh | Nhật (tham chiếu bản Toho Gas) | Việt Nam |
| --- | --- | --- |
| Tuyển dụng | Tuyển đồng loạt sinh viên mới, không ghi rõ công việc | \[Inference\] Tuyển theo vị trí, nhiều người có kinh nghiệm; BRG có cả chuyên gia nước ngoài ([BRG](https://www.brggroup.vn/about-us.html)) |
| Nghỉ việc | Rất thấp (Toho Gas 1,93%) | [Talentnet–Mercer 2025](https://www.sggp.org.vn/tu-du-lieu-den-con-nguoi-5-dieu-can-biet-cho-chien-luoc-dai-ngo-thoi-ai-post820176.html): trung bình 9,8% ở doanh nghiệp nội, 6,6% ở doanh nghiệp đa quốc gia. [Khách sạn Đà Nẵng](https://theleader.vn/diem-nghen-lon-nhat-cua-nganh-du-lich--khach-san-da-nang-trong-giai-doan-tang-truong-moi-d47481.html): 18,9%; 25% đơn vị từ 30% trở lên |
| Cắt giảm | Hạn chế lạm dụng quyền sa thải; thông lệ giữ việc | [Bộ luật Lao động 2019, Điều 42](https://baolaocai.vn/nghi-viec-vi-ly-do-thay-doi-co-cau-nguoi-lao-dong-duoc-huong-quyen-loi-gi-post373268.html): khi đổi cơ cấu, công nghệ phải có phương án sử dụng lao động; có chỗ làm mới thì **ưu tiên đào tạo lại**; trao đổi với tổ chức đại diện người lao động, báo trước 30 ngày cho UBND tỉnh; trợ cấp mất việc 1 tháng lương/năm, tối thiểu 2 tháng |
| Điều chuyển | Công ty quyết định (人事異動) | [Điều 29](https://www.careerlink.vn/cam-nang-viec-lam/goc-ky-nang/cach-ung-xu-khi-bi-dieu-chuyen-cong-viec): chuyển tạm thời tối đa 60 ngày làm việc cộng dồn/năm nếu không có đồng ý; giữ lương cũ 30 ngày làm việc, sau đó ít nhất 85%. Đổi hẳn công việc phải thỏa thuận sửa hợp đồng (Điều 33) |
| Trong nhóm công ty | Biệt phái (出向), chuyển hẳn (転籍) phổ biến | [Mỗi công ty trong tập đoàn có quyền và nghĩa vụ của doanh nghiệp độc lập](https://thuviennhadat.vn/phap-luat/cong-ty-khong-chi-tra-tro-cap-thoi-viec-la-dung-hay-sai-597467.html). \[Inference\] Chuyển hẳn giữa công ty thường là chấm dứt hợp đồng cũ, ký hợp đồng mới; cần luật sư xác nhận |
| Thị trường | Thiếu người do dân số già | Tuyển dụng thận trọng: 35% doanh nghiệp định tuyển thêm năm 2026, 47,7% giữ nguyên quy mô; lương tăng 6,2–6,3%, thấp nhất 10 năm (Talentnet–Mercer 2025) |

### 2.2 Doanh nghiệp Việt Nam đang ứng phó AI thế nào

- **Ngân hàng: giảm ở mảng hỗ trợ, tuyển ở mảng số.** [28 ngân hàng niêm yết giảm hơn 3.000 người trong quý I/2026](https://thitruongtaichinhtiente.vn/print/82920.html), trong khi tuyển dữ liệu, AI, an ninh mạng tăng. VietinBank gộp phòng ban trùng chức năng và chuyển người sang kinh doanh. \[Inference\] Mô hình chủ đạo vẫn là "giảm rồi tuyển", chuyển đổi nội bộ ít được công bố.
- **FPT: AI-first trong nhân sự.** [Trợ lý nhân sự ảo Maya xử lý hơn 50.000 yêu cầu/tháng của khoảng 13.000 nhân viên](https://baodautu.vn/the-he-nhan-su-mang-ma-gen-ai-first-d430047.html); hơn 1.000 AI agent; mục tiêu 2025 là 80–100% nhân sự dịch vụ CNTT cho thị trường nước ngoài dùng AI thành thạo, khoảng 20% kỹ sư thành kỹ sư ứng dụng AI.
- **Tiền lệ của chính BRG: cam kết giữ người khi tái cơ cấu.** Khi BRG (qua Vinamco) nắm 65% Hapro năm 2018, bà Nguyễn Thị Nga cho biết [toàn bộ nhân viên tiếp tục làm việc và không bị nghỉ việc](https://kisvn.vn/dhdcd-hapro-chu-tich-brg-nguyen-thi-nga-lam-chu-tich-hapro); HĐQT sẽ tái cơ cấu bộ máy từ Phó Tổng giám đốc trở lên và sắp xếp lao động "theo năng lực phù hợp với từng vị trí". Phương án cổ phần hóa trước đó có [630 lao động, 550 chuyển sang công ty cổ phần, 80 dôi dư](https://baodautu.vn/nha-nuoc-se-thoai-toan-bo-von-tai-hapro-ban-65-cho-nha-dau-tu-chien-luoc-d73677.html).

### 2.3 Kết luận cho bài toán

&#91;Inference\] BRG không thể chỉ dùng điều chuyển một chiều kiểu Nhật, vì luật giới hạn và người giỏi dễ nghỉ việc. BRG cũng không nên chỉ dùng "giảm rồi tuyển" như nhiều ngân hàng, vì trái cam kết giữ người tập đoàn từng đưa ra ở Hapro và vì ngành khách sạn – golf đang thiếu người. Cách phù hợp là **thị trường nhân lực nội bộ tự nguyện, dựa trên skill**, có hồ sơ cho thấy tập đoàn đã ưu tiên đào tạo lại trước khi cắt giảm.

## 3. Bối cảnh 3: sau khi phát triển, đưa người vào job nội bộ nào

Người được đào tạo mà không có job đích sẽ rời đi. Ở Việt Nam rủi ro này cao hơn Nhật vì chuyển việc dễ hơn. \[Inference\]

### 3.1 Các cơ chế bố trí nội bộ ở doanh nghiệp Việt Nam

| Cơ chế | Ai chủ động | Cách vận hành | Lưu ý pháp lý |
| --- | --- | --- | --- |
| Bổ nhiệm, điều động theo quy hoạch | Công ty | Lãnh đạo quyết định; phổ biến ở doanh nghiệp gốc nhà nước \[Inference\] | Đổi hẳn công việc phải thỏa thuận (Điều 33) |
| Chuyển tạm thời làm công việc khác | Công ty | Theo nhu cầu sản xuất kinh doanh ghi trong nội quy | Tối đa 60 ngày làm việc/năm nếu không đồng ý (Điều 29) |
| Tuyển dụng nội bộ | Phòng ban cần người | Đăng vị trí và yêu cầu, nhân viên ứng tuyển | Sửa hợp đồng khi trúng tuyển |
| Dự án nội bộ, kiêm nhiệm một phần thời gian | Cả hai | Làm cho đơn vị khác trước khi chuyển hẳn | Thời gian và thù lao cần thỏa thuận \[Inference\] |
| Chuyển công ty trong tập đoàn | Công ty và người lao động | Chấm dứt hợp đồng cũ, ký với công ty mới \[Inference\] | Mỗi công ty là doanh nghiệp độc lập; trợ cấp thôi việc và thâm niên cần xử lý |

### 3.2 Dịch chuyển nội bộ có giữ được người không

- [LinkedIn Global Talent Trends (10/2022)](https://news.linkedin.com/2022/october/talent-connect-2022): người đã chuyển vị trí nội bộ có **75%** khả năng ở lại sau 2 năm, so với **56%** ở người chưa chuyển.
- [PwC Hopes and Fears 2025 – Việt Nam](https://www.pwc.com/vn/vn/publications/vietnam-publications/hopes-fears-vietnam-2025.html) (hơn 1.000 người, công bố 1/2026): 38% người lao động Việt Nam dùng AI tạo sinh hằng ngày (toàn cầu 14%); 74% nói được cung cấp nguồn lực phát triển; 51% có thể đề nghị tăng lương trong 12 tháng tới.
- [Khảo sát 331 đơn vị khách sạn (Hoteljob.vn, 2026)](https://theleader.vn/diem-nghen-lon-nhat-cua-nganh-du-lich--khach-san-da-nang-trong-giai-doan-tang-truong-moi-d47481.html): 203/331 đơn vị cho rằng người nghỉ vì thu nhập hoặc vì job khác hấp dẫn hơn.

Ý nghĩa: người lao động Việt Nam đã dùng AI nhiều và muốn lộ trình rõ. Một bước chuyển nội bộ phải đi kèm thu nhập và triển vọng rõ ràng, nếu không họ sẽ chọn thị trường ngoài. \[Inference\]

### 3.3 Vì sao chuyển nội bộ khó chạy trong một tập đoàn đa ngành

&#91;Inference\] Giả thuyết rút từ bản Toho Gas (Recruit Works) và cấu trúc BRG, cần kiểm chứng:

1. Quản lý giữ người giỏi; phòng đi không bù được chỗ trống.
2. Tiêu chí chọn không minh bạch; người xin chuyển sợ bị xem là thiếu gắn bó.
3. Chuyển giữa công ty thành viên đụng hợp đồng, thâm niên, thang lương và phúc lợi khác nhau.
4. Văn hóa khác nhau: doanh nghiệp gốc nhà nước (Hapro), liên doanh Nhật (FujiMart, đô thị thông minh), khách sạn mang thương hiệu quốc tế, ngân hàng niêm yết.
5. &#91;Speculation\] Khách sạn do tập đoàn quốc tế quản lý có thể dùng hệ thống và chuẩn nhân sự của hãng, nên dữ liệu skill không nằm ở BRG.
6. Không đo kết quả sau khi chuyển.

### 3.4 Job nội bộ nào để đưa người vào

Với một tập đoàn đa ngành như BRG, điểm đến nên xếp thành bốn nhóm. \[Inference\]

| Nhóm job đích | Ví dụ trong BRG | Nguồn người phù hợp |
| --- | --- | --- |
| **A. Job của dự án chiến lược** | Thành phố thông minh Bắc Hà Nội (dự kiến 100.000–200.000 người sống và làm việc), BRIGHTPARK Ninh Bình, siêu thị FujiMart mở mới | Nhân sự bán lẻ, khách sạn, bất động sản có skill kề cận |
| **B. Job số, dữ liệu và AI** | Dữ liệu khách hàng xuyên hệ sinh thái (BRG Elite Card), vận hành kênh số, tự động hóa quy trình, an toàn thông tin | Người nghiệp vụ có nền dữ liệu |
| **C. Job cũ nâng cấp** | Thu ngân → tư vấn bán hàng đa kênh; lễ tân → trải nghiệm khách và doanh thu; văn phòng → vận hành có AI hỗ trợ | Chính người đang làm job đó |
| **D. Job thiếu người** | Khách sạn, golf, F&B, bếp, quản lý cấp trung, người đào tạo nghề | Người từ job bị tự động hóa; người lớn tuổi, tay nghề cao làm người dạy |

Điểm mấu chốt: **phát triển phải bắt đầu từ job đích**. Nếu đào tạo trước rồi mới tìm chỗ, người học xong dễ mang skill sang công ty khác.

## 4. Hồ sơ Tập đoàn BRG

BRG là tập đoàn tư nhân đa ngành khoảng 22.000 người, lớn lên nhiều nhờ mua lại và liên doanh. Bài toán career development vì thế là bài toán của nhiều pháp nhân và nhiều văn hóa. \[Inference\]

### 4.1 Doanh nghiệp

- [Thành lập năm 1993](https://www.brggroup.vn/about-us.html) bởi bà Nguyễn Thị Nga, khởi đầu là doanh nghiệp xuất nhập khẩu. BRG tự giới thiệu có "hàng chục" công ty thành viên và liên doanh, gần 22.000 nhân viên.
- Năm 2025, [tập đoàn nộp ngân sách hơn 18.000 tỷ đồng, thuộc Top 4 doanh nghiệp tư nhân](https://thitruongtaichinhtiente.vn/print/85520.html). Ngày 12/9/2026 bà Nga nhận danh hiệu Anh hùng Lao động.
- BRG từng là cổ đông chiến lược của nhiều doanh nghiệp nhà nước cổ phần hóa hoặc có vốn nhà nước: [Thăng Long GTC, OSC Việt Nam, Intimex (hơn 45%)](https://e.theleader.vn/hapro-becomes-the-acquisition-target-of-brg-group-d2525.html), [Thăng Long GTC cổ phần hóa 2015, BRG nắm 27%](https://doanhnhan.baophapluat.vn/khach-san-intercontinental-hanoi-westlake-doi-chu-15004.html), Hapro (65% từ 2018).

| Mảng | Đơn vị, thương hiệu chính | Ghi chú |
| --- | --- | --- |
| Golf | [Kings Island, Legend Hill, Ruby Tree, BRG Đà Nẵng](https://golfbusinessnews.com/news/corporate/brg-groups-golf-course-quartet-join-asian-golf-industry-federation); [Legend Valley (2023), Golden Sands Huế (2024)](https://www.brggroup.vn/history-of-development.html) | Hợp tác Nicklaus Design |
| Khách sạn – nghỉ dưỡng | InterContinental Hanoi Westlake, Hilton Garden Inn Hanoi, Sheraton Grand Danang, Sheraton Nha Trang; Legend Valley Hotel, Century Riverside Huế, Mondial Huế, bốn khách sạn Vũng Tàu | [Đối tác Hilton, Marriott, IHG](https://www.brggroup.vn/international-partners.html) |
| Bán lẻ – thương mại | BRGMart; FujiMart (liên doanh Sumitomo); Hapro; Intimex | [FujiMart: liên doanh ký 3/2022, mục tiêu thêm 50 cửa hàng đến 2028](https://en.vietnamplus.vn/brg-group-japanese-partner-to-open-more-fujimart-stores-in-vietnam/224050.vnp); mở 12 cửa hàng năm 2024, 6 năm 2025 |
| Bất động sản – đô thị | [Thành phố thông minh Bắc Hà Nội](https://viettimes.vn/chinh-thuc-khoi-cong-du-an-thanh-pho-thong-minh-bac-ha-noi-post188719.html) (liên doanh Sumitomo, gần 272 ha, 4,2 tỷ USD, khởi công 19/8/2025); Diamond Place Lê Văn Lương (2024); Times Square Hanoi | Mục tiêu đô thị trung hòa carbon đầu tiên |
| Vui chơi giải trí | BRIGHTPARK Ninh Bình | Vận hành trong tổ hợp Legend Valley |
| Tài chính – ngân hàng | [SeABank (HOSE: SSB)](https://vnexpress.net/seabank-bao-lai-6-868-ty-dong-5009386.html): hơn 5.300 nhân viên, 181 điểm giao dịch, hơn 4 triệu khách hàng | Ngân hàng niêm yết; bà Nga là Phó Chủ tịch Thường trực HĐQT |
| Khác | Gốm Chu Đậu, DNA Pharma |  |

**Bài toán career development vì thế là bài toán cấp hệ sinh thái, không chỉ của công ty mẹ.**

### 4.2 Chiến lược

- **Định hướng chung:** ["Going Global", phát triển bền vững, hội nhập sâu chuỗi giá trị toàn cầu](https://viettimes.vn/tap-doan-brg-ban-linh-tien-phong-va-kien-dinh-muc-tieu-phat-trien-ben-vung-post194236.html); coi thể thao – du lịch (golf) là ngành công nghiệp xanh. Sân golf thứ hai của Legend Valley dự kiến mở 5/2026 (theo tin 1/2026).
- **Đô thị thông minh:** 6 nhóm giải pháp (năng lượng, quản trị, đời sống, sức khỏe – học tập, di chuyển, kinh tế thông minh); dự kiến thu hút 100.000–200.000 người sống và làm việc.
- **Công nghệ:** BRG [sẽ mở rộng hợp tác khoa học – công nghệ, chuyển đổi số và đổi mới sáng tạo](https://nhandan.vn/hop-tac-cong-nghe-la-chia-khoa-thanh-cong-cua-doanh-nghiep-trong-ky-nguyen-vuon-minh-post914957.html); ký hợp tác chiến lược BRG – SeABank – ĐHQG Hà Nội về nghiên cứu và chuyển giao công nghệ (theo tin 10/2025). Tháng 9/2026, Chủ tịch Quốc hội đề nghị BRG và SeABank "đẩy mạnh chuyển đổi số, ứng dụng khoa học công nghệ hiện đại, trí tuệ nhân tạo".
- **SeABank:** chiến lược "Hội tụ số"; năm 2025 tái cơ cấu toàn diện mô hình kinh doanh theo ngành dọc.

&#91;Unverified\] Chưa tìm thấy kế hoạch trung hạn hay chiến lược AI cấp tập đoàn được BRG công bố công khai.

### 4.3 Nhân sự

| Chỉ số | Giá trị |
| --- | --- |
| Nhân viên toàn tập đoàn | Gần 22.000 (BRG); \[Unverified\] chưa rõ có gồm SeABank hay không |
| SeABank: quy mô | Hơn 5.300 nhân viên, 181 điểm giao dịch |
| SeABank: đào tạo (2025) | [Học viện SeABank; 1.541 khóa học; trung bình 62 giờ/người](https://cloud-cdn.seabank.com.vn/seabank-web/SB_BC%20PTBV-2025_VN%20up.pdf) |
| SeABank: gắn kết | 90,37% hài lòng; 90,5% muốn gắn bó ít nhất 2 năm; "Nơi làm việc tốt nhất Việt Nam" năm thứ 5 liên tiếp |
| SeABank: thu nhập bình quân | 31,6 triệu đồng/người/tháng (+4,9%) |
| SeABank: nữ quản lý | 47% cán bộ quản lý, lãnh đạo là nữ |
| Hapro khi cổ phần hóa | 630 lao động, 550 chuyển sang công ty cổ phần, 80 dôi dư |
| Khách sạn, golf, bán lẻ, bất động sản | Không tìm thấy số liệu công khai |

Đọc số liệu: SeABank công bố nhân sự rõ nhất. Phần còn lại của BRG gần như không có số công khai. \[Speculation\] Phần lớn trong 22.000 người có thể là nhân viên dịch vụ tuyến đầu (khách sạn, golf, siêu thị); cần BRG xác nhận.

### 4.4 Chính sách nhân sự hiện thấy

- **Sứ mệnh:** BRG cam kết [tạo và duy trì hàng chục nghìn việc làm, mở cơ hội nghề nghiệp chuyên nghiệp, thu hút nhân tài quốc tế](https://www.brggroup.vn/statement-mission.html).
- **Tiền lệ tái cơ cấu:** khi nhận Hapro, BRG cam kết giữ toàn bộ nhân viên và sắp xếp lại theo năng lực (mục 2.2).
- **SeABank:** có học viện nội bộ và cam kết "lộ trình đào tạo và thăng tiến rõ ràng".
- **Chuyên gia nước ngoài** ở các vị trí vận hành golf, khách sạn. \[Inference\]

### 4.5 Những điểm chưa thấy công bố

- &#91;Unverified\] Không thấy báo cáo vốn nhân lực cấp tập đoàn; BRG chưa niêm yết nên không bắt buộc công bố.
- Không rõ hệ thống nhân sự lõi dùng chung hay riêng từng công ty.
- Không rõ có tuyển nội bộ hay luân chuyển giữa công ty thành viên không.
- &#91;Speculation\] Khách sạn mang thương hiệu quốc tế có thể theo chuẩn và hệ thống nhân sự của hãng quản lý.

Những điểm này là câu hỏi đầu tiên cần hỏi BRG (mục 8.3).

## 5. Bài toán career development của BRG

### 5.1 Phát biểu bài toán

> Làm sao để hệ sinh thái BRG, khoảng 22.000 người trải trên hàng chục pháp nhân và nhiều văn hóa, chuyển được đủ người có đủ skill từ các job đang thu hẹp do AI và tự động hóa sang các job đang thiếu hoặc mới (khách sạn – golf, đô thị thông minh, số và dữ liệu), đúng lúc chiến lược cần, mà vẫn giữ chân người giỏi và tuân thủ luật Việt Nam?

### 5.2 Bảy vấn đề cấu thành (giả thuyết cần kiểm chứng với khách hàng)

&#91;Inference\] Toàn bộ bảng là giả thuyết rút từ nguồn công khai; mức chắc chắn là đánh giá của người viết.

| # | Vấn đề | Bằng chứng hiện có | Mức chắc chắn |
| --- | --- | --- | --- |
| P1 | **Cầu không rõ:** chưa thấy con số cần bao nhiêu người, skill gì cho đô thị thông minh, FujiMart mở mới, golf và khách sạn mới, job số | Không thấy kế hoạch nhân lực công khai; dự án mới nêu quy mô nhưng không nêu nhu cầu nhân sự | Trung bình |
| P2 | **Cung không thấy:** skill thực của nhân viên chưa số hóa theo chuẩn chung; mỗi đơn vị và hãng quản lý dùng chuẩn riêng | Ngoài SeABank, không có số liệu nhân sự công khai | Trung bình |
| P3 | **Học không nối với job:** đào tạo theo từng đơn vị, đo bằng giờ học, không theo job đích liên công ty | SeABank báo cáo 62 giờ/người, không báo cáo số người vào job mới | Trung bình |
| P4 | **Ma sát khi chuyển:** hợp đồng, thâm niên, thang lương, phúc lợi khác nhau giữa công ty; đổi hẳn công việc cần đồng ý; quản lý giữ người | Bộ luật Lao động Điều 29, 33; mỗi công ty là doanh nghiệp độc lập | Cao |
| P5 | **Thiếu thông tin và lý do để ở lại:** nhân viên không biết job nội bộ nào mở, cần skill gì; người giỏi chọn thị trường ngoài | Nghỉ việc 9,8% (doanh nghiệp nội), khách sạn 18,9% | Cao |
| P6 | **Ranh giới pháp nhân và văn hóa:** doanh nghiệp gốc nhà nước, liên doanh Nhật, khách sạn thương hiệu quốc tế, ngân hàng niêm yết | Cấu trúc sở hữu ở mục 4.1 | Cao |
| P7 | **Không đo kết quả:** không biết người đã học hoặc đã chuyển có tạo giá trị không | Không thấy chỉ số vốn nhân lực cấp tập đoàn | Trung bình |

### 5.3 Ràng buộc phải tôn trọng

- **Luật Lao động.** Điều chuyển tạm thời tối đa 60 ngày làm việc/năm nếu không có đồng ý (Điều 29); đổi hẳn công việc phải thỏa thuận (Điều 33). Khi đổi cơ cấu, công nghệ phải có phương án sử dụng lao động và ưu tiên đào tạo lại (Điều 42, 44). \[Inference\] Giải pháp nên tạo được hồ sơ cho thấy tập đoàn đã ưu tiên đào tạo lại và bố trí nội bộ. Nội dung này cần luật sư xác nhận.
- **Dữ liệu cá nhân.** [Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, Điều 25](https://tienphong.vn/doanh-nghiep-khi-cham-dut-hop-dong-phai-xoa-du-lieu-ca-nhan-nguoi-lao-dong-post1764533.tpo) (hiệu lực 1/1/2026): tuyển dụng chỉ được yêu cầu thông tin phục vụ mục đích tuyển dụng; công cụ công nghệ quản lý người lao động phải đúng luật và người lao động phải được biết; phải xóa dữ liệu khi chấm dứt hợp đồng, trừ khi có thỏa thuận hoặc luật khác. [Nghị định 356/2025/NĐ-CP](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan) (thay Nghị định 13/2023): đồng ý phải rõ và kiểm chứng được; hồ sơ đánh giá tác động do Bộ Công an (A05) xem xét trước; có yêu cầu về nhân sự bảo vệ dữ liệu và chuyển dữ liệu ra nước ngoài.
- **AI.** Luật Trí tuệ nhân tạo (hiệu lực 1/3/2026) xếp rủi ro cao cho hệ thống có thể gây thiệt hại đáng kể đến quyền, lợi ích hợp pháp. \[Inference\] AI gợi ý bố trí nhân sự có thể thuộc nhóm này tùy văn bản hướng dẫn; thiết kế an toàn là AI chỉ đề xuất, con người quyết định.
- **Đối thoại với người lao động.** Cho thôi việc vì đổi cơ cấu phải trao đổi với tổ chức đại diện người lao động; ILO khuyến nghị đối thoại xã hội khi đưa AI vào. Dữ liệu skill không được dùng để đánh giá trừ điểm.
- **Ngân hàng niêm yết.** \[Inference\] SeABank có quản trị riêng và quy định an toàn thông tin của ngành ngân hàng; dữ liệu nhân sự ngân hàng có thể không chia sẻ chung với các công ty khác.
- **Đối tác quốc tế.** \[Speculation\] Hợp đồng quản lý khách sạn (Hilton, Marriott, IHG) và liên doanh Sumitomo có thể quy định quyền quyết định nhân sự và quyền dữ liệu.
- **Chất lượng dịch vụ tuyến đầu.** \[Inference\] Không rút người khỏi khách sạn, sân golf vào mùa cao điểm khi chưa có người thay.

## 6. Hướng giải pháp nghiệp vụ

Đề xuất: một **thị trường nhân lực nội bộ dựa trên skill** cho toàn hệ sinh thái BRG, vận hành theo vòng khép kín sáu bước.

### 6.1 Nguyên tắc thiết kế

1. **Bắt đầu từ job đích, không từ khóa học.** Mọi lộ trình trỏ về một job nội bộ có thật, gắn với kế hoạch kinh doanh (dự án mới, cửa hàng mới, khách sạn – golf).
2. **Skill là ngôn ngữ chung.** Job, người, khóa học, cơ hội đều mô tả bằng cùng một bộ skill: Khung năng lực số (TT 02/2025) cho skill số nền, VTOS/ACCSTP cho khách sạn – du lịch, SFIA 9 cho skill số chuyên sâu, cộng skill riêng của BRG.
3. **Tự nguyện và minh bạch.** Không ép điều chuyển; người lao động thấy rõ job, khoảng cách skill, thu nhập và lộ trình. Phù hợp Điều 29 và 33.
4. **Thử trước khi chuyển hẳn.** Dự án nội bộ, ca làm ở đơn vị khác, mùa cao điểm golf – khách sạn giúp cả người lẫn đơn vị thử. \[Inference\]
5. **Toàn hệ sinh thái, tôn trọng ranh giới pháp nhân.** Dữ liệu và quyết định thuộc từng công ty; nền tảng chỉ kết nối khi nhân viên đồng ý.
6. **Đo đến tận nơi.** Đo số người đã vào đúng job và tạo được giá trị, không chỉ số giờ học.

### 6.2 Vòng career development khép kín (sáu bước)

&#91;embedded content: Vòng career development khép kín · 6 bước, vấn đề P1–P7\]

Bước 1 lấy cầu từ kế hoạch kinh doanh; bước 6 đo kết quả rồi cập nhật cầu và cung cho vòng sau. Dòng cuối mỗi ô ghi ai làm và vấn đề được giải quyết.

### 6.3 Biện pháp cụ thể cho từng vấn đề

- **P1 – Danh mục nhân sự động theo kịch bản:** bản đồ job theo ba giai đoạn (0–1 năm, 1–2 năm, 2–3 năm) cho từng mảng. Gắn với kịch bản: tốc độ mở FujiMart (kế hoạch liên doanh 5–10 cửa hàng/năm), tiến độ đô thị thông minh, tỷ lệ giao dịch số tại SeABank, công suất khách sạn – golf mùa cao điểm.
- **P2 – Hồ sơ skill có bằng chứng:** tự khai là điểm bắt đầu; bổ sung từ lịch sử công việc, chứng chỉ (VTOS/ACCSTP, ngoại ngữ, chứng chỉ ngân hàng), kết quả đào tạo, xác nhận của quản lý. Mỗi skill có độ tin cậy. Người làm lâu năm không có bằng: [công nhận kỹ năng đã có (RPL)](https://doanhnghiephoinhap.vn/tp-ho-chi-minh-muon-chuan-hoa-nhan-luc-khach-san-theo-chuan-asean-148551.html), như đề xuất cho ngành khách sạn TP.HCM.
- **P3 – Lộ trình học theo job đích:** ưu tiên skill kề cận với cái đã giỏi. Dùng năng lực có sẵn: Học viện SeABank, đào tạo caddie và khách sạn của từng cơ sở, hợp tác ĐHQG Hà Nội cho skill dữ liệu và AI. \[Inference\]
- **P4 – Giảm ma sát khi chuyển:**
  - Ứng tuyển ẩn danh đến vòng chọn lọc; quản lý hiện tại chỉ biết khi đã vào danh sách ngắn.
  - Quy tắc bù người: hệ thống đề xuất người hoặc cách thay (tự động hóa, tuyển thay, dự án) cho phòng đi.
  - Tiêu chí chọn công khai, dựa trên skill.
  - Mẫu thỏa thuận chuyển công ty trong tập đoàn: cách tính thâm niên, trợ cấp thôi việc, thang lương tương đương. \[Inference\] Cần luật sư thiết kế.
  - Dự án nội bộ 10–20% thời gian trước khi chuyển hẳn, có thỏa thuận bằng văn bản.
- **P5 – Định hướng cho từng người:** trang nghề nghiệp cá nhân hiển thị job đang mở trong toàn hệ sinh thái, khoảng cách skill, khóa học, người đi trước, khoảng thu nhập. AI hỗ trợ chuẩn bị buổi trao đổi nghề nghiệp với quản lý.
- **P6 – Thị trường nội bộ cấp hệ sinh thái:** đăng vị trí và dự án của mọi công ty tham gia trên một nơi. Mỗi pháp nhân (SeABank, khách sạn do hãng quản lý, liên doanh) tự quyết định tham gia và chia sẻ dữ liệu gì.
- **P7 – Đo hiệu quả:** theo dõi người đã chuyển trong 90 ngày và 12 tháng (đánh giá, gắn kết, giữ chân); lập bảng chỉ số vốn nhân lực cấp tập đoàn.

### 6.4 Đưa người vào job nội bộ nào: ma trận nguồn – đích (giả thuyết)

| Nguồn (job thu hẹp hoặc đổi) | Đích khả thi | Kỹ năng chuyển đổi chính |
| --- | --- | --- |
| Giao dịch viên, hỗ trợ gián tiếp ngân hàng | Tư vấn tài chính, chăm sóc khách hàng số; dịch vụ khách cao cấp ở khách sạn – golf | Giao tiếp khách hàng, tuân thủ quy trình |
| Thu ngân, nhập liệu kho siêu thị | Tư vấn bán hàng đa kênh, vận hành cửa hàng FujiMart mới, F&B khách sạn | Hiểu khách, kỷ luật vận hành |
| Văn phòng, hành chính, nhân sự ở các công ty | Phân tích dữ liệu, vận hành quy trình tự động, nhân sự bảo vệ dữ liệu cá nhân | Hiểu quy trình; kinh nghiệm quản lý nhân sự, tổ chức được tính vào chuẩn nhân sự bảo vệ dữ liệu ([Nghị định 356](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan)) |
| Lễ tân, đặt chỗ, tổng đài khách sạn – golf | Quản trị doanh thu, CRM, vận hành BRG Elite Card | Hiểu khách, ngoại ngữ |
| Bán hàng, vận hành bất động sản truyền thống | Vận hành đô thị thông minh, dịch vụ cư dân, quản lý năng lượng và ESG | Quan hệ khách hàng, hiểu dự án |
| Nhân viên lâu năm ở doanh nghiệp gốc nhà nước (ví dụ Hapro) | Xuất khẩu, chuỗi cung ứng cho bán lẻ, kiểm soát chất lượng | Chuyên môn sâu, quan hệ đối tác |
| Người lớn tuổi, tay nghề cao ở golf – khách sạn | Người dạy nghề, đánh giá viên theo VTOS/ACCSTP | Chuyên môn sâu |

Ma trận này là giả thuyết. \[Inference\] Cần BRG xác nhận job nào đang thu hẹp và mảng nào đang thiếu người.

## 7. Giải pháp công nghệ

### 7.1 Định vị

Một **nền tảng career development và thị trường nhân lực nội bộ dựa trên skill** cho hệ sinh thái BRG, chạy trên kiến trúc Workforce Graph. Có thể đóng gói thành module Career Development của AINAVI: giao diện tiếng Việt, từ điển skill theo khung Việt Nam, dữ liệu lưu tại Việt Nam. Tuyển nội bộ chạy trên ATS và kiểm tra skill dùng thi trực tuyến sẵn có của AINAVI.

Nền tảng **không thay** hệ thống nhân sự lõi, hệ thống đào tạo hay công cụ AI tạo sinh mà từng công ty đang dùng. Nó là lớp ở giữa, nối cầu (job) với cung (người) qua ranh giới các pháp nhân.

### 7.2 Sáu khối chức năng

| Khối | Chức năng | Người dùng | Vấn đề |
| --- | --- | --- | --- |
| **M1. Kiến trúc job và từ điển skill** | Mô tả job bằng skill. Từ điển ba tầng: chung (Khung năng lực số TT 02/2025, SFIA 9); ngành (VTOS/ACCSTP, tiêu chuẩn kỹ năng nghề quốc gia, ngân hàng, bán lẻ, golf, đô thị thông minh và ESG); skill riêng BRG. Song ngữ Việt – Anh. AI gợi ý skill từ mô tả công việc hiện có | Nhân sự, đơn vị | P1, P3 |
| **M2. Hồ sơ skill có bằng chứng** | AI đọc lịch sử công việc, dự án, chứng chỉ, kết quả đào tạo và bài thi trực tuyến để đề xuất skill. Nhân viên và quản lý xác nhận. Mỗi skill có độ tin cậy, giảm dần nếu không cập nhật. Có công nhận kỹ năng đã có (RPL) | Nhân viên, quản lý | P2 |
| **M3. Danh mục nhân sự động** | Bản đồ cung – cầu theo mảng, công ty, job, giai đoạn. Mô phỏng theo kịch bản (tốc độ mở cửa hàng, tiến độ dự án, tỷ lệ giao dịch số). Cảnh báo thiếu người kế thừa. Xuất số liệu cho báo cáo vốn nhân lực | Ban Tổng giám đốc, nhân sự | P1, P7 |
| **M4. Định hướng nghề nghiệp cá nhân** | Job phù hợp theo mức sẵn sàng; khoảng cách skill; skill chuyển đổi gần nhất; khóa học từ hệ thống đào tạo; người đi trước; khoảng thu nhập. AI tóm tắt để chuẩn bị buổi trao đổi với quản lý. Có bản điện thoại cho nhân viên tuyến đầu | Nhân viên, quản lý | P3, P5 |
| **M5. Thị trường nhân lực nội bộ** | Đăng tuyển nội bộ, dự án, ca làm ở đơn vị khác trong hệ sinh thái. Ghép nối có giải thích (vì sao hợp, thiếu gì). Ứng tuyển ẩn danh đến danh sách ngắn. Quy trình duyệt hai đơn vị. Gợi ý bù người | Nhân viên, đơn vị, nhân sự | P4, P6 |
| **M6. Hỗ trợ điều chuyển và theo dõi** | Đề xuất phương án bố trí (con người quyết). Mẫu thỏa thuận chuyển công ty. Kế hoạch kế thừa. Theo dõi 90 ngày và 12 tháng. Lưu hồ sơ "đã ưu tiên đào tạo lại" cho phương án sử dụng lao động | Nhân sự, quản lý mới | P4, P7 |

### 7.3 Kiến trúc

&#91;embedded content: Kiến trúc đề xuất · nguồn dữ liệu, nền tảng 3 lớp, 4 nhóm người dùng\]

Dữ liệu chảy từ hệ thống của từng công ty vào nền tảng; lớp pháp nhân và đồng ý quyết định hồ sơ nào được thấy ở công ty khác.

- **Lớp dữ liệu:** Workforce Graph trên Neo4j với 7 lớp (bối cảnh kinh doanh, năng lực, tổ chức và job, từ điển skill, con người và bằng chứng, mạng lưới, phát triển tương lai), thêm lớp **pháp nhân trong hệ sinh thái** (nhân viên thuộc công ty nào, đồng ý chia sẻ dữ liệu với ai). Dữ liệu định danh lưu riêng ở PostgreSQL có mã hóa, tách theo pháp nhân; graph chỉ dùng mã ẩn danh.
- **Lớp AI:**
  - Trích xuất skill từ văn bản tiếng Việt (hồ sơ cá nhân, mô tả công việc, đánh giá, chứng chỉ) và chuẩn hóa về từ điển skill.
  - Ghép nối có giải thích, gợi ý lộ trình, tóm tắt buổi trao đổi nghề nghiệp.
  - Mọi gợi ý của AI đều có bước con người xác nhận và được ghi lại để truy vết.
- **Lớp ứng dụng:** web tiếng Việt cho nhân viên, quản lý, nhân sự, ban Tổng giám đốc; bản điện thoại cho nhân viên khách sạn, golf, siêu thị.
- **Tích hợp (cần xác nhận hệ thống thực tế của BRG):**
  - Hệ thống nhân sự lõi của từng công ty: tổ chức, chức danh, lịch sử công tác.
  - Hệ thống đào tạo và e-learning (ví dụ Học viện SeABank): khóa học, kết quả.
  - AINAVI: ATS cho tuyển nội bộ, thi trực tuyến để kiểm tra skill.
  - Hệ thống đánh giá (chỉ đọc những trường được phép); đăng nhập một lần.
- **Hạ tầng:** dữ liệu lưu tại Việt Nam. \[Inference\] Với SeABank, cần theo thêm quy định an toàn thông tin của ngành ngân hàng; phương án an toàn là triển khai riêng cho ngân hàng, chỉ chia sẻ hồ sơ khi nhân viên đồng ý.

### 7.4 Quản trị và đạo đức dữ liệu

- Dữ liệu skill chỉ dùng cho phát triển và bố trí, **không dùng để đánh giá trừ điểm hay xếp hạng cắt giảm**. Nói rõ với nhân viên và tổ chức đại diện người lao động.
- Nhân viên xem được toàn bộ hồ sơ skill và bằng chứng, có quyền sửa. Thời hạn xử lý yêu cầu theo Nghị định 356 (truy cập, chỉnh sửa: phản hồi trong 2 ngày làm việc, thực hiện trong 10 ngày).
- Chia sẻ hồ sơ sang công ty khác trong hệ sinh thái cần đồng ý rõ ràng, kiểm chứng được.
- Không ra quyết định điều chuyển tự động. AI chỉ đề xuất, con người quyết và được ghi lại.
- Xóa hoặc ẩn danh dữ liệu khi chấm dứt hợp đồng, trừ khi có thỏa thuận hoặc luật khác (Điều 25 Luật Bảo vệ dữ liệu cá nhân).
- Lập hồ sơ đánh giá tác động xử lý dữ liệu trước khi xử lý dữ liệu thật; chỉ định nhân sự bảo vệ dữ liệu cá nhân.

### 7.5 Chỉ số thành công

| Nhóm | Chỉ số |
| --- | --- |
| Nhìn thấy | % nhân viên có hồ sơ skill đã xác nhận; % job có mô tả skill |
| Dịch chuyển | Số người vào job đích mỗi năm (dự án mới, job số, job thiếu người); % vị trí lấp bằng người nội bộ; thời gian lấp vị trí |
| Tham gia | % nhân viên dùng trang nghề nghiệp; số đơn ứng tuyển và dự án nội bộ; số công ty thành viên tham gia |
| Hiệu quả | Giữ chân và đánh giá của người đã chuyển sau 12 tháng; chi phí so với tuyển ngoài |
| Tuân thủ và an toàn | 100% chuyển đổi công việc có thỏa thuận bằng văn bản; không vị trí tuyến đầu nào thiếu người thay mùa cao điểm; 0 sự cố dữ liệu |

## 8. Lộ trình PoC, rủi ro và câu hỏi cho khách hàng

### 8.1 PoC 12 tuần

**Phạm vi đề xuất:** một cặp "nguồn – đích" rõ nhất trong khu vực Hà Nội. Ví dụ: thu ngân và văn phòng của khối bán lẻ (nguồn) sang cửa hàng FujiMart mới, F&B và dịch vụ khách của khối khách sạn – golf, cùng một số job số (đích). Khoảng 200–300 nhân viên, 20–30 job đích, 2–3 công ty thành viên. \[Inference\] SeABank nên vào giai đoạn 2 vì có quy định riêng của ngân hàng. BRG cần chọn cặp thật.

&#91;embedded content: Lộ trình PoC đề xuất · 6 giai đoạn, 2 cửa quyết định\]

Bốn tuần đầu chỉ dùng dữ liệu ẩn danh; dữ liệu thật chỉ được xử lý sau khi hồ sơ đánh giá tác động được chấp thuận (cửa 1). Việc chính của từng giai đoạn:

- **Khảo sát và dữ liệu:** phỏng vấn ban Tổng giám đốc, nhân sự, kế hoạch và 2–3 trưởng đơn vị; thu mô tả job, dữ liệu đào tạo, dữ liệu nhân sự ẩn danh; lập hồ sơ đánh giá tác động.
- **Từ điển skill:** ghép TT 02/2025, VTOS/ACCSTP, SFIA 9 và skill ngành; mô tả 20–30 job đích bằng skill.
- **Hồ sơ skill thí điểm:** AI trích xuất, nhân viên và quản lý xác nhận; công nhận kỹ năng đã có.
- **Bản đồ cung – cầu:** trang định hướng nghề nghiệp, gợi ý lộ trình học.
- **Chạy thử tuyển nội bộ:** một đợt tuyển nội bộ hoặc dự án nội bộ trên ATS của AINAVI; thu phản hồi.
- **Đánh giá:** so với tiêu chí PoC bên dưới, lập kế hoạch mở rộng.

**Tiêu chí thành công của PoC (đề xuất, cần thống nhất với khách hàng):**

- ≥ 70% nhân viên thí điểm xác nhận hồ sơ skill.
- ≥ 80% gợi ý skill của AI được chấp nhận.
- Ban Tổng giám đốc dùng bản đồ cung – cầu trong ít nhất một cuộc họp kế hoạch nhân sự.
- Số đơn ứng tuyển nội bộ hoặc dự án nội bộ cao hơn rõ rệt so với đợt gần nhất.
- 100% trường hợp chuyển trong PoC có thỏa thuận bằng văn bản.

### 8.2 Rủi ro và cách giảm

| Rủi ro | Cách giảm |
| --- | --- |
| Nhân viên sợ dữ liệu skill bị dùng để đánh giá hoặc cắt giảm | Cam kết bằng văn bản về mục đích; trao đổi với tổ chức đại diện người lao động; nhân viên kiểm soát hồ sơ của mình |
| Quản lý cản trở vì sợ mất người | Ứng tuyển ẩn danh; cơ chế bù người; đưa việc "cho đi người giỏi" vào đánh giá quản lý |
| Người học xong nhảy việc | Gắn học với job đích và thu nhập rõ ràng. \[Unverified\] Có thể dùng hợp đồng đào tạo có cam kết thời gian làm việc (Điều 62 Bộ luật Lao động 2019), cần luật sư kiểm tra |
| Từ điển skill quá lớn, không ai duy trì | Bắt đầu nhỏ, theo khung có sẵn; mỗi mảng một người chịu trách nhiệm; AI hỗ trợ cập nhật |
| AI trích xuất sai skill từ văn bản tiếng Việt | Luôn có bước con người xác nhận; đo độ chính xác trong PoC |
| Dữ liệu và quyết định thuộc nhiều pháp nhân, đối tác quốc tế | Mỗi pháp nhân tự chọn tham gia; chia sẻ theo đồng ý; rà soát hợp đồng quản lý và liên doanh |
| Hồ sơ đánh giá tác động dữ liệu chưa được chấp thuận đúng hạn | Lập hồ sơ ngay tuần 1–2; dùng dữ liệu ẩn danh cho đến khi được chấp thuận |
| Rút người khỏi dịch vụ tuyến đầu mùa cao điểm | Ràng buộc cứng: vị trí tuyến đầu phải có người thay trước khi duyệt chuyển; lịch chuyển tránh mùa cao điểm |
| Chồng chéo với hệ thống nhân sự hiện có | Định vị là lớp nối, không thay thế; tích hợp hai chiều |

### 8.3 Câu hỏi cần hỏi BRG (bước nghiên cứu tiếp theo)

**Chiến lược và cầu:**

1. Đến 2027–2028, các dự án mới (đô thị thông minh, FujiMart, golf – khách sạn, BRIGHTPARK) cần thêm bao nhiêu người, job gì?
2. Job nào đang hoặc sẽ thu hẹp do tự động hóa, kênh số và AI? Bao nhiêu người?
3. BRG đã có kế hoạch nhân lực hoặc chiến lược AI cấp tập đoàn chưa?

**Cung và dữ liệu:**

4. Con số khoảng 22.000 người gồm những pháp nhân nào? Có gồm SeABank không?
5. Dữ liệu nhân sự và đào tạo nằm ở đâu (hệ thống nào, dùng chung hay từng công ty, Excel)? Đã có mô tả job chưa?
6. Với khách sạn do hãng quốc tế quản lý, dữ liệu và quyết định nhân sự thuộc ai?

**Bố trí:**

7. Hiện có tuyển nội bộ, luân chuyển giữa công ty thành viên không? Mỗi năm bao nhiêu người chuyển?
8. Khi chuyển công ty trong tập đoàn, BRG đang xử lý hợp đồng, thâm niên, trợ cấp thế nào?
9. Có định mở dự án nội bộ, ca làm ở đơn vị khác, hoặc quy tắc tuyển nội bộ trước tuyển ngoài không?

**Tổ chức và điều kiện:**

10. Ai là chủ đầu tư và người ra quyết định: ban Tổng giám đốc tập đoàn, khối nhân sự hay từng công ty?
11. Yêu cầu bảo mật, nơi lưu dữ liệu, nhân sự bảo vệ dữ liệu cá nhân đã có chưa, quy trình mua sắm?
12. Công đoàn và tổ chức đại diện người lao động cần được tham vấn ở bước nào?

## 9. Nguồn

**BRG và hệ sinh thái**

- [BRG – Giới thiệu](https://www.brggroup.vn/about-us.html)
- [BRG – Lịch sử phát triển](https://www.brggroup.vn/history-of-development.html)
- [BRG – Tuyên bố và sứ mệnh](https://www.brggroup.vn/statement-mission.html)
- [BRG – Đối tác quốc tế](https://www.brggroup.vn/international-partners.html)
- [Thị trường Tài chính Tiền tệ – Anh hùng Lao động Nguyễn Thị Nga, số liệu nộp ngân sách 2025 (9/2026)](https://thitruongtaichinhtiente.vn/print/85520.html)
- [VietTimes – BRG năm 2025 và định hướng (1/2026)](https://viettimes.vn/tap-doan-brg-ban-linh-tien-phong-va-kien-dinh-muc-tieu-phat-trien-ben-vung-post194236.html)
- [Nhân Dân – Hợp tác công nghệ của BRG (10/2025)](https://nhandan.vn/hop-tac-cong-nghe-la-chia-khoa-thanh-cong-cua-doanh-nghiep-trong-ky-nguyen-vuon-minh-post914957.html)
- [VietTimes – Khởi công Thành phố thông minh Bắc Hà Nội (8/2025)](https://viettimes.vn/chinh-thuc-khoi-cong-du-an-thanh-pho-thong-minh-bac-ha-noi-post188719.html)
- [VietnamPlus – Liên doanh FujiMart BRG – Sumitomo (3/2022)](https://en.vietnamplus.vn/brg-group-japanese-partner-to-open-more-fujimart-stores-in-vietnam/224050.vnp)
- [Golf Business News – Bốn sân golf của BRG (2017)](https://golfbusinessnews.com/news/corporate/brg-groups-golf-course-quartet-join-asian-golf-industry-federation)
- [The Leader – BRG và các thương vụ cổ phần hóa (3/2018)](https://e.theleader.vn/hapro-becomes-the-acquisition-target-of-brg-group-d2525.html)
- [Doanh nhân – Thăng Long GTC và InterContinental Hanoi Westlake (3/2019)](https://doanhnhan.baophapluat.vn/khach-san-intercontinental-hanoi-westlake-doi-chu-15004.html)
- [KIS – ĐHĐCĐ Hapro 2018](https://kisvn.vn/dhdcd-hapro-chu-tich-brg-nguyen-thi-nga-lam-chu-tich-hapro)
- [Báo Đầu tư – Phương án cổ phần hóa Hapro (12/2017)](https://baodautu.vn/nha-nuoc-se-thoai-toan-bo-von-tai-hapro-ban-65-cho-nha-dau-tu-chien-luoc-d73677.html)
- [VnExpress – Kết quả SeABank 2025 (1/2026)](https://vnexpress.net/seabank-bao-lai-6-868-ty-dong-5009386.html)
- [SeABank – Báo cáo Phát triển bền vững 2025](https://cloud-cdn.seabank.com.vn/seabank-web/SB_BC%20PTBV-2025_VN%20up.pdf)

**Thị trường lao động và AI**

- [WEF Future of Jobs Report 2025 – Digest](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/)
- [ILO – Generative AI and jobs in Viet Nam (4/2026)](https://www.ilo.org/resource/news/generative-ai-could-transform-millions-jobs-viet-nam-new-ilo-brief-shows)
- [VnEconomy – AI thay đổi luật chơi trong quản trị nhân lực (4/2026)](https://vneconomy.vn/ai-dang-thay-doi-luat-choi-trong-quan-tri-nhan-luc.htm)
- [PwC – Hopes and Fears 2025, báo cáo Việt Nam](https://www.pwc.com/vn/vn/publications/vietnam-publications/hopes-fears-vietnam-2025.html)
- [SGGP – Báo cáo Talentnet–Mercer 2025 (10/2025)](https://www.sggp.org.vn/tu-du-lieu-den-con-nguoi-5-dieu-can-biet-cho-chien-luoc-dai-ngo-thoi-ai-post820176.html)
- [LinkedIn – Global Talent Trends, dịch chuyển nội bộ và giữ chân (10/2022)](https://news.linkedin.com/2022/october/talent-connect-2022)
- [Báo Đầu tư – FPT và nhân sự AI-first (11/2025)](https://baodautu.vn/the-he-nhan-su-mang-ma-gen-ai-first-d430047.html)

**Ngân hàng**

- [VietnamFinance – Khảo sát NHNN về cắt giảm nhân sự (6/2025)](https://vietnamfinance.vn/ngan-hang-chuyen-doi-so-bao-gio-moi-dung-sa-thai-nhan-su-d128861.html)
- [DNSE – Nhân sự ngân hàng 2024–2026 (5/2026)](https://www.dnse.com.vn/senses/tin-tuc/ngan-hang-o-at-cat-giam-hang-ngan-nhan-su-ai-co-phai-la-thu-pham-chinh-35224497)
- [Thị trường Tài chính Tiền tệ – Ngân hàng tái phân bổ nhân sự (5/2026)](https://thitruongtaichinhtiente.vn/print/82920.html)

**Du lịch – khách sạn**

- [The Leader – Nhân lực du lịch, khách sạn Đà Nẵng (8/2026)](https://theleader.vn/diem-nghen-lon-nhat-cua-nganh-du-lich--khach-san-da-nang-trong-giai-doan-tang-truong-moi-d47481.html)
- [Báo Đầu tư – Nhân lực ngành du lịch, khách sạn (11/2025)](https://baodautu.vn/cong-bo-top-10-noi-lam-viec-tot-nhat-viet-nam-nganh-du-lich---khach-san---resort-d437620.html)
- [Doanh nghiệp và Hội nhập – Chuẩn hóa nhân lực khách sạn theo chuẩn ASEAN (9/2026)](https://doanhnghiephoinhap.vn/tp-ho-chi-minh-muon-chuan-hoa-nhan-luc-khach-san-theo-chuan-asean-148551.html)

**Pháp lý Việt Nam**

- [Đại biểu Nhân dân – Quốc hội thông qua Luật Trí tuệ nhân tạo (12/2025)](https://daibieunhandan.vn/quoc-hoi-thong-qua-luat-tri-tue-nhan-tao-10399959.html)
- [Tiền Phong – Điều 25 Luật Bảo vệ dữ liệu cá nhân (7/2025)](https://tienphong.vn/doanh-nghiep-khi-cham-dut-hop-dong-phai-xoa-du-lieu-ca-nhan-nguoi-lao-dong-post1764533.tpo)
- [EY – Nghị định 356/2025/NĐ-CP](https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan)
- [Báo Lào Cai – Điều 42, 47 Bộ luật Lao động 2019 (9/2023)](https://baolaocai.vn/nghi-viec-vi-ly-do-thay-doi-co-cau-nguoi-lao-dong-duoc-huong-quyen-loi-gi-post373268.html)
- [CareerLink – Điều 29, 33 Bộ luật Lao động 2019 (8/2026)](https://www.careerlink.vn/cam-nang-viec-lam/goc-ky-nang/cach-ung-xu-khi-bi-dieu-chuyen-cong-viec)
- [Thư viện Nhà đất – Công ty trong tập đoàn là doanh nghiệp độc lập (11/2024)](https://thuviennhadat.vn/phap-luat/cong-ty-khong-chi-tra-tro-cap-thoi-viec-la-dung-hay-sai-597467.html)

**Khung skill**

- [VnEconomy – Khung năng lực số cho người học (2/2025)](https://vneconomy.vn/bo-giao-duc-va-dao-tao-ban-hanh-khung-nang-luc-so-cho-nguoi-hoc.htm)
- [SFIA 9 – Release notes](https://sfia-online.org/en/sfia-9/sfia-9-release-notes)

Các nhãn \[Inference\], \[Speculation\], \[Unverified\] trong tài liệu đánh dấu nội dung suy luận hoặc chưa kiểm chứng được từ nguồn mở. Phần pháp lý không phải tư vấn luật.
