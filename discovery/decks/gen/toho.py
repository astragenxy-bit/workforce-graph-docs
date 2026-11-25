# Generates the content slides of the Toho Gas deck into ../toho/project/slides/.
# Hand-maintained HTML (not written here): thanks and the migrated appendix slides
# (ap-usecases, ap-roles, ap-matrix, ap-five-whys, ap-principles, ap-sources).
import sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import ic, footer, head, section, write, hdrow, arrow, shot
from blocks import (overview_slide, roles_slide, flow_slide, arch_slide, dataflow_slide, ai_slide,
                    compliance_slide, problems_slide, system_arch_slide, cover_slide)

ROOT = os.path.abspath(os.path.join(HERE, '..', 'toho'))
FT = footer('TALENT FLOW · TOHO GAS')
BLOB = json.load(open(os.path.join(ROOT, 'blobs.json')))  # name -> /_blob/<id>
S = {}
SAMPLE = 'dữ liệu mẫu trong môi trường thử nghiệm'


# ---------- cover: the description is drawn as the labelled illustration ----------
S['cover'] = cover_slide('cover', 'FPT IS · THÁNG 11/2026', 'Talent Flow<br>cho Toho Gas',
    'Từ chiến lược đến kỹ năng của từng thành viên',
    ['Nghiệp vụ<br>nhân sự', 'Luồng<br>dữ liệu', 'Tri thức<br>doanh nghiệp', 'AI'],
    ['Phát triển<br>nghề nghiệp', 'Điều chuyển<br>nhân lực nội bộ'],
    'TALENT FLOW · TÀI LIỆU TRAO ĐỔI VỚI TOHO GAS',
    'Talent Flow là nền tảng phát triển nghề nghiệp và điều chuyển nhân lực nội bộ dựa trên kỹ năng, kết hợp nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp và AI. Hình minh họa: bốn thành phần (nghiệp vụ nhân sự, luồng dữ liệu, tri thức doanh nghiệp, AI) hội về kỹ năng ở trung tâm và tạo ra hai kết quả: phát triển nghề nghiệp, điều chuyển nhân lực nội bộ. Talent Flow hỗ trợ nhóm Toho Gas chuyển kế hoạch trung hạn thành nhu cầu kỹ năng cụ thể và bố trí nhân sự nội bộ cho mảng chiến lược.')

# ---------- context (unchanged content) ----------
def dcard(icon, label, name, change, skill, hl=False):
    return ('<div class="card%s">%s<h3 class="h3">%s</h3>'
            '<p class="t">%s</p><p class="t"><b style="color:#A85A00">Kỹ năng mới:</b> %s</p></div>') % (
        ' hl' if hl else '', ic(icon, label=label), name, change, skill)

S['context'] = section('context', head('BỐI CẢNH', 'Bốn hướng thay đổi công việc trong ngành gas Nhật Bản') +
'''<div class="content">
<div class="g4">
%s
%s
%s
%s
</div>
<div class="row" style="align-items:stretch">
<div class="band" style="flex:1"><div class="hd"><p class="lbl">保安人材</p><p class="t" style="flex:1">Thiếu nhân lực an toàn do dân số già; METI xác định là vấn đề chính sách, cùng smart 保安 và truyền nghề (技能伝承).</p></div></div>
<div class="card" style="width:300px;flex:none"><p class="stat">39%%</p><p class="cap">kỹ năng cốt lõi đổi đến 2030 · WEF</p></div>
<div class="card" style="width:300px;flex:none"><p class="stat">85,1%%</p><p class="cap">doanh nghiệp thiếu nhân lực DX · IPA</p></div>
</div>
</div>
''' % (dcard('svg:gauge', 'Tự động hóa', 'Tự động hóa', 'Đọc đồng hồ (検針) sang smart meter; tuần tra sang drone, camera AI', 'Dữ liệu thiết bị, vận hành tự động'),
       dcard('svg:bolt', 'Điện', 'Điện, năng lượng', 'Bán gas mở rộng sang bán điện, tái tạo, giao dịch điện', 'Thị trường điện, dự báo, quản trị rủi ro', True),
       dcard('svg:leaf', 'Trung hòa carbon', 'Trung hòa carbon', 'e-methane, hydrogen, thu hồi CO₂', 'Kỹ thuật hóa học mới, dự án quốc tế', True),
       dcard('svg:headset', 'Dịch vụ khách hàng', 'Dịch vụ khách hàng', 'Tổng đài, bán hàng sang kênh số, AI hỗ trợ', 'Marketing số, phân tích, thiết kế dịch vụ')),
'[Inference] Phần lớn thay đổi là kỹ năng mới cho vị trí hiện có, không chỉ là vị trí mới cần nhân sự mới. Bốn hướng thay đổi theo nghiên cứu ngành; nền cam là hai hướng gắn với mảng chiến lược của Toho Gas. Song song, nhân lực an toàn thiếu và cần truyền nghề, nên không thể rút nhân sự khỏi vị trí an toàn khi chưa có người thay thế. Nguồn: WEF Future of Jobs 2025; IPA DX動向2025; METI 2025.', FT)

# ---------- toho-today (unchanged content) ----------
segs = [('Gas', 3391, '#14203C', '#F3F4F7'), ('LPG, năng lượng khác', 1284, '#5B6478', '#F3F4F7'),
        ('Điện', 196, '#FCA010', '#14203C'), ('Khác', 1260, '#C9D0DC', '#14203C')]
