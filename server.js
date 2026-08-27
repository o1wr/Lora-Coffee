const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// توجيه الخادم لقراءة الملفات من المجلد الحالي مباشرة
app.use(express.static(__dirname));

app.get('/api/status', (req, res) => {
    res.json({ status: "Online", message: "🚀 سيرفر محمصة لورا يعمل بنجاح!" });
});

app.listen(PORT, () => {
    console.log(`=================================`);
    console.log(`🚀 Server running on port ${PORT}`);
    console.log(`🌐 Local Link: http://localhost:${PORT}`);
    console.log(`=================================`);
});