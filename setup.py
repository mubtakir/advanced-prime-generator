#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
إعداد تثبيت مشروع الأعداد الأولية المتقدم
==========================================

ملف الإعداد لتثبيت المشروع كحزمة Python

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

from setuptools import setup, find_packages
import os

# قراءة ملف README
def read_readme():
    """قراءة ملف README للوصف الطويل"""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "مولد الأعداد الأولية المتقدم - خوارزمية مبتكرة لإيجاد الأعداد الأولية"

# قراءة متطلبات المشروع
def read_requirements():
    """قراءة ملف requirements.txt"""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # تصفية التعليقات والأسطر الفارغة
            requirements = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    requirements.append(line)
            return requirements
    except FileNotFoundError:
        return []

setup(
    # معلومات أساسية
    name="advanced-prime-generator",
    version="1.0.0",
    author="مبتكر",
    author_email="mubtakir@example.com",
    description="خوارزمية متطورة لإيجاد الأعداد الأولية باستخدام جدول ضرب الأعداد الفردية",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mubtakir/advanced-prime-generator",
    
    # تصنيف المشروع
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    
    # الكلمات المفتاحية
    keywords="prime numbers, mathematics, algorithms, sieve, number theory, الأعداد الأولية",
    
    # الحزم والملفات
    packages=find_packages(),
    py_modules=["prime_generator", "examples", "test_prime_generator"],
    
    # متطلبات Python
    python_requires=">=3.7",
    
    # المتطلبات
    install_requires=[
        # المكتبات الأساسية مدمجة في Python
    ],
    
    # المتطلبات الاختيارية
    extras_require={
        "visualization": ["matplotlib>=3.5.0"],
        "analysis": ["numpy>=1.21.0", "pandas>=1.3.0"],
        "performance": ["numba>=0.56.0"],
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "all": [
            "matplotlib>=3.5.0",
            "numpy>=1.21.0", 
            "pandas>=1.3.0",
            "numba>=0.56.0",
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ]
    },
    
    # نقاط الدخول للأوامر
    entry_points={
        "console_scripts": [
            "prime-generator=prime_generator:main",
            "prime-examples=examples:main",
            "prime-test=test_prime_generator:run_comprehensive_tests",
        ],
    },
    
    # ملفات البيانات
    package_data={
        "": ["*.md", "*.txt", "*.json"],
    },
    
    # تضمين ملفات إضافية
    include_package_data=True,
    
    # معلومات إضافية
    project_urls={
        "Bug Reports": "https://github.com/mubtakir/advanced-prime-generator/issues",
        "Source": "https://github.com/mubtakir/advanced-prime-generator",
        "Documentation": "https://advanced-prime-generator.readthedocs.io/",
    },
    
    # الترخيص
    license="MIT",
    
    # منصات مدعومة
    platforms=["any"],
    
    # معلومات إضافية للتوزيع
    zip_safe=False,
)

# معلومات ما بعد التثبيت
print("""
🎉 تم تثبيت مولد الأعداد الأولية المتقدم بنجاح!

الأوامر المتاحة:
  prime-generator    - تشغيل المولد الرئيسي
  prime-examples     - تشغيل الأمثلة التطبيقية
  prime-test         - تشغيل الاختبارات الشاملة

للبدء:
  python -m prime_generator

للمساعدة:
  python -m prime_generator --help

الوثائق: https://advanced-prime-generator.readthedocs.io/
""")