total = sum(s[1] for s in segs)
bar = ''.join('<div class="seg" style="width:%.1f%%;background:%s">%s</div>' % (
    v * 100.0 / total, c, ('<p style="color:%s">%s</p>' % (tc, '{:,}'.format(v).replace(',', '.'))) if v > 500 else '') for n, v, c, tc in segs)
legend = ''.join('<div class="hd" style="gap:10px"><div style="width:24px;height:24px;border-radius:4px;background:%s;flex:none"></div><p class="t"%s>%s · %s</p></div>' % (
    c, ' style="color:#A85A00;font-weight:700"' if n == 'Điện' else '', n, '{:,}'.format(v).replace(',', '.')) for n, v, c, tc in segs)
tiles = [('14,7 năm', 'thâm niên bình quân, công ty mẹ'), ('1,93%', 'tỷ lệ nghỉ việc FY2024'),
         ('224', 'DX人材, vượt mục tiêu 200'), ('~1.500', 'người dùng Graffer AI Studio')]
S['toho-today'] = section('toho-today', head('HIỆN TRẠNG TOHO GAS', 'Chiến lược rõ ràng, dịch chuyển nhân sự chưa được lượng hóa',
'Kế hoạch trung hạn 2025–2027 đẩy nhanh phân bổ lại nguồn lực; chưa công bố số liệu dịch chuyển nhân sự.') +
'''<div class="content">
<div class="card"><p class="lbl">6.131 NHÂN VIÊN HỢP NHẤT THEO MẢNG · 3/2026</p>
<div class="share">%s</div>
<div class="row" style="gap:40px">%s<p class="tb" style="color:#A85A00;margin-left:auto">Mảng điện ≈ 3%% nhân sự</p></div>
</div>
<div class="row" style="align-items:stretch">
<div class="card" style="flex:1"><p class="lbl">ĐẦU TƯ 2025–2027 · TỶ YÊN</p>
<div class="hbar"><p class="bl">Mảng chiến lược</p><div class="track"><div class="fill" style="width:100%%"></div></div><p class="bv">~130</p></div>
<div class="hbar"><p class="bl">Mảng lõi</p><div class="track"><div class="fill navy" style="width:84.6%%"></div></div><p class="bv">~110</p></div>
<p class="cap">Nguồn: Kế hoạch trung hạn 2025–2027; Báo cáo tích hợp 2025; báo cáo chứng khoán FY2026</p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;width:860px;flex:none">
%s
</div>
</div>
</div>
''' % (bar, legend, '\n'.join('<div class="card" style="padding:18px 22px;gap:6px"><p class="stat" style="font-size:48px">%s</p><p class="cap">%s</p></div>' % t for t in tiles)),
'Đầu tư cho mảng chiến lược lớn hơn mảng lõi, trong khi mảng điện chỉ có 196 trên 6.131 nhân viên (khoảng 3%). Thâm niên cao và tỷ lệ nghỉ việc thấp phản ánh mô hình tuyển dụng thành viên (メンバーシップ型雇用). Công ty mẹ khoảng 970 người; phần lớn nhân sự thuộc các công ty con. Chế độ nhân sự mới từ 4/2026 nhằm phát huy nhân sự có chuyên môn sâu và cho phép thăng tiến sớm nhân sự trẻ. Báo cáo tích hợp nêu kế hoạch xây dựng 人材ポートフォリオ nhưng chưa có số liệu dịch chuyển. Graffer AI Studio triển khai tại khoảng 30 công ty nhóm (ASCII).', FT)

# ---------- problem ----------
S['problem'] = section('problem',
'''<p class="eyebrow">BÀI TOÁN</p>
<p class="statement">Làm thế nào để nhóm Toho Gas, khoảng 6.000 nhân sự gần như không nghỉ việc và không sa thải, dịch chuyển đủ nhân sự có kỹ năng phù hợp từ mảng lõi đang thu hẹp sang mảng chiến lược và các vị trí mới của AI, đúng thời điểm chiến lược yêu cầu, đồng thời giữ an toàn cung cấp và sự gắn kết của nhân viên?</p>
<div class="bar"></div>
<div class="content" style="gap:28px">
<p class="lbl">BA RÀNG BUỘC</p>
<div class="g3">
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">Khoảng 30 công ty con; công ty mẹ khoảng 970 người</p></div>
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">An toàn cung cấp là ưu tiên tuyệt đối</p></div>
<div class="card" style="gap:12px">%s<p class="t28" style="color:#F3F4F7">Chế độ nhân sự mới vận hành từ 4/2026</p></div>
</div>
<p class="note">[Inference] Bảy vấn đề cấu thành, cần kiểm chứng cùng Toho Gas: Phụ lục A7. Phân tích nguyên nhân 5 Whys: Phụ lục A5.</p>
</div>
''' % (ic('svg:city', 'sm', 'Công ty con'), ic('svg:helmet', 'sm', 'An toàn'), ic('Clock', 'sm')),
'Phát biểu bài toán trong một câu. Ba ràng buộc: nhân sự phân bổ ở nhiều công ty con, an toàn cung cấp không được ảnh hưởng, giải pháp khớp chế độ nhân sự mới thay vì đề xuất chế độ khác. Bảy vấn đề cấu thành là giả thuyết (Phụ lục A7), cần kiểm chứng trong workshop.', FT, cls='dark')

