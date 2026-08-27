let currentUser = null;
let cart = [];
let products = [
    { id: 1, name: "محصول كولومبيا - 250g", price: 4.5, img: "https://via.placeholder.com/150" },
    { id: 2, name: "محصول إثيوبيا - 250g", price: 5.0, img: "https://via.placeholder.com/150" }
];

// 🔗 رابط الـ Webhook الخاص بقناتك
const DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1393661139486216263/fRneK4Jz729aU4_1q91gI34qfR_N5QO3k_zE2oA4qR1-xX9Y_8_wZ";

function loginUser() {
    const email = document.getElementById('loginEmail').value;
    const pass = document.getElementById('loginPass').value;

    if (!email || !pass) return alert("يرجى إدخال البيانات كاملة");

    if (email === "admin@lora.com" && pass === "admin123") {
        currentUser = { email, role: "admin" };
        document.getElementById('adminDashboardSection').style.display = "block";
    } else {
        currentUser = { email, role: "user" };
        document.getElementById('adminDashboardSection').style.display = "none";
    }

    document.getElementById('loginSection').style.display = "none";
    document.getElementById('storeSection').style.display = "block";
    document.getElementById('userStatusText').innerText = currentUser.email;

    renderProducts();
}

function logoutUser() {
    currentUser = null;
    cart = [];
    document.getElementById('loginSection').style.display = "block";
    document.getElementById('storeSection').style.display = "none";
    document.getElementById('adminDashboardSection').style.display = "none";
    document.getElementById('userStatusText').innerText = "غير مسجل";
    document.getElementById('cartCount').innerText = "0";
}

function renderProducts() {
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = "";
    products.forEach(p => {
        grid.innerHTML += `
            <div style="background: #0f121d; padding: 10px; border-radius: 8px; text-align: center;">
                <img src="${p.img}" style="width: 100%; border-radius: 5px;">
                <h4>${p.name}</h4>
                <p style="color: #ffd700;">${p.price.toFixed(3)} د.ك</p>
                <button onclick="addToCart(${p.id})">إضافة للسلة 🛒</button>
            </div>
        `;
    });
}

function addToCart(id) {
    const item = products.find(p => p.id === id);
    if (item) {
        cart.push(item);
        document.getElementById('cartCount').innerText = cart.length;
        alert(`تمت إضافة ${item.name} للسلة!`);
    }
}

function addProductByAdmin() {
    const name = document.getElementById('adminProdName').value;
    const price = parseFloat(document.getElementById('adminProdPrice').value);
    const img = document.getElementById('adminProdImg').value || "https://via.placeholder.com/150";

    if (!name || isNaN(price)) return alert("يرجى إدخال اسم وسعر صحيح");

    products.push({ id: Date.now(), name, price, img });
    renderProducts();
    alert("تم إضافة المنتج بنجاح!");
}

function addPromoCodeByAdmin() {
    const code = document.getElementById('adminCode').value;
    const discount = document.getElementById('adminDiscount').value;
    if (!code || !discount) return alert("يرجى إدخال كود الخصم والنسبة");
    alert(`تم حفظ كود الخصم: ${code} بنسبة ${discount}%`);
}

// 🚀 إرسال الطلب عبر الـ Webhook
async function checkoutOrder() {
    if (cart.length === 0) return alert("السلة فارغة!");

    let totalPrice = 0;
    let itemsList = "";

    cart.forEach((item, index) => {
        totalPrice += item.price;
        itemsList += `${index + 1}. **${item.name}** - ${item.price.toFixed(3)} د.ك\n`;
    });

    const payload = {
        username: "Lora Coffee",
        avatar_url: "https://cdn-icons-png.flaticon.com/512/2935/2935413.png",
        embeds: [{
            title: "☕ طلب جديد من موقع محمصة لورا",
            color: 3066993,
            fields: [
                { name: "👤 البريد الإلكتروني", value: currentUser ? currentUser.email : "زائر", inline: true },
                { name: "💰 المجموع الكلي", value: `${totalPrice.toFixed(3)} د.ك`, inline: true },
                { name: "📦 عناصر الطلب", value: itemsList }
            ],
            timestamp: new Date().toISOString()
        }]
    };

    try {
        const response = await fetch(DISCORD_WEBHOOK_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            alert("تم إرسال طلبك بنجاح! 🎉");
            cart = [];
            document.getElementById('cartCount').innerText = "0";
        } else {
            alert("حدث خطأ أثناء إرسال الطلب إلى الـ Webhook.");
        }
    } catch (err) {
        console.error(err);
        alert("تعذر الإرسال، تأكد من الاتصال بالإنترنت.");
    }
}