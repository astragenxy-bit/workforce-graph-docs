# Generates the content slides of the BRG deck into ../brg/project/slides/.
# Hand-maintained HTML (not written here): thanks and the migrated appendix slides
# (ap-principles, ap-matrix, ap-roles, ap-legal, ap-sources).
import sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import ic, footer, head, section, timeline, write, hdrow, arrow, shot, rounded_bus
from blocks import (overview_slide, roles_slide, flow_slide, arch_slide, dataflow_slide, ai_slide,
                    compliance_slide, problems_slide, system_arch_slide, cover_slide)

ROOT = os.path.abspath(os.path.join(HERE, '..', 'brg'))
FT = footer('TALENT FLOW · BRG')
BLOB = json.load(open(os.path.join(ROOT, 'blobs.json')))  # name -> /_blob/<id>
S = {}
BLUR = 'dữ liệu đã làm mờ'


# ---------- cover: the description is drawn as the labelled illustration ----------
S['cover'] = cover_slide('cover', 'FPT IS · THÁNG 11/2026', 'Talent Flow',
    'Từ dự án chiến lược đến kỹ năng của từng nhân sự',
    ['Nghiệp vụ<br>nhân sự', 'Luồng<br>dữ liệu', 'Tri thức<br>doanh nghiệp', 'AI'],
    ['Phát triển<br>nghề nghiệp', 'Điều chuyển<br>nhân lực<br>nội bộ'],
    'TALENT FLOW · TÀI LIỆU TRAO ĐỔI VỚI <span style="color:#FCA010"><b>BRG</b></span>',
    'Talent Flow là nền tảng phát triển nghề nghiệp và điều chuyển nhân lực nội bộ dựa trên kỹ năng, kết hợp nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp và AI. Hình minh họa: bốn thành phần (nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp, AI) hội về kỹ năng ở trung tâm và tạo ra hai kết quả: phát triển nghề nghiệp, điều chuyển nhân lực nội bộ. Talent Flow hỗ trợ BRG bố trí nhân sự phù hợp cho các dự án mới (đô thị thông minh, FujiMart, golf – khách sạn) từ nguồn nhân lực sẵn có.')

# ---------- context (unchanged content) ----------
def sector(icon, label, name, roles, stat, cap, hl=False):
    return ('<div class="card%s" style="flex:1">%s<h3 class="h3">%s</h3>'
            '<p class="t">%s</p>'
            '<p class="stat">%s</p><p class="cap">%s</p></div>') % (
        ' hl' if hl else '', ic(icon, label=label), name, roles, stat, cap)

S['context'] = section('context', head('BỐI CẢNH', 'AI thay đổi yêu cầu công việc tại bốn lĩnh vực của BRG',
'[Inference] Vị trí thu hẹp và vị trí thiếu nhân sự xuất hiện đồng thời, tạo cơ hội dịch chuyển nội bộ.') +
'''<div class="content">
<div class="row" style="gap:16px">
<div class="col" style="flex:1"><p class="lbl">VỊ TRÍ THU HẸP</p>
<div class="row" style="gap:16px">
%s
%s
</div>
</div>
<div class="col" style="width:150px;flex:none;align-items:center;justify-content:center">
<x-shape kind="arrow-right" class="bigarrow" style="width:110px;height:56px"></x-shape>
<p class="tb" style="text-align:center">Dịch chuyển nội bộ</p>
</div>
<div class="col" style="flex:1"><p class="lbl">VỊ TRÍ THIẾU NHÂN SỰ HOẶC MỚI</p>
<div class="row" style="gap:16px">
%s
%s
</div>
</div>
</div>
</div>
''' % (
    sector('svg:bank', 'Ngân hàng', 'Ngân hàng', 'Giao dịch viên, nhập liệu chuyển sang kênh số', '21%', 'ngân hàng tiếp tục giảm nhân sự · NHNN, quý I/2025'),
    sector('svg:cart', 'Bán lẻ', 'Bán lẻ', 'Thu ngân, nhập liệu kho, đặt hàng thủ công', 'Cao nhất', 'nhóm chịu tác động AI · ILO; thu ngân giảm nhiều nhất · WEF'),
    sector('svg:golf', 'Khách sạn – golf', 'Khách sạn – golf', 'Dịch vụ khách hàng, F&amp;B, bếp, quản lý', '60.000', 'lao động cần mỗi năm, đào tạo đáp ứng ~20.000 · Hoteljob.vn', True),
    sector('svg:city', 'Đô thị thông minh', 'Đô thị thông minh', 'Vận hành đô thị số, năng lượng, cư dân, ESG', '6 nhóm', 'giải pháp thông minh · Thành phố thông minh Bắc Hà Nội', True)),
'Hai lĩnh vực đầu có vị trí thu hẹp do kênh số và tự động hóa; hai lĩnh vực sau thiếu nhân sự hoặc mở mới. Đây là điều kiện để dịch chuyển nhân sự nội bộ thay cho cắt giảm và tuyển mới song song. Nguồn: VietnamFinance 6/2025, ILO 4/2026, WEF 2025, Hoteljob.vn, VietTimes 8/2025. Nhận định cần BRG xác nhận bằng số liệu của từng lĩnh vực.', FT)

# ---------- brg-today: hub with rounded elbow connectors in their own grid cells ----------
def node(icon, label, name, brands):
    return ('<div class="card" style="height:104px;padding:0 22px;justify-content:center"><div class="hd">%s'
            '<div><p class="tb">%s</p><p class="cap">%s</p></div></div></div>') % (ic(icon, 'sm', label), name, brands)