# ---------- talent-flow overview ----------
S['talent-flow'] = overview_slide('talent-flow', 'GIẢI PHÁP · TALENT FLOW', 'Bốn câu hỏi, bốn luồng hoạt động trên một nền tri thức chung',
    'Lớp kết nối giữa nhu cầu (vị trí) và nguồn lực (nhân sự); không thay thế hệ thống nhân sự, đào tạo hay AI hiện có.',
    [('Chart', 'Tổ chức cần gì?', 'Năng lực, vị trí, số lượng, thời điểm'),
     ('Users', 'Hiện có gì?', 'Kỹ năng, mức thành thạo, bằng chứng'),
     ('Search', 'Còn thiếu gì?', 'Khoảng cách theo ưu tiên, thời hạn'),
     ('Play', 'Cần làm gì?', 'Đào tạo, điều chuyển, biệt phái, tuyển')],
    '',
    [('1', 'Lộ trình phát triển', '', 'Nhân viên · Cấp trên', 'Hồ sơ kỹ năng, IDP theo ngạch mới'),
     ('2', 'An toàn và kế thừa', '', 'Cấp trên · Nhân sự', 'Mức tối thiểu nhân lực 保安, truyền nghề'),
     ('3', 'Tuyển dụng nội bộ', '', 'Nhân viên · Người đăng tuyển', '社内公募 bảo mật, có phương án bù người'),
     ('4', 'Chiến lược nhân lực', '', 'Ban giám đốc · Văn phòng DX', 'Danh mục nhân sự, cung – cầu theo giai đoạn')],
    'Talent Flow kết nối chiến lược kinh doanh với kỹ năng của từng thành viên, không thay thế hệ thống nhân sự lõi, hệ thống đào tạo hay công cụ AI tạo sinh hiện có. Phase 1 xây dựng dữ liệu kỹ năng đủ tin cậy (luồng 1, 2); Phase 2 dùng dữ liệu đó cho bố trí nhân sự (luồng 3, 4).', FT,
    phases=[('PHASE 1 · DỮ LIỆU KỸ NĂNG ĐÁNG TIN CẬY', 2), ('PHASE 2 · BỐ TRÍ NHÂN SỰ', 2)])

# ---------- roles ----------
S['roles'] = roles_slide('roles', 'VAI TRÒ THAM GIA', 'Tám vai trò, mỗi vai trò có phạm vi và luồng công việc riêng',
    shot(BLOB['tf-menu'], 'Màn hình Việc cần làm với menu theo vai trò', 820, 513, 'Menu, việc cần làm theo quyền của vai trò · ' + SAMPLE),
    [('Users', 'Nhân viên', 'Hồ sơ kỹ năng, IDP, ứng tuyển nội bộ', False),
     ('CheckCircle', 'Cấp trên', 'Duyệt IDP, hậu kiểm, kế thừa', False),
     ('Search', 'Người đăng tuyển', 'Đăng tuyển, xem hồ sơ ẩn danh', False),
     ('Settings', 'Nhân sự công ty', 'Chuỗi sáu bước, quyết định điều chuyển', False),
     ('Globe', 'Nhân sự tập đoàn', 'Điều phối giữa các công ty trong nhóm', False),
     ('Chart', 'Ban giám đốc', 'Cung – cầu, so sánh kịch bản', False),
     ('Lightbulb', 'Văn phòng DX', 'Từ điển kỹ năng DX, số liệu tổng hợp', False),
     ('Key', 'Quản trị', 'Tài khoản, dữ liệu nạp, tác vụ hệ thống', False)],
    'Menu hiển thị theo quyền của vai trò; phân quyền kiểm soát tại máy chủ. Cấp trên không phê duyệt IDP hay bằng chứng của chính mình. Ban giám đốc và Văn phòng DX chỉ xem số liệu tổng hợp, nhóm dưới 5 người được ẩn. Phạm vi dữ liệu của từng vai trò: Phụ lục A3. Giao diện hỗ trợ tiếng Nhật và tiếng Việt.', FT)

# ---------- four flows ----------
S['flow-dev'] = flow_slide('flow-dev', 'PHASE 1 · LUỒNG 1 · LỘ TRÌNH PHÁT TRIỂN', 'Nhân viên lập lộ trình, cấp trên phê duyệt và xác minh',
    shot(BLOB['my-path'], 'Màn hình Lộ trình của tôi', 860, 470, 'Lộ trình của tôi · ' + SAMPLE),
    [('Lộ trình của tôi', 'Nhân viên · vị trí hiện tại, mục tiêu 12–24 tháng', False),
     ('Tự đánh giá', 'Nhân viên · theo DSS ver.2.0, kỹ năng ngành', False),
     ('Lập IDP', 'Nhân viên · AI gợi ý khóa học, mentor', False),
     ('Phê duyệt IDP ◆', 'Cấp trên', True),
     ('Học, nộp bằng chứng', 'Nhân viên · khóa học, chứng chỉ, dự án', False),
     ('Hậu kiểm ◆', 'Cấp trên · trong 5 ngày làm việc', True)],
    '◆ Bước có người phê duyệt',
    'Mỗi bước có màn hình riêng; thanh tiến trình thể hiện bước hiện tại và người phụ trách. Nguyên tắc không tự phê duyệt: cấp trên không phê duyệt IDP hay bằng chứng của chính mình. Hồ sơ kỹ năng có bằng chứng: AI trích xuất từ lịch sử 人事異動 và 職務経歴, cấp trên xác nhận. Kỹ năng được ghi nhận khi độ tin cậy từ 0,5.', FT)

