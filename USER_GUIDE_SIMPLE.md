# دليل الاستخدام البسيط

# Simple User Guide

## مولد الأعداد الأولية المتقدم

### للرياضيين المبتدئين في البرمجة

---

## 🎯 ما هذا البرنامج؟

هذا البرنامج يجد الأعداد الأولية (مثل 2, 3, 5, 7, 11, 13...) باستخدام طريقة جديدة ومتطورة.

**مثال**: إذا طلبت منه الأعداد الأولية حتى 20، سيعطيك: 2, 3, 5, 7, 11, 13, 17, 19

---

## 📋 ما تحتاجه قبل البدء

### 1. تأكد من وجود Python على جهازك

**في Windows:**

1. اضغط `Windows + R`
2. اكتب `cmd` واضغط Enter
3. اكتب `python --version` واضغط Enter
4. إذا ظهر رقم إصدار (مثل Python 3.9.0) فأنت جاهز ✅
5. إذا ظهرت رسالة خطأ، حمّل Python من: https://python.org

**في Mac:**

1. اضغط `Cmd + Space`
2. اكتب `Terminal` واضغط Enter
3. اكتب `python3 --version` واضغط Enter
4. إذا ظهر رقم إصدار فأنت جاهز ✅

**في Linux:**

1. افتح Terminal
2. اكتب `python3 --version` واضغط Enter
3. إذا لم يكن موجود، اكتب: `sudo apt install python3`

### 2. حمّل ملفات البرنامج

1. احفظ جميع ملفات البرنامج في مجلد واحد
2. تأكد أن الملفات التالية موجودة:
   - `prime_generator.py`
   - `run.py`
   - `test_prime_generator.py`

---

## 🚀 كيفية تشغيل البرنامج

### الطريقة الأولى: التشغيل البسيط (الأسهل)

1. **افتح سطر الأوامر:**

   - Windows: اضغط `Windows + R`، اكتب `cmd`
   - Mac: اضغط `Cmd + Space`، اكتب `Terminal`
   - Linux: افتح Terminal

2. **انتقل إلى مجلد البرنامج:**

   ```
   cd المسار_إلى_مجلد_البرنامج
   ```

   **مثال في Windows:**

   ```
   cd C:\Users\اسمك\Desktop\prime-generator
   ```

   **مثال في Mac/Linux:**

   ```
   cd /Users/اسمك/Desktop/prime-generator
   ```

3. **شغّل البرنامج:**

   ```
   python run.py --quick 1000
   ```

   هذا سيجد جميع الأعداد الأولية حتى 1000

### الطريقة الثانية: التشغيل التفاعلي

1. **شغّل البرنامج الرئيسي:**

   ```
   python prime_generator.py
   ```

2. **اتبع التعليمات على الشاشة:**
   - سيسألك عن الرقم الذي تريد البحث حتى إليه
   - اكتب الرقم واضغط Enter
   - انتظر حتى ينتهي البرنامج

---

## 📖 أمثلة عملية خطوة بخطوة

### مثال 1: إيجاد الأعداد الأولية حتى 100

1. افتح سطر الأوامر
2. انتقل إلى مجلد البرنامج
3. اكتب:
   ```
   python run.py --quick 100
   ```
4. ستحصل على النتيجة:
   ```
   ✅ تم العثور على 25 عدد أولي
   📁 النتائج محفوظة في: primes_list.txt
   🔢 الأعداد الأولية: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
   ```

### مثال 2: إيجاد الأعداد الأولية حتى 10,000

1. اكتب:
   ```
   python run.py --quick 10000
   ```
2. انتظر قليلاً (قد يستغرق ثوانٍ قليلة)
3. ستحصل على 1,229 عدد أولي

### مثال 3: التشغيل التفاعلي

1. اكتب:
   ```
   python prime_generator.py
   ```
2. ستظهر رسالة:
   ```
   مرحباً! هذه هي المرة الأولى لتشغيل البرنامج.
   يرجى إدخال الحد الأقصى للبحث عن الأعداد الأولية:
   ```
3. اكتب الرقم الذي تريده (مثل 500) واضغط Enter
4. انتظر النتيجة

---

## 📁 أين تجد النتائج؟

بعد تشغيل البرنامج، ستجد ملفات جديدة في نفس المجلد:

### 1. ملف النتائج: `primes_list.txt`

- يحتوي على قائمة بجميع الأعداد الأولية
- كل رقم في سطر منفصل
- يمكن فتحه بأي محرر نصوص

**مثال على المحتوى:**

```
2
3
5
7
11
13
17
19
23
29
```

### 2. ملف الحالة: `prime_state.json`

- يحفظ آخر رقم تم فحصه
- يساعد البرنامج على الاستكمال من حيث توقف

### 3. ملف السجل: `prime_log.txt`

- يسجل جميع العمليات التي قام بها البرنامج
- مفيد لمعرفة ما حدث في حالة وجود مشاكل

---

## 🔄 الاستكمال من حيث توقفت

**الميزة الذكية**: البرنامج يتذكر آخر رقم فحصه!

### مثال:

