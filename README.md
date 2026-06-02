# Vacuum Cleaner - Personal Project 
Dự án cá nhân mô phỏng hoạt động của Robot hút bụi trong không gian dạng lưới, áp dụng các thuật toán tìm kiếm trong không gian trạng thái để tìm ra đường đi giúp Robot dọn dẹp sạch rác.   
Phần Giao diện đồ họa trực quan được xây dựng bằng Tkinter.

---

## Cấu trúc dự án

Dự án được tổ chức theo cấu trúc module để dễ dàng quản lý và mở rộng. Với 3 phần chính:
* **algorithms:** Thư mục chứa các thuật toán.
* **utils:** Thư mục chứa các class và hàm hỗ trợ.
* file **gui.ipynb**: Giao diện người dùng (Tkinter chạy trên Jupyter).
```
vacuum_cleaner_personal_project/
│
├── algorithms/                
│   ├── __init__.py
│   ├── a_star.py               # A* Search
│   ├── bfs.py                  # Breadth-First Search
│   ├── dfs.py                  # Depth-First Search
│   ├── greedy_search.py        # Greedy Search
│   ├── hill_climbing.py        # Các biến thể Hill Climbing (Simple, Steepest, Stochastic, Random restart)
│   ├── ida_star.py             # Iterative Deepening A* 
│   ├── ids.py                  # Iterative Deepening Search
│   └── ucs.py                  # Uniform Cost Search
│
├── utils/                      
│   ├── __init__.py
│   ├── helpers.py              # Sinh trạng thái con, kiểm tra trạng thái, ...
│   └── node.py                 # Định nghĩa cấu trúc Node cho không gian trạng thái, bao gồm state, parent, action, path_cost
│                                 dễ dàng tính toán và truy vấn chuỗi hành động
│
└── gui.ipynb                   # Giao diện điều khiển
```

---

## Môi trường sử dụng 

* **Python:** Phiên bản `3.13.x`.
* **Tkinter:** Thư viện giao diện (được tích hợp sẵn với Python).
* **IDE:** VS Code có cài đặt Jupyter Notebook.

---

## Hướng dẫn sử dụng

### Bước 1: Tải dự án về máy

```bash
git clone github.com/Duc-Luong060106/vacuum_cleaner_personal_project
cd vacuum_cleaner_personal_project
```

### Bước 2: Khởi động môi trường

Khởi động Jupyter Notebook:

```bash
jupyter notebook

```

### Bước 3: Chạy giao diện

Mở file `gui.ipynb` và run cell chứa phần gọi giao diện.

### Bước 4: Thao tác trên ứng dụng

* Chọn thuật toán muốn thực thi.
* Chọn số hàng và số cột, ấn nút `TẠO` để random ma trận đầu vào. 
* Quan sát quá trình robot di chuyển và kết quả. 

---

## Các thuật toán đã triển khai

| Loại tìm kiếm | Thuật toán |Chú thích|
| --- | --- | --- |
| **Tìm kiếm mù** | BFS |  |
|  | DFS |  |
|  | IDS |  |
|  | UCS |  |
| **Tìm kiếm có thông tin** | Greedy Search |  |
|  | A* |  |
|  | IDA* |  |
| **Tìm kiếm cục bộ** | Hill Climbing | |

---

## Tác giả

* **Họ và tên:** Phạm Trần Đức Lương
* **MSSV:** 24110281
* **Môn học:** Trí tuệ nhân tạo (ARIN330585)
* **GitHub Profile:** [@ducluong](https://github.com/Duc-Luong060106)