SAFE_NOTE = ('<div class="band" style="padding:20px 26px"><div class="hd">%s<p class="t" style="flex:1">Quyết định làm đơn vị thấp hơn mức tối thiểu bị chặn; '
             'chỉ bộ phận nhân sự được phép vượt, kèm lý do và phương án bù đắp.</p></div></div>') % ic('svg:helmet', 'sm', 'An toàn')
S['flow-safety'] = flow_slide('flow-safety', 'PHASE 1 · LUỒNG 2 · AN TOÀN VÀ KẾ THỪA', 'Mức tối thiểu nhân lực an toàn là ràng buộc cứng',
    shot(BLOB['safety'], 'Màn hình số người có chứng chỉ theo đơn vị', 860, 352, 'Số người có chứng chỉ theo đơn vị, dự báo 180 ngày · ' + SAMPLE),
    [('Cảnh báo sớm', 'Chứng chỉ sắp hết hạn, đơn vị sắp dưới mức', False),
     ('Xem mức tối thiểu', 'Cấp trên · dự báo 180 ngày', False),
     ('Kế hoạch truyền nghề ◆', 'Cấp trên đề cử người kế thừa', True),
     ('Bổ sung vào IDP', 'Nhân viên · lấy hoặc gia hạn chứng chỉ', False),
     ('Kiểm tra khi điều chuyển ◆', 'Đơn vị không được xuống dưới mức tối thiểu', True)],
    '◆ Bước có người phê duyệt',
    'Mức tối thiểu gồm mức theo quy định và chuẩn nội bộ. Trong môi trường thí điểm, chuẩn nội bộ là giả định và sẽ được thay bằng quy chế an toàn của Toho Gas. Nhân lực an toàn già hóa, khó tuyển dụng; mọi quyết định điều chuyển được kiểm tra với mức tối thiểu của đơn vị.', FT, extra_left=SAFE_NOTE)

S['flow-mobility'] = flow_slide('flow-mobility', 'PHASE 2 · LUỒNG 3 · TUYỂN DỤNG NỘI BỘ 社内公募', 'Tuyển dụng nội bộ bảo mật, phòng đi có phương án bù người',
    shot(BLOB['tf-match'], 'Màn hình Tuyển dụng nội bộ', 860, 536, 'Tuyển dụng nội bộ · ' + SAMPLE),
    [('Đăng tuyển', 'Người đăng tuyển · vị trí mảng chiến lược', False),
     ('Ứng tuyển ẩn danh', 'Nhân viên · bằng hồ sơ kỹ năng', False),
     ('Vòng trong ◆', 'Người đăng tuyển chọn; phòng hiện tại được báo', True),
     ('Phòng đi ◆', 'Đồng ý hoặc hoãn, nhận phương án bù người', True),
     ('Quyết định ◆', 'Nhân sự · kiểm tra mức an toàn của đơn vị', True),
     ('Tiếp nhận', 'Kế hoạch 90 ngày cho nhân sự mới', False)],
    '◆ Bước có người phê duyệt',
    'Vòng sơ loại chỉ xem hồ sơ kỹ năng ẩn danh; quy tắc ẩn danh kiểm soát tại máy chủ, không chỉ ẩn trên giao diện. Phòng hiện tại được thông báo khi hồ sơ vào vòng trong và nhận gợi ý phương án bù người. Mức an toàn của đơn vị luôn được kiểm tra trước khi điều chuyển.', FT)

S['flow-strategy'] = flow_slide('flow-strategy', 'PHASE 2 · LUỒNG 4 · CHIẾN LƯỢC NHÂN LỰC', 'Danh mục nhân sự gắn với kế hoạch kinh doanh 2025–2027',
    shot(BLOB['portfolio'], 'Màn hình Danh mục nhân sự, cung – cầu theo vị trí', 860, 522, 'Danh mục nhân sự: cung – cầu theo vị trí · ' + SAMPLE),
    [('Bối cảnh', 'Ban giám đốc · kế hoạch trung hạn 2025–2027', False),
     ('Năng lực', 'Nhân sự, Văn phòng DX · vị trí, năng lực cần có', False),
     ('Con người', 'Kỹ năng hiện có, từ luồng 1', False),
     ('Thiếu hụt ◆', 'Khoảng trống theo vị trí, công ty, giai đoạn', True),
     ('Hành động ◆', 'Đào tạo, tuyển nội bộ, biệt phái, tuyển ngoài', True),
     ('Theo dõi', 'Sau 90 ngày, 12 tháng; chỉ số vốn con người', False)],
    '◆ Bước có người phê duyệt',
    'Ban giám đốc và Văn phòng DX so sánh kịch bản trước khi phân bổ nguồn lực; chỉ xem số liệu tổng hợp, nhóm dưới 5 người được ẩn. Cung – cầu theo vị trí, công ty, giai đoạn H1/H2/H3. Kịch bản theo chỉ số kế hoạch trung hạn (e-methane, smart meter, mảng điện) với ràng buộc 保安.', FT)