ENDS = [52, 168, 284]
S['brg-today'] = section('brg-today', head('HIỆN TRẠNG BRG', 'Hệ sinh thái đa ngành với nhiều pháp nhân và dự án mới') +
'''<div class="content">
<div style="display:grid;grid-template-columns:1fr 72px 312px 72px 1fr;align-items:center">
<div class="col" style="gap:12px">
%s
%s
%s
</div>
%s
<div style="width:312px;height:312px;border-radius:50%%;background:#14203C;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px">
<p class="stat" style="color:#FCA010;font-size:72px">~22.000</p>
<p class="t" style="color:#F3F4F7;text-align:center">nhân viên, hàng chục<br>công ty và liên doanh</p>
</div>
%s
<div class="col" style="gap:12px">
%s
%s
%s
</div>
</div>
<div class="g4">
<div class="card" style="padding:22px 24px"><p class="stat">4,2 tỷ USD</p><p class="cap">Thành phố thông minh Bắc Hà Nội, khởi công 8/2025</p></div>
<div class="card" style="padding:22px 24px"><p class="stat">+50</p><p class="cap">cửa hàng FujiMart theo mục tiêu đến năm 2028</p></div>
<div class="card" style="padding:22px 24px"><p class="stat">1.541</p><p class="cap">khóa học tại Học viện SeABank năm 2025</p></div>
<div class="card hl" style="padding:22px 24px"><p class="stat">2018</p><p class="cap">Hapro: toàn bộ nhân viên tiếp tục làm việc</p></div>
</div>
<p class="note">Nguồn: BRG; VietTimes 8/2025; VietnamPlus 3/2022; SeABank, Báo cáo phát triển bền vững 2025; The Leader 3/2018.</p>
</div>
''' % (node('svg:bank', 'Ngân hàng', 'Tài chính – ngân hàng', 'SeABank · hơn 5.300 nhân viên'),
       node('svg:cart', 'Bán lẻ', 'Bán lẻ – thương mại', 'BRGMart, FujiMart, Hapro, Intimex'),
       node('svg:city', 'Bất động sản', 'Bất động sản – đô thị', 'Thành phố thông minh Bắc Hà Nội'),
       rounded_bus(72, 336, ENDS, 'left', label='Ba lĩnh vực nối vào tập đoàn'),
       rounded_bus(72, 336, ENDS, 'right', label='Tập đoàn nối ra ba lĩnh vực'),
       node('svg:golf', 'Golf', 'Golf', 'Kings Island, Legend Hill, Ruby Tree'),
       node('Home', '', 'Khách sạn – nghỉ dưỡng', 'InterContinental, Hilton, Sheraton'),
       node('Star', '', 'Vui chơi giải trí', 'BRIGHTPARK Ninh Bình')),
'Nhu cầu nhân lực phát sinh từ các dự án lớn, trong khi nhân sự phân bổ tại hàng chục công ty với chuẩn quản lý riêng. Số liệu từ nguồn công khai; phạm vi con số 22.000 (có gồm SeABank hay không) cần BRG xác nhận. Thành phố thông minh Bắc Hà Nội: liên doanh Sumitomo, gần 272 ha, khởi công 19/8/2025. Học viện SeABank: trung bình 62 giờ đào tạo mỗi người năm 2025.', FT)

# ---------- problem ----------
S['problem'] = section('problem',
'''<p class="eyebrow">BÀI TOÁN</p>
<p class="statement">Làm thế nào để hệ sinh thái BRG, khoảng 22.000 nhân sự tại hàng chục pháp nhân, dịch chuyển đủ nhân sự có kỹ năng phù hợp từ vị trí đang thu hẹp sang vị trí đang thiếu hoặc mới, đúng thời điểm chiến lược yêu cầu, đồng thời giữ chân nhân sự giỏi và tuân thủ pháp luật Việt Nam?</p>
<div class="bar"></div>
<div class="content" style="gap:28px">
<p class="lbl">BA RÀNG BUỘC</p>
<div class="g3">
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">Nhiều pháp nhân, chuẩn quản lý khác nhau</p></div>
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">Thay đổi công việc lâu dài cần người lao động đồng ý</p></div>
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">Luật Bảo vệ dữ liệu cá nhân, Luật Trí tuệ nhân tạo hiệu lực từ 2026</p></div>
</div>
<p class="note">[Inference] Bảy vấn đề cấu thành, cần kiểm chứng cùng BRG: Phụ lục A2.</p>
</div>
''' % (ic('svg:city', 'sm', 'Pháp nhân'), ic('Users', 'sm'), ic('svg:scale', 'sm', 'Pháp lý')),
'Phát biểu bài toán trong một câu. Ba ràng buộc là lý do không áp dụng được cách điều chuyển một chiều: nhiều pháp nhân, quyền đồng ý của người lao động, quy định mới về dữ liệu và AI. Bảy vấn đề cấu thành là giả thuyết, trình bày tại Phụ lục A2, cần kiểm chứng trong workshop.', FT, cls='dark')

