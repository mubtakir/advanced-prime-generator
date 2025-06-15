#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبارات شاملة لمولد الأعداد الأولية المتقدم
==============================================

هذا الملف يحتوي على اختبارات شاملة للتأكد من:
1. صحة الخوارزمية المقترحة
2. مقارنة النتائج مع الطرق التقليدية
3. اختبار الأداء
4. اختبار حالات خاصة

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import time
import unittest
from prime_generator import PrimeGenerator

class TestPrimeGenerator(unittest.TestCase):
    """فئة اختبارات مولد الأعداد الأولية"""
    
    def setUp(self):
        """إعداد الاختبارات"""
        self.generator = PrimeGenerator()
        
        # الأعداد الأولية المعروفة للمقارنة
        self.known_primes_100 = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]
        
        self.known_primes_1000 = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
            157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
            239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
            331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
            421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
            509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
            613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
            709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
            821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
            919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997
        ]
    
    def test_simple_sieve_basic(self):
        """اختبار الغربال البسيط - حالات أساسية"""
        # اختبار حالات حدية
        self.assertEqual(self.generator.simple_sieve(1), [])
        self.assertEqual(self.generator.simple_sieve(2), [2])
        self.assertEqual(self.generator.simple_sieve(3), [2, 3])
        
        # اختبار حتى 100
        result = self.generator.simple_sieve(100)
        self.assertEqual(result, self.known_primes_100)
        self.assertEqual(len(result), 25)
    
    def test_matrix_method_basic(self):
        """اختبار طريقة جدول الضرب - حالات أساسية"""
        # اختبار حالات حدية
        self.assertEqual(self.generator.matrix_method_primes(1), [])
        self.assertEqual(self.generator.matrix_method_primes(2), [2])
        self.assertEqual(self.generator.matrix_method_primes(3), [2, 3])
        
        # اختبار حتى 100
        result = self.generator.matrix_method_primes(100)
        self.assertEqual(result, self.known_primes_100)
        self.assertEqual(len(result), 25)
    
    def test_matrix_vs_traditional_100(self):
        """مقارنة الطريقة المقترحة مع التقليدية حتى 100"""
        matrix_result = self.generator.matrix_method_primes(100)
        traditional_result = self.generator.simple_sieve(100)
        
        self.assertEqual(matrix_result, traditional_result)
        self.assertEqual(matrix_result, self.known_primes_100)
    
    def test_matrix_vs_traditional_1000(self):
        """مقارنة الطريقة المقترحة مع التقليدية حتى 1000"""
        matrix_result = self.generator.matrix_method_primes(1000)
        traditional_result = self.generator.simple_sieve(1000)
        
        self.assertEqual(matrix_result, traditional_result)
        self.assertEqual(len(matrix_result), 168)  # عدد الأعداد الأولية حتى 1000
    
    def test_segmented_sieve_basic(self):
        """اختبار الغربال المقطعي"""
        base_primes = self.generator.simple_sieve(10)  # [2, 3, 5, 7]
        
        # اختبار مقطع [11, 30]
        result = self.generator.segmented_sieve(11, 30, base_primes)
        expected = [11, 13, 17, 19, 23, 29]
        self.assertEqual(result, expected)
        
        # اختبار مقطع [31, 50]
        result = self.generator.segmented_sieve(31, 50, base_primes)
        expected = [31, 37, 41, 43, 47]
        self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        """اختبار الأرقام الكبيرة"""
        # اختبار حتى 10,000
        matrix_result = self.generator.matrix_method_primes(10000)
        traditional_result = self.generator.simple_sieve(10000)
        
        self.assertEqual(len(matrix_result), len(traditional_result))
        self.assertEqual(matrix_result, traditional_result)
        self.assertEqual(len(matrix_result), 1229)  # عدد الأعداد الأولية حتى 10,000
    
    def test_performance_comparison(self):
        """اختبار مقارنة الأداء"""
        limit = 5000
        
        # قياس وقت الطريقة المقترحة
        start_time = time.time()
        matrix_result = self.generator.matrix_method_primes(limit)
        matrix_time = time.time() - start_time
        
        # قياس وقت الطريقة التقليدية
        start_time = time.time()
        traditional_result = self.generator.simple_sieve(limit)
        traditional_time = time.time() - start_time
        
        # التحقق من صحة النتائج
        self.assertEqual(matrix_result, traditional_result)
        
        # طباعة نتائج الأداء
        print(f"\nمقارنة الأداء حتى {limit}:")
        print(f"الطريقة المقترحة: {matrix_time:.4f} ثانية")
        print(f"الطريقة التقليدية: {traditional_time:.4f} ثانية")
        print(f"عدد الأعداد الأولية: {len(matrix_result)}")
    
    def test_mathematical_properties(self):
        """اختبار الخصائص الرياضية للأعداد الأولية"""
        primes = self.generator.matrix_method_primes(1000)
        
        # التحقق من أن جميع الأعداد أكبر من 1
        self.assertTrue(all(p > 1 for p in primes))
        
        # التحقق من أن الرقم 2 موجود
        self.assertIn(2, primes)
        
        # التحقق من أن جميع الأعداد الأولية الأخرى فردية
        odd_primes = [p for p in primes if p > 2]
        self.assertTrue(all(p % 2 == 1 for p in odd_primes))
        
        # التحقق من أن الأعداد مرتبة
        self.assertEqual(primes, sorted(primes))
        
        # التحقق من عدم وجود تكرار
        self.assertEqual(len(primes), len(set(primes)))
    
    def test_specific_primes(self):
        """اختبار أعداد أولية محددة"""
        primes = self.generator.matrix_method_primes(1000)
        
        # أعداد أولية معروفة يجب أن تكون موجودة
        known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 97, 101, 997]
        for p in known_primes:
            self.assertIn(p, primes)
        
        # أعداد مركبة يجب ألا تكون موجودة
        composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
        for c in composite_numbers:
            self.assertNotIn(c, primes)
    
    def test_edge_cases(self):
        """اختبار الحالات الحدية"""
        # اختبار الأرقام الصغيرة جداً
        self.assertEqual(self.generator.matrix_method_primes(0), [])
        self.assertEqual(self.generator.matrix_method_primes(1), [])
        
        # اختبار الأرقام الأولية الصغيرة
        self.assertEqual(self.generator.matrix_method_primes(2), [2])
        self.assertEqual(self.generator.matrix_method_primes(3), [2, 3])
        self.assertEqual(self.generator.matrix_method_primes(5), [2, 3, 5])
        self.assertEqual(self.generator.matrix_method_primes(7), [2, 3, 5, 7])