# ---------- knowledge architecture ----------
S['architecture'] = arch_slide('architecture', 'KIẾN TRÚC CƠ SỞ TRI THỨC', 'Workforce Graph là lõi tri thức dùng chung cho toàn nhóm',
    [('ỨNG DỤNG', 'Web tiếng Nhật', ['Nhân viên', 'Cấp trên', 'Nhân sự', 'Ban giám đốc', ('Di động cho hiện trường', 'o')], ''),
     ('LỚP AI', 'Người xác nhận', ['Trích xuất kỹ năng', 'Chuẩn hóa', 'Ghép nối có giải thích', 'Gợi ý lộ trình'], ''),
     ('WORKFORCE GRAPH', '7 lớp + mở rộng', ['Bối cảnh kinh doanh', 'Năng lực', 'Tổ chức, vị trí', 'Từ điển kỹ năng',
                                              'Con người, bằng chứng', 'Mạng lưới', 'Phát triển tương lai', ('Công ty, 出向, vị trí 保安', 'x')], 'core'),
     ('ĐỊNH DANH', 'Mã hóa riêng', ['Lưu riêng, có mã hóa', 'Graph chỉ lưu mã ẩn danh', ('Đội Việt Nam: dữ liệu ẩn danh', 'o')], ''),
     ('TÍCH HỢP', 'Cần xác nhận', ['Nhân sự lõi, SAP', 'Đào tạo, DX人材', 'Quản trị mục tiêu', ('Graffer AI Studio', 'o')], '')],
    'QUẢN TRỊ',
    [('Key', 'Phân quyền theo vai trò, công ty'), ('CheckCircle', 'Thông báo 共同利用'), ('Users', 'Người xác nhận gợi ý AI'),
     ('Activity', 'Nhật ký truy cập'), ('Lock', 'Ẩn nhóm dưới 5 người'), ('Globe', 'Dữ liệu tại Nhật Bản')],
    'Workforce Graph gồm 7 lớp: bối cảnh kinh doanh, năng lực, tổ chức và vị trí, từ điển kỹ năng, con người và bằng chứng, mạng lưới, phát triển tương lai. Với Toho Gas bổ sung lớp công ty trong nhóm (công ty gốc, công ty đang làm khi biệt phái 出向) và nhãn vị trí 保安 luôn phải có người đủ điều kiện. Graph chỉ lưu mã ẩn danh; dữ liệu định danh lưu riêng, có mã hóa. Tích hợp (cần Toho Gas xác nhận): hệ thống nhân sự lõi và SAP (theo nguồn báo chí công nghệ, đang chuyển lên S/4HANA Cloud); đào tạo, kết quả DX人材; quản trị mục tiêu và đánh giá theo chế độ mới (chỉ đọc trường được phép). [Inference] Graffer AI Studio có thể dùng làm giao diện hỏi đáp về nghề nghiệp. Kiến trúc tổng thể của giải pháp: Phụ lục A1.', FT)

# ---------- data flow ----------
S['data-flow'] = dataflow_slide('data-flow', 'LUỒNG DỮ LIỆU', 'Tám chặng dữ liệu, ba điểm con người kiểm soát',
    [('Nguồn dữ liệu', 'Kế hoạch trung hạn, lịch sử 人事異動, 職務経歴, kết quả DX人材', ''),
     ('Cổng pháp lý ◆', 'Thông báo 共同利用; đội Việt Nam dùng dữ liệu ẩn danh', 'ap'),
     ('Chuẩn hóa', 'Ngạch theo chế độ mới 4/2026, ánh xạ về DSS ver.2.0', ''),
     ('AI trích xuất kỹ năng', 'Văn bản tiếng Nhật: 職務経歴, báo cáo dự án', ''),
     ('Người xác nhận ◆', 'Nhân viên, cấp trên xác nhận; ghi vết mọi gợi ý', 'ap'),
     ('Workforce Graph', 'Chỉ lưu mã ẩn danh; lớp công ty trong nhóm', 'core'),
     ('Suy luận, mô phỏng', 'Kịch bản theo kế hoạch trung hạn; ràng buộc 保安', ''),
     ('Người quyết định ◆', 'Quyết định 人事異動; kênh tự nguyện 社内公募', 'ap')],
    'Kết quả sau 90 ngày và 12 tháng cập nhật Workforce Graph',
    'Dữ liệu định danh lưu riêng, có mã hóa · graph chỉ dùng mã ẩn danh · dữ liệu kỹ năng không dùng để chấm điểm trừ',
    'Tám chặng: nguồn, cổng pháp lý, chuẩn hóa, AI trích xuất kỹ năng, người xác nhận, Workforce Graph, suy luận và mô phỏng, người quyết định. Ba chặng có dấu ◆ luôn có con người kiểm soát. Với Toho Gas, chia sẻ trong nhóm dựa trên thông báo 共同利用; điểm xuyên biên giới là đội phát triển tại Việt Nam (Điều 28 個人情報保護法). Đầu ra gồm dữ liệu cho công bố vốn con người.', FT)