# ---------- talent-flow overview ----------
S['talent-flow'] = overview_slide('talent-flow', 'GIẢI PHÁP · TALENT FLOW', 'Bốn câu hỏi, ba luồng hoạt động trên một nền tri thức chung',
    'Lớp kết nối giữa nhu cầu (vị trí) và nguồn lực (nhân sự); không thay thế hệ thống nhân sự, đào tạo hay AI hiện có.',
    [('Chart', 'Tổ chức cần gì?', 'Năng lực, vị trí, số lượng, thời điểm'),
     ('Users', 'Hiện có gì?', 'Kỹ năng, mức thành thạo, bằng chứng'),
     ('Search', 'Còn thiếu gì?', 'Khoảng cách theo ưu tiên, thời hạn'),
     ('Play', 'Cần làm gì?', 'Đào tạo, điều chuyển, tuyển dụng')],
    'BA LUỒNG HOẠT ĐỘNG',
    [('1', 'Phát triển cá nhân', '', 'Nhân viên · Quản lý trực tiếp', 'Hồ sơ kỹ năng có bằng chứng, IDP được phê duyệt'),
     ('2', 'Dịch chuyển nội bộ', '', 'Nhân viên · Nhân sự · hai đơn vị', 'Ứng tuyển ẩn danh, chuyển công ty có thỏa thuận'),
     ('3', 'Chiến lược nhân lực', '', 'Ban Tổng giám đốc · Nhân sự tập đoàn', 'Thiếu hụt theo đơn vị, kế hoạch hành động')],
    'Talent Flow là lớp kết nối, không thay thế hệ thống nhân sự lõi, hệ thống đào tạo hay công cụ AI tạo sinh hiện có của từng công ty. Ba luồng dùng chung một nền tri thức: hồ sơ kỹ năng từ luồng 1 là đầu vào của luồng 2 và 3; hành động của luồng 3 được thực hiện qua luồng 1 (đào tạo) và luồng 2 (điều chuyển).', FT)

# ---------- roles ----------
S['roles'] = roles_slide('roles', 'VAI TRÒ THAM GIA', 'Bảy vai trò, mỗi vai trò có phạm vi và luồng công việc riêng',
    shot(BLOB['brg-menu'], 'Màn hình Việc cần làm với menu theo vai trò', 820, 513, 'Menu, việc cần làm theo quyền của vai trò · ' + BLUR),
    [('Users', 'Nhân viên', 'Hồ sơ kỹ năng, IDP, ứng tuyển nội bộ', False),
     ('CheckCircle', 'Quản lý trực tiếp', 'Duyệt IDP, xác minh kỹ năng', False),
     ('Search', 'Người đăng tuyển', 'Đăng cơ hội, xem ứng viên ẩn danh', False),
     ('Settings', 'Nhân sự pháp nhân', 'Chuỗi sáu bước, quyết định điều chuyển', False),
     ('Globe', 'Nhân sự tập đoàn', 'Điều phối giữa pháp nhân, có đồng ý', False),
     ('Chart', 'Ban Tổng giám đốc', 'Bản đồ cung – cầu, so sánh kịch bản', False),
     ('Key', 'Quản trị hệ thống', 'Tài khoản, dữ liệu nạp, tác vụ hệ thống', False),
     ('Lock', 'Nguyên tắc chung', 'Không tự phê duyệt; ghi nhật ký', True)],
    'Menu hiển thị theo quyền của vai trò; phân quyền kiểm soát tại máy chủ. Quản lý không phê duyệt IDP hay bằng chứng của chính mình. Ban Tổng giám đốc chỉ xem số liệu tổng hợp, nhóm dưới 5 người được ẩn. Phạm vi dữ liệu của từng vai trò: Phụ lục A5. Ảnh chụp từ môi trường thử nghiệm của Talent Flow, dữ liệu đã làm mờ.', FT)

# ---------- three flows ----------
S['flow-dev'] = flow_slide('flow-dev', 'LUỒNG 1 · PHÁT TRIỂN CÁ NHÂN', 'Nhân viên chủ động phát triển, quản lý xác minh kỹ năng',
    shot(BLOB['brg-idp'], 'Màn hình Kế hoạch phát triển cá nhân', 860, 543, 'Màn hình IDP · môi trường thử nghiệm, ' + BLUR),
    [('Hồ sơ kỹ năng', 'Nhân viên · kỹ năng và độ tin cậy', False),
     ('Tự đánh giá', 'Nhân viên · theo từ điển kỹ năng chung', False),
     ('Lập IDP', 'Nhân viên · AI gợi ý khóa học, mentor', False),
     ('Phê duyệt IDP ◆', 'Quản lý trực tiếp', True),
     ('Học, nộp bằng chứng', 'Nhân viên · khóa học, chứng chỉ, dự án', False),
     ('Xác minh kỹ năng ◆', 'Quản lý · hậu kiểm trong 5 ngày làm việc', True)],
    '◆ Bước có người phê duyệt',
    'Kết quả của luồng 1 là hồ sơ kỹ năng có bằng chứng, dùng cho luồng 2 và luồng 3. Kỹ năng chỉ được ghi nhận khi độ tin cậy đạt ngưỡng. Nguồn học: Học viện SeABank, đào tạo tại cơ sở (khách sạn, golf, bán lẻ). Người làm lâu năm chưa có bằng cấp được công nhận kỹ năng đã có (RPL).', FT)

