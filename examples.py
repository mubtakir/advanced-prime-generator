#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أمثلة تطبيقية لمولد الأعداد الأولية المتقدم
===========================================

هذا الملف يحتوي على أمثلة متنوعة لاستخدام المشروع:
1. أمثلة أساسية
2. مقارنات الأداء
3. تحليل إحصائي
4. تطبيقات عملية

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import time
import json
import matplotlib.pyplot as plt
from prime_generator import PrimeGenerator

def basic_usage_example():
    """مثال أساسي على الاستخدام"""
    print("=" * 50)
    print("مثال أساسي: إيجاد الأعداد الأولية حتى 100")
    print("=" * 50)
    
    generator = PrimeGenerator()
    
    # استخدام الطريقة المقترحة
    primes = generator.matrix_method_primes(100)
    
    print(f"الأعداد الأولية حتى 100:")
    print(primes)
    print(f"العدد الكلي: {len(primes)}")
    print(f"أكبر عدد أولي: {max(primes)}")
    print(f"أصغر عدد أولي: {min(primes)}")

def performance_comparison_example():
    """مثال على مقارنة الأداء"""
    print("\n" + "=" * 50)
    print("مقارنة الأداء بين الطرق المختلفة")
    print("=" * 50)
    
    generator = PrimeGenerator()
    test_limits = [100, 500, 1000, 5000, 10000]
    
    results = []
    
    for limit in test_limits:
        print(f"\nاختبار حتى {limit}:")
        
        # الطريقة المقترحة
        start_time = time.time()
        matrix_primes = generator.matrix_method_primes(limit)
        matrix_time = time.time() - start_time
        
        # الطريقة التقليدية
        start_time = time.time()
        traditional_primes = generator.simple_sieve(limit)
        traditional_time = time.time() - start_time
        
        # حفظ النتائج
        result = {
            'limit': limit,
            'count': len(matrix_primes),
            'matrix_time': matrix_time,
            'traditional_time': traditional_time,
            'speedup': traditional_time / matrix_time if matrix_time > 0 else 1
        }
        results.append(result)
        
        print(f"  عدد الأعداد الأولية: {result['count']}")
        print(f"  الطريقة المقترحة: {matrix_time:.4f} ثانية")
        print(f"  الطريقة التقليدية: {traditional_time:.4f} ثانية")
        print(f"  نسبة السرعة: {result['speedup']:.2f}x")
        print(f"  النتائج متطابقة: {'✓' if matrix_primes == traditional_primes else '✗'}")
    
    return results

def statistical_analysis_example():
    """مثال على التحليل الإحصائي"""
    print("\n" + "=" * 50)
    print("التحليل الإحصائي للأعداد الأولية")
    print("=" * 50)
    
    generator = PrimeGenerator()
    
    # تحليل توزيع الأعداد الأولية
    limits = [100, 500, 1000, 5000, 10000]
    
    for limit in limits:
        primes = generator.matrix_method_primes(limit)
        
        # حساب الإحصائيات
        count = len(primes)
        density = (count / limit) * 100
        
        # حساب الفجوات بين الأعداد الأولية
        gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
        avg_gap = sum(gaps) / len(gaps) if gaps else 0
        max_gap = max(gaps) if gaps else 0
        
        print(f"\nإحصائيات حتى {limit}:")
        print(f"  عدد الأعداد الأولية: {count}")
        print(f"  الكثافة: {density:.2f}%")
        print(f"  متوسط الفجوة: {avg_gap:.2f}")
        print(f"  أكبر فجوة: {max_gap}")

def twin_primes_example():
    """مثال على إيجاد الأعداد الأولية التوأم"""
    print("\n" + "=" * 50)
    print("البحث عن الأعداد الأولية التوأم")
    print("=" * 50)
    
    generator = PrimeGenerator()
    primes = generator.matrix_method_primes(1000)
    
    # البحث عن الأعداد الأولية التوأم (p, p+2)
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i+1]))
    
    print(f"الأعداد الأولية التوأم حتى 1000:")
    for twin in twin_primes:
        print(f"  {twin[0]}, {twin[1]}")
    
    print(f"\nإجمالي أزواج الأعداد الأولية التوأم: {len(twin_primes)}")

def prime_factorization_example():
    """مثال على تحليل الأعداد إلى عوامل أولية"""
    print("\n" + "=" * 50)
    print("تحليل الأعداد إلى عوامل أولية")
    print("=" * 50)
    
    generator = PrimeGenerator()
    primes = generator.matrix_method_primes(100)
    
    def factorize(n):
        """تحليل العدد n إلى عوامل أولية"""
        factors = []
        for p in primes:
            if p * p > n:
                break
            while n % p == 0:
                factors.append(p)
                n //= p
        if n > 1:
            factors.append(n)
        return factors
    
    # أمثلة على التحليل
    test_numbers = [12, 24, 36, 48, 60, 72, 84, 96]
    
    for num in test_numbers:
        factors = factorize(num)
        factors_str = " × ".join(map(str, factors))
        print(f"  {num} = {factors_str}")