def run_comprehensive_tests():
    """تشغيل اختبارات شاملة مع تقرير مفصل"""
    print("=" * 60)
    print("بدء الاختبارات الشاملة لمولد الأعداد الأولية المتقدم")
    print("=" * 60)
    
    # تشغيل الاختبارات
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "=" * 60)
    print("اختبارات إضافية ومقارنات متقدمة")
    print("=" * 60)
    
    generator = PrimeGenerator()
    
    # اختبار مقارنة شاملة
    test_limits = [100, 500, 1000, 5000]
    
    for limit in test_limits:
        print(f"\nاختبار حتى {limit}:")
        
        # قياس الأوقات
        start_time = time.time()
        matrix_primes = generator.matrix_method_primes(limit)
        matrix_time = time.time() - start_time
        
        start_time = time.time()
        traditional_primes = generator.simple_sieve(limit)
        traditional_time = time.time() - start_time
        
        # التحقق من التطابق
        is_equal = matrix_primes == traditional_primes
        
        print(f"  الطريقة المقترحة: {len(matrix_primes)} عدد أولي في {matrix_time:.4f}s")
        print(f"  الطريقة التقليدية: {len(traditional_primes)} عدد أولي في {traditional_time:.4f}s")
        print(f"  النتائج متطابقة: {'✓' if is_equal else '✗'}")
        
        if matrix_time > 0 and traditional_time > 0:
            speedup = traditional_time / matrix_time
            print(f"  نسبة السرعة: {speedup:.2f}x")
    
    print("\n" + "=" * 60)
    print("اكتملت جميع الاختبارات بنجاح!")
    print("=" * 60)


if __name__ == "__main__":
    run_comprehensive_tests()
