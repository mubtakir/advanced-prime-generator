#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف التكوين لمشروع الأعداد الأولية المتقدم
==========================================

هذا الملف يحتوي على جميع الإعدادات والثوابت المستخدمة في المشروع

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import os

# ===============================
# إعدادات الملفات والمجلدات
# ===============================

# أسماء الملفات الأساسية
STATE_FILE = "prime_state.json"
PRIMES_FILE = "primes_list.txt"
LOG_FILE = "prime_log.txt"

# مجلدات النتائج والتقارير
RESULTS_DIR = "results"
REPORTS_DIR = "reports"
EXPORTS_DIR = "exports"

# إنشاء المجلدات إذا لم تكن موجودة
def ensure_directories():
    """إنشاء المجلدات المطلوبة إذا لم تكن موجودة"""
    for directory in [RESULTS_DIR, REPORTS_DIR, EXPORTS_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)

# ===============================
# إعدادات الخوارزمية
# ===============================

# حجم المقطع الافتراضي للغربال المقطعي
DEFAULT_SEGMENT_SIZE = 32768

# الحد الأقصى للاستخدام المباشر لطريقة جدول الضرب
MATRIX_METHOD_LIMIT = 100000

# الحد الأدنى للتشغيل
MIN_LIMIT = 2

# الحد الأقصى الموصى به للتشغيل السريع
RECOMMENDED_QUICK_LIMIT = 1000000

# ===============================
# إعدادات الأداء
# ===============================

# حجم الذاكرة المفضل (بالبايت)
PREFERRED_MEMORY_SIZE = 64 * 1024 * 1024  # 64 MB

# عدد الخيوط للمعالجة المتوازية (مستقبلي)
MAX_THREADS = 4

# فترة حفظ الحالة (بالثواني)
STATE_SAVE_INTERVAL = 60

# ===============================
# إعدادات التسجيل
# ===============================

# مستوى التسجيل
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR

# تنسيق الطابع الزمني
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

# الحد الأقصى لحجم ملف السجل (بالبايت)
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10 MB

# عدد ملفات السجل المحفوظة
LOG_BACKUP_COUNT = 5

# ===============================
# إعدادات التصدير
# ===============================

# صيغ التصدير المدعومة
SUPPORTED_EXPORT_FORMATS = ["txt", "csv", "json", "xml"]

# ترميز الملفات
FILE_ENCODING = "utf-8"

# فاصل CSV
CSV_DELIMITER = ","

# مسافة بادئة JSON
JSON_INDENT = 2

# ===============================
# إعدادات الاختبارات
# ===============================

# الحدود المستخدمة في الاختبارات
TEST_LIMITS = [10, 50, 100, 500, 1000, 5000]

# الأعداد الأولية المعروفة للتحقق
KNOWN_PRIMES_100 = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]

# عدد الأعداد الأولية المتوقع لحدود مختلفة
EXPECTED_PRIME_COUNTS = {
    10: 4,
    100: 25,
    1000: 168,
    10000: 1229,
    100000: 9592,
    1000000: 78498
}

# ===============================
# إعدادات الرسوم البيانية
# ===============================

# حجم الرسم البياني الافتراضي
DEFAULT_FIGURE_SIZE = (12, 8)

# دقة الصورة (DPI)
FIGURE_DPI = 300

# ألوان الرسوم البيانية
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff7f0e',
    'info': '#17a2b8'
}

# ===============================
# إعدادات واجهة المستخدم
# ===============================

# عرض الخط في الطرفية
TERMINAL_WIDTH = 80

# رموز الحالة
STATUS_SYMBOLS = {
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    'running': '🔄',
    'completed': '🎉'
}

# ===============================
# رسائل النظام
# ===============================

MESSAGES = {
    'welcome': "مرحباً بك في مولد الأعداد الأولية المتقدم!",
    'first_run': "هذه هي المرة الأولى لتشغيل البرنامج.",
    'continuing': "استكمال من حيث توقف البرنامج سابقاً.",
    'completed': "تم إنجاز العملية بنجاح!",
    'interrupted': "تم إيقاف البرنامج بواسطة المستخدم.",
    'error': "حدث خطأ غير متوقع.",
    'invalid_input': "إدخال غير صالح. يرجى المحاولة مرة أخرى.",
    'file_saved': "تم حفظ الملف بنجاح.",
    'state_loaded': "تم تحميل الحالة السابقة.",
    'state_saved': "تم حفظ الحالة الحالية."
}

# ===============================
# إعدادات التحقق من الصحة
# ===============================

# الحد الأدنى والأقصى للمدخلات
INPUT_LIMITS = {
    'min_limit': 2,
    'max_limit': 10**12,  # تريليون
    'recommended_limit': 10**6  # مليون
}

# أنماط التحقق من صحة المدخلات
VALIDATION_PATTERNS = {
    'positive_integer': r'^[1-9]\d*$',
    'file_name': r'^[a-zA-Z0-9_\-\.]+$'
}

# ===============================
# إعدادات التحسين
# ===============================

# عتبات التحسين
OPTIMIZATION_THRESHOLDS = {
    'use_segmented_sieve': 100000,
    'enable_parallel_processing': 1000000,
    'use_memory_mapping': 10000000
}

# إعدادات الذاكرة
MEMORY_SETTINGS = {
    'segment_size_small': 16384,    # 16 KB
    'segment_size_medium': 65536,   # 64 KB
    'segment_size_large': 262144,   # 256 KB
    'max_memory_usage': 0.8         # 80% من الذاكرة المتاحة
}

# ===============================
# دوال المساعدة
# ===============================

def get_optimal_segment_size(limit):
    """حساب حجم المقطع الأمثل بناءً على الحد"""
    if limit < 10000:
        return MEMORY_SETTINGS['segment_size_small']
    elif limit < 100000:
        return MEMORY_SETTINGS['segment_size_medium']
    else:
        return MEMORY_SETTINGS['segment_size_large']

def should_use_matrix_method(limit):
    """تحديد ما إذا كان يجب استخدام طريقة جدول الضرب"""
    return limit <= MATRIX_METHOD_LIMIT

def should_use_segmented_sieve(limit):
    """تحديد ما إذا كان يجب استخدام الغربال المقطعي"""
    return limit > OPTIMIZATION_THRESHOLDS['use_segmented_sieve']

def get_progress_interval(limit):
    """حساب فترة عرض التقدم بناءً على الحد"""
    if limit < 1000:
        return 100
    elif limit < 10000:
        return 1000
    elif limit < 100000:
        return 10000
    else:
        return 100000

# ===============================
# معلومات المشروع
# ===============================

PROJECT_INFO = {
    'name': 'مولد الأعداد الأولية المتقدم',
    'name_en': 'Advanced Prime Numbers Generator',
    'version': '1.0.0',
    'author': 'مبتكر',
    'author_en': 'Mubtakir',
    'email': 'mubtakir@example.com',
    'description': 'خوارزمية متطورة لإيجاد الأعداد الأولية باستخدام جدول ضرب الأعداد الفردية',
    'description_en': 'Advanced algorithm for finding prime numbers using odd numbers multiplication table',
    'license': 'MIT',
    'url': 'https://github.com/mubtakir/advanced-prime-generator'
}

# تهيئة المجلدات عند استيراد الملف
if __name__ != "__main__":
    ensure_directories()