S['flow-mobility'] = flow_slide('flow-mobility', 'LUỒNG 2 · DỊCH CHUYỂN NỘI BỘ', 'Cơ hội đăng tập trung, ứng tuyển ẩn danh, chuyển có thỏa thuận',
    shot(BLOB['brg-match'], 'Màn hình Tuyển dụng nội bộ', 860, 536, 'Tuyển dụng nội bộ · môi trường thử nghiệm, ' + BLUR),
    [('Đăng cơ hội', 'Người đăng tuyển · vị trí, dự án, ca cao điểm', False),
     ('Ứng tuyển ẩn danh', 'Nhân viên · bằng hồ sơ kỹ năng', False),
     ('Vòng trong ◆', 'Quản lý hiện tại được thông báo', True),
     ('Đồng thuận ◆', 'Hai đơn vị đồng ý, có phương án bù nhân sự', True),
     ('Thỏa thuận ◆', 'Văn bản về thâm niên, lương', True),
     ('Theo dõi', 'Sau 90 ngày và 12 tháng', False)],
    '◆ Bước có người phê duyệt · ràng buộc chi tiết: Phụ lục A6',
    'Cơ hội của các công ty tham gia được đăng tập trung; mỗi pháp nhân chủ động quyết định việc tham gia. Ứng tuyển ẩn danh giảm lo ngại bị đánh giá thiếu gắn bó. Tuyến đầu mùa cao điểm chỉ điều chuyển khi có người thay. Mẫu thỏa thuận chuyển công ty trong tập đoàn cần luật sư của BRG thiết kế.', FT)

S['flow-strategy'] = flow_slide('flow-strategy', 'LUỒNG 3 · CHIẾN LƯỢC NHÂN LỰC', 'Từ thay đổi chiến lược đến kế hoạch nhân sự theo đơn vị',
    shot(BLOB['brg-context'], 'Màn hình Bản đồ bối cảnh', 860, 542, 'Bản đồ bối cảnh · môi trường thử nghiệm, ' + BLUR),
    [('Bối cảnh', 'Ban Tổng giám đốc · chiến lược, dự án mới', False),
     ('Năng lực', 'Nhân sự · vị trí, năng lực cần có', False),
     ('Con người', 'Kỹ năng hiện có, từ luồng 1', False),
     ('Thiếu hụt ◆', 'Nhân sự · khoảng trống theo đơn vị, thời hạn', True),
     ('Hành động ◆', 'Đào tạo, điều chuyển, tuyển ngoài', True),
     ('Theo dõi', 'Số liệu tổng hợp, ẩn nhóm dưới 5 người', False)],
    '◆ Bước có người phê duyệt',
    'Chuỗi sáu bước là luồng của bộ phận nhân sự và Ban Tổng giám đốc. Hai bước có dấu ◆ luôn có người có thẩm quyền phê duyệt. Bản đồ cung – cầu theo lĩnh vực, công ty, vị trí và giai đoạn; mô phỏng theo kịch bản (tốc độ mở cửa hàng, tiến độ dự án, tỷ lệ giao dịch số).', FT)

# ---------- knowledge architecture ----------
S['architecture'] = arch_slide('architecture', 'KIẾN TRÚC CƠ SỞ TRI THỨC', 'Workforce Graph là lõi tri thức dùng chung cho mọi vai trò',
    [('ỨNG DỤNG', 'Web tiếng Việt', ['Nhân viên', 'Quản lý', 'Nhân sự', 'Ban Tổng giám đốc', ('Di động cho tuyến đầu', 'o')], ''),
     ('LỚP AI', 'Người xác nhận', ['Trích xuất kỹ năng', 'Chuẩn hóa', 'Ghép nối có giải thích', 'Gợi ý lộ trình'], ''),
     ('WORKFORCE GRAPH', '7 lớp + mở rộng', ['Bối cảnh kinh doanh', 'Năng lực', 'Tổ chức, vị trí', 'Từ điển kỹ năng',
                                              'Con người, bằng chứng', 'Mạng lưới', 'Phát triển tương lai', ('Pháp nhân và đồng ý', 'x')], 'core'),
     ('ĐỊNH DANH', 'Mã hóa riêng', ['Pháp nhân A', 'Pháp nhân B', 'Pháp nhân khác', ('SeABank: đề xuất tách riêng', 'o')], ''),
     ('TÍCH HỢP', 'Cần xác nhận', ['Nhân sự lõi', 'Học viện SeABank', 'AINAVI: tuyển nội bộ', 'Đăng nhập một lần'], '')],
    'QUẢN TRỊ',
    [('Key', 'Phân quyền theo vai trò, pháp nhân'), ('CheckCircle', 'Đồng ý theo mục đích'), ('Users', 'Người xác nhận gợi ý AI'),
     ('Activity', 'Nhật ký truy cập'), ('Lock', 'Ẩn nhóm dưới 5 người'), ('Globe', 'Dữ liệu tại Việt Nam')],
    'Workforce Graph gồm 7 lớp: bối cảnh kinh doanh, năng lực, tổ chức và vị trí, từ điển kỹ năng, con người và bằng chứng, mạng lưới, phát triển tương lai. Với BRG bổ sung lớp pháp nhân và đồng ý: nhân viên thuộc pháp nhân nào, đồng ý chia sẻ hồ sơ với ai. Graph chỉ lưu mã ẩn danh; dữ liệu định danh lưu riêng theo pháp nhân, có mã hóa. Từ điển kỹ năng ba tầng: chung (Thông tư 02/2025, SFIA 9), ngành (VTOS/ACCSTP), riêng của BRG. [Inference] Với SeABank, phương án an toàn là triển khai riêng theo quy định an toàn thông tin ngành ngân hàng. Tích hợp (cần xác nhận theo hệ thống thực tế của BRG): hệ thống nhân sự lõi của từng pháp nhân (tổ chức, chức danh, lịch sử công tác); đào tạo và e-learning như Học viện SeABank; AINAVI cho tuyển nội bộ và thi trực tuyến kiểm tra kỹ năng; hệ thống đánh giá (chỉ đọc trường được phép); đăng nhập một lần. Kiến trúc tổng thể của giải pháp: Phụ lục A1.', FT)

