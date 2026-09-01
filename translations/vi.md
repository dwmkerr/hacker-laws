# 💻📖 luật của hacker

Các Luật, Lý thuyết, Nguyên tắc và Mẫu sẽ hữu ích cho các nhà phát triển phần mềm.

[Bản dịch](#translations) : [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇫🇷](./translations/fr.md) [🇮🇹](./translations/it-IT.md) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇹🇷](./translations/tr.md) [🇮🇩](./translations/id.md) [🇯🇵](./translations/jp.md) [🇵🇱](./translations/pl.md)

Bạn thích dự án này? Vui lòng xem xét [tài trợ cho tôi](https://github.com/sponsors/dwmkerr) và các [dịch giả](#translations) . Ngoài ra, hãy xem podcast này trên [The Changelog - Luật để tin tặc tồn tại](https://changelog.com/podcast/403) để tìm hiểu thêm về dự án! Bạn cũng có thể [tải xuống sách điện tử PDF mới nhất](https://github.com/dwmkerr/hacker-laws/releases/latest/download/hacker-laws.pdf) . Hãy xem [Hướng dẫn dành cho cộng tác viên](./.github/contributing.md) nếu bạn muốn đóng góp!

---

<!-- vim-markdown-toc GFM -->

- [Giới thiệu](#introduction)
- [Định luật](#laws)
  - [Nguyên tắc 90–9–1 (Quy tắc 1%)](#9091-principle-1-rule)
  - [Định luật Amdahl](#amdahls-law)
  - [Lý thuyết cửa sổ vỡ](#the-broken-windows-theory)
  - [Luật Brooks](#brooks-law)
  - [Định lý CAP (Định lý Brewer)](#cap-theorem-brewers-theorem)
  - [Định luật Conway](#conways-law)
  - [Định luật Cunningham](#cunninghams-law)
  - [Số Dunbar](#dunbars-number)
  - [Hiệu ứng Dunning-Kruger](#the-dunning-kruger-effect)
  - [Luật phù hợp](#fitts-law)
  - [Luật Gall](#galls-law)
  - [Luật Goodhart](#goodharts-law)
  - [Hanlon Razor](#hanlons-razor)
  - [Luật Hick (Luật Hick-Hyman)](#hicks-law-hick-hyman-law)
  - [Định luật Hofstadter](#hofstadters-law)
  - [Định luật Hutber](#hutbers-law)
  - [Chu kỳ Hype &amp; Định luật Amara](#the-hype-cycle--amaras-law)
  - [Luật Hyrum (Luật của các giao diện ngầm)](#hyrums-law-the-law-of-implicit-interfaces)
  - [Định luật Kernighan](#kernighans-law)
  - [Luật Linus](#linuss-law)
  - [Định luật Metcalfe](#metcalfes-law)
  - [Định luật Moore](#moores-law)
  - [Định luật Murphy / Định luật Sod](#murphys-law--sods-law)
  - [Dao cạo của Occam](#occams-razor)
  - [Định luật Parkinson](#parkinsons-law)
  - [Hiệu ứng tối ưu hóa sớm](#premature-optimization-effect)
  - [Định luật Putt](#putts-law)
  - [Luật Reed](#reeds-law)
  - [Định luật Bảo toàn Độ phức tạp (Định luật Tesler)](#the-law-of-conservation-of-complexity-teslers-law)
  - [Định luật Demeter](#the-law-of-demeter)
  - [Luật trừu tượng rò rỉ](#the-law-of-leaky-abstractions)
  - [Luật tầm thường](#the-law-of-triviality)
  - [Triết lý Unix](#the-unix-philosophy)
  - [Quy tắc hướng đạo](#the-scout-rule)
  - [Mô hình Spotify](#the-spotify-model)
  - [Quy tắc hai chiếc bánh pizza](#the-two-pizza-rule)
  - [Luật Wadler](#wadlers-law)
  - [Định luật Wheaton](#wheatons-law)
- [Nguyên tắc](#principles)
  - [Tất cả các mô hình đều sai (Định luật George Box)](#all-models-are-wrong-george-boxs-law)
  - [Chesterton's Fence](#chestertons-fence)
  - [Hiệu ứng Biển Chết](#the-dead-sea-effect)
  - [Nguyên tắc Dilbert](#the-dilbert-principle)
  - [Nguyên tắc Pareto (Quy tắc 80/20)](#the-pareto-principle-the-8020-rule)
  - [Nguyên tắc Shirky](#the-shirky-principle)
  - [Nguyên tắc Peter](#the-peter-principle)
  - [Nguyên tắc Chắc chắn (Định luật Postel)](#the-robustness-principle-postels-law)
  - [SOLID](#solid)
  - [Nguyên tắc trách nhiệm duy nhất](#the-single-responsibility-principle)
  - [Nguyên tắc Mở / Đóng](#the-openclosed-principle)
  - [Nguyên tắc thay thế Liskov](#the-liskov-substitution-principle)
  - [Nguyên tắc phân tách giao diện](#the-interface-segregation-principle)
  - [Nguyên tắc đảo ngược phụ thuộc](#the-dependency-inversion-principle)
  - [Nguyên tắc DRY](#the-dry-principle)
  - [Nguyên tắc KISS](#the-kiss-principle)
  - [YAGNI](#yagni)
  - [Sự sụp đổ của máy tính phân tán](#the-fallacies-of-distributed-computing)
- [Danh sách đọc](#reading-list)
- [Những nguồn thông tin trên mạng](#online-resources)
- [Sách điện tử PDF](#pdf-ebook)
- [Tệp âm thanh](#podcast)
- [Bản dịch](#translations)
- [Các dự án liên quan](#related-projects)
- [Đóng góp](#contributing)
- [SẼ LÀM](#todo)

<!-- vim-markdown-toc -->

## Giới thiệu

Có rất nhiều luật mà mọi người thảo luận khi nói về phát triển phân mềm. Kho lưu trữ này là tài liệu tham khảo và tổng quan về một số kho lưu trữ phổ biến nhất. Hãy chia sẻ và gửi bài PR!

❗: Kho lưu trữ này chứa giải thích về một số luật, nguyên tắc và khuôn mẫu, nhưng không _ủng hộ_ bất kỳ điều nào trong số đó. Liệu chúng có nên được áp dụng hay không sẽ luôn là vấn đề tranh luận và phụ thuộc rất nhiều vào những gì bạn đang làm.

## Luật

Và chúng ta bắt đầu!

### Nguyên tắc 90–9–1 (Quy tắc 1%)

[Quy tắc 1% trên Wikipedia](<https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture)>)

Nguyên tắc 90-9-1 gợi ý rằng trong một cộng đồng internet như wiki, 90% người tham gia chỉ xem nội dung, 9% chỉnh sửa hoặc sửa đổi nội dung và 1% người tham gia thêm nội dung.

Ví dụ trong thế giới thực:

- Một nghiên cứu năm 2014 trên bốn mạng xã hội về sức khỏe cho thấy 1% hàng đầu tạo ra 73% bài đăng, 9% tiếp theo chiếm trung bình ~ 25% và 90% còn lại chiếm trung bình 2% ( [Tham khảo](https://www.jmir.org/2014/2/e33/) )

Xem thêm:

- [Nguyên tắc Pareto](#the-pareto-principle-the-8020-rule)

### Định luật Amdahl

[Luật Amdahl trên Wikipedia](https://en.wikipedia.org/wiki/Amdahl%27s_law)

> Định luật Amdahl là một công thức cho thấy _tốc độ tiềm năng_ của một tác vụ tính toán có thể đạt được bằng cách tăng tài nguyên của một hệ thống. Thường được sử dụng trong tính toán song song, nó có thể dự đoán lợi ích thực tế của việc tăng số lượng bộ xử lý, điều này bị giới hạn bởi khả năng song song của chương trình.

Minh họa tốt nhất với một ví dụ. Nếu một chương trình có hai phần: phần A, phần này chỉ có thể thực hiện bằng một bộ xử lý đơn lẻ và phần B, có thể được thực hiện song song trên nhiều bộ xử lý, thì chúng ta thấy rằng việc thêm nhiều bộ xử lý vào hệ thống thực thi chương trình chỉ có thể có một lợi ích hạn chế. Nó có khả năng cải thiện đáng kể tốc độ của phần B - nhưng tốc độ của phần A sẽ không thay đổi.

Sơ đồ dưới đây cho thấy một số ví dụ về những cải tiến tiềm năng về tốc độ:

<img width="480px" src="./images/amdahls-law.svg" alt="Diagram: Amdahl's Law">

_(Tham khảo hình ảnh: Bởi Daniels219 tại Wikipedia tiếng Anh, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)_

Như có thể thấy, ngay cả một chương trình có thể chạy song song 50% sẽ được hưởng lợi rất ít khi vượt quá 10 đơn vị xử lý, trong khi một chương trình có thể song song 95% vẫn có thể đạt được những cải thiện tốc độ đáng kể với hơn một nghìn đơn vị xử lý.

Như [Định luật Moore](#moores-law) chậm, và tốc độ tăng tốc của bộ xử lý đơn lẻ chậm lại, thì song song hóa là chìa khóa để cải thiện hiệu suất. Ví dụ như lập trình đồ họa - với tính toán dựa trên Shader hiện đại, các pixel hoặc mảnh riêng lẻ có thể được hiển thị song song - đây là lý do tại sao các card đồ họa hiện đại thường có hàng nghìn lõi xử lý (GPU hoặc Shader Units).

Xem thêm:

- [Luật Brooks](#brooks-law)
- [định luật Moore](#moores-law)

### Lý thuyết cửa sổ vỡ

[Lý thuyết cửa sổ vỡ trên Wikipedia](https://en.wikipedia.org/wiki/Broken_windows_theory)

Lý thuyết Cửa sổ Vỡ cho thấy rằng các dấu hiệu tội phạm có thể nhìn thấy (cửa sổ kính bị vỡ) dẫn đến tội phạm ngày càng nghiêm trọng hơn (hoặc làm suy thoái môi trường hơn nữa).

Lý thuyết này đã được áp dụng cho phát triển phần mềm, cho thấy rằng mã chất lượng kém (hoặc [Nợ kỹ thuật](#TODO) ) có thể dẫn đến nhận thức rằng các nỗ lực cải thiện chất lượng có thể bị bỏ qua hoặc định giá thấp, do đó dẫn đến mã chất lượng kém hơn. Hiệu ứng này giảm dần dẫn đến chất lượng giảm mạnh theo thời gian.

Xem thêm:

- [Technical Debt](#TODO)

Ví dụ:

- [Lập trình thực dụng: Phần mềm Entropy](https://flylib.com/books/en/1.315.1.15/1/)
- [Kinh dị mã hóa: Lý thuyết cửa sổ bị hỏng](https://blog.codinghorror.com/the-broken-window-theory/)
- [OpenSource: Niềm vui của Lập trình - Lý thuyết Cửa sổ Vỡ](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

### Luật Brooks

[Luật Brooks trên Wikipedia](https://en.wikipedia.org/wiki/Brooks%27s_law)

> Thêm nhân lực vào một dự án phát triển phần mềm bị chậm tiến độ sẽ làm nó chậm hơn.

Luật này cho thấy rằng trong nhiều trường hợp, việc cố gắng đẩy nhanh tiến độ giao một dự án vốn đã bị chậm, bằng cách bổ sung thêm người, sẽ khiến việc giao dự án chậm hơn. Brooks rõ ràng rằng đây là một sự đơn giản hóa quá mức, tuy nhiên, lý do chung là với thời gian gia tăng của các nguồn tài nguyên mới và tổng chi phí liên lạc, tốc độ ngắn hạn tức thời sẽ giảm xuống. Ngoài ra, nhiều nhiệm vụ có thể không chia nhỏ được hơn nữa (chia nhỏ công việc là phân phối công việc ra các nguồn lực để xử lý) dẫn đến tốc độ tăng tiềm năng cũng thấp hơn.

Cụm từ phổ biến trong giao hàng "Chín phụ nữ không thể sinh con trong một tháng" liên quan đến Luật Brooks, đặc biệt, thực tế là một số loại công việc không thể phân chia hoặc song song.

Đây là chủ đề trung tâm của cuốn sách ' [The Mythical Man Month](#reading-list) '.

Xem thêm:

- [Thần chết xuất hiện](#todo)
- [Danh sách đọc: Tháng người đàn ông thần thoại](#reading-list)

### Định lý CAP (Định lý Brewer)

Định lý CAP (do Eric Brewer định nghĩa) tuyên bố rằng đối với một kho lưu trữ dữ liệu phân tán, chỉ có thể thực hiện hai trong ba bảo đảm sau (nhiều nhất):

- Tính đồng bộ (Consistency): khi đọc dữ liệu, mọi yêu cầu đều nhận được _dữ liệu gần đây nhất_ hoặc lỗi được trả về
- Tính sẵn sàng (Availability): khi đọc dữ liệu, mọi yêu cầu đều nhận được _phản hồi không lỗi_ , mà không cần đảm bảo rằng đó là dữ liệu _mới nhất_
- Chịu lỗi(P-Partition Tolerance): khi một số lượng tùy ý yêu cầu mạng giữa các nút không thành công, hệ thống tiếp tục hoạt động như thiết kế.

Cốt lõi của lý do là như sau. Không thể đảm bảo sai biệt cục bộ không xảy ra (xem [Sự sụp đổ của Máy tính Phân tán](#the-fallacies-of-distributed-computing) ). Do đó, trong trường hợp sai biệt cục bộ, chúng ta có thể hoặc ngưng công việc (tăng tính đồng bộ và giảm tính sẵn sàng) hoặc tiếp tục công việc (tăng tính sẵn sàng nhưng giảm tính đồng bộ).

Tên gọi xuất phát từ các chữ cái đầu tiên (Consistency, Availability, Partition Tolerance). Lưu ý rằng điều rất quan trọng cần lưu ý là điều này _không_ liên quan đến [_ACID_](#TODO) , có định nghĩa khác về tính đồng bộ. Gần đây hơn, [định lý PACELC](#TODO) đã được phát triển để bổ sung các ràng buộc về độ trễ và tính đồng bộ khi mạng _không bị_ sai biệt cục bộ (tức là khi hệ thống đang hoạt động như mong đợi).

Hầu hết các nền tảng cơ sở dữ liệu hiện đại đều thừa nhận định lý này một cách ngầm định bằng cách cung cấp cho người dùng cơ sở dữ liệu tùy chọn để lựa chọn giữa việc họ muốn một hoạt động có tính khả dụng cao (có thể bao gồm 'đọc bẩn') hay một hoạt động nhất quán cao (ví dụ: một 'số đại biểu được thừa nhận ghi ').

Ví dụ trong thế giới thực:

- [Bên trong Google Cloud Spanner và Định lý CAP](https://cloud.google.com/blog/products/gcp/inside-cloud-spanner-and-the-cap-theorem) - Đi vào chi tiết về cách hoạt động của Cloud Spanner, thoạt đầu có vẻ giống như một nền tảng có _tất cả_ các đảm bảo của CAP, nhưng bên dưới cơ bản là một hệ thống CP.

Xem thêm:

- [AXIT](#TODO)
- [Sự sụp đổ của máy tính phân tán](#the-fallacies-of-distributed-computing)
- [PACELC](#TODO)

### Định luật Conway

[Luật Conway trên Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

Luật này gợi ý rằng các biên giới kỹ thuật của một hệ thống sẽ phản ánh cấu trúc của tổ chức. Nó thường được nhắc đến khi xem xét các cải tiến của tổ chức, Luật Conway gợi ý rằng nếu một tổ chức được cấu trúc thành nhiều đơn vị nhỏ, không kết nối thì phần mềm mà nó tạo ra sẽ là như vậy. Nếu một tổ chức được xây dựng nhiều hơn xung quanh 'ngành dọc' được định hướng xung quanh các tính năng hoặc dịch vụ, hệ thống phần mềm cũng sẽ phản ánh điều này.

Xem thêm:

- [Mô hình Spotify](#the-spotify-model)

### Định luật Cunningham

[Định luật Cunningham trên Wikipedia](https://en.wikipedia.org/wiki/Ward_Cunningham#Cunningham's_Law)

> Cách tốt nhất để có câu trả lời đúng trên Internet không phải là đặt câu hỏi, mà là hẫy đăng câu trả lời sai.

Theo Steven McGeady, Ward Cunningham đã khuyên anh ta vào đầu những năm 1980: "Cách tốt nhất để có câu trả lời đúng trên Internet không phải là đặt một câu hỏi, mà là hẫy đăng câu trả lời sai." McGeady gọi đây là định luật Cunningham, mặc dù Cunningham phủ nhận quyền sở hữu gọi nó là "trích dẫn sai". Mặc dù ban đầu đề cập đến các tương tác trên Usenet, luật đã được sử dụng để mô tả cách hoạt động của các cộng đồng trực tuyến khác (ví dụ: Wikipedia, Reddit, Twitter, Facebook).

Xem thêm:

- [XKCD 386: "Cuộc gọi nghĩa vụ"](https://xkcd.com/386/)

### Số Dunbar

[Số Dunbar trên Wikipedia](https://en.wikipedia.org/wiki/Dunbar%27s_number)

"Con số của Dunbar là một giới hạn nhận thức được đề xuất cho số người mà một người có thể duy trì các mối quan hệ xã hội ổn định - các mối quan hệ trong đó một cá nhân biết mỗi người là ai và mối quan hệ của mỗi người với mọi người khác như thế nào." Không có một con số chính xác. "... [Dunbar] đề xuất rằng con người chỉ có thể thoải mái duy trì 150 mối quan hệ ổn định." Ông đặt con số vào một bối cảnh xã hội hơn, "số lượng người mà bạn sẽ không cảm thấy xấu hổ khi tham gia một cuộc uống không được mời nếu bạn tình cờ gặp họ trong một quán bar." Các ước tính cho con số thường nằm trong khoảng từ 100 đến 250.

Giống như mối quan hệ ổn định giữa các cá nhân, mối quan hệ của nhà phát triển với cơ sở mã cần nỗ lực để duy trì. Khi đối mặt với các dự án lớn phức tạp, hoặc sở hữu nhiều dự án, chúng tôi dựa trên quy ước, chính sách và quy trình được mô hình hóa để mở rộng quy mô. Con số của Dunbar không chỉ quan trọng cần ghi nhớ khi văn phòng phát triển mà còn khi thiết lập phạm vi cho các nỗ lực của nhóm hoặc quyết định khi nào một hệ thống nên đầu tư vào công cụ để hỗ trợ mô hình hóa và tự động hóa chi phí hậu cần. Đặt con số vào bối cảnh kỹ thuật, đó là số lượng dự án (hoặc độ phức tạp được chuẩn hóa của một dự án) mà bạn cảm thấy tự tin khi tham gia vòng quay theo cuộc gọi để hỗ trợ.

Xem thêm:

- [Định luật Conway](#conways-law)

### Hiệu ứng Dunning-Kruger

[Hiệu ứng Dunning-Kruger trên Wikipedia](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect)

> Nếu bạn không đủ năng lực, bạn không thể biết mình kém cỏi ... Kỹ năng cần để đưa ra một câu trả lời đúng, chính là kỹ năng cần để nhận ra một câu trả lời đúng.
>
> ( [David Dunning](https://en.wikipedia.org/wiki/David_Dunning) )

Hiệu ứng Dunning-Kruger là một khuynh hướng nhận thức lý thuyết được David Dunning và Justin Kruger mô tả trong một bài báo và nghiên cứu tâm lý năm 1999. Nghiên cứu cho thấy rằng những người có mức năng lực thấp trong một nhiệm vụ có khả năng đánh giá quá cao khả năng của họ trong nhiệm vụ. Lý do được đề xuất cho sự thiên vị này là một người cần có _nhận thức_ đầy đủ về mức độ phức tạp của một vấn đề hoặc lĩnh vực để có thể đưa ra ý kiến sáng suốt về khả năng làm việc của họ trong lĩnh vực đó.

Hiệu ứng Dunning-Kruger đôi khi được sử dụng để mô tả một hiệu ứng có liên quan, nhưng không nhất thiết ngụ ý mà có thể được mô tả là "Một người càng ít hiểu về một vấn đề, họ càng tin rằng họ có thể dễ dàng giải quyết các vấn đề đó, như họ có nhiều khả năng thấy miền là _đơn giản_ ". Hiệu ứng tổng quát hơn này rất phù hợp trong công nghệ. Nó sẽ gợi ý rằng những người ít quen thuộc với một vấn đề, chẳng hạn như thành viên nhóm không chuyên về kỹ thuật hoặc thành viên nhóm ít kinh nghiệm, có nhiều khả năng _đánh giá thấp_ nỗ lực cần thiết để giải quyết một vấn đề trong không gian này.

Khi sự hiểu biết và kinh nghiệm của một người trong một lĩnh vực tăng lên, họ cũng có thể gặp phải một tác động khác, đó là họ có xu hướng _đánh giá quá cao_ khả năng của _người khác_ hoặc _đánh giá thấp_ khả năng của chính họ, vì họ đã trở nên có kinh nghiệm trong lĩnh vực đó. Trong mọi trường hợp, những tác động này là _thành kiến về nhận thức_ . Như với bất kỳ sự thiên vị nào, sự hiểu biết rằng nó có thể có thường sẽ đủ để giúp tránh những thách thức - vì khi có nhận thức về sự thiên vị, nhiều đầu vào và ý kiến hơn có thể được đưa vào để cố gắng loại bỏ những thành kiến này. Một liên quan mật thiết là sự thiên vị về [ưu thế](https://en.wikipedia.org/wiki/Illusory_superiority) của Huyễn Ảnh.

Ví dụ trong thế giới thực:

- [Apple vs. FBI: Tại sao Diều hâu chống khủng bố này lại chuyển hướng](https://fortune.com/2016/03/10/apple-fbi-lindsay-graham/) - Năm 2016, Thượng nghị sĩ Lindsey Graham đã thay đổi lập trường của mình về việc Apple tạo ra một 'cửa sau' trong mã hóa thiết bị của họ. Ban đầu, Graham đã chỉ trích Apple thách thức yêu cầu tạo một 'cửa sau', mà ông cho là cần thiết để điều tra các âm mưu khủng bố tiềm ẩn. Tuy nhiên, nhờ sự thừa nhận của chính Graham, khi anh ấy hiểu thêm về độ phức tạp kỹ thuật của miền, anh ấy nhận ra rằng anh ấy đã cho rằng nó đơn giản hơn nhiều so với những gì anh ấy đã nhận ra và rằng một cửa hậu như vậy có thể gây ra những hậu quả tiêu cực nghiêm trọng. Đây có thể được coi là một ví dụ về hiệu ứng Dunning-Kruger - một chuyên gia an ninh mạng có thể sẽ hiểu ngay lập tức về cách một cửa hậu như vậy có thể bị khai thác, vì họ có hiểu biết sâu sắc về miền, một người dân có thể cho rằng bảo mật điện thoại tương tự hơn đối với _bảo mật vật lý_ khi có thể thực hiện được 'khóa chính' để thực thi pháp luật, nhưng sự tương tự này không áp dụng đủ tốt để mô tả mã hóa hiện đại trong an ninh mạng.

### Luật Fitts'

[Luật phù hợp với Wikipedia](https://en.wikipedia.org/wiki/Fitts%27s_law)

Định luật Fitts dự đoán rằng thời gian cần thiết để di chuyển đến một khu vực mục tiêu là một hàm của khoảng cách đến mục tiêu chia cho chiều rộng của mục tiêu.

<img width="300px" src="./images/fitts-law.svg" alt="Diagram: Fitts Law">

Hệ quả của luật này quy định rằng khi thiết kế UX hoặc UI, các phần tử tương tác phải càng lớn càng tốt và khoảng cách giữa vùng chú ý của người dùng và phần tử tương tác phải càng nhỏ càng tốt. Điều này có hậu quả về thiết kế, chẳng hạn như nhóm các nhiệm vụ thường được sử dụng với nhau.

Nó cũng chính thức hóa khái niệm 'góc ma thuật', các góc của màn hình mà người dùng có thể 'quét' chuột của họ để dễ dàng nhấn - đó là nơi có thể đặt các phần tử giao diện người dùng chính. Nút Start của Windows nằm ở một góc kỳ diệu, giúp bạn dễ dàng lựa chọn và như một sự tương phản thú vị, nút 'đóng cửa sổ' của MacOS _không_ nằm ở một góc ma thuật, nên khó có thể nhấn nhầm.

Xem thêm:

- [Năng lực thông tin của hệ thống vận động của con người trong việc điều khiển biên độ vận động.](https://www.semanticscholar.org/paper/The-information-capacity-of-the-human-motor-system-Fitts/634c9fde5f1c411e4487658ac738dcf18d98ea8d)

### Luật Gall

[Luật Gall trên Wikipedia](<https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law>)

> Một hệ thống phức tạp luôn luôn được phát hiện là đã được phát triển từ một hệ thống đơn giản đã hoạt động. Một hệ thống phức tạp được thiết kế từ đầu không bao giờ hoạt động và không thể được vá để làm cho nó hoạt động. Bạn phải bắt đầu lại với một hệ thống hoạt động đơn giản.
>
> ( [John Gall](<https://en.wikipedia.org/wiki/John_Gall_(author)>) )

Định luật Gall ngụ ý rằng những nỗ lực _thiết kế_ các hệ thống phức tạp có khả năng thất bại cao. Các hệ thống phức tạp cao hiếm khi được xây dựng trong một lần, mà thực tế là phát triển từ các hệ thống đơn giản hơn.

Ví dụ cổ điển là world-wide-web. Ở trạng thái hiện tại, nó là một hệ thống rất phức tạp. Tuy nhiên, ban đầu nó được định nghĩa là một cách đơn giản để chia sẻ nội dung giữa các tổ chức học thuật. Nó đã rất thành công trong việc đáp ứng những mục tiêu này và ngày càng phát triển trở nên phức tạp hơn theo thời gian.

Xem thêm:

- [KISS (Giữ nó đơn giản, ngu ngốc)](#the-kiss-principle)

### Luật Goodhart

[Định luật Goodhart trên Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law)

> Mọi hệ thống có xu hướng sụp đổ khi chịu áp lực thống kê quan sát với mục đích kiểm soát đặt lên nó
>
> _Charles Goodhart_

Cũng thường được gọi là:

> Khi đo lường trở thành mục tiêu, nó không còn là một đo lường tốt.
>
> _Marilyn Strathern_

Luật nói rằng các tối ưu hóa theo hướng đo lường, có thể dẫn đến việc giảm giá trị của chính kết quả đo lường. Việc áp dụng một cách mù quáng các bộ đo lường ( [KPI](https://en.wikipedia.org/wiki/Performance_indicator) ) cho một quy trình dẫn đến hiệu quả bị bóp méo. Mọi người có xu hướng tối ưu hóa cục bộ bằng cách "chơi" hệ thống để đáp ứng các chỉ số cụ thể, thay vì chú ý đến kết quả tổng thể của các hành động của họ.

Ví dụ trong thế giới thực:

- Các bài kiểm tra không có xác nhận đáp ứng kỳ vọng về độ bao phủ của mã, mặc dù thực tế là mục đích của số liệu là tạo ra phần mềm được kiểm tra tốt.
- Khi điểm hiệu suất của nhà phát triển được tính bằng số dòng lệnh được cam kết, sẽ dẫn đến số dòng lệnh bị phình ra một cách vô cớ.

Xem thêm:

- [Luật Goodhart: Cách đo lường những điều sai trái thúc đẩy hành vi trái đạo đức](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Dilbert trên phần mềm không có lỗi](https://dilbert.com/strip/1995-11-13)

### Hanlon Razor

[Hanlon Razor trên Wikipedia](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Kết quả xấu không thể giải thích được bằng ác ý, mà bằng sự ngu dốt
>
> Robert J. Hanlon

Nguyên tắc này gợi ý rằng những hành động dẫn đến một kết quả xấu không phải là do ý chí xấu. Thay vào đó, kết quả xấu có nhiều khả năng là do những hành động hoặc tác động không được hiểu một cách đầy đủ.

### Luật Hick (Luật Hick-Hyman)

[Luật Hick trên Wikipedia](https://en.wikipedia.org/wiki/Hick%27s_law)

> Thời gian quyết định tăng theo logarit với số lượng tùy chọn bạn có thể chọn.
>
> William Edmund Hick và Ray Hyman

Trong phương trình dưới đây, `T` là thời gian để đưa ra quyết định, `n` là số lựa chọn và `b` là hằng số được xác định bằng phân tích dữ liệu.

![Luật Hicks](./images/hicks-law.svg)

_(Hình ảnh tham khảo: Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/Hick%27s_law)_

Luật này chỉ áp dụng khi số lượng tùy chọn được _sắp xếp_ , ví dụ, theo thứ tự bảng chữ cái. Điều này được ngụ ý trong lôgarit cơ số hai - ngụ ý người ra quyết định về cơ bản đang thực hiện _tìm kiếm nhị phân_ . Nếu các tùy chọn không được sắp xếp hợp lý, các thử nghiệm cho thấy thời gian thực hiện là tuyến tính.

Điều này có tác động đáng kể trong thiết kế giao diện người dùng; đảm bảo rằng người dùng có thể dễ dàng tìm kiếm thông qua các tùy chọn dẫn đến việc ra quyết định nhanh hơn.

Một mối tương quan cũng đã được chỉ ra trong Định luật Hick giữa chỉ số IQ và thời gian phản ứng như được thể hiện trong [Tốc độ xử lý thông tin: Thay đổi phát triển và liên kết với trí thông minh](https://www.sciencedirect.com/science/article/pii/S0022440599000369) .

Xem thêm:

- [Luật Fitts](#fitts-law)

### Định luật Hofstadter

[Hofstadter's Law on Wikipedia](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> Nó luôn mất nhiều thời gian hơn bạn dự tính, ngay cả khi bạn tính đến Định luật Hofstadter.
>
> (Douglas Hofstadter)

Bạn có thể nghe thấy luật này được đề cập đến khi xem xét các ước tính về thời gian. Có vẻ như một sự sai lầm trong phát triển phần mềm là chúng ta có xu hướng không giỏi trong việc ước tính chính xác thời gian một thứ gì đó sẽ được phân phối.

Đây là từ cuốn sách ' [Gödel, Escher, Bach: Một bím tóc vàng vĩnh cửu](#reading-list) '.

Xem thêm:

- [Danh sách đọc: Gödel, Escher, Bach: Một bím tóc vàng vĩnh cửu](#reading-list)

### Định luật Hutber

[Luật Hutber trên Wikipedia](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Cải tiến nghĩa là xấu đi.
>
> ( [Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber) )

Luật này gợi ý rằng những cải tiến đối với một hệ thống sẽ dẫn đến sự hư hỏng ở các bộ phận khác, hoặc nó sẽ che giấu sự hư hỏng khác, dẫn đến sự suy thoái về tổng thể so với trạng thái hiện tại của hệ thống.

Ví dụ: giảm độ trễ phản hồi cho một điểm cuối cụ thể có thể gây ra các vấn đề về thông lượng và dung lượng tăng thêm trong luồng yêu cầu, ảnh hưởng đến một hệ thống con hoàn toàn khác.

### Chu kỳ Hype &amp; Định luật Amara

[Chu kỳ cường điệu hóa trên Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

> Chúng ta có xu hướng đánh giá cao hiệu quả của một công nghệ trong ngắn hạn và đánh giá thấp hiệu quả về lâu dài.
>
> (Roy Amara)

Hype Cycle là hình ảnh đại diện cho sự sôi động và phát triển của công nghệ theo thời gian, ban đầu được sản xuất bởi Gartner. Nó được hiển thị tốt nhất bằng hình ảnh:

![Chu kỳ Hype](./images/hype-cycle.svg)

_(Tham khảo hình ảnh: Bởi Jeremykemp tại Wikipedia tiếng Anh, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)_

Nói tóm lại, chu kỳ này cho thấy rằng thường có sự bùng nổ về công nghệ mới và tác động tiềm tàng của nó. Các đội thường nhanh chóng tham gia vào các công nghệ này, và đôi khi cảm thấy thất vọng với kết quả. Điều này có thể là do công nghệ chưa đủ trưởng thành hoặc các ứng dụng trong thế giới thực vẫn chưa được thực hiện đầy đủ. Sau một khoảng thời gian nhất định, khả năng của công nghệ tăng lên và các cơ hội thực tế để sử dụng nó cũng tăng lên, và các nhóm cuối cùng có thể trở nên hiệu quả. Câu nói của Roy Amara tóm tắt điều này một cách ngắn gọn nhất - "Chúng ta có xu hướng đánh giá quá cao tác dụng của một công nghệ trong ngắn hạn và đánh giá thấp về lâu dài".

### Luật Hyrum (Luật của các giao diện ngầm)

[Luật trực tuyến của Hyrum](http://www.hyrumslaw.com/)

> Với đủ số lượng người dùng đủ lớn, điều bạn cam kết trong đặc tả không quan trọng: tất cả các hành vi có thể quan sát được trên hệ thống của bạn sẽ phụ thuộc vào ai đó.
>
> (Hyrum Wright)

Luật của Hyrum tuyên bố rằng khi bạn có một _số lượng đủ lớn lời gọi đến bộ_ API, tất cả các hành vi của API (ngay cả những hành vi không được định nghĩa là một phần của hợp đồng công khai) cuối cùng sẽ phụ thuộc vào ai đó. Ví dụ đơn giản có thể là các tính phi chức năng, như thời gian phản hồi của một API. Một ví dụ tinh tế hơn có thể là người tiêu dùng đang dựa vào việc áp dụng regex cho một thông báo lỗi để xác định _loại_ lỗi của một API. Ngay cả khi hợp đồng công khai của API không nêu gì về nội dung của thông báo, cho biết người dùng nên sử dụng mã lỗi liên quan, _một số_ người dùng có thể sử dụng thông báo và việc thay đổi thông báo về cơ bản sẽ phá vỡ API đối với những người dùng đó.

Xem thêm:

- [Luật trừu tượng rò rỉ](#the-law-of-leaky-abstractions)
- [XKCD 1172](https://xkcd.com/1172/)

### Định luật Kernighan

> Gỡ lỗi khó gấp đôi so với viết mã ngay từ đầu. Do đó, nếu bạn viết mã một cách khéo léo nhất có thể, theo định nghĩa, bạn không đủ thông minh để gỡ lỗi nó.
>
> (Brian Kernighan)

Định luật Kernighan được đặt tên cho [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) và bắt nguồn từ một trích dẫn từ cuốn sách [Các yếu tố của phong cách lập trình của](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style) Kernighan và Plauger:

> Mọi người đều biết rằng việc gỡ lỗi khó gấp đôi so với việc viết một chương trình ngay từ đầu. Vì vậy, nếu bạn thông minh hết mức có thể khi bạn viết nó, làm thế nào bạn sẽ gỡ lỗi nó?

Mặc dù hyperbolic, Luật Kernighan đưa ra lập luận rằng mã đơn giản được ưu tiên hơn mã phức tạp, bởi vì việc gỡ lỗi bất kỳ vấn đề nào phát sinh trong mã phức tạp có thể tốn kém hoặc thậm chí không khả thi.

Xem thêm:

- [Nguyên tắc KISS](#the-kiss-principle)
- [Triết lý Unix](#the-unix-philosophy)
- [Dao cạo của Occam](#occams-razor)

### Luật Linus

[Luật Linus trên Wikipedia](https://en.wikipedia.org/wiki/Linus%27s_law)

> Càng nhiều người nhìn vào sẽ lấy ra nhiều lỗi.
>
> _Eric S. Raymond_

Luật này chỉ đơn giản nói rằng càng nhiều người có thể nhìn thấy một vấn đề, thì khả năng một người nào đó đã nhìn thấy và giải quyết vấn đề đó trước đây, hoặc một cái gì đó tương tự.

Mặc dù ban đầu nó được sử dụng để mô tả giá trị của các mô hình mã nguồn mở cho các dự án, nó có thể được chấp nhận cho bất kỳ loại dự án phần mềm nào. Nó cũng có thể được mở rộng cho các quy trình - nhiều đánh giá mã hơn, phân tích tĩnh hơn và các quy trình kiểm tra đa nguyên tắc sẽ làm cho các vấn đề hiển thị và dễ xác định hơn.

Một tuyên bố chính thức hơn có thể là:

> Với cơ sở người thử nghiệm beta và đồng phát triển đủ lớn, hầu hết mọi vấn đề sẽ được xác định một cách nhanh chóng và có thể được giải quyết bởi những người đã từng gặp sự cố tương tự trước đây.

Luật này được đặt tên để vinh danh [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) trong cuốn sách " [The Cathedral and the Bazaar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar) " của Eric S. Raymond.

### Định luật Metcalfe

[Luật Metcalfe trên Wikipedia](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Trong lý thuyết mạng, giá trị của một hệ thống tăng lên xấp xỉ bình phương của số lượng người dùng của hệ thống.

Luật này dựa trên số lượng các kết nối theo cặp có thể có trong một hệ thống và có liên quan chặt chẽ với Định [luật Reed](#reeds-law) . Odlyzko và những người khác đã lập luận rằng cả Định luật Reed và Định luật Metcalfe đều phóng đại giá trị của hệ thống bằng cách không tính đến giới hạn nhận thức của con người về hiệu ứng mạng; xem [Số của Dunbar](#dunbars-number) .

Xem thêm:

- [Luật Reed](#reeds-law)
- [Số Dunbar](#dunbars-number)

### Định luật Moore

[Định luật Moore trên Wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)

> Số lượng bóng bán dẫn trong một mạch tích hợp tăng gấp đôi khoảng hai năm một lần.

Thường được sử dụng để minh họa tốc độ tuyệt đối mà công nghệ bán dẫn và chip đã được cải thiện, dự đoán của Moore đã được chứng minh là có độ chính xác cao trong khoảng thời gian từ những năm 1970 đến cuối những năm 2000. Trong những năm gần đây, xu hướng đã thay đổi một chút, một phần do [những hạn chế vật lý về mức độ thu nhỏ của các thành phần](https://en.wikipedia.org/wiki/Quantum_tunnelling) . Tuy nhiên, những tiến bộ trong quá trình song song hóa và những thay đổi có khả năng mang tính cách mạng trong công nghệ bán dẫn và điện toán lượng tử có thể có nghĩa là Định luật Moore có thể tiếp tục đúng trong nhiều thập kỷ tới.

### Định luật Murphy / Sod

[Định luật Murphy trên Wikipedia](https://en.wikipedia.org/wiki/Murphy%27s_law)

> Điều gì có thể xảy ra sai sót sẽ xảy ra sai sót.

Liên quan đến [Edward A. Murphy, Định luật Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.) _Murphy_ nói rằng nếu cái gì sai, nó sẽ lòi ra.

Đây là một câu châm ngôn phổ biến giữa các nhà phát triển. Đôi khi điều không mong muốn xảy ra khi phát triển, thử nghiệm hoặc thậm chí trong quá trình sản xuất. Điều này cũng có thể liên quan đến Định _luật Sod_ (phổ biến hơn trong tiếng Anh Anh):

> Nếu điều gì đó có thể xảy ra, nó sẽ xảy ra vào thời điểm tồi tệ nhất có thể.

Những 'luật' này thường được sử dụng theo nghĩa truyện tranh. Tuy nhiên, các hiện tượng như [_Thiên lệch xác nhận_](#TODO) và [_Thiên lệch lựa chọn_](#TODO) có thể khiến mọi người có lẽ quá nhấn mạnh các định luật này (phần lớn khi mọi thứ hoạt động, chúng không được chú ý, tuy nhiên, thất bại lại được chú ý nhiều hơn và thu hút nhiều thảo luận hơn).

Xem thêm:

- [Khuynh hướng xác nhận](#TODO)
- [Xu hướng lựa chọn](#TODO)

### Occam's Razor

[Occam's Razor trên Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)

> Các thực thể không nên được nhân lên khi không cần thiết.
>
> William của Ockham

Occam nói rằng trong số một số giải pháp khả thi, giải pháp khả dĩ nhất là giải pháp có ít khái niệm và giả định nhất. Giải pháp này là giải pháp đơn giản nhất và chỉ giải quyết được vấn đề đã cho, mà không tạo ra sự phức tạp ngẫu nhiên và hậu quả tiêu cực có thể xảy ra.

Xem thêm:

- [YAGNI](#yagni)
- [Không có viên đạn bạc: Sự phức tạp tình cờ và sự phức tạp thiết yếu](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Thí dụ:

- [Phát triển phần mềm tinh gọn: Loại bỏ lãng phí](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Định luật Parkinson

[Parkinson's Law on Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Công việc mở rộng để lấp đầy thời gian có sẵn để hoàn thành.

Trong bối cảnh ban đầu, Luật này dựa trên các nghiên cứu về các bộ máy quan liêu. Nó có thể được áp dụng một cách bi quan cho các sáng kiến phát triển phần mềm, lý thuyết cho rằng các nhóm sẽ hoạt động kém hiệu quả cho đến khi thời hạn gần kề, sau đó vội vàng hoàn thành công việc trước thời hạn, do đó làm cho thời hạn thực tế hơi tùy tiện.

Nếu luật này được kết hợp với Định luật [Hofstadter](#hofstadters-law) , một quan điểm thậm chí còn bi quan hơn - công việc sẽ mở rộng để lấp đầy thời gian có sẵn để hoàn thành và _vẫn mất nhiều thời gian hơn dự kiến_ .

Xem thêm:

- [Định luật Hofstadter](#hofstadters-law)

### Hiệu ứng tối ưu hóa sớm

[Tối ưu hóa sớm trên WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Tối ưu sớm là gốc rễ của mọi xấu xa.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

Trong bài báo của Donald Knuth, [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements) , ông đã viết: "Các lập trình viên lãng phí rất nhiều thời gian để suy nghĩ hoặc lo lắng về tốc độ của các phần không quan trọng trong chương trình của họ và những nỗ lực về hiệu quả này thực sự có tác động tiêu cực mạnh khi gỡ lỗi và bảo trì được xem xét. Chúng ta nên quên đi những hiệu quả nhỏ, nói rằng khoảng 97% thời gian: **tối ưu hóa sớm là gốc rễ của mọi điều xấu** . Tuy nhiên, chúng ta không nên bỏ qua cơ hội của mình trong 3% quan trọng đó. "

Tuy nhiên, _Tối ưu hóa sớm_ có thể được định nghĩa (theo thuật ngữ ít tải hơn) là tối ưu hóa trước khi chúng ta biết rằng chúng ta cần phải làm như vậy.

### Định luật Putt

[Luật Putt trên Wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Công nghệ bị chi phối bởi hai loại người, những người hiểu những gì họ không quản lý và những người quản lý những gì họ không hiểu.

Định luật Putt thường được tuân theo bởi Hệ quả Putt:

> Mọi hệ thống phân cấp kỹ thuật, theo thời gian, phát triển một sự nghịch đảo năng lực.

Những tuyên bố này cho thấy rằng do các tiêu chí lựa chọn khác nhau và xu hướng trong cách tổ chức nhóm, sẽ có một số người có kỹ năng ở các cấp làm việc của một tổ chức kỹ thuật và một số người trong vai trò quản lý không nhận thức được sự phức tạp và thách thức của công việc mà họ đang quản lý. Điều này có thể là do các hiện tượng như [Nguyên tắc Peter](#the-peter-principle) hoặc [Nguyên tắc Dilbert](#the-dilbert-principle) .

Tuy nhiên, cần nhấn mạnh rằng các Luật như thế này là khái quát rộng lớn và có thể áp dụng cho _một số_ loại hình tổ chức và không áp dụng cho các loại hình tổ chức khác.

Xem thêm:

- [Nguyên tắc Peter](#the-peter-principle)
- [Nguyên tắc Dilbert](#the-dilbert-principle)

### Luật Reed

[Luật Reed trên Wikipedia](https://en.wikipedia.org/wiki/Reed's_law)

> Tiện ích trên các mạng lớn, đặc biệt là mạng xã hội, sẽ có quy mô theo cấp số nhân so với quy mô của mạng.

Luật này dựa trên lý thuyết đồ thị, trong đó tiện ích mở rộng theo số lượng các nhóm con, nhanh hơn số lượng người tham gia hoặc số lượng các kết nối theo cặp có thể có. Odlyzko và những người khác đã lập luận rằng Định luật Reed phóng đại quá mức tiện ích của hệ thống bằng cách không tính đến các giới hạn nhận thức của con người về các hiệu ứng mạng; xem [Số của Dunbar](#dunbars-number) .

Xem thêm:

- [Định luật Metcalfe](#metcalfes-law)
- [Số Dunbar](#dunbars-number)

### Định luật Bảo toàn Độ phức tạp (Định luật Tesler)

[Luật bảo tồn sự phức tạp trên Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Luật này nói rằng có một lượng phức tạp nhất định trong một hệ thống và chúng không thể giảm bớt.

Một số phức tạp trong một hệ thống là 'vô tình'. Đó là hệ quả của cấu trúc kém, sai lầm hoặc chỉ là mô hình hóa vấn đề cần giải quyết một cách tồi tệ. Sự phức tạp do sơ ý có thể được giảm bớt (hoặc loại bỏ). Tuy nhiên, một số phức tạp là 'nội tại' là hệ quả của sự phức tạp vốn có trong vấn đề đang được giải quyết. Sự phức tạp này có thể được di chuyển, nhưng không được loại bỏ.

Một yếu tố thú vị đối với luật này là gợi ý rằng ngay cả khi đơn giản hóa toàn bộ hệ thống, độ phức tạp nội tại vẫn không giảm, nó được _chuyển đến người dùng_ , người phải hành xử theo cách phức tạp hơn.

### Định luật Demeter

[Định luật Demeter trên Wikipedia](https://en.wikipedia.org/wiki/Law_of_Demeter)

> Đừng nói chuyện với người lạ.

Định luật Demeter, còn được gọi là "Nguyên tắc của kiến thức ít nhất" là một nguyên tắc cho thiết kế phần mềm, đặc biệt thích hợp trong các ngôn ngữ hướng đối tượng.

Nó nói rằng một đơn vị phần mềm chỉ nên nói chuyện với các cộng tác viên trực tiếp của nó. Một đối tượng `A` có tham chiếu đến đối tượng `B` có thể gọi các phương thức của nó, nhưng nếu `B` có tham chiếu đến đối tượng `C` , `A` không nên gọi các phương thức của `C` Vì vậy, nếu `C` có phương thức `doThing()` `A` không nên gọi nó trực tiếp; `B.getC().doThis()` .

Việc tuân theo nguyên tắc chính này sẽ giới hạn phạm vi thay đổi, giúp chúng dễ dàng hơn và an toàn hơn trong tương lai.

### Luật trừu tượng rò rỉ

[Luật về sự tóm tắt rò rỉ trên Joel trên phần mềm](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Tất cả những thiết kế trừu tượng không tầm thường, ở một mức độ nào đó, đều bị rò rỉ.
>
> ( [Joel Spolsky](https://twitter.com/spolsky) )

Luật này quy định rằng trừu tượng, thường được sử dụng trong máy tính để đơn giản hóa làm việc với các hệ thống phức tạp, trong một số tình huống nhất định sẽ làm 'rò rỉ' các phần tử của hệ thống cơ bản, điều này làm cho trừu tượng hoạt động theo cách không mong muốn.

Một ví dụ có thể đang tải một tệp và đọc nội dung của nó. Các API hệ thống tệp là một phần _trừu tượng_ của các hệ thống nhân cấp thấp hơn, bản thân chúng là một phần trừu tượng đối với các quá trình vật lý liên quan đến việc thay đổi dữ liệu trên đĩa từ tính (hoặc bộ nhớ flash cho SSD). Trong hầu hết các trường hợp, việc xử lý một tệp như một luồng dữ liệu nhị phân sẽ hoạt động. Tuy nhiên, đối với ổ đĩa từ tính, việc đọc dữ liệu tuần tự sẽ _nhanh hơn đáng kể_ so với truy cập ngẫu nhiên (do lỗi trang tăng lên), nhưng đối với ổ đĩa SSD, chi phí này sẽ không xuất hiện. Cần phải hiểu chi tiết cơ bản để đối phó với trường hợp này (ví dụ: các tệp chỉ mục cơ sở dữ liệu được cấu trúc để giảm chi phí truy cập ngẫu nhiên), chi tiết triển khai 'rò rỉ' trừu tượng mà nhà phát triển có thể cần phải biết.

Ví dụ trên có thể trở nên phức tạp _hơn khi có nhiều nội dung_ trừu tượng hơn. Hệ điều hành Linux cho phép các tệp được truy cập qua mạng nhưng được trình bày cục bộ dưới dạng tệp 'bình thường'. Tóm tắt này sẽ 'rò rỉ' nếu có lỗi mạng. Nếu nhà phát triển coi các tệp này là tệp 'bình thường' mà không xem xét đến thực tế là chúng có thể phải chịu độ trễ và lỗi mạng, thì các giải pháp sẽ có lỗi.

Bài báo mô tả luật cho thấy rằng việc phụ thuộc quá nhiều vào những điều trừu tượng, kết hợp với sự hiểu biết kém về các quy trình cơ bản, thực sự khiến việc xử lý vấn đề trong một số trường hợp _trở nên phức tạp hơn._

Xem thêm:

- [Định luật Hyrum](#hyrums-law-the-law-of-implicit-interfaces)

Ví dụ trong thế giới thực:

- [Photoshop khởi động chậm](https://forums.adobe.com/thread/376152) - một vấn đề tôi gặp phải trong quá khứ. Photoshop khởi động chậm, đôi khi mất vài phút. Có vẻ như vấn đề là khi khởi động, nó đọc một số thông tin về máy in mặc định hiện tại. Tuy nhiên, nếu máy in đó thực sự là một máy in mạng, thì quá trình này có thể mất rất nhiều thời gian. Sự _trừu tượng_ của một máy in mạng được trình bày cho hệ thống tương tự như một máy in cục bộ đã gây ra sự cố cho người dùng trong các tình huống kết nối kém.

### Luật về Sự tầm thường

[Luật Sự Tầm Thường trên Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

Luật này gợi ý rằng các nhóm sẽ dành nhiều thời gian và sự chú ý hơn cho những vấn đề nhỏ nhặt hoặc thẩm mỹ hơn là những vấn đề nghiêm trọng và thực chất.

Ví dụ hư cấu phổ biến được sử dụng là một ủy ban phê duyệt kế hoạch cho nhà máy điện hạt nhân, họ dành phần lớn thời gian để thảo luận về cấu trúc của nhà để xe đạp, thay vì thiết kế quan trọng hơn nhiều cho chính nhà máy điện. Có thể khó đưa ra ý kiến đóng góp có giá trị cho các cuộc thảo luận về các chủ đề rất lớn, phức tạp nếu không có sự chuẩn bị hoặc chuyên môn cao về chủ đề. Tuy nhiên, mọi người muốn được xem là đóng góp ý kiến đóng góp có giá trị. Do đó, có xu hướng tập trung quá nhiều thời gian vào những chi tiết nhỏ, có thể dễ dàng lý giải, nhưng không nhất thiết phải có tầm quan trọng đặc biệt.

Ví dụ hư cấu ở trên đã dẫn đến việc sử dụng thuật ngữ 'lo thiết kế nhà để xe đạp' như một cách diễn đạt cho việc lãng phí thời gian vào những chi tiết nhỏ nhặt. Một thuật ngữ liên quan là ' [Yak Shaving](https://en.wiktionary.org/wiki/yak_shaving) ', có nghĩa là một hoạt động dường như không liên quan nhưng là một phần của chuỗi dài các điều kiện tiên quyết đối với nhiệm vụ chính.

### Triết lý Unix

[Triết lý Unix trên Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

Triết lý của Unix là các thành phần phần mềm phải nhỏ và tập trung vào làm tốt một việc cụ thể. Điều này có thể giúp dễ dàng hơn trong việc xây dựng hệ thống bằng cách biên soạn các đơn vị nhỏ, đơn giản, được xác định rõ ràng, thay vì sử dụng các chương trình lớn, phức tạp, đa mục đích.

Các thực hành hiện đại như 'Kiến trúc Microservice' có thể được coi là một ứng dụng của luật này, trong đó các dịch vụ nhỏ, tập trung và thực hiện một việc cụ thể, cho phép hành vi phức tạp bao gồm các khối xây dựng đơn giản.

### Quy tắc Scout

[Quy tắc hướng đạo sinh trên O'Reilly](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)

> Luôn để lại mã tốt hơn khi bạn tìm thấy.
>
> (Robert C. Martin (Uncle Bob))

Dựa trên "Quy tắc Hướng đạo", là "luôn để khu cắm trại sạch sẽ hơn khi bạn đến", Quy tắc Hướng đạo trong lập trình chỉ đơn giản là "luôn để mã sạch hơn những gì bạn tìm thấy".

Điều này đã được giới thiệu trong chương đầu tiên của cuốn sách [Clean Code](https://www.goodreads.com/book/show/3735293-clean-code) của Bob Martin. Quy tắc gợi ý rằng các nhà phát triển nên thực hiện 'tái cấu trúc lạc quan', có nghĩa là cố gắng cải thiện chất lượng tổng thể của mã khi bạn làm việc trên nó. Nếu bạn thấy lỗi, hãy cố gắng sửa chữa hoặc làm sạch nó. Tuy nhiên, khi thực hiện các thay đổi đối với mã có vẻ không chính xác, bạn nên nhớ [Chesterton's Fence](#chestertons-fence) !

Xem thêm:

- [Danh sách đọc: Mã sạch](#reading-list)
- [Chesterton's Fence](#chestertons-fence)
- [Lý thuyết cửa sổ bị hỏng](#broken-windows-theory)

https://www.amazon.sg/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882

### Mô hình Spotify

[Mô hình Spotify trên Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Mô hình Spotify là một phương pháp tiếp cận cấu trúc tổ chức và nhóm đã được phổ biến bởi 'Spotify'. Trong mô hình này, các nhóm được tổ chức xung quanh các tính năng, thay vì công nghệ.

Mô hình Spotify cũng phổ biến các khái niệm về Bộ lạc, Bang hội, Chi hội, là các thành phần khác trong cơ cấu tổ chức của chúng.

Các thành viên của tổ chức đã mô tả rằng ý nghĩa thực tế của các nhóm này thay đổi, phát triển và là một thử nghiệm đang diễn ra. Thực tế là mô hình là một _quá trình đang vận động_ , chứ không phải là một mô hình cố định tiếp tục dẫn đến các cách hiểu khác nhau về cấu trúc, có thể dựa trên các bài thuyết trình của nhân viên tại các hội nghị. Điều này có nghĩa là 'ảnh chụp nhanh' có thể được bên thứ ba 'đóng gói lại' như một _cấu trúc cố định_ , với thực tế là mô hình động sẽ bị mất.

### Quy tắc hai chiếc bánh pizza

> Nếu một 2 chiếc bánh pizza không đủ cho một nhóm, thì nhóm đó đã quá lớn
>
> (Jeff Bezos)

Quy tắc này cho thấy rằng bất kể quy mô của công ty, các đội nên đủ nhỏ để có thể ăn hai chiếc pizza. Được gán cho Jeff Bezos và Amazon, niềm tin này cho thấy rằng các đội lớn vốn đã kém hiệu quả. Điều này được hỗ trợ bởi thực tế là khi quy mô nhóm tăng tuyến tính, liên kết giữa mọi người sẽ tăng theo bậc hai; do đó chi phí phối hợp và giao tiếp cũng tăng theo bậc hai. Nếu chi phí phối hợp này về cơ bản là tổng chi phí, thì các nhóm nhỏ hơn nên được ưu tiên hơn.

Số lượng liên kết giữa mọi người có thể được biểu thị bằng `n(n-1)/2` trong đó n = số người.

<img width="200px" alt="Đồ thị hoàn chỉnh; Liên kết giữa mọi người" src="./images/complete-graph.svg">

### Luật Wadler

[Luật của Wadler trên wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Trong bất kỳ thiết kế ngôn ngữ nào, tổng thời gian dành để thảo luận về một tính năng trong danh sách này tỷ lệ thuận với hai phần được nâng lên với sức mạnh của vị trí của nó.
>
> 1. Ngữ nghĩa học
> 2. Cú pháp
> 3. Cú pháp từ vựng
> 4. Cú pháp đơn giản của nhận xét
>
> (Nói tóm lại, cứ mỗi giờ dành cho ngữ nghĩa thì 8 giờ sẽ dành cho cú pháp của chú thích).

Tương tự như [Định luật về tính tầm thường](#the-law-of-triviality) , Định luật của Wadler cho biết khi thiết kế một ngôn ngữ, lượng thời gian dành cho các cấu trúc ngôn ngữ cao hơn một cách tương xứng so với tầm quan trọng của những tính năng đó.

Xem thêm:

- [Luật tầm thường](#the-law-of-triviality)

### Định luật Wheaton

[Liên kết](http://www.wheatonslaw.com/)

[Ngày chính thức](https://dontbeadickday.com/)

> Đừng khôn kiểu ranh ma.
>
> _Wil Wheaton_

Được đặt ra bởi Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory), luật đơn giản, ngắn gọn và mạnh mẽ này nhằm mục đích tăng cường sự hòa hợp và tôn trọng trong một tổ chức chuyên nghiệp. Nó có thể được áp dụng khi nói chuyện với đồng nghiệp, thực hiện đánh giá mã, phản bác các quan điểm khác, phê bình và nói chung, hầu hết các tương tác chuyên nghiệp mà con người có với nhau.

## Nguyên tắc

Các nguyên tắc thường có nhiều khả năng là các hướng dẫn liên quan đến thiết kế.

### Tất cả các mô hình đều sai (Định luật George Box)

[Tất cả các mô hình đều sai](https://en.wikipedia.org/wiki/All_models_are_wrong)

> Tất cả các mô hình đều sai, nhưng một số mô hình hữu ích.
>
> _George Box_

Nguyên tắc này cho thấy rằng tất cả các mô hình hệ thống đều có sai sót, nhưng miễn là chúng không _quá_ sai sót thì chúng có thể hữu ích. Nguyên tắc này có nguồn gốc từ thống kê nhưng cũng áp dụng cho các mô hình khoa học và máy tính.

Yêu cầu cơ bản của hầu hết các phần mềm là mô hình hóa một hệ thống nào đó. Bất kể hệ thống được mô hình hóa là mạng máy tính, thư viện, biểu đồ kết nối xã hội hay bất kỳ loại hệ thống nào khác, nhà thiết kế sẽ phải quyết định mức độ chi tiết thích hợp để mô hình hóa. Quá nhiều chi tiết có thể dẫn đến quá nhiều phức tạp, quá ít chi tiết có thể khiến mô hình không hoạt động được.

Xem thêm:

- [Luật trừu tượng rò rỉ](#the-law-of-leaky-abstractions)

### Chesterton's Fence

[Chesterton's Fence trên Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence)

> Không nên cải cách cho đến khi hiểu được lý do đằng sau tình trạng hiện tại.

Nguyên tắc này có liên quan trong kỹ thuật phần mềm khi loại bỏ nợ kỹ thuật. Mỗi dòng của một chương trình ban đầu được viết bởi một người nào đó vì một lý do nào đó. Chesterton's Fence gợi ý rằng người ta nên cố gắng hiểu ngữ cảnh và ý nghĩa của mã một cách đầy đủ, trước khi thay đổi hoặc loại bỏ nó, ngay cả khi thoạt nhìn nó có vẻ thừa hoặc không chính xác.

Tên của nguyên tắc này bắt nguồn từ một câu chuyện của [GK Chesterton](https://en.wikipedia.org/wiki/G._K._Chesterton) . Một người đàn ông băng qua hàng rào giữa đường. Anh ta phàn nàn với thị trưởng rằng hàng rào vô dụng này đang cản trở, và yêu cầu dỡ bỏ nó. Thị trưởng hỏi tại sao lại có hàng rào ngay từ đầu. Khi người đàn ông nói rằng anh ta không biết, thị trưởng nói, "Nếu bạn không biết mục đích của nó, tôi chắc chắn sẽ không để bạn gỡ bỏ nó. Hãy đi tìm hiểu công dụng của nó, và sau đó tôi có thể cho phép bạn phá hủy. nó."

### Hiệu ứng Biển Chết

[Hiệu ứng Biển Chết với Bruce F. Webster](http://brucefwebster.com/2008/04/11/the-wetware-crisis-the-dead-sea-effect/)

> Các kỹ sư CNTT tài năng là những người có nhiều khả năng ra đi, ... [những người có xu hướng] ở lại [là] - những kỹ sư CNTT kém tài năng và hiệu quả.
>
> _Bruce F. Webster_

"Hiệu ứng Biển Chết" cho thấy rằng trong bất kỳ tổ chức nào, kỹ năng / tài năng / hiệu quả của các kỹ sư thường tỷ lệ nghịch với thời gian của họ trong công ty.

Thông thường, các kỹ sư có tay nghề cao sẽ dễ dàng kiếm được việc làm ở nơi khác và là những người đầu tiên làm như vậy. Những kỹ sư có kỹ năng lạc hậu hoặc yếu kém sẽ có xu hướng ở lại công ty, vì rất khó tìm việc làm ở nơi khác. Điều này đặc biệt rõ ràng nếu họ nhận được mức lương tăng dần theo thời gian làm việc tại công ty, vì việc nhận được mức thù lao tương đương ở những nơi khác có thể là một thách thức.

### Nguyên tắc Dilbert

[Nguyên tắc Dilbert trên Wikipedia](https://en.wikipedia.org/wiki/Dilbert_principle)

> Các công ty có xu hướng thăng chức một cách có hệ thống những nhân viên không đủ năng lực lên ban quản lý để đưa họ ra khỏi quy trình làm việc.
>
> _Scott Adams_

Là một khái niệm quản lý được phát triển bởi Scott Adams (tác giả của bộ truyện tranh Dilbert), Nguyên tắc Dilbert được lấy cảm hứng từ [Nguyên tắc Peter](#the-peter-principle) . Theo Nguyên tắc Dilbert, những nhân viên chưa từng có năng lực sẽ được thăng chức lên cấp quản lý để hạn chế thiệt hại mà họ có thể gây ra. Adams lần đầu tiên giải thích nguyên tắc này trong một bài báo trên Tạp chí Phố Wall năm 1995, và mở rộng nó trong cuốn sách kinh doanh năm 1996 của ông, [Nguyên tắc Dilbert](#reading-list) .

Xem thêm:

- [Nguyên tắc Peter](#the-peter-principle)
- [Định luật Putt](#putts-law)

### Nguyên tắc Pareto (Quy tắc 80/20)

[Nguyên tắc Pareto trên Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle)

> Hầu hết mọi thứ trong cuộc sống không được phân bổ đồng đều.

Nguyên tắc Pareto gợi ý rằng trong một số trường hợp, phần lớn kết quả đến từ một số ít đầu vào:

- 80% một phần mềm nhất định có thể được viết trong 20% tổng thời gian được phân bổ (ngược lại, 20% mã khó nhất chiếm 80% thời gian)
- 20% nỗ lực tạo ra 80% kết quả
- 20% công việc tạo ra 80% doanh thu
- 20% lỗi gây ra 80% sự cố
- 20% tính năng được dùng 80%

Vào những năm 1940, kỹ sư người Mỹ-Romania, Tiến sĩ Joseph Juran, người được công nhận rộng rãi là cha đẻ của kiểm soát chất lượng, [đã bắt đầu áp dụng nguyên tắc Pareto cho các vấn đề chất lượng](https://en.wikipedia.org/wiki/Joseph_M._Juran) .

Nguyên tắc này còn được gọi là: Quy tắc 80/20, Quy luật số ít và Nguyên tắc về yếu tố thưa thớt.

Ví dụ trong thế giới thực:

- Vào năm 2002, Microsoft đã báo cáo rằng bằng cách sửa 20% lỗi được báo cáo nhiều nhất, 80% lỗi liên quan và sự cố trong windows và office sẽ bị loại bỏ ( [Tham khảo](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm) ).

### Nguyên tắc Shirky

[Nguyên tắc Shirky được giải thích như sau](https://kk.org/thetechnium/the-shirky-prin/)

> Các tổ chức sẽ cố gắng duy trì vấn đề mà họ là giải pháp.
>
> _Clay Shirky_

Nguyên tắc Shirky gợi ý rằng các giải pháp phức tạp - một công ty, một ngành hoặc một công nghệ - có thể trở nên quá tập trung vào vấn đề mà họ đang giải quyết, đến nỗi chúng có thể vô tình kéo dài vấn đề. Điều này có thể là cố ý (một công ty đang cố gắng tìm ra những sắc thái mới cho một vấn đề để biện minh cho việc tiếp tục phát triển một giải pháp), hoặc vô tình (không thể hoặc không sẵn sàng chấp nhận hoặc xây dựng một giải pháp giải quyết được hoàn toàn hoặc loại bỏ nó).

Có quan hệ với:

- Câu nói nổi tiếng của Upton Sinclair, _"Rất khó để khiến một người đàn ông hiểu điều gì đó, khi mức lương của anh ta phụ thuộc vào việc anh ta không hiểu điều đó!"_
- Clay Christensen's _The Innovator's Dilemma_

Xem thêm:

- [Nguyên tắc Pareto](#the-pareto-principle-the-8020-rule)

### Nguyên tắc Peter

[Nguyên tắc Peter trên Wikipedia](https://en.wikipedia.org/wiki/Peter_principle)

> Những người trong một công ty có xu hướng nâng cao đến "mức độ kém cỏi" của họ.
>
> _Laurence J. Peter_

Một khái niệm quản lý được phát triển bởi Laurence J. Peter, Nguyên tắc Peter quan sát rằng những người làm tốt công việc của họ được thăng chức, cho đến khi họ đạt đến mức độ mà họ không còn thành công nữa ("mức độ kém cỏi" của họ). Tại thời điểm này, khi họ cao cấp hơn, họ ít có khả năng bị loại khỏi tổ chức hơn (trừ khi làm quá sai) và sẽ tiếp tục ở một vai trò mà họ có ít kỹ năng nội lực, như những kỹ năng ngày đầu đã tạo ra họ thành công, những kỹ năng cũ này không nhất thiết phải có cho công việc mới của họ.

Điều này đặc biệt quan tâm đến các kỹ sư - những người ban đầu bắt đầu với vai trò kỹ thuật sâu sắc, nhưng thường có con đường sự nghiệp dẫn đến _quản lý_ các kỹ sư khác - đòi hỏi một bộ kỹ năng cơ bản khác.

Xem thêm:

- [Nguyên tắc Dilbert](#the-dilbert-principle)
- [Định luật Putt](#putts-law)

### Nguyên tắc mạnh mẽ (Định luật Postel)

[Nguyên tắc Vững Chắc trên Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Bảo thủ trong những gì bạn làm, tự do trong những gì bạn chấp nhận từ người khác.

Thường được áp dụng trong phần mềm Ứng Dụng Máy Chủ, nguyên tắc này nói rằng những gì bạn trả về cho Đầu Vào phải tối thiểu và phù hợp nhất có thể, nhưng Ứng Dụng Máy Chủ có thể xử lý được các Đầu Vào không đúng định dạng.

Mục tiêu của nguyên tắc này là xây dựng các hệ thống mạnh mẽ, vì chúng có thể xử lý Lời Gọi kém. Tuy nhiên, cân nhắc những tác động tiềm ẩn về bảo mật của việc chấp nhận đầu vào không đúng định dạng, đặc biệt nếu quá trình xử lý đầu vào đó không được kiểm tra tốt. Những tác động này và các vấn đề khác được Eric Allman mô tả trong [Nguyên tắc Vững Chắc được xem xét lại](https://queue.acm.org/detail.cfm?id=1999945) .

Việc cho phép Đầu Vào không tuân thủ theo thời gian có thể làm suy yếu khả năng phát triển vì những người triển khai cuối cùng sẽ dựa vào tính tự do này để xây dựng các tính năng của chúng.

Xem thêm:

- [Định luật Hyrum](#hyrums-law-the-law-of-implicit-interfaces)

### SOLID

Đây là một từ viết tắt, dùng để chỉ:

- S: [The Single Responsibility Principle - Nguyên tắc Đúng Một Trách nhiệm](#the-single-responsibility-principle)
- O: [The Open/Closed Principle - Nguyên tắc Mở / Đóng](#the-openclosed-principle)
- L: [The Liskov Substitution Principle - Nguyên tắc thay thế Liskov ](#the-liskov-substitution-principle)
- I: [The Interface Segregation Principle - Nguyên tắc phân tách giao diện](#the-interface-segregation-principle)
- D: [The Dependency Inversion Principle - Nguyên tắc đảo ngược phụ thuộc](#the-dependency-inversion-principle)

Đây là những nguyên tắc chính trong [Lập trình hướng đối tượng](#todo) . Các nguyên tắc thiết kế như vậy sẽ có thể hỗ trợ các nhà phát triển xây dựng các hệ thống dễ bảo trì hơn.

### Nguyên tắc Đúng Một Trách Nhiệm

[Nguyên tắc Đúng Một Trách Nhiệm trên Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Mỗi mô-đun hoặc lớp chỉ nên có một trách nhiệm duy nhất và trách nhiệm này chỉ do mô-đun hoặc lớp đó thực hiện.

Nguyên tắc đầu tiên trong số các nguyên tắc ' [SOLID'.](#solid) Nguyên tắc này gợi ý rằng các mô-đun hoặc lớp chỉ nên làm một việc và một việc duy nhất và ngược lại trách nhiệm này chỉ do mô-đun hoặc lớp đó thực hiện. Cụ thể, có nghĩa là một thay đổi nhỏ, đơn lẻ đối với một tính năng của chương trình sẽ chỉ yêu cầu một sự thay đổi trong một thành phần. Ví dụ: việc thay đổi cách mật khẩu được xác thực về độ phức tạp sẽ chỉ yêu cầu thay đổi một phần của chương trình.

Về mặt lý thuyết, điều này sẽ làm cho mã mạnh hơn và dễ thay đổi hơn. Biết rằng một thành phần đang được thay đổi chỉ có một trách nhiệm duy nhất có nghĩa là việc _kiểm tra_ sự thay đổi đó sẽ dễ dàng hơn. Sử dụng ví dụ trước đó, việc thay đổi thành phần độ phức tạp của mật khẩu chỉ có thể ảnh hưởng đến các tính năng liên quan đến độ phức tạp của mật khẩu. Có thể khó hơn nhiều để lập luận về tác động của một thay đổi đối với một thành phần có nhiều trách nhiệm.

Xem thêm:

- [Lập trình hướng đối tượng](#todo)
- [SOLID](#solid)

### Nguyên tắc Mở / Đóng

[Nguyên tắc Mở / Đóng trên Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Các Thực Thể phần mềm phải thiết kế sao cho dễ để thêm mới, thay mới và không cần sửa đổi mã cũ.

Nguyên tắc thứ hai của nguyên tắc ' [SOLID'.](#solid) Nguyên tắc này nói rằng các Thực Thể (có thể là lớp, mô-đun, chức năng, v.v.) sẽ có thể dễ dàng _mở rộng_, nhưng _hành vi hiện tại_ của chúng không bị ảnh hưởng, khó bị thay đổi một cách vô ý. Nên khi thay đổi, ta chỉ cần thêm cái mới mà không sửa cái cũ.

Như một ví dụ giả định, hãy tưởng tượng một mô-đun có thể chuyển tài liệu Markdown thành HTML. Bây giờ hãy tưởng tượng có một cú pháp mới được thêm vào đặc tả Markdown, bổ sung hỗ trợ cho các phương trình toán học. Mô-đun nên được _mở để mở rộng_ để triển khai cú pháp toán học mới. Tuy nhiên, các triển khai cú pháp hiện có (như đoạn văn, dấu đầu dòng, v.v.) nên được _đóng lại để sửa đổi_ . Chúng đã hoạt động, chúng tôi không muốn mọi người thay đổi chúng.

Nguyên tắc này có liên quan đặc biệt đối với lập trình hướng đối tượng, nơi chúng ta có thể thiết kế các đối tượng để dễ dàng mở rộng, nhưng sẽ tránh thiết kế các đối tượng có thể làm thay đổi hành vi hiện tại của chúng theo những cách không mong muốn.

Xem thêm:

- [Lập trình hướng đối tượng](#todo)
- [SOLID](#solid)

### Nguyên tắc thay thế Liskov

[Nguyên tắc thay thế Liskov trên Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Chương trình thiết kế để có thể thay thế một lớp bằng một lớp con mở rộng của lớp đó mà không làm hỏng chương trình.

Nguyên tắc thứ ba của nguyên tắc ' [SOLID'.](#solid) Nguyên tắc này nói rằng nếu một thành phần phụ thuộc vào một kiểu, thì nó sẽ có thể sử dụng các kiểu con của kiểu đó mà hệ thống không bị lỗi hoặc phải biết chi tiết về kiểu con đó là gì.

Ví dụ, hãy tưởng tượng chúng ta có một phương thức đọc tài liệu XML từ một cấu trúc đại diện cho một tệp. Nếu phương thức sử dụng loại cơ sở là 'tệp', thì bất kỳ thứ gì bắt nguồn từ 'tệp' sẽ có thể được sử dụng trong hàm. Nếu 'tệp' hỗ trợ tìm kiếm ngược lại và trình phân tích cú pháp XML sử dụng chức năng đó, nhưng loại dẫn xuất 'tệp mạng' không thành công khi tìm kiếm ngược lại, thì 'tệp mạng' sẽ vi phạm nguyên tắc.

Nguyên tắc này có liên quan đặc biệt đối với lập trình hướng đối tượng, trong đó phân cấp kiểu phải được mô hình hóa cẩn thận để tránh gây nhầm lẫn cho người dùng hệ thống.

Xem thêm:

- [Lập trình hướng đối tượng](#todo)
- [SOLID](#solid)

### Nguyên tắc phân tách giao diện

[Nguyên tắc phân tách giao diện trên Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> Không một Ứng Dụng Khách nào buộc phải phụ thuộc vào các Phương Thức mà nó không sử dụng.

Nguyên tắc thứ tư của nguyên tắc ' [SOLID'.](#solid) Nguyên tắc này nói rằng Ứng Dụng Khách không nên phụ thuộc vào các chức năng của thành phần đó mà nó không sử dụng.

Ví dụ, hãy tưởng tượng chúng ta có một phương thức đọc tài liệu XML từ một cấu trúc đại diện cho một tệp. Nó chỉ cần đọc byte, chuyển tới hoặc lùi trong tệp. Nếu phương pháp này cần được cập nhật vì một tính năng không liên quan của cấu trúc tệp thay đổi (chẳng hạn như bản cập nhật cho mô hình quyền được sử dụng để đại diện cho bảo mật tệp), thì nguyên tắc đó đã bị vô hiệu. Tệp sẽ tốt hơn nếu triển khai giao diện 'luồng có thể tìm kiếm' và trình đọc XML sử dụng giao diện đó.

Nguyên tắc này có liên quan đặc biệt đối với lập trình hướng đối tượng, trong đó các giao diện, cấu trúc phân cấp và các kiểu trừu tượng được sử dụng để [giảm thiểu sự ghép nối](#todo) giữa các thành phần khác nhau. [Kiểu Duck](#todo) là một phương pháp thực thi nguyên tắc này bằng cách loại bỏ các giao diện rõ ràng.

Xem thêm:

- [Lập trình hướng đối tượng](#todo)
- [SOLID](#solid)
- [duck typing](#todo)
- [Tách rời](#todo)

### Nguyên tắc đảo ngược phụ thuộc

[Nguyên tắc đảo ngược phụ thuộc trên Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Các mô-đun mức phác thảo không bị phụ thuộc vào các triển khai cụ thể.

Nguyên tắc thứ năm của nguyên tắc ' [SOLID'.](#solid) Nguyên tắc này nói rằng các thành phần thiết kế mức cao - trừu tượng, không cần phải biết cụ thể các thành phần mà chúng phụ thuộc.

Chữ "đảo ngược" trong nguyên tắc này có lẽ lấy từ chuỗi thức ăn trong tự nhiên: trong tự nhiên các sinh vật cấp cao trong chuỗi thức ăn phụ-thuộc vào các sinh vật cấp thấp.

Ví dụ, hãy tưởng tượng chúng ta có một chương trình đọc dữ liệu từ một trang web. Chúng tôi giả định rằng thành phần chính sẽ phải biết về một thành phần tải xuống nội dung trang web, sau đó là một thành phần có thể đọc siêu dữ liệu. Nếu nhìn theo Nghịch Đảo Phụ Thuộc, thì thành phần chính [1] sẽ nhìn vào một thành phần trừu tượng có thể "nạp dữ liệu" [2], và [2] sẽ nhìn vào một thành phần trừu tượng khác có thể "đọc siêu dữ liệu từ một luồng byte". Thành phần chính [1] sẽ không biết về TCP / IP, HTTP, HTML, v.v.

Trong thực tế, điều đó cũng có nghĩa là một thành phần điều phối riêng biệt phải đảm bảo việc triển khai chính xác các kiểu trừu tượng được sử dụng (ví dụ: trong ví dụ trước, _một cái gì đó_ vẫn phải cung cấp cho thành phần trình đọc siêu dữ liệu một trình tải xuống tệp HTTP và trình đọc thẻ meta HTML). Sau đó, điều này chạm vào các mẫu như [Inversion of Control](#todo) và [Dependency Injection](#todo) .

Xem thêm:

- [Lập trình hướng đối tượng](#todo)
- [SOLID](#solid)
- [Đảo ngược kiểm soát](#todo)
- [Tiêm phụ thuộc](#todo)

### Nguyên tắc DRY

[Nguyên tắc DRY trên Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Trong một hệ thống, mỗi phần kiến thức có: một đại diện duy nhất, rõ ràng, có thẩm quyền.

DRY là từ viết tắt của _Don't Repeat Yourself_ . Nguyên tắc này nhằm mục đích giúp các nhà phát triển giảm thiểu việc lặp lại mã và giữ thông tin ở một nơi duy nhất và được trích dẫn vào năm 1999 bởi Andrew Hunt và Dave Thomas trong cuốn sách [Nhà phát triển thực dụng.](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

> Ngược lại với DRY sẽ là _WET_ (Viết mọi thứ hai lần hoặc mỉa mai là Chúng tôi thích đánh máy).

Trên thực tế, nếu bạn có cùng một phần thông tin ở hai (hoặc nhiều) nơi khác nhau, bạn có thể sử dụng DRY để hợp nhất chúng thành một thông tin duy nhất và sử dụng lại bất cứ nơi nào bạn muốn / cần.

Xem thêm:

- [Nhà phát triển thực dụng](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### Nguyên tắc KISS

[KISS trên Wikipedia](https://en.wikipedia.org/wiki/KISS_principle)

> Giữ cho nó thật đơn giản, ngốc cũng làm được

Nguyên tắc KISS nói rằng hầu hết các hệ thống hoạt động tốt nhất nếu chúng được giữ đơn giản thay vì phức tạp; do đó, sự đơn giản nên là mục tiêu chính trong thiết kế và nên tránh sự phức tạp không cần thiết. Bắt nguồn từ Hải quân Hoa Kỳ vào năm 1960, cụm từ này đã được gắn liền với kỹ sư máy bay Kelly Johnson.

Nguyên tắc này được thể hiện rõ nhất qua câu chuyện về việc Johnson giao cho một nhóm kỹ sư thiết kế một số công cụ, với thách thức rằng chiếc máy bay phản lực mà họ đang thiết kế phải được sửa chữa bởi một thợ cơ khí trung bình trong điều kiện chiến đấu chỉ với những công cụ này. Do đó, "ngu ngốc" đề cập đến mối quan hệ giữa cách mọi thứ bị hỏng và sự tinh vi của các công cụ có sẵn để sửa chữa chúng, chứ không phải khả năng của chính các kỹ sư.

Xem thêm:

- [Luật Gall](#galls-law)

### YAGNI

[YAGNI trên Wikipedia](https://en.wikipedia.org/wiki/You_ain%27t_gonna_need_it)

Đây là từ viết tắt của **\*Y**ou **A**in't **G**onna **N**eed **I**t\* .

> Chỉ làm khi bạn thực sự cần, không bao giờ làm khi bạn nghĩ rằng bạn cần chúng.
>
> ( [Ron Jeffries](https://twitter.com/RonJeffries) ) (Đồng sáng lập XP và tác giả của cuốn sách "Cài đặt lập trình cực đoan")

_Nguyên tắc Lập trình Cực đoan_ (XP) này đề xuất các nhà phát triển chỉ triển khai chức năng cần thiết cho các yêu cầu trước mắt và tránh triển khai chức năng mà do dự đoán tương lai nghĩ ra.

Tuân thủ nguyên tắc này sẽ giảm số lượng mã không sử dụng trong cơ sở mã và tránh lãng phí thời gian và công sức vào chức năng không mang lại giá trị.

Xem thêm:

- [Danh sách đọc: Lập trình cực đoan đã được cài đặt](#reading-list)

### Sự sụp đổ của máy tính phân tán

[Sự sụp đổ của máy tính phân tán trên Wikipedia](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

Còn được gọi là Các lỗi _của Máy tính Nối mạng_ , Các Sai lầm là một danh sách các phỏng đoán (hoặc niềm tin) về máy tính phân tán, có thể dẫn đến thất bại trong quá trình phát triển phần mềm. Các giả định là:

- Mạng đáng tin cậy
- Độ trễ bằng 0
- Băng thông là vô hạn
- Mạng an toàn
- Cấu trúc liên kết không thay đổi
- Có một quản trị viên
- Chi phí vận chuyển bằng 0
- Mạng đồng nhất

Bốn mục đầu tiên đã được liệt kê bởi [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) và [Tom Lyon](https://twitter.com/aka_pugs) vào khoảng năm 1991 và lần đầu tiên được [James Gosling](https://en.wikipedia.org/wiki/James_Gosling) xếp vào danh sách "Các di sản của Máy tính nối mạng". [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch) đã thêm vào các ngụy biện thứ 5, 6 và 7. Vào cuối những năm 90, Gosling đã thêm vào sự nguỵ biện thứ 8.

Nhóm được truyền cảm hứng từ những gì đang xảy ra tại thời điểm đó bên trong [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) .

Những ngụy biện này cần được xem xét cẩn thận khi thiết kế mã có khả năng phục hồi; giả sử bất kỳ lỗi ngụy biện nào trong số này có thể dẫn đến logic sai sót không giải quyết được các thực tế và sự phức tạp của hệ thống phân tán.

Xem thêm:

- [Tìm kiếm sự sụp đổ của máy tính phân tán (Phần 1) - Vaidehi Joshi trên phương tiện](https://medium.com/baseds/foraging-for-the-fallacies-of-distributed-computing-part-1-1b35c3b85b53)

## Danh sách đọc

Nếu bạn thấy những khái niệm này thú vị, bạn có thể thưởng thức những cuốn sách sau đây.

- [Mã sạch - Robert C. Martin](https://www.goodreads.com/book/show/3735293-clean-code) - Một trong những cuốn sách được đánh giá cao nhất về cách viết mã sạch, có thể bảo trì.
- [Cài đặt Lập trình Cực đoan - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Trình bày các nguyên tắc cốt lõi của Lập trình Cực đoan.
- [Gödel, Escher, Bach: Một bím tóc vàng vĩnh cửu - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - Sách này khó phân loại. [Hofstadter's Law](#hofstadters-law) là từ cuốn sách.
- [Cấu trúc và diễn giải các chương trình máy tính - Harold Abelson, Gerald Jay Sussman, Julie Sussman](https://www.goodreads.com/book/show/43713) - Nếu bạn là một sinh viên khoa học tổng hợp hoặc kỹ thuật điện tử tại MIT hoặc Cambridge, đây là phần giới thiệu của bạn về lập trình. Được báo cáo rộng rãi như là một bước ngoặt trong cuộc đời của mọi người.
- [The Cathedral and the Bazaar - Eric S. Raymond](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar) - một bộ sưu tập các bài tiểu luận trên mã nguồn mở. Cuốn sách này là nguồn gốc của [Luật Linus](#linuss-law) .
- [Nguyên tắc Dilbert - Scott Adams](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - Một cái nhìn truyện tranh về doanh nghiệp nước Mỹ, của tác giả đã tạo ra [Nguyên tắc Dilbert](#the-dilbert-principle) .
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - Một bộ sách kinh điển về kỹ thuật phần mềm. [Luật của Brooks](#brooks-law) là chủ đề trung tâm của cuốn sách.
- [Nguyên tắc Peter - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Một truyện tranh khác về những thách thức của các tổ chức lớn hơn và quản lý con người, nguồn gốc của [Nguyên tắc Peter](#the-peter-principle) .

## Những nguồn thông tin trên mạng

Một số tài nguyên hữu ích và đọc.

- [CB Insights: 8 quy luật thúc đẩy thành công trong lĩnh vực công nghệ: Quy tắc 2 chiếc bánh Pizza của Amazon, Nguyên tắc 80/20, &amp; hơn thế nữa](https://www.cbinsights.com/research/report/tech-laws-success-failure) - một bản viết thú vị về một số quy luật có ảnh hưởng lớn trong lĩnh vực công nghệ.

## Sách điện tử PDF

Dự án có sẵn dưới dạng sách điện tử PDF, hãy [tải xuống sách điện tử PDF mới nhất bằng liên kết này](https://github.com/dwmkerr/hacker-laws/releases/latest/download/hacker-laws.pdf) hoặc kiểm tra [trang phát hành](https://github.com/dwmkerr/hacker-laws/releases) để biết các phiên bản cũ hơn.

Phiên bản sách điện tử mới được tạo tự động khi thẻ phiên bản mới được đẩy.

## Tệp âm thanh

Luật Hacker đã được giới thiệu trong [The Changelog](https://changelog.com/podcast/403) , bạn có thể xem tập Podcast bằng liên kết bên dưới:

<a href="https://changelog.com/podcast/403" target="_blank"></a>

## Bản dịch

Nhờ một số cộng tác viên tuyệt vời, Luật Hacker có sẵn ở một số ngôn ngữ. Vui lòng xem xét tài trợ cho người điều hành!

| Ngôn ngữ                                                                      | Người điều hành                                                                                             | Trạng thái                                                                                                                |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [🇮🇩 Bahasa Indonesia / Indonesia](./translations/pt-BR.md)                    | [arywidiantara](https://github.com/arywidiantara)                                                           | [](https://gitlocalize.com/repo/2513/id?utm_source=badge)                                                                 |
| [🇧🇷 Brasileiro / Brazil](./translations/pt-BR.md)                             | [Eugênio Moreira](https://github.com/eugenioamn) , [Leonardo Costa](https://github.com/leofc97)             | [](https://gitlocalize.com/repo/2513/pt-BR?utm_source=badge)                                                              |
| [🇨🇳 中文 / tiếng Trung](https://github.com/nusr/hacker-laws-zh)               | [Steve Xu](https://github.com/nusr)                                                                         | Hoàn thành một phần                                                                                                       |
| [🇩🇪 Deutsch / tiếng Đức](./translations/de.md)                                | [Vikto](https://github.com/viktodergunov)                                                                   | [](https://gitlocalize.com/repo/2513/de?utm_source=badge)                                                                 |
| [🇫🇷 Français / tiếng Pháp](./translations/fr.md)                              | [Kevin Bockelandt](https://github.com/KevinBockelandt)                                                      | [](https://gitlocalize.com/repo/2513/fr?utm_source=badge)                                                                 |
| [🇬🇷 ελληνικά / tiếng Hy Lạp](./translations/el.md)                            | [Panagiotis Gourgaris](https://github.com/0gap)                                                             | [](https://gitlocalize.com/repo/2513/el?utm_source=badge)                                                                 |
| [🇮🇹 Italiano / Ý](https://github.com/csparpa/hacker-laws-it)                  | [Claudio Sparpaglione](https://github.com/csparpa)                                                          | Hoàn thành một phần                                                                                                       |
| [🇯🇵 JP 日本語 / tiếng Nhật](./translations/jp.md)                             | [Fumikazu Fujiwara](https://github.com/freddiefujiwara)                                                     | [](https://gitlocalize.com/repo/2513/ja?utm_source=badge)                                                                 |
| [🇰🇷 한국어 / tiếng Hàn Quốc](https://github.com/codeanddonuts/hacker-laws-kr) | [Bánh vòng](https://github.com/codeanddonuts)                                                               | Hoàn thành một phần                                                                                                       |
| [🇱🇻 Latviešu Valoda / Latvia](./translations/lv.md)                           | [Arturs Jansons](https://github.com/iegik)                                                                  | [](https://gitlocalize.com/repo/2513/lv?utm_source=badge)                                                                 |
| [🇷🇺 Русская версия / tiếng Nga](https://github.com/solarrust/hacker-laws)     | [Alena Batitskaya](https://github.com/solarrust)                                                            | Hoàn thành một phần                                                                                                       |
| [🇪🇸 Castellano / tiếng Tây Ban Nha](./translations/es-ES.md)                  | [Manuel Rubio](https://github.com/manuel-rubio) ( [Nhà tài trợ](https://github.com/sponsors/manuel-rubio) ) | Hoàn thành một phần                                                                                                       |
| [🇹🇷 Türkçe / tiếng Thổ Nhĩ Kỳ](https://github.com/umutphp/hacker-laws-tr)     | [Umut Işık](https://github.com/umutphp)                                                                     | [](https://gitlocalize.com/repo/2513/tr?utm_source=badge)                                                                 |
| [🇺🇦 українська мова / tiếng Ukraina](./translations/uk.md)                    | [Nazar](https://github.com/troyane) , [Helga Lastivka](https://github.com/HelgaLastivka)                    | [](https://gitlocalize.com/repo/2513/uk?utm_source=badge)                                                                 |
| [🇻🇳 Tiếng Việt / Vietnamese](./translations/vu.md)                            | [Nguyên](https://github.com/truonghoangnguyen), [Trương Hoàng](https://github.com/truonghoangnguyen) | [![gitlocalized ](https://gitlocalize.com/repo/2513/vi/badge.svg)](https://gitlocalize.com/repo/2513/vi?utm_source=badge) |

Nếu bạn muốn cập nhật bản dịch, chỉ cần [mở một yêu cầu kéo](https://github.com/dwmkerr/hacker-laws/pulls) . Nếu bạn muốn thêm ngôn ngữ mới, hãy đăng nhập vào [GitLocalize](https://gitlocalize.com/) để tạo tài khoản, sau đó mở một vấn đề yêu cầu quản lý ngôn ngữ và tôi sẽ thêm bạn vào dự án! Nó cũng sẽ rất hữu ích nếu bạn có thể mở một yêu cầu kéo để cập nhật bảng ở trên và liên kết ở đầu tệp.

## Các dự án liên quan

- [Mẹo trong ngày](https://tips.darekkay.com/html/hacker-laws-en.html) - Nhận luật / nguyên tắc của hacker hàng ngày.
- [Luật Hacker CLI](https://github.com/umutphp/hacker-laws-cli) - Liệt kê, xem và xem các luật ngẫu nhiên từ thiết bị đầu cuối!
- [Hành động của Luật Hacker](https://github.com/marketplace/actions/hacker-laws-action) - Thêm Luật Hacker ngẫu nhiên vào một yêu cầu kéo như một món quà nhỏ cho người đóng góp, cảm ơn [Umut Işık](https://github.com/umutphp)

## Đóng góp

Hãy đóng góp! [Nêu vấn đề](https://github.com/dwmkerr/hacker-laws/issues/new) nếu bạn muốn đề xuất bổ sung hoặc thay đổi hoặc [Mở yêu cầu kéo](https://github.com/dwmkerr/hacker-laws/compare) để đề xuất các thay đổi của riêng bạn.

Hãy nhớ đọc [Nguyên tắc đóng góp](./.github/contributing.md) để biết các yêu cầu về văn bản, văn phong, v.v. Vui lòng lưu ý [Quy tắc Ứng xử](./.github/CODE_OF_CONDUCT.md) khi tham gia vào các cuộc thảo luận về dự án.

## SẼ LÀM

Chào! Nếu bạn đến đây, bạn đã nhấp vào một liên kết đến một chủ đề mà tôi chưa viết lên, xin lỗi về điều này - đây là công việc đang được tiến hành!

Vui lòng nêu [vấn đề](https://github.com/dwmkerr/hacker-laws/issues) yêu cầu thêm chi tiết hoặc [Mở yêu cầu kéo](https://github.com/dwmkerr/hacker-laws/pulls) để gửi định nghĩa đề xuất của bạn về chủ đề.