1. **المرة الأولى**: شغّل البرنامج حتى 1000
2. **المرة الثانية**: شغّل البرنامج مرة أخرى
3. **سيقول لك**: "تم حساب الأعداد الأولية سابقاً حتى الرقم 1000"
4. **اكتب رقم أكبر**: مثل 5000
5. **سيكمل من 1001 إلى 5000** بدلاً من البدء من الصفر

هذا يوفر الوقت كثيراً!

---

## 🧪 كيفية اختبار البرنامج

للتأكد أن البرنامج يعمل بشكل صحيح:

```
python run.py --test
```

سيقوم بفحص نفسه ويخبرك إذا كان كل شيء يعمل بشكل صحيح.

---

## 📊 عرض الإحصائيات

لمعرفة ما أنجزه البرنامج حتى الآن:

```
python run.py --stats
```

ستحصل على معلومات مثل:

- آخر رقم تم فحصه
- عدد الأعداد الأولية المكتشفة
- حجم ملف النتائج

---

## 🎨 أمثلة متقدمة (اختيارية)

إذا كنت تريد رؤية أمثلة أكثر تعقيداً:

```
python run.py --examples
```

سيعرض لك:

- مقارنة بين الطرق المختلفة
- إحصائيات مفصلة
- رسوم بيانية (إذا كان لديك matplotlib)

---

## ❓ حل المشاكل الشائعة

### المشكلة: "python is not recognized"

**الحل**:

- تأكد من تثبيت Python
- أعد تشغيل سطر الأوامر
- جرب `python3` بدلاً من `python`

### المشكلة: "No such file or directory"

**الحل**:

- تأكد أنك في المجلد الصحيح
- استخدم `ls` (Mac/Linux) أو `dir` (Windows) لرؤية الملفات
- تأكد أن ملف `prime_generator.py` موجود

### المشكلة: البرنامج بطيء جداً

**الحل**:

- ابدأ برقم صغير (مثل 1000)
- للأرقام الكبيرة (أكثر من 100,000) انتظر أكثر
- أغلق البرامج الأخرى لتوفير الذاكرة

### المشكلة: رسائل خطأ غريبة

**الحل**:

- شغّل الاختبار: `python run.py --test`
- تأكد أن جميع الملفات موجودة
- أعد تحميل الملفات إذا لزم الأمر

---

## 💡 نصائح للاستخدام الأمثل

### 1. ابدأ بأرقام صغيرة

- جرب 100 أولاً
- ثم 1000
- ثم 10,000
- وهكذا...

### 2. احفظ النتائج

- انسخ ملف `primes_list.txt` إلى مكان آمن
- يمكنك فتحه في Excel أو أي برنامج جداول

### 3. استخدم الاستكمال

- لا تبدأ من الصفر في كل مرة
- دع البرنامج يكمل من حيث توقف

### 4. راقب الذاكرة

- للأرقام الكبيرة جداً (مليون فأكثر)
- تأكد أن لديك ذاكرة كافية
- أغلق البرامج الأخرى

---

## 📞 المساعدة والدعم

### إذا احتجت مساعدة:

1. **شغّل المساعدة**:

   ```
   python run.py --help
   ```

2. **اقرأ ملف السجل**:

   - افتح `prime_log.txt`
   - ابحث عن رسائل الخطأ

3. **جرب الاختبار**:

   ```
   python run.py --test
   ```

4. **ابدأ من جديد**:
   - احذف `prime_state.json`
   - شغّل البرنامج مرة أخرى

---

## 🎉 مبروك!

الآن أنت تعرف كيفية استخدام مولد الأعداد الأولية المتقدم!

**تذكر**:

- ابدأ بأرقام صغيرة
- استخدم `python run.py --quick رقم` للتشغيل السريع
- النتائج محفوظة في `primes_list.txt`
- البرنامج يتذكر آخر رقم فحصه

**استمتع باكتشاف الأعداد الأولية!** 🔢✨

---

## 📋 ملخص الأوامر السريعة

### للنسخ واللصق المباشر:

```bash
# التشغيل السريع - الأعداد الأولية حتى 1000
python run.py --quick 1000

# التشغيل التفاعلي
python prime_generator.py

# اختبار البرنامج
python run.py --test

# عرض الإحصائيات
python run.py --stats

# عرض المساعدة
python run.py --help

# أمثلة متقدمة
python run.py --examples
```

### أمثلة بأرقام مختلفة:

```bash
# أرقام صغيرة (سريع جداً)
python run.py --quick 100
python run.py --quick 500

# أرقام متوسطة (ثوانٍ قليلة)
python run.py --quick 5000
python run.py --quick 10000

# أرقام كبيرة (دقائق قليلة)
python run.py --quick 100000
python run.py --quick 1000000
```

---

## 🎯 خطوات البداية السريعة (في دقيقتين)

### الخطوة 1: تحقق من Python

```bash
python --version
```

إذا ظهر رقم إصدار ← أنت جاهز ✅
إذا ظهر خطأ ← حمّل Python من python.org

### الخطوة 2: انتقل للمجلد

```bash
cd مسار_مجلد_البرنامج
```

### الخطوة 3: شغّل البرنامج

```bash
python run.py --quick 100
```

### الخطوة 4: اعرض النتائج

افتح ملف `primes_list.txt` في أي محرر نصوص

**تهانينا! 🎉 أنت الآن تستخدم مولد الأعداد الأولية المتقدم!**