# ---------- data flow ----------
S['data-flow'] = dataflow_slide('data-flow', 'LUỒNG DỮ LIỆU', 'Tám chặng dữ liệu, ba điểm con người kiểm soát',
    [('Nguồn dữ liệu', 'Nhân sự lõi từng pháp nhân, đào tạo, chứng chỉ, mô tả công việc', ''),
     ('Cổng pháp lý ◆', 'Đồng ý kiểm chứng được; đánh giá tác động trước khi dùng dữ liệu thật', 'ap'),
     ('Chuẩn hóa', 'Quy đổi chức danh của nhiều pháp nhân về từ điển chung', ''),
     ('AI trích xuất kỹ năng', 'Từ văn bản tiếng Việt, tiếng Anh', ''),
     ('Người xác nhận ◆', 'Nhân viên, quản lý xác nhận; ghi vết mọi gợi ý', 'ap'),
     ('Workforce Graph', 'Chỉ lưu mã ẩn danh; lớp pháp nhân và đồng ý', 'core'),
     ('Suy luận, mô phỏng', 'Kịch bản theo dự án, mùa vụ; giới hạn 60 ngày', ''),
     ('Người quyết định ◆', 'AI chỉ đề xuất; quyết định được ghi lại', 'ap')],
    'Kết quả sau 90 ngày và 12 tháng cập nhật Workforce Graph',
    'Dữ liệu định danh lưu riêng theo pháp nhân · graph chỉ dùng mã ẩn danh · dữ liệu kỹ năng không dùng để chấm điểm trừ',
    'Tám chặng: nguồn, cổng pháp lý, chuẩn hóa, AI trích xuất kỹ năng, người xác nhận, Workforce Graph, suy luận và mô phỏng, người quyết định. Ba chặng có dấu ◆ luôn có con người kiểm soát. Với BRG, dữ liệu sang pháp nhân khác cần đồng ý kiểm chứng được; hồ sơ đánh giá tác động gửi A05 trước khi dùng dữ liệu thật (Nghị định 356). Nhịp vận hành theo sự kiện và mùa vụ: mở cửa hàng, mốc dự án, mùa cao điểm.', FT)

# ---------- AI principles ----------
S['ai'] = ai_slide('ai', 'NGUYÊN TẮC HOẠT ĐỘNG CỦA AI', 'AI đề xuất, người có thẩm quyền quyết định',
    [('Dữ liệu đã ẩn danh', False), ('AI gợi ý, kèm lý do', False), ('◆ Người phụ trách quyết định', True), ('Lưu kết quả, ghi nhật ký', False)],
    [('Users', 'Con người quyết định', 'AI không tự điều chuyển, không tự loại hồ sơ'),
     ('Lightbulb', 'Giải thích được', 'Mỗi gợi ý kèm lý do và kỹ năng còn thiếu'),
     ('svg:ban', 'Không chấm điểm trừ', 'Dữ liệu kỹ năng chỉ dùng để phát triển, bố trí'),
     ('Lock', 'Bảo vệ dữ liệu', 'Ẩn danh trước khi AI xử lý; đồng ý theo mục đích'),
     ('Activity', 'Truy vết được', 'Nhật ký hoạt động AI; nhân viên xem, sửa được hồ sơ')],
    'TRIỂN KHAI', 'SaaS, Private Cloud hoặc máy chủ tại doanh nghiệp · dữ liệu và mô hình AI đặt tại Việt Nam',
    'AI đảm nhận phần đọc, chuẩn hóa và gợi ý: trích xuất kỹ năng từ văn bản tiếng Việt, tiếng Anh; chuẩn hóa về từ điển kỹ năng chung; gợi ý mức độ phù hợp kèm lý do và kỹ năng còn thiếu; gợi ý lộ trình học, mentor. Kết quả tự đánh giá không phải xếp hạng chính thức. Phương án triển khai chọn theo yêu cầu bảo mật của từng pháp nhân; chuyển dữ liệu ra nước ngoài cần hồ sơ theo Nghị định 356.', FT)

# ---------- compliance (overview; article detail in appendix A6) ----------
METER = ('<div class="row" style="gap:12px;align-items:center"><div class="meter" style="flex:1">'
         '<div class="fill" style="width:75%"></div></div><p class="cap" style="color:#14203C">Ví dụ: <b>45/60 ngày</b></p></div>')
HUMAN = ('<div class="mini"><p class="pill soft">AI đề xuất</p>%s<p class="pill">Người quyết định</p></div>' % arrow('arrow-s', style='width:32px;height:22px'))
S['compliance'] = compliance_slide('compliance', 'TUÂN THỦ', 'Yêu cầu pháp lý được thiết kế thành chức năng của hệ thống',
    [dict(icon='Users', theme='Người lao động', laws=['Bộ luật Lao động 2019<br>Điều 29, 33, 42, 44'],
          req='Tối đa 60 ngày điều chuyển tạm thời/năm khi chưa đồng ý; ưu tiên đào tạo lại',
          visual=METER, feats=['Cảnh báo trước giới hạn 60 ngày', 'Lưu hồ sơ ưu tiên đào tạo lại']),
     dict(icon='Lock', theme='Dữ liệu cá nhân', laws=['Luật Bảo vệ dữ liệu cá nhân · 1/1/2026', 'Nghị định 356/2025/NĐ-CP'],
          req='Đồng ý kiểm chứng được; đánh giá tác động; xóa dữ liệu khi chấm dứt hợp đồng',
          visual='', feats=['Ghi nhận đồng ý theo mục đích', 'PoC dùng dữ liệu ẩn danh', 'Xóa, ẩn danh theo quy tắc lưu giữ']),
     dict(icon='Lightbulb', theme='Trí tuệ nhân tạo', laws=['Luật Trí tuệ nhân tạo · 1/3/2026'],
          req='Quản lý hệ thống AI theo mức độ rủi ro',
          visual=HUMAN, feats=['Nhật ký hoạt động AI, truy vết']),
     ],
    'Thông tin tham khảo cho thiết kế, không phải tư vấn pháp lý; cần bộ phận pháp chế của BRG xác nhận. Chi tiết theo điều khoản: Phụ lục A7.',
    'Bộ luật Lao động: chuyển lâu dài cần thỏa thuận (Điều 33); thay đổi cơ cấu, công nghệ cần phương án sử dụng lao động (Điều 42, 44). Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 có hiệu lực từ 1/1/2026. Nghị định 356 quy định hồ sơ đánh giá tác động do A05 xem xét. Việc AI gợi ý bố trí nhân sự có thuộc nhóm rủi ro cao hay không phụ thuộc văn bản hướng dẫn. Con số 45/60 là ví dụ minh họa giao diện.', FT)

