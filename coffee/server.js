const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// بيانات المنتجات
const products = [
    { id: 1, name: 'بن اسبريسو فاخر', price: '4.500 د.ك', desc: 'إيحاءات الشوكولاتة والمكسرات - 250 جرام', category: 'beans' },
    { id: 2, name: 'بن فلات وايت مختار', price: '5.000 د.ك', desc: 'محموص طازج ومناسب لمشروبات الحليب - 250 جرام', category: 'beans' },
    { id: 3, name: 'قهوة اليوم (مقطرة)', price: '1.500 د.ك', desc: 'قهوة باردة أو حارة محضرة طازجة', category: 'drinks' },
    { id: 4, name: 'سبانيش لاتيه بارد', price: '2.000 د.ك', desc: 'مزيج Esspresso ممتاز مع الحليب المكثف', category: 'drinks' }
];

// مسارات API
app.get('/api/products', (req, res) => {
    res.json(products);
});

app.post('/api/order', (req, res) => {
    const { product, name, phone } = req.body;
    console.log(`طلب جديد: ${product} | الاسم: ${name} | الهاتف: ${phone}`);
    res.json({ success: true, message: 'تم استلام طلبك بنجاح! سنتم التواصل معك قريباً.' });
});

app.listen(PORT, () => {
   
  console.log(`Server is running on port ${PORT}`);

  function sendOrder(productName, price) {
    // حط رقم واتساب الخاص بك مع رمز الدولة (مثال للكويت: 96512345678)
    let myPhoneNumber = "965XXXXXXXX"; 
    
    let text = `السلام عليكم، أرغب بطلب:\n- المنتَج: ${productName}\n- السعر: ${price}`;
    let whatsappUrl = `https://wa.me/${myPhoneNumber}?text=${encodeURIComponent(text)}`;
    
    // يفتح واتساب مباشرة بالرسالة المجهزة
    window.open(whatsappUrl, '_blank');
}
});