def goldbach_conjecture_example():
    """مثال على اختبار حدسية جولدباخ"""
    print("\n" + "=" * 50)
    print("اختبار حدسية جولدباخ")
    print("=" * 50)
    
    generator = PrimeGenerator()
    primes = generator.matrix_method_primes(1000)
    primes_set = set(primes)
    
    print("حدسية جولدباخ: كل عدد زوجي أكبر من 2 يمكن كتابته كمجموع عددين أوليين")
    print("\nأمثلة:")
    
    # اختبار أعداد زوجية
    even_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    for even in even_numbers:
        found = False
        for p1 in primes:
            if p1 > even // 2:
                break
            p2 = even - p1
            if p2 in primes_set:
                print(f"  {even} = {p1} + {p2}")
                found = True
                break
        
        if not found:
            print(f"  {even}: لم يتم العثور على تمثيل!")

def save_results_example():
    """مثال على حفظ النتائج في ملفات مختلفة"""
    print("\n" + "=" * 50)
    print("حفظ النتائج في ملفات مختلفة")
    print("=" * 50)
    
    generator = PrimeGenerator()
    primes = generator.matrix_method_primes(1000)
    
    # حفظ في ملف JSON
    data = {
        'limit': 1000,
        'count': len(primes),
        'primes': primes,
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    with open('primes_1000.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    # حفظ في ملف CSV
    with open('primes_1000.csv', 'w', encoding='utf-8') as f:
        f.write('index,prime\n')
        for i, p in enumerate(primes, 1):
            f.write(f'{i},{p}\n')
    
    # حفظ في ملف نصي
    with open('primes_1000.txt', 'w', encoding='utf-8') as f:
        f.write(f'الأعداد الأولية حتى 1000\n')
        f.write(f'العدد الكلي: {len(primes)}\n')
        f.write(f'التاريخ: {time.strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        
        for i, p in enumerate(primes):
            f.write(f'{p}')
            if (i + 1) % 10 == 0:
                f.write('\n')
            else:
                f.write(', ')
    
    print("تم حفظ النتائج في:")
    print("  - primes_1000.json")
    print("  - primes_1000.csv") 
    print("  - primes_1000.txt")

def visualization_example():
    """مثال على رسم بياني للأعداد الأولية"""
    print("\n" + "=" * 50)
    print("رسم بياني لتوزيع الأعداد الأولية")
    print("=" * 50)
    
    try:
        generator = PrimeGenerator()
        
        # جمع البيانات
        limits = range(100, 1001, 100)
        counts = []
        densities = []
        
        for limit in limits:
            primes = generator.matrix_method_primes(limit)
            count = len(primes)
            density = (count / limit) * 100
            
            counts.append(count)
            densities.append(density)
        
        # رسم الرسوم البيانية
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # رسم عدد الأعداد الأولية
        ax1.plot(limits, counts, 'b-o', linewidth=2, markersize=6)
        ax1.set_xlabel('الحد الأقصى')
        ax1.set_ylabel('عدد الأعداد الأولية')
        ax1.set_title('نمو عدد الأعداد الأولية')
        ax1.grid(True, alpha=0.3)
        
        # رسم كثافة الأعداد الأولية
        ax2.plot(limits, densities, 'r-s', linewidth=2, markersize=6)
        ax2.set_xlabel('الحد الأقصى')
        ax2.set_ylabel('الكثافة (%)')
        ax2.set_title('كثافة الأعداد الأولية')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('prime_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("تم حفظ الرسم البياني في: prime_distribution.png")
        
    except ImportError:
        print("تحتاج إلى تثبيت matplotlib لعرض الرسوم البيانية:")
        print("pip install matplotlib")

def main():
    """تشغيل جميع الأمثلة"""
    print("🔢 أمثلة تطبيقية لمولد الأعداد الأولية المتقدم")
    print("=" * 60)
    
    # تشغيل الأمثلة
    basic_usage_example()
    performance_comparison_example()
    statistical_analysis_example()
    twin_primes_example()
    prime_factorization_example()
    goldbach_conjecture_example()
    save_results_example()
    visualization_example()
    
    print("\n" + "=" * 60)
    print("🎉 اكتملت جميع الأمثلة بنجاح!")
    print("=" * 60)

if __name__ == "__main__":
    main()