# ---------- poc (unchanged content) ----------
phases = [('Khảo sát, dữ liệu ẩn danh', 1, 2, False), ('Từ điển kỹ năng, vị trí đích', 3, 4, False),
          ('Hồ sơ kỹ năng thí điểm', 5, 7, True), ('Bản đồ cung – cầu', 8, 9, False),
          ('Vận hành thử nội bộ', 10, 11, False), ('Đánh giá, kế hoạch mở rộng', 12, 12, True)]
g = ['<p class="gl" style="grid-column:1;grid-row:1"><b>Tuần</b></p>']
g += ['<p class="gh" style="grid-column:%d;grid-row:1">%d</p>' % (w + 1, w) for w in range(1, 13)]
for r, (lab, a, b, hl) in enumerate(phases, start=2):
    g.append('<p class="gl" style="grid-column:1;grid-row:%d">%s</p>' % (r, lab))
    g.append('<div class="gb%s" style="grid-column:%d / %d;grid-row:%d"></div>' % (' hl' if hl else '', a + 1, b + 2, r))
g.append('<p class="gl" style="grid-column:1;grid-row:8"><b>◆ Quyết định 1</b></p>')
g.append('<div class="gd" style="grid-column:6;grid-row:8"><x-shape kind="diamond" class="dia"></x-shape></div>')
g.append('<p class="cap" style="grid-column:7 / 14;grid-row:8">Hồ sơ đánh giá tác động được chấp thuận: xử lý dữ liệu thật</p>')
g.append('<p class="gl" style="grid-column:1;grid-row:9"><b>◆ Quyết định 2</b></p>')
g.append('<p class="cap" style="grid-column:2 / 13;grid-row:9;text-align:right">Mở rộng sang các công ty khác và SeABank</p>')
g.append('<div class="gd" style="grid-column:13;grid-row:9"><x-shape kind="diamond" class="dia"></x-shape></div>')
S['poc'] = section('poc', head('BẮT ĐẦU · PoC 12 TUẦN', 'PoC trên một nhóm vị trí nguồn – đích, hai điểm quyết định') +
'''<div class="content">
<div class="row" style="flex-wrap:wrap;gap:12px"><p class="pill soft">200–300 nhân viên</p><p class="pill soft">20–30 vị trí đích</p><p class="pill soft">2–3 công ty thành viên tại Hà Nội</p><p class="pill soft">SeABank tham gia giai đoạn 2</p></div>
<div class="gantt">
%s
</div>
</div>
''' % '\n'.join(g),
'Bốn tuần đầu chỉ sử dụng dữ liệu ẩn danh; hồ sơ đánh giá tác động được lập từ tuần 1–2. Nếu hồ sơ chưa được chấp thuận, PoC tiếp tục trên dữ liệu ẩn danh. Ví dụ nhóm nguồn – đích: thu ngân, văn phòng khối bán lẻ chuyển sang cửa hàng FujiMart mới, F&B khách sạn – golf và một số vị trí số (Phụ lục A4). BRG lựa chọn nhóm vị trí thực tế.', FT)

# ---------- kpi (unchanged content) ----------
tiles = [('≥ 70%', 'nhân viên thí điểm xác nhận hồ sơ kỹ năng'), ('≥ 80%', 'gợi ý kỹ năng của AI được chấp nhận'),
         ('≥ 1', 'cuộc họp kế hoạch nhân sự dùng bản đồ cung – cầu'), ('Tăng', 'hồ sơ ứng tuyển, dự án nội bộ so với đợt trước'),
         ('100%', 'trường hợp điều chuyển có thỏa thuận văn bản')]
comm = [('CheckCircle', 'Mọi thiếu hụt, IDP, điều chuyển có người phê duyệt'), ('svg:ban', 'Không dùng dữ liệu kỹ năng để chấm điểm trừ'),
        ('Lock', 'Dữ liệu định danh bảo mật riêng, ghi nhật ký'), ('Users', 'Tuyến đầu cao điểm chỉ điều chuyển khi có người thay')]
