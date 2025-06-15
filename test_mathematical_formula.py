#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اختبار مبسط للتعبير الرياضي المطور
"""

import math
from typing import Set

def sqrt_floor(n: int) -> int:
    """√̂(n) = ⌊√n⌋"""
    return int(math.sqrt(n))

def traditional_sieve(n: int) -> Set[int]:
    """الغربال التقليدي للمقارنة"""
    if n < 2:
        return set()
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for p in range(2, sqrt_floor(n) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    
    return {i for i in range(2, n + 1) if sieve[i]}

def advanced_mathematical_formula(n: int, delta: int = 1000) -> Set[int]:
    """
    تطبيق الصيغة الرياضية المطورة:
    𝒫_n = 𝒫_{√̂(n)} ∪̇ ⋃_{i=1}^{⌈(n-√̂(n))/δ⌉} Φ(S_i, B_n)
    """
    print(f"🧮 تطبيق الصيغة المطورة حتى {n}")
    
    # الخطوة 1: √̂(n)
    sqrt_n = sqrt_floor(n)
    print(f"📐 √̂({n}) = {sqrt_n}")
    
    # الخطوة 2: B_n = الأعداد الأولية الأساسية
    base_primes = traditional_sieve(sqrt_n)
    print(f"🔢 الأعداد الأولية الأساسية: {sorted(list(base_primes))}")
    
    # الخطوة 3: تهيئة النتيجة
    result = base_primes.copy()
    
    # الخطوة 4: عدد المقاطع
    k_n = math.ceil((n - sqrt_n) / delta)
    print(f"📊 عدد المقاطع: {k_n}")
    
    # الخطوة 5: معالجة المقاطع
    for i in range(1, k_n + 1):
        # تعريف المقطع
        start = sqrt_n + (i - 1) * delta + 1
        end = min(sqrt_n + i * delta, n)
        
        if start > n:
            break
            
        print(f"🔍 المقطع {i}: [{start}, {end}]")
        
        # الأعداد الفردية في المقطع
        odd_candidates = set()
        for x in range(start, end + 1):
            if x % 2 == 1:  # فردي فقط
                odd_candidates.add(x)
        
        print(f"   📋 المرشحين الفرديين: {len(odd_candidates)}")
        
        # دالة الغربلة Φ(S_i, B_n)
        primes_in_segment = set()
        for candidate in odd_candidates:
            is_prime = True
            for p in base_primes:
                if candidate != p and candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes_in_segment.add(candidate)
        
        print(f"   ✅ أعداد أولية: {len(primes_in_segment)}")
        if len(primes_in_segment) <= 5:
            print(f"   🔢 الأعداد: {sorted(list(primes_in_segment))}")
        
        # إضافة للنتيجة
        result.update(primes_in_segment)
    
    print(f"🎉 النتيجة النهائية: {len(result)} عدد أولي")
    return result

def test_formula():
    """اختبار الصيغة الرياضية"""
    print("🔬 اختبار التعبير الرياضي المطور")
    print("=" * 50)
    
    # اختبار على أرقام صغيرة
    test_cases = [30, 50, 100]
    
    for n in test_cases:
        print(f"\n🎯 اختبار حتى {n}")
        
        # النتيجة من الصيغة المطورة
        advanced_result = advanced_mathematical_formula(n, delta=20)
        
        # النتيجة من الطريقة التقليدية
        traditional_result = traditional_sieve(n)
        
        # المقارنة
        is_equal = advanced_result == traditional_result
        
        print(f"📊 الصيغة المطورة: {len(advanced_result)} عدد")
        print(f"📊 الطريقة التقليدية: {len(traditional_result)} عدد")
        print(f"✅ متطابقة: {'نعم' if is_equal else 'لا'}")
        
        if is_equal:
            sorted_result = sorted(list(advanced_result))
            print(f"🔢 النتيجة: {sorted_result}")
        else:
            print("❌ خطأ في التطبيق!")
            return False
    
    print("\n🎉 جميع الاختبارات نجحت!")
    print("✅ التعبير الرياضي المطور يعمل بشكل صحيح!")
    return True

if __name__ == "__main__":
    test_formula()
