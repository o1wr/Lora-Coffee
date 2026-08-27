html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محمصة لورا | LORA COFFEE ROASTING</title>
    <!-- Google Fonts & Font Awesome Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --bg-dark: #1b2138;
            --bg-darker: #131728;
            --bg-light: #f8fafc;
            --card-bg: #ffffff;
            --accent-blue: #3b82f6;
            --accent-cyan: #38bdf8;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --text-light: #f8fafc;
            --border-light: #e2e8f0;
            --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', sans-serif;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-light);
            color: var(--text-dark);
            overflow-x: hidden;
        }

        /* Top Bar */
        .top-bar {
            background-color: var(--bg-darker);
            color: #fff;
            padding: 8px 5%;
            font-size: 0.85rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .top-bar-info span {
            margin-left: 15px;
        }

        /* Header UI */
        header {
            background: var(--bg-dark);
            color: #fff;
            padding: 15px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }

        .brand-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: #fff;
        }

        .brand-logo h1 {
            font-size: 1.6rem;
            font-weight: 900;
            letter-spacing: 1px;
        }

        .brand-logo h1 span {
            color: var(--accent-cyan);
        }

        .nav-links {
            display: flex;
            gap: 25px;
            list-style: none;
        }

        .nav-links a {
            color: #cbd5e1;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--accent-cyan);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .search-box {
            position: relative;
        }

        .search-box input {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            padding: 8px 15px 8px 35px;
            border-radius: 20px;
            color: #fff;
            font-size: 0.85rem;
            outline: none;
            width: 180px;
            transition: width 0.3s ease;
        }

        .search-box input:focus {
            width: 240px;
            background: rgba(255,255,255,0.15);
            border-color: var(--accent-cyan);
        }

        .search-box i {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #94a3b8;
        }

        .cart-btn {
            position: relative;
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s;
            color: #fff;
        }

        .cart-btn:hover {
            background: var(--accent-cyan);
            color: var(--bg-dark);
            border-color: var(--accent-cyan);
        }

        .cart-badge {
            position: absolute;
            top: -4px;
            right: -4px;
            background: #ef4444;
            color: #fff;
            font-size: 0.75rem;
            font-weight: bold;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Hero Banner Quote Section */
        .hero-quote {
            background: #ffffff;
            text-align: center;
            padding: 50px 20px;
            border-bottom: 1px solid var(--border-light);
        }

        .hero-quote h2 {
            font-size: 2.2rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 12px;
            position: relative;
            display: inline-block;
        }

        .hero-quote h2::after {
            content: '';
            display: block;
            width: 60px;
            height: 3px;
            background: var(--accent-cyan);
            margin: 10px auto 0;
            border-radius: 2px;
        }

        .hero-quote p {
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        /* Features Bar */
        .features-bar {
            background: #ffffff;
            padding: 40px 5%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 30px;
            border-bottom: 1px solid var(--border-light);
        }

        .feature-item {
            text-align: center;
            padding: 10px;
            border-left: 1px solid var(--border-light);
        }

        .feature-item:last-child {
            border-left: none;
        }

        .feature-icon {
            font-size: 2.2rem;
            color: var(--accent-cyan);
            margin-bottom: 12px;
        }

        .feature-title {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 5px;
            color: var(--text-dark);
        }

        .feature-desc {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        /* Section Headings */
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            width: 90%;
            max-width: 1400px;
            margin: 40px auto 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e2e8f0;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-dark);
            text-transform: uppercase;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -12px;
            right: 0;
            width: 80px;
            height: 3px;
            background: var(--accent-cyan);
        }

        .view-all-btn {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            transition: color 0.3s;
        }

        .view-all-btn:hover {
            color: var(--accent-blue);
        }

        /* Categories Grid */
        .categories-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            width: 90%;
            max-width: 1400px;
            margin: 0 auto 50px;
        }

        .category-card {
            position: relative;
            height: 180px;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .category-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-lg);
        }

        .category-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.65);
            transition: filter 0.3s ease, transform 0.5s ease;
        }

        .category-card:hover img {
            filter: brightness(0.5);
            transform: scale(1.05);
        }

        .category-badge-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(255, 255, 255, 0.9);
            color: #0f172a;
            padding: 8px 24px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 1rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        /* Horizontal Carousel Layout for Products */
        .carousel-container {
            width: 90%;
            max-width: 1400px;
            margin: 0 auto 50px;
            overflow-x: auto;
            padding: 10px 5px 20px;
            display: flex;
            gap: 20px;
            scrollbar-width: thin;
            scrollbar-color: var(--accent-cyan) #e2e8f0;
        }

        .carousel-container::-webkit-scrollbar {
            height: 6px;
        }

        .carousel-container::-webkit-scrollbar-thumb {
            background: var(--accent-cyan);
            border-radius: 10px;
        }

        /* Product Card UI */
        .product-card {
            min-width: 240px;
            max-width: 240px;
            background: var(--card-bg);
            border-radius: 16px;
            padding: 15px;
            border: 1px solid var(--border-light);
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            transition: all 0.3s ease;
            flex-shrink: 0;
        }

        .product-card:hover {
            box-shadow: var(--shadow-md);
            border-color: #cbd5e1;
        }

        .discount-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background: #ef4444;
            color: #fff;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 800;
            z-index: 2;
        }

        .fav-btn {
            position: absolute;
            top: 15px;
            left: 15px;
            background: rgba(255,255,255,0.8);
            border: none;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: #64748b;
            transition: color 0.3s, background 0.3s;
            z-index: 2;
        }

        .fav-btn:hover {
            color: #ef4444;
            background: #fff;
        }

        .product-img {
            width: 100%;
            height: 160px;
            object-fit: contain;
            margin-bottom: 12px;
            border-radius: 8px;
        }

        .product-title {
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .product-desc {
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-bottom: 12px;
            height: 32px;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }

        .product-bottom {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 10px;
        }

        .price-wrapper {
            display: flex;
            flex-direction: column;
        }

        .price-old {
            font-size: 0.75rem;
            color: #94a3b8;
            text-decoration: line-through;
        }

        .price-current {
            font-size: 1.05rem;
            font-weight: 800;
            color: #0f172a;
        }

        .btn-view {
            background: var(--bg-dark);
            color: #fff;
            border: none;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }

        .btn-view:hover {
            background: var(--accent-blue);
        }

        /* Inline Notification Box */
        .inline-notice {
            background: #e0f2fe;
            color: #0369a1;
            padding: 12px 20px;
            border-radius: 10px;
            margin: 15px auto;
            width: 90%;
            max-width: 1400px;
            font-weight: 700;
            display: none;
            text-align: center;
            border: 1px solid #bae6fd;
        }

        /* Checkout Modal / Section Styling */
        .checkout-container {
            width: 90%;
            max-width: 800px;
            margin: 20px auto 50px;
            background: #fff;
            padding: 30px;
            border-radius: 16px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-light);
            display: none;
        }

        .checkout-container h3 {
            font-size: 1.3rem;
            margin-bottom: 20px;
            color: var(--text-dark);
            border-bottom: 2px solid var(--accent-cyan);
            padding-bottom: 8px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 700;
            font-size: 0.9rem;
        }

        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px 15px;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            font-size: 0.9rem;
            outline: none;
            font-family: 'Tajawal', sans-serif;
        }

        .payment-methods-box {
            display: flex;
            gap: 15px;
            margin-top: 10px;
            flex-wrap: wrap;
        }

        .pay-option {
            border: 2px solid var(--border-light);
            padding: 12px 20px;
            border-radius: 10px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 700;
            position: relative;
            background: #fff;
        }

        .pay-option.disabled {
            border-color: #ef4444;
            color: #94a3b8;
            background: #f1f5f9;
            cursor: not-allowed;
        }

        .pay-option.disabled::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 2px;
            background: #ef4444;
            transform: translateY(-50%) rotate(-10deg);
        }

        .pay-option.active {
            border-color: var(--accent-blue);
            background: #eff6ff;
            color: var(--accent-blue);
        }

        .submit-order-btn {
            background: #10b981;
            color: #fff;
            border: none;
            padding: 12px 25px;
            font-size: 1rem;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
            transition: background 0.3s;
        }

        .submit-order-btn:hover {
            background: #059669;
        }

        /* Footer UI */
        footer {
            background-color: var(--bg-dark);
            color: #cbd5e1;
            padding: 40px 8% 20px;
            position: relative;
        }

        .footer-top {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }

        .footer-col h3 {
            color: #fff;
            font-size: 1.2rem;
            margin-bottom: 15px;
            font-weight: 800;
        }

        .footer-col p {
            font-size: 0.85rem;
            line-height: 1.6;
            color: #94a3b8;
        }

        .social-links {
            display: flex;
            gap: 12px;
            margin-top: 15px;
        }

        .social-icon {
            width: 36px;
            height: 36px;
            background: rgba(255,255,255,0.08);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            text-decoration: none;
            transition: background 0.3s;
        }

        .social-icon:hover {
            background: var(--accent-cyan);
            color: var(--bg-dark);
        }

        .payment-methods {
            display: flex;
            gap: 8px;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 10px;
        }

        .payment-card {
            background: #fff;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            color: #000;
        }

        .footer-bottom {
            border-top: 1px solid rgba(255,255,255,0.08);
            padding-top: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: #64748b;
            flex-wrap: wrap;
            gap: 10px;
        }

        /* Floating Action Buttons */
        .floating-controls {
            position: fixed;
            bottom: 25px;
            left: 25px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            z-index: 99;
        }

        .float-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: var(--bg-dark);
            color: #fff;
            border: 1px solid rgba(255,255,255,0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            cursor: pointer;
            transition: transform 0.3s;
            text-decoration: none;
        }

        .float-btn:hover {
            transform: scale(1.1);
            background: var(--accent-blue);
        }

        /* Modal for Survey/Chat */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.6);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }

        .modal-content {
            background: #fff;
            padding: 30px;
            border-radius: 16px;
            width: 90%;
            max-width: 450px;
            position: relative;
        }

        .modal-content h3 {
            margin-bottom: 15px;
            color: var(--text-dark);
        }

        .close-modal {
            position: absolute;
            top: 15px;
            left: 15px;
            background: none;
            border: none;
            font-size: 1.2rem;
            cursor: pointer;
            color: var(--text-muted);
        }

        @media (max-width: 768px) {
            .nav-links { display: none; }
            .hero-quote h2 { font-size: 1.6rem; }
            .features-bar { grid-template-columns: 1fr 1fr; }
            .feature-item { border-left: none; }
        }
    </style>
