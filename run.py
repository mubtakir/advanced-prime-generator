#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف التشغيل السريع لمشروع الأعداد الأولية المتقدم
==============================================

هذا الملف يوفر طرق سريعة لتشغيل المشروع بدون تفاعل

الاستخدام:
  python run.py --help                    # عرض المساعدة
  python run.py --quick 1000              # تشغيل سريع حتى 1000
  python run.py --test                    # تشغيل الاختبارات
  python run.py --examples                # تشغيل الأمثلة
  python run.py --compare 5000            # مقارنة الطرق حتى 5000
  python run.py --stats                   # عرض الإحصائيات

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import sys
import argparse
from prime_generator import PrimeGenerator
import test_prime_generator
import examples

def quick_run(limit):
    """تشغيل سريع لإيجاد الأعداد الأولية"""
    print(f"🚀 تشغيل سريع: إيجاد الأعداد الأولية حتى {limit}")
    print("=" * 50)
    
    generator = PrimeGenerator()
    
    if limit <= 100000:
        primes = generator.matrix_method_primes(limit)
        generator.append_primes_to_file(primes)
        generator.save_state(limit)
        
        print(f"✅ تم العثور على {len(primes)} عدد أولي")
        print(f"📁 النتائج محفوظة في: primes_list.txt")
        
        # عرض آخر 10 أعداد أولية
        if len(primes) >= 10:
            print(f"🔢 آخر 10 أعداد أولية: {primes[-10:]}")
        else:
            print(f"🔢 جميع الأعداد الأولية: {primes}")
    else:
        print("⚠️  للأرقام الكبيرة، استخدم البرنامج الرئيسي: python prime_generator.py")

def run_tests():
    """تشغيل الاختبارات"""
    print("🧪 تشغيل الاختبارات الشاملة")
    print("=" * 50)
    test_prime_generator.run_comprehensive_tests()

def run_examples():
    """تشغيل الأمثلة"""
    print("📚 تشغيل الأمثلة التطبيقية")
    print("=" * 50)
    examples.main()

def compare_methods(limit):
    """مقارنة الطرق المختلفة"""
    print(f"⚖️  مقارنة الطرق حتى {limit}")
    print("=" * 50)
    
    generator = PrimeGenerator()
    generator.compare_methods(limit)

def show_stats():
    """عرض الإحصائيات"""
    print("📊 إحصائيات المشروع")
    print("=" * 50)
    
    generator = PrimeGenerator()
    generator.display_statistics()

def show_help():
    """عرض المساعدة المفصلة"""
    help_text = """
🔢 مولد الأعداد الأولية المتقدم - دليل الاستخدام
=====================================================

الأوامر المتاحة:

1. التشغيل السريع:
   python run.py --quick <رقم>
   مثال: python run.py --quick 1000

2. تشغيل الاختبارات:
   python run.py --test

3. تشغيل الأمثلة:
   python run.py --examples

4. مقارنة الطرق:
   python run.py --compare <رقم>
   مثال: python run.py --compare 5000

5. عرض الإحصائيات:
   python run.py --stats

6. التشغيل التفاعلي الكامل:
   python prime_generator.py

الميزات الرئيسية:
- خوارزمية مبتكرة لإيجاد الأعداد الأولية
- توفير 50% من المساحة
- نظام تخزين مستمر
- مقارنات أداء شاملة
- اختبارات تلقائية

للمزيد من المعلومات، راجع README.md
"""
    print(help_text)

def main():
    """الدالة الرئيسية"""
    parser = argparse.ArgumentParser(
        description="مولد الأعداد الأولية المتقدم - تشغيل سريع",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  python run.py --quick 1000      # إيجاد الأعداد الأولية حتى 1000
  python run.py --test            # تشغيل الاختبارات
  python run.py --examples        # تشغيل الأمثلة
  python run.py --compare 5000    # مقارنة الطرق حتى 5000
  python run.py --stats           # عرض الإحصائيات
        """
    )
    
    parser.add_argument(
        '--quick', '-q',
        type=int,
        metavar='LIMIT',
        help='تشغيل سريع لإيجاد الأعداد الأولية حتى الحد المحدد'
    )
    
    parser.add_argument(
        '--test', '-t',
        action='store_true',
        help='تشغيل الاختبارات الشاملة'
    )
    
    parser.add_argument(
        '--examples', '-e',
        action='store_true',
        help='تشغيل الأمثلة التطبيقية'
    )
    
    parser.add_argument(
        '--compare', '-c',
        type=int,
        metavar='LIMIT',
        help='مقارنة الطرق المختلفة حتى الحد المحدد'
    )
    
    parser.add_argument(
        '--stats', '-s',
        action='store_true',
        help='عرض إحصائيات المشروع'
    )
    
    # إذا لم يتم تمرير أي معاملات، عرض المساعدة
    if len(sys.argv) == 1:
        show_help()
        return
    
    args = parser.parse_args()
    
    try:
        if args.quick:
            quick_run(args.quick)
        elif args.test:
            run_tests()
        elif args.examples:
            run_examples()
        elif args.compare:
            compare_methods(args.compare)
        elif args.stats:
            show_stats()
        else:
            show_help()
            
    except KeyboardInterrupt:
        print("\n⏹️  تم إيقاف البرنامج بواسطة المستخدم")
    except Exception as e:
        print(f"❌ خطأ: {e}")
        print("💡 للمساعدة: python run.py --help")

if __name__ == "__main__":
    main()
