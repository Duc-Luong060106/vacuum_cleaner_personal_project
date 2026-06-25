# Vacuum Cleaner + CSP Viet Nam map + Caro with Adversarial search - Personal Project 

---

## Mục tiêu
- Mô phỏng hoạt động của **Robot hút bụi** trong không gian dạng lưới, áp dụng các thuật toán tìm kiếm trong không gian trạng thái để tìm ra đường đi giúp Robot dọn dẹp sạch rác, với phần **Giao diện đồ họa trực quan (GUI)** được xây dựng bằng `Tkinter`.
- Áp dụng các thuật toán trong nhóm **Tìm kiếm thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP)** cho việc tô màu 34 tỉnh/thành Việt Nam, với kết quả tìm được trực quan hóa bởi thư viện `Matplotlib`.
- Tạo ra **Agent chơi cờ Caro** sử dụng các thuật toán trong nhóm **Tìm kiếm đối kháng (Adversarial search)**, với phần **Giao diện (GUI)** triển khai bằng `Tkinter`.

---

## Cấu trúc dự án

### 1. Vacuum Cleaner
Dự án được tổ chức theo cấu trúc module để dễ dàng quản lý và mở rộng. Với 3 phần chính:
* **algorithms:** Thư mục chứa các thuật toán.
* **utils:** Thư mục chứa các class và hàm hỗ trợ.
* file **gui.ipynb**: Giao diện người dùng (Tkinter chạy trên Jupyter) và chứa hàm chạy chương trình.
```
vacuum_cleaner_personal_project/
│
├── algorithms/                
│   ├── __init__.py
│   ├── bfs.py                  # Breadth-First Search
│   ├── dfs.py                  # Depth-First Search
│   ├── ids.py                  # Iterative Deepening Search
│   ├── ucs.py                  # Uniform Cost Search
│   ├── greedy_search.py        # Greedy Search
│   ├── a_star.py               # A* Search
│   ├── ida_star.py             # Iterative Deepening A* 
│   ├── hill_climbing.py        # Các biến thể Hill Climbing (Simple, Steepest, Stochastic, Random restart)
│   ├── local_beam_search.py    # Local Beam Search
│   ├── simulated_annealing.py  # Simulated Annealing Search
│   ├── sensorless_search.py    # Sensorless Search (Tìm kiếm trong môi trường không nhìn thấy)
│   ├── partial_obs_search.py   # Partially Observable State Space Search (Tìm kiếm trong môi trường nhìn thấy 1 phần)
│   └── and_or_graph_search.py  # And-Or Search
│
├── utils/                      
│   ├── __init__.py
│   ├── helpers.py              # Sinh trạng thái con, kiểm tra trạng thái, ...
│   └── node.py                 # Định nghĩa cấu trúc Node cho không gian trạng thái, bao gồm state, parent, action, path_cost
│                                 dễ dàng tính toán và truy vấn chuỗi hành động
│
└── gui.ipynb                   # Giao diện điều khiển
```

### 2. CSP Viet Nam map 
Xây dựng các hàm thuật toán và file **show_csp_vietnam_map.ipynb** đọc đọc dataset và trực quan hóa. 
```
csp_vietnam_map/
│
├── backtracking.py                # Backtracking Search
├── forward_checking.py            # Forward Checking Search
├── ac_3.py                        # Ac-3
├── min_conflicts.py               # Min-conflicts Search
├── helper.py                      # Định nghĩa class Csp cho bài toán tìm kiếm thỏa mãn ràng buộc
├── show_csp_vietnam_map.ipynb     # Chạy các thuật toán và trực quan hóa kết quả bằng `Matplotlib`
└── vn_provices.geojson            # Dataset Vị trí địa lý các tỉnh Việt Nam phục vụ cho trực quan hóa 
```

### 3. Caro with Adversarial search
Xây dựng các hàm thuật toán và file **caro_gui.py** xây dựng giao diện GUI. 
```
adversarial_search_caro/
│
├── minimax_search.py        # MiniMax Search
├── alpha_beta_search.py     # Alpha-Beta Search
├── expectimax_search.py     # Expectimax Search
├── helper.py                # Helper định nghĩa các hàm sử dụng chung: get_next_turn (Lượt tiếp theo X/O),
│                               generate_next_states (Sinh ra các trạng thái (nước đi) tiếp theo),
│                               is_terminal, evaluate_if_terminal (Kiểm tra trò chơi kết thúc và tính điểm)
└── caro_gui.py              # Chương trình chính chứa giao diện và nơi bắt đầu chương trình
```

---

## Môi trường sử dụng 

* **Python:** Phiên bản `3.13.x`.
* **IDE:** VS Code có cài đặt Jupyter Notebook.
* **Tkinter:** Thư viện giao diện (được tích hợp sẵn với Python).
* **Matplotlib:** Thư viện vẽ biểu đồ và trực quan hóa dữ liệu. Dự án sử dụng Matplotlib phiên bản `3.10.3`.

---

## Hướng dẫn sử dụng

### Bước 1: Tải dự án về máy

```bash
git clone https://github.com/Duc-Luong060106/vacuum_cleaner_personal_project.git
cd vacuum_cleaner_personal_project
```

### Bước 2: Khởi động môi trường

Khởi động Jupyter Notebook:

```bash
jupyter notebook

```

### Bước 3: Chạy giao diện