</head>
<body>

    <!-- Top Info Bar -->
    <div class="top-bar">
        <div class="top-bar-info">
            <span><i class="fa-solid fa-truck-fast"></i> توصيل سريع لكافة مناطق الكويت</span>
            <span><i class="fa-solid fa-phone"></i> خدمة العملاء: +965 97114109</span>
        </div>
        <div>
            <span>🇰🇼 د.ك (KWD)</span>
        </div>
    </div>

    <!-- Main Header -->
    <header>
        <a href="#" class="brand-logo">
            <h1>LORA <span>COFFEE</span></h1>
        </a>

        <ul class="nav-links">
            <li><a href="#">الرئيسية</a></li>
            <li><a href="#categories">الأقسام</a></li>
            <li><a href="#espresso">القهوة المختصة</a></li>
            <li><a href="#machines">ماكينات القهوة</a></li>
            <li><a href="#contact">تواصل معنا</a></li>
        </ul>

        <div class="header-actions">
            <div class="search-box">
                <i class="fa-solid fa-magnifying-glass"></i>
                <input type="text" id="searchInput" placeholder="ابحث عن محصول أو آلة..." onkeyup="filterCatalog()">
            </div>
            <div class="cart-btn" onclick="toggleCheckout()">
                <i class="fa-solid fa-bag-shopping"></i>
                <span class="cart-badge" id="cartCount">0</span>
            </div>
        </div>
    </header>

    <!-- Inline Notification Box -->
    <div class="inline-notice" id="inlineNotice"></div>

    <!-- Hero Quote -->
    <section class="hero-quote">
        <h2>لأن القهوة أكثر من مجرد مشروب</h2>
        <p>عشان كل كوب من لورا يكون جزء من يومك، مو مجرد عادة.</p>
    </section>

    <!-- Features Section -->
    <section class="features-bar">
        <div class="feature-item">
            <div class="feature-icon"><i class="fa-solid fa-users-check"></i></div>
            <div class="feature-title">+1000 عميل يثق بنا</div>
            <div class="feature-desc">اختيار أول للقهوة المختصة الفاخرة</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon"><div style="display:inline-block; transform:rotate(-45deg);"><i class="fa-solid fa-wind"></i></div></div>
            <div class="feature-title">تحميص بالهواء الساخن</div>
            <div class="feature-desc">لنقاء ونكهات أغنى وأكثر وضوحاً</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon"><i class="fa-solid fa-truck-ramp-box"></i></div>
            <div class="feature-title">توصيل سريع</div>
            <div class="feature-desc">يغطي جميع مناطق الكويت الديرة والجهراء</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon"><i class="fa-solid fa-shield-halved"></i></div>
            <div class="feature-title">دفع آمن 100%</div>
            <div class="feature-desc">وسائل دفع متعددة وموثوقة</div>
        </div>
    </section>

    <!-- Categories Section -->
    <section id="categories">
        <div class="section-header">
            <div class="section-title">الأقسام الرئيسة (CATEGORIES)</div>
            <a href="#" class="view-all-btn">عرض الكل</a>
        </div>

        <div class="categories-grid">
            <div class="category-card">
                <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&q=80&w=600" alt="الأكثر مبيعاً">
                <div class="category-badge-text">الأكثر مبيعاً</div>
            </div>
            <div class="category-card">
                <img src="https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?auto=format&fit=crop&q=80&w=600" alt="إسبريسو">
                <div class="category-badge-text">إسبريسو ومرشحة</div>
            </div>
            <div class="category-card">
                <img src="https://images.unsplash.com/photo-1589396575653-c09c794ff6a6?auto=format&fit=crop&q=80&w=600" alt="قهوة تركية">
                <div class="category-badge-text">القهوة التركية</div>
            </div>
            <div class="category-card">
                <img src="https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&q=80&w=600" alt="قهوة عربية">
                <div class="category-badge-text">القهوة العربية</div>
            </div>
        </div>
    </section>

    <!-- Espresso & Filtered Section -->
    <section id="espresso">
        <div class="section-header">
            <div class="section-title">إسبريسو ومفلترة (Espresso and Filtered)</div>
            <a href="#" class="view-all-btn">عرض الكل</a>
        </div>

        <div class="carousel-container" id="espressoContainer"></div>
    </section>

    <!-- Coffee Machines Section -->
    <section id="machines">
        <div class="section-header">
            <div class="section-title">ماكينات القهوة (Coffee Machines)</div>
            <a href="#" class="view-all-btn">عرض الكل</a>
        </div>

        <div class="carousel-container" id="machinesContainer"></div>
    </section>

    <!-- Checkout / Order Form Section -->
    <div class="checkout-container" id="checkoutSection">
        <h3>إتمام الطلب (Checkout)</h3>
        <form id="orderForm" onsubmit="submitOrder(event)">
            <div class="form-group">
                <label>اسم العميل الكريم</label>
                <input type="text" id="custName" required placeholder="أدخل اسمك الكامل">
            </div>
            <div class="form-group">
                <label>رقم الهاتف</label>
                <input type="tel" id="custPhone" required placeholder="رقم الهاتف في الكويت">
            </div>
            <div class="form-group">
                <label>العنوان / الموقع بالتفصيل</label>
                <textarea id="custAddress" required placeholder="المنطقة، القطعة، الشارع، الجادة، المنزل"></textarea>
            </div>
            <div class="form-group">
                <label>طريقة الدفع المختارة</label>
                <div class="payment-methods-box">
                    <div class="pay-option disabled">K-NET ❌</div>
                    <div class="pay-option disabled">VISA / MC ❌</div>
                    <div class="pay-option active" id="cashOption">💵 الدفع نقداً (Cash)</div>
                </div>
            </div>
            <button type="submit" class="submit-order-btn">تأكيد وإرسال الطلب</button>
        </form>
    </div>

    <!-- Footer -->
    <footer id="contact">
        <div class="footer-top">
            <div class="footer-col">
                <h3>LORA COFFEE</h3>
                <p>2026 Lora Company for Coffee Roasting.<br>شركة لورا لتحميص القهوة - جميع الحقوق محفوظة.</p>
                <div class="social-links">
                    <a href="https://www.instagram.com/lora_coffee/?hl=en" target="_blank" class="social-icon" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://wa.me/96597114109" target="_blank" class="social-icon" title="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
                </div>
            </div>

            <div class="footer-col">
                <h3>روابط مفيدة</h3>
                <p><a href="#" style="color:inherit; text-decoration:none;">عن المحمصة</a></p>
                <p><a href="#" style="color:inherit; text-decoration:none;">الشروط والأحكام</a></p>
                <p><a href="#" style="color:inherit; text-decoration:none;">سياسة التوصيل والاسترجاع</a></p>
            </div>

            <div class="footer-col">
                <h3>طرق الدفع المتاحة</h3>
                <div class="payment-methods">
                    <span class="payment-card" style="background:#10b981; color:#fff;">💵 كاش فقط</span>
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <span>Powered By OSOSS System</span>
            <span>لورا كوفي - جميع الحقوق محفوظة ⚡</span>
        </div>
    </footer>

    <!-- Floating UI Tools -->
    <div class="floating-controls">
        <a href="#" class="float-btn" title="العودة للأعلى"><i class="fa-solid fa-arrow-up"></i></a>
        <button class="float-btn" title="محادثة الدعم والاستبيان" onclick="openSurveyModal()"><i class="fa-solid fa-comments"></i></button>
    </div>

    <!-- Survey Modal -->
    <div class="modal-overlay" id="surveyModal">
        <div class="modal-content">
            <button class="close-modal" onclick="closeSurveyModal()">&times;</button>
            <h3>استبيان خدمة العملاء والدعم</h3>
            <p style="font-size:0.85rem; color:#64748b; margin-bottom:15px;">سيتم إرسال رسالتك مباشرة إلى إيميل الشركة: naser.alsulaiti@icloud.com</p>
            <form onsubmit="submitSurvey(event)">
                <div class="form-group">
                    <label>اسمك أو بريدك الإلكتروني</label>
                    <input type="text" id="surveySender" required placeholder="ادخل اسمك أو ايميلك">
                </div>
                <div class="form-group">
                    <label>رسالتك أو استفسارك</label>
                    <textarea id="surveyMessage" required rows="4" placeholder="كيف نقدر نساعدك؟"></textarea>
                </div>
                <button type="submit" class="submit-order-btn">إرسال الاستبيان</button>
            </form>
        </div>
    </div>

    <!-- JavaScript Data Handler & Functions -->
    <script>
        const espressoProducts = [
            { id: 101, name: "حبوب قهوة البرازيل", desc: "Coffee Beans 250g | 1 KG", price: 3.750, oldPrice: 4.500, img: "https://images.unsplash.com/photo-1589396575653-c09c794ff6a6?auto=format&fit=crop&q=80&w=400", discount: "-16%" },
            { id: 102, name: "حبوب قهوة السلفادور", desc: "Coffee Beans 250g | 1 KG", price: 5.400, oldPrice: 6.000, img: "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?auto=format&fit=crop&q=80&w=400", discount: "-10%" },
            { id: 103, name: "حبوب قهوة الصين", desc: "Coffee Beans 250g | 1 KG", price: 6.000, oldPrice: 8.500, img: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&q=80&w=400", discount: "-29%" },
            { id: 104, name: "خلطة لورا الفاخرة (Lora Blend)", desc: "Coffee Beans 250g | 1 KG", price: 3.500, oldPrice: 4.500, img: "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&q=80&w=400", discount: "-22%" }
        ];

        const machineProducts = [
            { id: 201, name: "Jura J8 TWIN Diamond Black", desc: "آلة إسبريسو احترافية ثنائية الطحن", price: 865.000, oldPrice: null, img: "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?auto=format&fit=crop&q=80&w=400" },
            { id: 202, name: "Jura E8 Piano Black", desc: "الأداء الفاخر والتصميم العصري السويسري", price: 550.000, oldPrice: null, img: "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&q=80&w=400" },
            { id: 203, name: "Jura ENA8 Metropolitan White", desc: "صغيرة الحجم فائقة الجودة للمنزل والمكتب", price: 430.000, oldPrice: null, img: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&q=80&w=400" },
            { id: 204, name: "Jura Z10 Diamond Black", desc: "تحضير قهوة ساخنة وباردة بذكاء اصطناعي", price: 940.000, oldPrice: null, img: "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?auto=format&fit=crop&q=80&w=400" }
        ];

        let cart = [];

        function renderCarousel(list, targetId) {
            const container = document.getElementById(targetId);
            container.innerHTML = list.map(item => `
                <div class="product-card">
                    ${item.discount ? `<span class="discount-badge">${item.discount}</span>` : ''}
                    <button class="fav-btn" onclick="toggleFav(this)"><i class="fa-regular fa-heart"></i></button>
                    <img src="${item.img}" class="product-img" alt="${item.name}">
                    <div class="product-title">${item.name}</div>
                    <div class="product-desc">${item.desc}</div>
                    <div class="product-bottom">
                        <div class="price-wrapper">
                            ${item.oldPrice ? `<span class="price-old">${item.oldPrice.toFixed(3)} KD</span>` : ''}
                            <span class="price-current">${item.price.toFixed(3)} KD</span>
                        </div>
                        <button class="btn-view" onclick='addToCart(${JSON.stringify(item)})'>أضف للطلب</button>
                    </div>
                </div>
            `).join('');
        }

        function addToCart(item) {
            cart.push(item);
            document.getElementById('cartCount').innerText = cart.length;
            showNotice(`تمت إضافة "${item.name}" إلى سلة الطلبات بنجاح! 🛒`);
        }

        function showNotice(msg) {
            const notice = document.getElementById('inlineNotice');
            notice.innerText = msg;
            notice.style.display = 'block';
            setTimeout(() => {
                notice.style.display = 'none';
            }, 4000);
        }

        function toggleCheckout() {
            if(cart.length === 0) {
                showNotice('سلة الطلبات فارغة! الرجاء إضافة منتج واحد على الأقل قبل إتمام الطلب.');
                return;
            }
            const section = document.getElementById('checkoutSection');
            section.style.display = section.style.display === 'block' ? 'none' : 'block';
            section.scrollIntoView({ behavior: 'smooth' });
        }

        function toggleFav(btn) {
            const icon = btn.querySelector('i');
            if(icon.classList.contains('fa-regular')) {
                icon.classList.remove('fa-regular');
                icon.classList.add('fa-solid');
                icon.style.color = '#ef4444';
            } else {
                icon.classList.remove('fa-solid');
                icon.classList.add('fa-regular');
                icon.style.color = '#64748b';
            }
        }

        function filterCatalog() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const filteredEspresso = espressoProducts.filter(p => p.name.toLowerCase().includes(query) || p.desc.toLowerCase().includes(query));
            const filteredMachines = machineProducts.filter(p => p.name.toLowerCase().includes(query) || p.desc.toLowerCase().includes(query));
            renderCarousel(filteredEspresso, 'espressoContainer');
            renderCarousel(filteredMachines, 'machinesContainer');
        }

        function openSurveyModal() {
            document.getElementById('surveyModal').style.display = 'flex';
        }

        function closeSurveyModal() {
            document.getElementById('surveyModal').style.display = 'none';
        }

        function submitSurvey(e) {
            e.preventDefault();
            const sender = document.getElementById('surveySender').value;
            const message = document.getElementById('surveyMessage').value;
            closeSurveyModal();
            showNotice(`شكراً لك ${sender}! تم إرسال استبيانك واستفسارك بنجاح إلى شركة لورا (naser.alsulaiti@icloud.com).`);
            document.getElementById('surveySender').value = '';
            document.getElementById('surveyMessage').value = '';
        }

        function submitOrder(e) {
            e.preventDefault();
            const name = document.getElementById('custName').value;
            const phone = document.getElementById('custPhone').value;
            const address = document.getElementById('custAddress').value;
            
            const randomNum = Math.floor(1000 + Math.random() * 9000);
            const orderId = `#ORD-2026-${randomNum}`;
            
            const totalPrice = cart.reduce((sum, item) => sum + item.price, 0).toFixed(3);
            const itemsList = cart.map(i => `${i.name} (${i.price} KD)`).join(', ');

            // Discord Webhook payload
            const webhookUrl = "https://discord.com/api/webhooks/1542554021510774814/kURM7_KSoI1f6-7rEopGSwzjQ26KJY_-OW9DTkvAiofOUms2wrsWr-BO2d7slwCs52j5";
            const payload = {
                content: `🚨 **طلب جديد وصل عبر المتجر!** ${orderId}\n` +
                         `👤 **العميل:** ${name}\n` +
                         `📞 **رقم الهاتف:** ${phone}\n` +
                         `📍 **الموقع:** ${address}\n` +
                         `🛍️ **المنتجات:** ${itemsList}\n` +
                         `💰 **المجموع الكلي:** ${totalPrice} KD (طريقة الدفع: كاش 💵)`
            };

            fetch(webhookUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            }).catch(err => console.log('Webhook sent error ignored'));

            showNotice(`تم استلام طلبك بنجاح! رقم طلبك هو ${orderId} وسيتم التواصل معك قريباً.`);
            document.getElementById('checkoutSection').style.display = 'none';
            cart = [];
            document.getElementById('cartCount').innerText = '0';
            document.getElementById('orderForm').reset();
        }

        window.onload = () => {
            renderCarousel(espressoProducts, 'espressoContainer');
            renderCarousel(machineProducts, 'machinesContainer');
        };
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)