#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مشروع الأعداد الأولية المتقدم
===============================

هذا المشروع يطبق خوارزمية جديدة ومتطورة لإيجاد الأعداد الأولية باستخدام:
1. جدول ضرب الأعداد الفردية (تحسين 50% في المساحة)
2. الغربال المقطعي (Segmented Sieve) لحل مشكلة الذاكرة
3. نظام تخزين مستمر للحالة والنتائج
4. صيغة رياضية أنيقة باستخدام نظرية المجموعات

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import zipfile
import xml.etree.ElementTree as ET
import re

def extract_text_from_docx(docx_path):
    """استخراج النص من ملف Word docx"""
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_file:
            # قراءة محتوى XML
            xml_content = zip_file.read('word/document.xml')

            # تحويل إلى نص وإزالة العلامات
            text = xml_content.decode('utf-8')

            # استخراج النص من علامات w:t
            pattern = r'<w:t[^>]*>([^<]*)</w:t>'
            matches = re.findall(pattern, text)

            # دمج النصوص
            extracted_text = ''.join(matches)

            # تنظيف النص
            extracted_text = re.sub(r'\s+', ' ', extracted_text)
            extracted_text = extracted_text.strip()

            return extracted_text

    except Exception as e:
        return f"خطأ في استخراج النص: {str(e)}"

if __name__ == "__main__":
    # استخراج النص من الملف
    docx_file = "فكرة اعداد اولية.docx"
    text = extract_text_from_docx(docx_file)

    print("محتوى الملف:")
    print("=" * 50)
    print(text)
    print("=" * 50)

    # حفظ النص في ملف
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("تم حفظ النص في ملف extracted_text.txt")