**1. Vacuum Cleaner**  
Mở file `gui.ipynb` và run cell chứa phần gọi giao diện.
* Chọn thuật toán muốn thực thi.
* Chọn số hàng và số cột, ấn nút `TẠO` để random ma trận đầu vào. 
* Quan sát quá trình robot di chuyển và kết quả. 

**2. CSP Viet Nam map**  
```bash
cd csp_vietnam_map
```
Run các cell để đọc dữ liệu từ file `vn_provices.geojson` và xem kết quả bản đồ được tô màu ở phần Output cell.

**3. Caro with Adversarial search**  
```bash
cd adversarial_search_caro
python caro_gui.py
```
* Cửa sổ giao diện hiện lên, thực hiện chọn Loại thuật toán cho Agent và Nước đi đầu tiên (Agent/ Người chơi).
* Thực hiện chơi và xem phần Log Panel ghi lại chi tiết các nước đi (Nước đi, thời gian tìm kiếm, Đánh giá (dựa trên kết quả trả về của thuật toán).

---

## Các thuật toán đã triển khai

| Loại tìm kiếm | Thuật toán |Chú thích|
| --- | --- | --- |
| **1. Tìm kiếm mù (Uninformed search)** | BFS | Xây dựng 2 cách tiếp cận cho thuật toán BFS (Tìm kiếm bằng cách duyệt theo chiều rộng) cho Máy hút bụi |
|  | DFS | Xây dựng 2 cách tiếp cận cho thuật toán DFS (Tìm kiếm bằng cách duyệt theo chiều sâu) cho Máy hút bụi |
|  | IDS | Xây dựng 2 cách tiếp cận cho thuật toán IDS (Tìm kiếm bằng cách duyệt rộng theo từng mức độ sâu) cho Máy hút bụi |
|  | UCS | Xây dựng thuật toán UCS  cho Máy hút bụi với g(n) = số ô bụi còn lại (có tích lũy qua từng bước) |
| **2. Tìm kiếm có thông tin (Informed search)** | Greedy Search | Xây dựng thuật toán Greedy search cho Máy hút bụi với h(n) = số ô bụi còn lại |
|  | A* | Xây dựng thuật toán A* cho Máy hút bụi với g(n) = g(parent) + số ô còn bụi, h(n) bằng khoảng cách manhattan BÉ NHẤT từ robot đến bụi |
|  | IDA* | Xây dựng thuật toán IDA* dựa trên A* nhưng duyệt theo từng mức của f(n) |
| **3. Tìm kiếm cục bộ (Local Search)** | Hill Climbing | Xây dựng nhóm thuật toán Hill Climbing: Simple, Steepests Ascent, ‎Stochastic, Random Restart cho Máy hút bụi với h(n) = Khoảng cách manhattan xa tới rác |
|  | Local Beam Search | Xây dựng thuật toán Local Beam Search với k tùy ý |
|  | Simulated Annealing | Xây dựng thuật toán Mô phỏng luyện kim với T0 = 100, Tmin = 10 và alpha = 0.98 |
| **4. Tìm kiếm môi trường phức tạp (Complex Environment)** | Sensorless | Xây dựng Sensorless Search dựa trên thuật toán BFS cách tiếp cận 2 với đầu vào chỉ biết Goal |
|  | Partially Observable | Xây dựng Tìm kiếm trong môi trường nhìn thấy 1 phần như Sensorless nhưng đầu vào có 1 phần của Start và 1 phần của Goal |
|  | And-Or Search | Xây dựng thuật toán And-Or Search với các ô [x, x] như [1, 1], [2, 2], ... hành động Up hoặc Down sẽ gây ra 2 hành động lỗi là [Right, Left] và ngược lại nếu hành động là Right hoặc Left thì sẽ gây ra thêm 2 hành động lỗi là [Up, Down] |
| **5. Tìm kiếm thỏa mãn ràng buộc (CSP)** | Backtracking Search | Xây dựng thuật toán Backtracking cho tô màu bản đồ Việt Nam, thử và quay lui đến khi các biến được gán giá trị thỏa ràng buộc |
|  | Forward Checking Search | Xây dựng thuật toán Forward Checking cho tô màu bản đồ Việt Nam, là biến thể của Backtrack  bằng việc giảm domain của các biến chưa gán nhãn |
|  | AC-3 | Xây dựng thuật toán Ac-3 giúp thu hẹp domain dựa vào ràng buộc cung và dùng Domain kết quả thu được cho tô màu bản đồ Việt Nam bằng thuật toán Forward Checking|
|  | Min-conflicts | Xây dựng thuật toán Min-conflicts cho tô màu bản đồ Việt Nam, với max_steps được truyền vào |
| **6. Tìm kiếm đối kháng (Adversarial search)** | Minimax Search | Xây dựng thuật toán Minimax Search cho cờ Caro |
|  | Alpha-Beta Search | Xây dựng thuật toán Alpha-Beta Search cho cờ Caro |
|  | ExpectiMax Search | Xây dựng thuật toán ExpectiMax Search cho cờ Caro |

---

## Kết quả thu được  

**1. Vacuum Cleaner**  



---

## Tác giả

* **Họ và tên:** Phạm Trần Đức Lương
* **MSSV:** 24110281
* **Môn học:** Trí tuệ nhân tạo (ARIN330585)
* **GitHub Profile:** [@ducluong](https://github.com/Duc-Luong060106)
