#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تطبيق التعبير الرياضي المطور لمولد الأعداد الأولية
=====================================================

هذا الملف يطبق الصيغة الرياضية المطورة بدقة:

𝒫_n = 𝒫_{√̂(n)} ∪̇ ⋃_{i=1}^{⌈(n-√̂(n))/δ⌉} {
    p ∈ (O_n ∩ [√̂(n) + (i-1)δ + 1, √̂(n) + iδ]) : 
    ∀q ∈ 𝒫_{√̂(n)}, p ∤ q ∧ q ∤ p
}

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import math
import time
from typing import List, Set, Tuple

class AdvancedMathematicalPrimeGenerator:
    """
    مولد الأعداد الأولية باستخدام التعبير الرياضي المطور
    """
    
    def __init__(self, delta: int = 32768):
        """
        تهيئة المولد
        
        Args:
            delta: حجم المقطع (δ في الصيغة الرياضية)
        """
        self.delta = delta
        self.state = {'last': 0, 'primes': set(), 'base_primes': set()}
    
    def sqrt_floor(self, n: int) -> int:
        """
        حساب √̂(n) = ⌊√n⌋
        الجذر التربيعي الصحيح
        """
        return int(math.sqrt(n))
    
    def odd_numbers_set(self, start: int, end: int) -> Set[int]:
        """
        حساب O_n = {2k+1 : k ∈ ℕ₀, start ≤ 2k+1 ≤ end}
        مجموعة الأعداد الفردية في النطاق [start, end]
        """
        # تأكد من أن start فردي
        if start % 2 == 0:
            start += 1
        
        return set(range(start, end + 1, 2))
    
    def base_primes_traditional_sieve(self, limit: int) -> Set[int]:
        """
        حساب B_n = {p ∈ P : p ≤ √̂(n)}
        الأعداد الأولية الأساسية باستخدام الغربال التقليدي
        """
        if limit < 2:
            return set()
        
        # غربال إراتوستينس التقليدي
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        
        for p in range(2, self.sqrt_floor(limit) + 1):
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
        
        return {i for i in range(2, limit + 1) if sieve[i]}
    
    def phi_sieve_function(self, S: Set[int], B: Set[int]) -> Set[int]:
        """
        دالة الغربلة: Φ(S, B) = {x ∈ S : ∀p ∈ B, (x ≢ 0 (mod p) ∨ x ∈ B)}
        
        Args:
            S: مجموعة الأعداد المراد غربلتها
            B: مجموعة الأعداد الأولية الأساسية
        
        Returns:
            مجموعة الأعداد الأولية في S
        """
        result = set()
        
        for x in S:
            is_prime = True
            
            # تحقق من قابلية القسمة على الأعداد الأولية الأساسية
            for p in B:
                if x != p and x % p == 0:
                    is_prime = False
                    break
            
            if is_prime:
                result.add(x)
        
        return result
    
    def segment_definition(self, i: int, delta: int, sqrt_n: int) -> Tuple[int, int]:
        """
        تعريف المقطع: Seg(i,δ,a) = [a + (i-1)δ, a + iδ - 1]
        
        Args:
            i: رقم المقطع
            delta: حجم المقطع
            sqrt_n: نقطة البداية (√̂(n))
        
        Returns:
            (start, end) للمقطع
        """
        start = sqrt_n + (i - 1) * delta + 1
        end = sqrt_n + i * delta
        return start, end
    
    def segments_count(self, n: int, sqrt_n: int) -> int:
        """
        حساب عدد المقاطع: k_n = ⌈(n - √̂(n))/δ⌉
        """
        return math.ceil((n - sqrt_n) / self.delta)
    
    def advanced_prime_generator(self, n: int) -> Set[int]:
        """
        التطبيق الكامل للصيغة الرياضية المطورة:
        
        𝒫_n = 𝒫_{√̂(n)} ∪̇ ⋃_{i=1}^{⌈(n-√̂(n))/δ⌉} {
            p ∈ (O_n ∩ [√̂(n) + (i-1)δ + 1, √̂(n) + iδ]) : 
            ∀q ∈ 𝒫_{√̂(n)}, p ∤ q ∧ q ∤ p
        }
        """
        print(f"🧮 تطبيق الصيغة الرياضية المطورة حتى {n}")
        start_time = time.time()
        
        # الخطوة 1: حساب √̂(n)
        sqrt_n = self.sqrt_floor(n)
        print(f"📐 √̂({n}) = {sqrt_n}")
        
        # الخطوة 2: حساب الأعداد الأولية الأساسية B_n
        base_primes = self.base_primes_traditional_sieve(sqrt_n)
        print(f"🔢 |B_{sqrt_n}| = {len(base_primes)} (الأعداد الأولية الأساسية)")
        print(f"   B_{sqrt_n} = {sorted(list(base_primes))}")
        
        # الخطوة 3: تهيئة النتيجة بالأعداد الأولية الأساسية
        result = base_primes.copy()
        
        # الخطوة 4: حساب عدد المقاطع المطلوبة
        k_n = self.segments_count(n, sqrt_n)
        print(f"📊 عدد المقاطع k_n = ⌈({n} - {sqrt_n})/{self.delta}⌉ = {k_n}")
        
        # الخطوة 5: معالجة كل مقطع
        total_candidates = 0
        total_primes_found = 0
        
        for i in range(1, k_n + 1):
            # تعريف المقطع الحالي
            seg_start, seg_end = self.segment_definition(i, self.delta, sqrt_n)
            seg_end = min(seg_end, n)  # تأكد من عدم تجاوز الحد
            
            if seg_start > n:
                break
            
            print(f"\n🔍 معالجة المقطع {i}: [{seg_start}, {seg_end}]")
            
            # حساب الأعداد الفردية في المقطع: O_n ∩ [seg_start, seg_end]
            odd_in_segment = self.odd_numbers_set(seg_start, seg_end)
            candidates_count = len(odd_in_segment)
            total_candidates += candidates_count
            
            print(f"   📋 عدد المرشحين الفرديين: {candidates_count}")
            
            # تطبيق دالة الغربلة: Φ(S_i, B_n)
            primes_in_segment = self.phi_sieve_function(odd_in_segment, base_primes)
            primes_found = len(primes_in_segment)
            total_primes_found += primes_found
            
            print(f"   ✅ أعداد أولية مكتشفة: {primes_found}")
            if primes_found > 0 and primes_found <= 10:
                print(f"   🔢 الأعداد: {sorted(list(primes_in_segment))}")
            elif primes_found > 10:
                sorted_primes = sorted(list(primes_in_segment))
                print(f"   🔢 أول 5: {sorted_primes[:5]}")
                print(f"   🔢 آخر 5: {sorted_primes[-5:]}")
            
            # إضافة النتائج للمجموعة الكلية
            result.update(primes_in_segment)
        
        # الخطوة 6: النتائج النهائية
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"\n🎉 اكتملت الصيغة الرياضية المطورة!")
        print(f"⏱️  الوقت المستغرق: {execution_time:.4f} ثانية")
        print(f"📊 إجمالي المرشحين الفرديين: {total_candidates}")
        print(f"🔢 إجمالي الأعداد الأولية: {len(result)}")
        print(f"📈 كفاءة الاكتشاف: {(len(result)/total_candidates)*100:.2f}%")
        print(f"💾 توفير المساحة: ~50% (معالجة الأعداد الفردية فقط)")
        
        return result
    
    def verify_against_traditional(self, n: int) -> bool:
        """
        التحقق من صحة النتائج مقابل الطريقة التقليدية
        """
        print(f"\n🔬 التحقق من الصحة مقابل الطريقة التقليدية حتى {n}")
        
        # النتائج من الصيغة المطورة
        advanced_result = self.advanced_prime_generator(n)
        
        # النتائج من الطريقة التقليدية
        traditional_result = self.base_primes_traditional_sieve(n)
        
        # المقارنة
        is_equal = advanced_result == traditional_result
        
        print(f"📊 الطريقة المطورة: {len(advanced_result)} عدد أولي")
        print(f"📊 الطريقة التقليدية: {len(traditional_result)} عدد أولي")
        print(f"✅ النتائج متطابقة: {'نعم' if is_equal else 'لا'}")
        
        if not is_equal:
            diff1 = advanced_result - traditional_result
            diff2 = traditional_result - advanced_result
            if diff1:
                print(f"❌ أعداد زائدة في المطورة: {sorted(list(diff1))}")
            if diff2:
                print(f"❌ أعداد ناقصة في المطورة: {sorted(list(diff2))}")
        
        return is_equal
    
    def performance_analysis(self, limits: List[int]) -> None:
        """
        تحليل الأداء على نطاقات مختلفة
        """
        print(f"\n📈 تحليل الأداء للصيغة الرياضية المطورة")
        print("=" * 60)
        
        for limit in limits:
            print(f"\n🎯 اختبار حتى {limit:,}")
            
            # قياس الوقت
            start_time = time.time()
            primes = self.advanced_prime_generator(limit)
            end_time = time.time()
            
            execution_time = end_time - start_time
            density = (len(primes) / limit) * 100
            
            print(f"   ⏱️  الوقت: {execution_time:.4f} ثانية")
            print(f"   🔢 الأعداد الأولية: {len(primes):,}")
            print(f"   📊 الكثافة: {density:.2f}%")
            print(f"   🚀 السرعة: {len(primes)/execution_time:.0f} عدد أولي/ثانية")