S['kpi'] = section('kpi', head('ĐO LƯỜNG VÀ CAM KẾT', 'Đo bằng nhân sự đảm nhận vị trí mới, không bằng giờ đào tạo',
'Tiêu chí thành công của PoC (đề xuất, thống nhất cùng BRG) và bốn cam kết với người dùng.') +
'''<div class="content">
<div class="g5">
%s
</div>
<div class="band"><p class="lbl">BỐN CAM KẾT VỚI NGƯỜI DÙNG</p>
<div class="g4">
%s
</div>
</div>
</div>
''' % ('\n'.join('<div class="card"><p class="stat">%s</p><p class="cap">%s</p></div>' % t for t in tiles),
       '\n'.join('<div class="hd">%s<p class="t" style="flex:1">%s</p></div>' % (ic(i, 'sm', 'Không'), t) for i, t in comm)),
'Các ngưỡng là đề xuất, cần thống nhất với BRG trước tuần 1. Sau PoC, bổ sung chỉ số dài hạn: số nhân sự đảm nhận vị trí đích mỗi năm, tỷ lệ vị trí lấp bằng nhân sự nội bộ, tỷ lệ giữ chân sau 12 tháng, chi phí so với tuyển ngoài.', FT)

# ---------- next-steps (unchanged content) ----------
def scard(n, title, items):
    return '<div class="card" style="flex:1"><div class="hd"><p class="num">%s</p><h3 class="h3">%s</h3></div><ul class="lst">%s</ul></div>' % (
        n, title, ''.join('<li>%s</li>' % i for i in items))

checks = ['Nhu cầu nhân sự dự án mới 2027–2028', 'Nơi lưu dữ liệu nhân sự, đào tạo', 'Quyền dữ liệu tại khách sạn do hãng quản lý',
          'Chính sách khi chuyển công ty', 'Đơn vị đầu tư, người quyết định']
S['next-steps'] = section('next-steps', head('BƯỚC TIẾP THEO', 'Ba bước khởi động cùng BRG') +
'''<div class="content">
<div class="row" style="gap:12px;align-items:stretch">
%s
<x-shape kind="arrow-right" class="arrow-s" style="align-self:center"></x-shape>
%s
<x-shape kind="arrow-right" class="arrow-s" style="align-self:center"></x-shape>
%s
</div>
<div class="card hl"><p class="lbl">NĂM NỘI DUNG CẦN BRG XÁC NHẬN</p>
<div class="g5">
%s
</div>
</div>
</div>
''' % (scard('1', 'Workshop nửa ngày', ['Kết quả cần đạt · 30 phút', 'Giả định hiện tại · 45 phút', 'Ràng buộc thực tế · 60 phút', 'Xây dựng phương án · 45 phút', 'Kiểm chứng, phạm vi PoC · 30 phút']),
       scard('2', 'Phạm vi PoC', ['Một nhóm vị trí nguồn – đích tại Hà Nội', '2–3 công ty thành viên', '20–30 vị trí đích, 200–300 nhân viên', 'Tiêu chí thành công trước tuần 1']),
       scard('3', 'Dữ liệu và pháp lý', ['Hồ sơ đánh giá tác động theo Nghị định 356', 'Nhân sự phụ trách bảo vệ dữ liệu', 'Dữ liệu ẩn danh trong bốn tuần đầu', 'Danh sách hệ thống nguồn']),
       '\n'.join('<div class="hd">%s<p class="t" style="flex:1">%s</p></div>' % (ic('Check', 'sm'), c) for c in checks)),
'Workshop khoảng 3,5 giờ, đi theo năm bước của phương pháp first principles (Phụ lục A3). Đầu ra: danh sách ràng buộc cứng có người chịu trách nhiệm và phạm vi PoC có điểm dừng. Thành phần đề xuất: nhân sự của 2–3 pháp nhân trong PoC, người phụ trách bảo vệ dữ liệu, lãnh đạo các dự án đích (đô thị thông minh, FujiMart, golf). Với BRG, phiên 2–3 nên chạy theo từng pháp nhân trước khi tổng hợp ở phiên 4.', FT)

# ================= APPENDIX =================
S['ap-architecture'] = system_arch_slide('ap-architecture', 'PHỤ LỤC A1 · KIẾN TRÚC TỔNG THỂ', 'Kiến trúc tổng thể đề xuất: từ người dùng đến hệ thống hiện có',
    ['Nhân viên', 'Quản lý', 'Nhân sự', 'Ban Tổng giám đốc', 'Quản trị'], ['Web tiếng Việt', 'Di động cho tuyến đầu'],
    ['M1 · Vị trí và từ điển kỹ năng', 'M2 · Hồ sơ kỹ năng, bằng chứng', 'M3 · Danh mục nhân sự động',
     'M4 · Định hướng nghề nghiệp', 'M5 · Thị trường nhân lực nội bộ', 'M6 · Điều chuyển và theo dõi'],
    ['Trích xuất kỹ năng', 'Chuẩn hóa', 'Ghép nối có giải thích', 'Gợi ý lộ trình', 'Mô phỏng kịch bản'],
    [('Workforce Graph · 7 lớp', 'k'), ('Lớp pháp nhân và đồng ý', 'o'), 'Kho định danh · mã hóa', 'Nhật ký truy vết'],
    ['Nạp dữ liệu từ hệ thống nguồn', 'Chỉ đọc trường được phép', 'Đăng nhập một lần'],
    ['Nhân sự lõi từng pháp nhân', 'Học viện SeABank', 'AINAVI: tuyển nội bộ, thi trực tuyến', 'Hệ thống đánh giá'],
    'Phân quyền theo vai trò, pháp nhân · đồng ý theo mục đích · ẩn danh trước khi AI xử lý · nhật ký truy cập',
    'SaaS, Private Cloud hoặc máy chủ tại doanh nghiệp · dữ liệu lưu tại Việt Nam · SeABank: đề xuất triển khai riêng',
    'Kiến trúc đề xuất theo tài liệu nghiên cứu BRG (mục 7.2, 7.3). Sáu module nghiệp vụ: M1 kiến trúc vị trí và từ điển kỹ năng; M2 hồ sơ kỹ năng có bằng chứng; M3 danh mục nhân sự động; M4 định hướng nghề nghiệp cá nhân; M5 thị trường nhân lực nội bộ; M6 hỗ trợ điều chuyển và theo dõi. Lớp dữ liệu theo tài liệu nghiên cứu: Workforce Graph trên Neo4j; dữ liệu định danh lưu ở PostgreSQL có mã hóa, tách theo pháp nhân; graph chỉ dùng mã ẩn danh. Mọi gợi ý của AI có bước người xác nhận và được ghi lại. Danh sách tích hợp cần xác nhận theo hệ thống thực tế của BRG. [Inference] Với SeABank, phương án an toàn là triển khai riêng, chỉ chia sẻ hồ sơ khi nhân viên đồng ý.', FT)