# ---------- AI principles ----------
S['ai'] = ai_slide('ai', 'NGUYÊN TẮC HOẠT ĐỘNG CỦA AI', 'AI đề xuất, người có thẩm quyền quyết định',
    [('Dữ liệu đã ẩn danh', False), ('AI gợi ý, kèm lý do', False), ('◆ Người phụ trách quyết định', True), ('Lưu kết quả, ghi nhật ký', False)],
    [('Users', 'Con người quyết định', 'AI không tự điều chuyển, không tự loại hồ sơ'),
     ('Lightbulb', 'Giải thích được', 'Mỗi gợi ý kèm lý do và kỹ năng còn thiếu'),
     ('svg:ban', 'Không chấm điểm trừ', 'Dữ liệu kỹ năng chỉ dùng để phát triển, bố trí'),
     ('Lock', 'Bảo vệ dữ liệu', 'Ẩn danh trước khi AI xử lý; thông báo 共同利用'),
     ('Activity', 'Truy vết được', 'Nhật ký hoạt động AI; nhân viên xem, sửa được hồ sơ')],
    'TRIỂN KHAI', 'SaaS, Private Cloud hoặc máy chủ tại doanh nghiệp · dữ liệu lưu tại Nhật Bản',
    'AI trích xuất kỹ năng từ văn bản tiếng Nhật (職務経歴, báo cáo, chứng chỉ), chuẩn hóa về DSS ver.2.0 và kỹ năng ngành, gợi ý mức độ phù hợp kèm lý do; luyện phỏng vấn cùng AI không ghi kết quả vào hồ sơ. Đội phát triển tại Việt Nam làm việc trên dữ liệu ẩn danh. [Inference] Có thể dùng Graffer AI Studio làm giao diện hỏi đáp về nghề nghiệp; cần Toho Gas xác nhận.', FT)

# ---------- compliance ----------
GATE = ('<div class="mini"><p class="pill soft">Điều chuyển</p>%s<p class="pill">Kiểm tra 保安</p></div>' % arrow('arrow-s', style='width:32px;height:22px'))
S['compliance'] = compliance_slide('compliance', 'TUÂN THỦ', 'Yêu cầu pháp lý và an toàn được thiết kế thành chức năng',
    [dict(icon='Users', theme='Dùng chung trong nhóm', laws=['個人情報保護法 · Điều 27'],
          req='Thông báo 共同利用 trước khi dùng chung dữ liệu trong nhóm',
          visual='', feats=['Thông báo gồm hạng mục kỹ năng', 'Phân quyền theo công ty, vai trò']),
     dict(icon='Globe', theme='Dữ liệu ra nước ngoài', laws=['個人情報保護法 · Điều 28'],
          req='Bên nhận ở nước ngoài cần có đồng ý hoặc hệ thống đạt chuẩn',
          visual='', feats=['Dữ liệu lưu tại Nhật Bản', 'Đội Việt Nam chỉ dùng dữ liệu ẩn danh']),
     dict(icon='svg:helmet', theme='An toàn cung cấp', laws=['保安 · quy định và chuẩn nội bộ'],
          req='Mỗi đơn vị duy trì đủ nhân lực có chứng chỉ an toàn',
          visual=GATE, feats=['Chặn quyết định dưới mức tối thiểu', 'Cảnh báo chứng chỉ sắp hết hạn'])],
    'Thông tin tham khảo cho thiết kế, không phải tư vấn pháp lý; cần Toho Gas xác nhận. Đề xuất trao đổi trước với công đoàn khi triển khai.',
    '個人情報保護法 Điều 27 (共同利用): thông báo trước hạng mục dữ liệu, công ty dùng chung, mục đích và người chịu trách nhiệm. Điều 28: cung cấp dữ liệu cá nhân cho bên ở nước ngoài; đội phát triển tại Việt Nam làm việc trên dữ liệu ẩn danh, hoặc hệ thống đáp ứng chuẩn theo Điều 28. Mức tối thiểu nhân lực an toàn gồm mức theo quy định và chuẩn nội bộ của Toho Gas.', FT, feat_h=200)

# ---------- roadmap (unchanged content) ----------
phases = [('Phỏng vấn, dữ liệu ẩn danh', 1, 2, False), ('Từ điển kỹ năng, vị trí đích', 3, 4, False),
          ('Hồ sơ kỹ năng thí điểm', 5, 7, True), ('Bản đồ cung – cầu, định hướng', 8, 9, False),
          ('Vận hành thử nội bộ', 10, 11, False), ('Đánh giá, mở rộng toàn nhóm', 12, 12, True)]
g = ['<p class="gl" style="grid-column:1;grid-row:1"><b>Tuần PoC</b></p>']
g += ['<p class="gh" style="grid-column:%d;grid-row:1">%d</p>' % (w + 1, w) for w in range(1, 13)]
for r, (lab, a, b, hl) in enumerate(phases, start=2):
    g.append('<p class="gl" style="grid-column:1;grid-row:%d">%s</p>' % (r, lab))
    g.append('<div class="gb%s" style="grid-column:%d / %d;grid-row:%d;height:36px"></div>' % (' hl' if hl else '', a + 1, b + 2, r))
g.append('<p class="gl" style="grid-column:1;grid-row:8"><b>◆ Quyết định</b></p>')
g.append('<p class="cap" style="grid-column:2 / 13;grid-row:8;text-align:right">Đi tiếp và mở rộng toàn nhóm</p>')
g.append('<div class="gd" style="grid-column:13;grid-row:8"><x-shape kind="diamond" class="dia"></x-shape></div>')
S['roadmap'] = section('roadmap', head('LỘ TRÌNH TRIỂN KHAI', 'Hai phase triển khai, bắt đầu bằng PoC 12 tuần') +
'''<div class="content">
<div class="g2">
<div class="card" style="padding:18px 24px"><div class="hd"><p class="pill">Phase 1</p><p class="t" style="flex:1"><b>Hồ sơ kỹ năng, phát triển cá nhân:</b> Lộ trình của tôi, IDP, duyệt và hậu kiểm, an toàn và kế thừa</p></div></div>
<div class="card navy" style="padding:18px 24px"><div class="hd"><p class="pill soft">Phase 2</p><p class="t" style="flex:1"><b style="color:#F3F4F7">Chiến lược, điều chuyển nội bộ:</b> chuỗi sáu bước, danh mục nhân sự, tuyển dụng nội bộ</p></div></div>
</div>
<div class="row" style="flex-wrap:wrap;gap:12px"><p class="pill soft">200–300 nhân viên</p><p class="pill soft">20–30 vị trí đích</p><p class="pill soft">Công ty mẹ và một công ty con</p></div>
<div class="gantt" style="row-gap:8px">
%s
</div>
</div>
''' % '\n'.join(g),
'Hai phase giúp dữ liệu kỹ năng đạt độ tin cậy cần thiết trước khi dùng cho bố trí nhân sự. Ví dụ nhóm nguồn – đích cho PoC: nghiệp vụ bán gas và văn phòng (nguồn) sang mảng điện, giải pháp và DX (đích); Toho Gas lựa chọn nhóm thực tế (Phụ lục A4). Phase 2 còn gồm điều chuyển định kỳ.', FT)