def main():
    """تشغيل التجربة الفعلية للتعبير الرياضي المطور"""
    print("🧮 تجربة فعلية للتعبير الرياضي المطور")
    print("=" * 60)
    
    # إنشاء مولد بحجم مقطع صغير للاختبار
    generator = AdvancedMathematicalPrimeGenerator(delta=1000)
    
    # اختبار 1: التحقق من الصحة
    print("\n🔬 اختبار 1: التحقق من الصحة")
    test_limits = [50, 100, 500]
    
    for limit in test_limits:
        is_correct = generator.verify_against_traditional(limit)
        if not is_correct:
            print(f"❌ فشل الاختبار عند {limit}")
            return
    
    print("✅ جميع اختبارات الصحة نجحت!")
    
    # اختبار 2: تحليل الأداء
    print("\n📈 اختبار 2: تحليل الأداء")
    performance_limits = [100, 500, 1000, 5000]
    generator.performance_analysis(performance_limits)
    
    # اختبار 3: مثال تفصيلي
    print("\n🔍 اختبار 3: مثال تفصيلي حتى 100")
    generator_detailed = AdvancedMathematicalPrimeGenerator(delta=20)
    result = generator_detailed.advanced_prime_generator(100)
    
    print(f"\n🎉 النتيجة النهائية حتى 100:")
    sorted_result = sorted(list(result))
    print(f"🔢 الأعداد الأولية: {sorted_result}")
    print(f"📊 العدد الكلي: {len(sorted_result)}")


if __name__ == "__main__":
    main()
