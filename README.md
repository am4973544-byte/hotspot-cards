# برنامج تكة Hotspot لسطح المكتب

هذا البرنامج هو نسخة سطح المكتب من مولد كروت ميكروتك.

## المميزات:
- يعمل كبرنامج مستقل على نظام Windows.
- يدعم الاتصال المباشر بأجهزة ميكروتك عبر API.
- إمكانية طباعة الكروت وحفظها كملفات PDF أو Excel.

## طريقة التشغيل:
1. قم بتثبيت متطلبات بايثون:
   ```bash
   pip install PySide6 PySide6-WebEngine
   ```
2. قم بتشغيل البرنامج:
   ```bash
   python main.py
   ```

## ملاحظة لمستخدمي ميكروتك:
تأكد من تفعيل خدمة API في الميكروتك:
- لخدمة REST API (Port 80/443): `/ip service set www-ssl disabled=no`
- لخدمة Native API (Port 8728): `/ip service set api disabled=no`