# ---------- kpi (unchanged content) ----------
tiles = [('≥ 70%', 'nhân viên thí điểm xác nhận hồ sơ kỹ năng'), ('≥ 80%', 'gợi ý kỹ năng của AI được chấp nhận'),
         ('≥ 1', 'cuộc họp kế hoạch nhân sự dùng bản đồ cung – cầu'), ('Tăng', 'hồ sơ ứng tuyển, dự án nội bộ so với đợt trước'),
         ('0', 'đơn vị an toàn dưới mức tối thiểu')]
comm = [('CheckCircle', 'Thiếu hụt, IDP, kế thừa, điều chuyển có người phê duyệt'), ('svg:ban', 'Không dùng dữ liệu kỹ năng để chấm điểm trừ'),
        ('Lock', 'Dữ liệu định danh bảo mật riêng, ghi nhật ký'), ('svg:helmet', 'Quyết định làm đơn vị dưới mức an toàn bị chặn')]
S['kpi'] = section('kpi', head('ĐO LƯỜNG VÀ CAM KẾT', 'Đo bằng nhân sự đảm nhận vị trí mới, không bằng giờ đào tạo',
'Tiêu chí thành công của PoC (đề xuất, thống nhất cùng Toho Gas) và bốn cam kết với người dùng.') +
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
       '\n'.join('<div class="hd">%s<p class="t" style="flex:1">%s</p></div>' % (ic(i, 'sm', 'Cam kết'), t) for i, t in comm)),
'Các ngưỡng là đề xuất, cần thống nhất với Toho Gas trước tuần 1. Chỉ số dài hạn sau PoC: số IDP đã phê duyệt, tỷ lệ hồ sơ kỹ năng đầy đủ, thời gian lấp vị trí bằng nhân sự nội bộ, số nhân sự đảm nhận vị trí đích, dữ liệu cho công bố vốn con người.', FT)

# ---------- next-steps (unchanged content) ----------
def scard(n, title, items):
    return '<div class="card" style="flex:1"><div class="hd"><p class="num">%s</p><h3 class="h3">%s</h3></div><ul class="lst">%s</ul></div>' % (
        n, title, ''.join('<li>%s</li>' % i for i in items))

checks = ['Nhu cầu mảng điện, nước ngoài, giải pháp', 'Vị trí thu hẹp do smart meter, RPA, AI', 'Hệ thống nhân sự lõi; tiến độ SAP',
          'Phạm vi dữ liệu: công ty mẹ hay toàn nhóm', 'Người quyết định; thời điểm tham vấn công đoàn']
S['next-steps'] = section('next-steps', head('BƯỚC TIẾP THEO', 'Ba bước khởi động cùng Toho Gas') +
'''<div class="content">
<div class="row" style="gap:12px;align-items:stretch">
%s
<x-shape kind="arrow-right" class="arrow-s" style="align-self:center"></x-shape>
%s
<x-shape kind="arrow-right" class="arrow-s" style="align-self:center"></x-shape>
%s
</div>
<div class="card hl"><p class="lbl">NĂM NỘI DUNG CẦN TOHO GAS XÁC NHẬN</p>
<div class="g5">
%s
</div>
</div>
</div>
''' % (scard('1', 'Workshop nửa ngày', ['Kết quả cần đạt · 30 phút', 'Giả định hiện tại · 45 phút', 'Ràng buộc thực tế · 60 phút', 'Xây dựng phương án · 45 phút', 'Kiểm chứng, phạm vi PoC · 30 phút']),
       scard('2', 'Phạm vi PoC', ['Một nhóm vị trí nguồn – đích rõ nhất', 'Công ty mẹ và một công ty con', '20–30 vị trí đích, 200–300 nhân viên', 'Tiêu chí thành công trước tuần 1']),
       scard('3', 'Dữ liệu và điều kiện', ['Thông báo 共同利用 gồm hạng mục kỹ năng', 'Mức dữ liệu đội Việt Nam được xử lý', 'Danh sách vị trí 保安, mức tối thiểu', 'Dữ liệu nhân sự ẩn danh khi khảo sát']),
       '\n'.join('<div class="hd">%s<p class="t" style="flex:1">%s</p></div>' % (ic('Check', 'sm'), c) for c in checks)),
'Workshop khoảng 3,5 giờ, đi theo năm bước của phương pháp first principles (Phụ lục A6). Đầu ra: danh sách ràng buộc cứng có người chịu trách nhiệm và phạm vi PoC có điểm dừng. Thành phần đề xuất: 人事部, đại diện mảng điện và mảng lõi, người phụ trách 保安; mời đại diện công đoàn dự phiên 2 và 3. Việc chuyển hệ thống lõi lên SAP S/4HANA Cloud theo nguồn báo chí công nghệ, cần Toho Gas xác nhận.', FT)