S['ap-problems'] = problems_slide('ap-problems', 'PHỤ LỤC A2 · VẤN ĐỀ CẤU THÀNH', 'Bảy vấn đề cần kiểm chứng cùng BRG',
    [('P1', 'Nhu cầu chưa lượng hóa', 'Dự án mới nêu quy mô, chưa nêu nhu cầu nhân sự theo kỹ năng', 'Trung bình'),
     ('P2', 'Năng lực chưa tổng hợp', 'Kỹ năng chưa số hóa theo chuẩn chung; mỗi đơn vị dùng chuẩn riêng', 'Trung bình'),
     ('P3', 'Đào tạo chưa gắn vị trí đích', 'Đo bằng giờ học (SeABank 62 giờ/người), chưa đo số người đảm nhận vị trí mới', 'Trung bình'),
     ('P4', 'Thủ tục chuyển công ty phức tạp', 'Hợp đồng, thâm niên, thang lương khác nhau; thay đổi lâu dài cần đồng ý (Điều 29, 33)', 'Cao'),
     ('P5', 'Thiếu thông tin cơ hội', 'Nhân viên chưa biết vị trí nội bộ đang mở; nghỉ việc ngành khách sạn 18,9%', 'Cao'),
     ('P6', 'Khác biệt pháp nhân, văn hóa', 'Doanh nghiệp gốc nhà nước, liên doanh Nhật Bản, khách sạn quốc tế, ngân hàng niêm yết', 'Cao'),
     ('P7', 'Chưa đo kết quả sau điều chuyển', 'Chưa có chỉ số vốn nhân lực cấp tập đoàn', 'Trung bình')],
    '[Inference] Toàn bộ bảng là giả thuyết rút từ nguồn công khai; mức chắc chắn là đánh giá của nhóm nghiên cứu.',
    'Mỗi vấn đề gắn với một chức năng của Talent Flow: P1, P7 với danh mục nhân sự động; P2 với hồ sơ kỹ năng có bằng chứng; P3, P5 với định hướng nghề nghiệp cá nhân; P4, P6 với thị trường nhân lực nội bộ và hỗ trợ điều chuyển.', FT)


S['ap-mobility'] = section('ap-mobility', head('PHỤ LỤC A6 · DỊCH CHUYỂN NỘI BỘ', 'Hiệu quả giữ chân và ràng buộc của kênh nội bộ') +
'''<div class="content">
%s
<div class="g2">
<div class="card"><p class="lbl">HIỆU QUẢ GIỮ CHÂN CỦA KÊNH NỘI BỘ</p>
<div class="hbar"><p class="bl">Đã chuyển vị trí nội bộ</p><div class="track"><div class="fill" style="width:75%%"></div></div><p class="bv">75%%</p></div>
<div class="hbar"><p class="bl">Chưa chuyển vị trí</p><div class="track"><div class="fill gray" style="width:56%%"></div></div><p class="bv">56%%</p></div>
<p class="cap">Khả năng ở lại sau 2 năm · LinkedIn Global Talent Trends, 10/2022</p></div>
<div class="card hl"><p class="lbl">RÀNG BUỘC CỨNG TRONG HỆ THỐNG</p>
%s
%s
%s
</div>
</div>
</div>
''' % (timeline([('1', 'Đăng cơ hội', 'Vị trí, dự án, ca cao điểm', False), ('2', 'Ứng tuyển', 'Ẩn danh, bằng hồ sơ kỹ năng', False),
                 ('3', 'Vòng trong ◆', 'Quản lý hiện tại được thông báo', True), ('4', 'Đồng thuận ◆', 'Hai đơn vị đồng ý, bù nhân sự', True),
                 ('5', 'Thỏa thuận ◆', 'Văn bản: thâm niên, lương', True), ('6', 'Theo dõi', 'Sau 90 ngày, 12 tháng', False)]),
       hdrow('Users', 'Tuyến đầu mùa cao điểm chỉ điều chuyển khi có người thay'),
       hdrow('Clock', 'Theo dõi ngày điều chuyển tạm thời so với giới hạn 60 ngày'),
       hdrow('Lock', 'Chia sẻ hồ sơ sang công ty khác khi nhân viên đồng ý')),
'Dự án nội bộ chiếm 10–20% thời gian. Ba bước có dấu ◆ cần phê duyệt. Ứng tuyển ẩn danh giảm lo ngại bị đánh giá thiếu gắn bó. Mẫu thỏa thuận chuyển công ty trong tập đoàn cần luật sư của BRG thiết kế.', FT)


for sid, html_ in S.items():
    write(ROOT, sid, html_)
print('written', len(S))