# ================= APPENDIX =================
S['ap-architecture'] = system_arch_slide('ap-architecture', 'PHỤ LỤC A1 · KIẾN TRÚC TỔNG THỂ', 'Kiến trúc tổng thể đề xuất: từ người dùng đến hệ thống hiện có',
    ['Nhân viên', 'Cấp trên', 'Nhân sự', 'Ban giám đốc', 'Văn phòng DX'], ['Web tiếng Nhật', 'Di động cho hiện trường'],
    ['M1 · Vị trí và từ điển kỹ năng', 'M2 · Hồ sơ kỹ năng, bằng chứng', 'M3 · Danh mục nhân sự động',
     'M4 · Định hướng nghề nghiệp', 'M5 · Thị trường nhân lực nội bộ', 'M6 · Điều chuyển và theo dõi'],
    ['Trích xuất kỹ năng', 'Chuẩn hóa DSS ver.2.0', 'Ghép nối có giải thích', 'Gợi ý lộ trình', 'Mô phỏng kịch bản'],
    [('Workforce Graph · 7 lớp', 'k'), ('Lớp công ty, 出向, vị trí 保安', 'o'), 'Kho định danh · mã hóa', 'Nhật ký truy vết'],
    ['Nạp dữ liệu từ hệ thống nguồn', 'Chỉ đọc trường được phép', 'Đăng nhập một lần'],
    ['Nhân sự lõi, SAP', 'Đào tạo, DX人材', 'Quản trị mục tiêu, đánh giá', ('Graffer AI Studio (cần xác nhận)', 'o')],
    'Phân quyền theo vai trò, công ty · thông báo 共同利用 · ẩn danh trước khi AI xử lý · nhật ký truy cập',
    'SaaS, Private Cloud hoặc máy chủ tại doanh nghiệp · dữ liệu lưu tại Nhật Bản · đội Việt Nam dùng dữ liệu ẩn danh',
    'Kiến trúc đề xuất theo tài liệu nghiên cứu Toho Gas (mục 7.2, 7.3). Sáu module nghiệp vụ: M1 kiến trúc vị trí và từ điển kỹ năng; M2 hồ sơ kỹ năng có bằng chứng; M3 danh mục nhân sự động; M4 định hướng nghề nghiệp; M5 thị trường nhân lực nội bộ (社内公募, dự án); M6 hỗ trợ điều chuyển và theo dõi. Lớp dữ liệu theo tài liệu nghiên cứu: Workforce Graph trên Neo4j, thêm lớp công ty trong nhóm; dữ liệu định danh lưu ở PostgreSQL có mã hóa; graph chỉ dùng mã ẩn danh. Tích hợp cần Toho Gas xác nhận: hệ thống nhân sự lõi và SAP (theo báo chí công nghệ, đang chuyển lên S/4HANA Cloud); quản trị mục tiêu và đánh giá theo chế độ mới chỉ đọc trường được phép. [Inference] Graffer AI Studio có thể dùng làm giao diện hỏi đáp về nghề nghiệp.', FT)

S['ap-problems'] = problems_slide('ap-problems', 'PHỤ LỤC A7 · VẤN ĐỀ CẤU THÀNH', 'Bảy vấn đề cần kiểm chứng cùng Toho Gas',
    [('P1', 'Nhu cầu chưa lượng hóa', 'Báo cáo tích hợp chưa có số liệu dịch chuyển nhân sự', 'Cao'),
     ('P2', 'Kỹ năng chưa số hóa theo chuẩn chung', 'Chỉ số DX人材 đo bằng số người đã học; số liệu chưa phủ toàn nhóm', 'Trung bình'),
     ('P3', 'Đào tạo chưa gắn vị trí đích', 'Mục tiêu 200 DX人材 chưa gắn với vị trí cụ thể', 'Trung bình'),
     ('P4', 'Tuyển nội bộ cần hai phòng đồng ý', 'Phòng đi chưa có người thay; ý kiến tọa đàm trong báo cáo tích hợp', 'Cao'),
     ('P5', 'Nhân viên trẻ thiếu thông tin', 'Tọa đàm: nhân viên trẻ chưa rõ vị trí, kỹ năng cần có', 'Cao'),
     ('P6', 'Ranh giới giữa các công ty con', 'Công ty mẹ khoảng 970 trên 6.100 người; dịch chuyển qua biệt phái', 'Cao'),
     ('P7', 'Chưa đo kết quả sau dịch chuyển', 'Tọa đàm: cần hỗ trợ sau chương trình đào tạo', 'Trung bình')],
    '[Inference] Toàn bộ bảng là giả thuyết rút từ nguồn công khai; mức chắc chắn là đánh giá của nhóm nghiên cứu.',
    'Mỗi vấn đề gắn với một chức năng của Talent Flow: P1, P7 với danh mục nhân sự; P2 với hồ sơ kỹ năng có bằng chứng; P3, P5 với lộ trình phát triển; P4, P6 với tuyển dụng nội bộ và hỗ trợ điều chuyển.', FT)

for sid, html_ in S.items():
    write(ROOT, sid, html_)
print('written', len(S))
