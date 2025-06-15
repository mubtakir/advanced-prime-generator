#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مولد الأعداد الأولية المتقدم
============================

خوارزمية متطورة لإيجاد الأعداد الأولية باستخدام:
- جدول ضرب الأعداد الفردية (تحسين 50%)
- الغربال المقطعي (Segmented Sieve)
- نظام تخزين مستمر للحالة

الصيغة الرياضية:
P_n = {2} ∪ {p ∈ O_n : p ∉ C_n ∧ p > 1}
حيث:
- O_n: مجموعة الأعداد الفردية
- C_n: مجموعة الأعداد المركبة الفردية
- P_n: مجموعة الأعداد الأولية

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import json
import math
import os
import time
from typing import List, Tuple

# أسماء الملفات الثابتة لتخزين الحالة والنتائج
STATE_FILE = "prime_state.json"
PRIMES_FILE = "primes_list.txt"
LOG_FILE = "prime_log.txt"

class PrimeGenerator:
    """مولد الأعداد الأولية المتقدم مع نظام التخزين المستمر"""
    
    def __init__(self):
        self.last_processed = 0
        self.total_primes_found = 0
        self.load_state()
    
    def load_state(self) -> None:
        """تحميل آخر حالة للبرنامج من ملف الحالة"""
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                    self.last_processed = state.get("last_processed_number", 0)
                    self.total_primes_found = state.get("total_primes_found", 0)
                    self.log(f"تم تحميل الحالة: آخر رقم معالج = {self.last_processed}")
            except Exception as e:
                self.log(f"خطأ في تحميل الحالة: {e}")
                self.last_processed = 0
                self.total_primes_found = 0
        else:
            self.log("أول تشغيل - لا توجد حالة سابقة")
    
    def save_state(self, last_number: int) -> None:
        """حفظ الحالة الجديدة للبرنامج"""
        try:
            state = {
                "last_processed_number": last_number,
                "total_primes_found": self.total_primes_found,
                "last_update": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(STATE_FILE, 'w', encoding='utf-8') as f:
                json.dump(state, f, ensure_ascii=False, indent=2)
            self.log(f"تم حفظ الحالة: آخر رقم = {last_number}")
        except Exception as e:
            self.log(f"خطأ في حفظ الحالة: {e}")
    
    def log(self, message: str) -> None:
        """كتابة رسالة في ملف السجل"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        try:
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception:
            pass  # تجاهل أخطاء السجل
        
        print(message)
    
    def append_primes_to_file(self, primes: List[int]) -> None:
        """إضافة الأعداد الأولية الجديدة إلى ملف النتائج"""
        try:
            with open(PRIMES_FILE, 'a', encoding='utf-8') as f:
                for p in primes:
                    f.write(f"{p}\n")
            self.total_primes_found += len(primes)
            self.log(f"تم إضافة {len(primes)} عدد أولي جديد")
        except Exception as e:
            self.log(f"خطأ في كتابة الأعداد الأولية: {e}")
    
    def simple_sieve(self, limit: int) -> List[int]:
        """غربال بسيط لإيجاد الأعداد الأولية الأساسية"""
        if limit < 2:
            return []
        
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        
        for p in range(2, int(math.sqrt(limit)) + 1):
            if sieve[p]:
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False
        
        return [i for i in range(2, limit + 1) if sieve[i]]
    
    def get_user_input(self) -> int:
        """الحصول على المدخلات من المستخدم"""
        if self.last_processed == 0:
            self.log("مرحباً! هذه هي المرة الأولى لتشغيل البرنامج.")
            self.log("سيتم تطبيق خوارزمية الغربال المقطعي المتقدم.")
            
            while True:
                try:
                    new_limit = int(input("يرجى إدخال الحد الأقصى للبحث عن الأعداد الأولية: "))
                    if new_limit < 2:
                        print("الحد الأقصى يجب أن يكون 2 أو أكثر.")
                        continue
                    return new_limit
                except ValueError:
                    print("إدخال غير صالح. يرجى إدخال رقم صحيح.")
        else:
            self.log(f"تم حساب الأعداد الأولية سابقاً حتى الرقم {self.last_processed}")
            self.log(f"إجمالي الأعداد الأولية المكتشفة: {self.total_primes_found}")
            
            while True:
                try:
                    new_limit = int(input(f"يرجى إدخال حد أقصى جديد (أكبر من {self.last_processed}): "))
                    if new_limit <= self.last_processed:
                        print(f"خطأ: الحد الجديد يجب أن يكون أكبر من {self.last_processed}")
                        continue
                    return new_limit
                except ValueError:
                    print("إدخال غير صالح. يرجى إدخال رقم صحيح.")
    
    def matrix_method_primes(self, limit: int) -> List[int]:
        """
        الطريقة المقترحة: جدول ضرب الأعداد الفردية
        
        الصيغة الرياضية:
        O_n = {x ∈ ℕ : x = 2k + 1, k ∈ ℕ₀, 1 ≤ x ≤ n}
        C_n = {x · y : x, y ∈ O_n, x ≥ 3, y ≥ x, x · y ≤ n}
        P_n = (O_n \ C_n) \ {1} ∪ {2}
        """
        if limit < 2:
            return []
        
        self.log(f"تطبيق طريقة جدول الضرب للأعداد الفردية حتى {limit}")
        
        # الخطوة 1: إنشاء قائمة الأعداد الفردية (المجموعة الأولى)
        odd_numbers = [i for i in range(1, limit + 1, 2)]
        self.log(f"عدد الأرقام الفردية: {len(odd_numbers)}")
        
        # الخطوة 2: إنشاء جدول الضرب (المجموعة الثانية)
        composite_numbers = set()
        
        # نبدأ من الرقم 3 (تجاهل 1 لأنه ليس أولي)
        for i in range(1, len(odd_numbers)):  # i يمثل الفهرس في odd_numbers
            x = odd_numbers[i]
            if x * x > limit:  # تحسين: إذا كان x² > limit، توقف
                break
            
            for j in range(i, len(odd_numbers)):  # j يمثل الفهرس في odd_numbers
                y = odd_numbers[j]
                product = x * y
                if product > limit:
                    break
                composite_numbers.add(product)
        
        self.log(f"عدد الأرقام المركبة الفردية: {len(composite_numbers)}")
        
        # الخطوة 3: إيجاد الأعداد الأولية (القائمة الثالثة)
        primes = []
        for num in odd_numbers:
            if num == 1:  # 1 ليس عدد أولي
                continue
            if num not in composite_numbers:
                primes.append(num)
        
        # إضافة الرقم 2 (العدد الأولي الوحيد الزوجي)
        if limit >= 2:
            primes.insert(0, 2)
        
        return sorted(primes)

    def segmented_sieve(self, start: int, end: int, base_primes: List[int]) -> List[int]:
        """
        الغربال المقطعي المتقدم

        يطبق الغربال على مقطع محدد [start, end] باستخدام الأعداد الأولية الأساسية
        """
        if start > end:
            return []

        # إنشاء مصفوفة للمقطع
        segment_size = end - start + 1
        segment = [True] * segment_size

        # تطبيق الغربال باستخدام الأعداد الأولية الأساسية
        for p in base_primes:
            if p * p > end:
                break

            # حساب نقطة البداية للغربلة في المقطع الحالي
            start_idx = max(p * p, (start + p - 1) // p * p)

            # غربلة مضاعفات p في المقطع
            for j in range(start_idx, end + 1, p):
                if j >= start:
                    segment[j - start] = False

        # جمع الأعداد الأولية من المقطع
        primes = []
        for i in range(segment_size):
            if segment[i]:
                num = start + i
                if num >= 2:  # تجاهل الأرقام أقل من 2
                    primes.append(num)

        return primes

    def advanced_segmented_sieve(self, new_limit: int) -> None:
        """
        الغربال المقطعي المتقدم مع التخزين المستمر

        يطبق الخوارزمية المطورة التي تحل مشاكل:
        1. محدودية الذاكرة
        2. خدعة الزحف
        3. التخزين المستمر للنتائج
        """
        start_time = time.time()

        # تحديد نقطة البداية
        start_range = max(2, self.last_processed + 1)

        self.log(f"بدء الغربال المقطعي من {start_range} إلى {new_limit}")

        # حساب الأعداد الأولية الأساسية
        limit_sqrt = int(math.sqrt(new_limit))
        self.log(f"حساب الأعداد الأولية الأساسية حتى {limit_sqrt}")

        base_primes = self.simple_sieve(limit_sqrt)
        self.log(f"تم العثور على {len(base_primes)} عدد أولي أساسي")

        # إذا كان هذا التشغيل الأول، احفظ الأعداد الأولية الأساسية
        if self.last_processed == 0:
            # احفظ الأعداد الأولية الأساسية التي تقع في النطاق المطلوب
            basic_primes_in_range = [p for p in base_primes if p <= new_limit]
            if basic_primes_in_range:
                self.append_primes_to_file(basic_primes_in_range)

        # تحديد حجم المقطع (يمكن تعديله حسب الذاكرة المتاحة)
        segment_size = min(32768, new_limit - start_range + 1)

        # معالجة النطاق على شكل مقاطع
        current_start = max(start_range, limit_sqrt + 1)

        while current_start <= new_limit:
            current_end = min(current_start + segment_size - 1, new_limit)

            self.log(f"معالجة المقطع [{current_start}, {current_end}]")

            # تطبيق الغربال على المقطع الحالي
            segment_primes = self.segmented_sieve(current_start, current_end, base_primes)

            # حفظ الأعداد الأولية الجديدة
            if segment_primes:
                self.append_primes_to_file(segment_primes)
                self.log(f"تم العثور على {len(segment_primes)} عدد أولي في هذا المقطع")

            current_start = current_end + 1

        # حفظ الحالة النهائية
        self.save_state(new_limit)

        elapsed_time = time.time() - start_time
        self.log(f"اكتملت العملية في {elapsed_time:.2f} ثانية")
        self.log(f"إجمالي الأعداد الأولية: {self.total_primes_found}")

    def compare_methods(self, limit: int = 1000) -> None:
        """مقارنة بين الطريقة المقترحة والطريقة التقليدية"""
        self.log(f"مقارنة الطرق حتى الحد {limit}")

        # الطريقة المقترحة
        start_time = time.time()
        matrix_primes = self.matrix_method_primes(limit)
        matrix_time = time.time() - start_time

        # الطريقة التقليدية
        start_time = time.time()
        traditional_primes = self.simple_sieve(limit)
        traditional_time = time.time() - start_time

        # المقارنة
        self.log("=" * 50)
        self.log("نتائج المقارنة:")
        self.log(f"الطريقة المقترحة: {len(matrix_primes)} عدد أولي في {matrix_time:.4f} ثانية")
        self.log(f"الطريقة التقليدية: {len(traditional_primes)} عدد أولي في {traditional_time:.4f} ثانية")
        self.log(f"النتائج متطابقة: {matrix_primes == traditional_primes}")
        self.log(f"الفرق الزمني: {abs(matrix_time - traditional_time):.4f} ثانية")
        self.log("=" * 50)

    def display_statistics(self) -> None:
        """عرض إحصائيات المشروع"""
        self.log("=" * 60)
        self.log("إحصائيات مشروع الأعداد الأولية المتقدم")
        self.log("=" * 60)
        self.log(f"آخر رقم تم معالجته: {self.last_processed:,}")
        self.log(f"إجمالي الأعداد الأولية المكتشفة: {self.total_primes_found:,}")

        if os.path.exists(PRIMES_FILE):
            file_size = os.path.getsize(PRIMES_FILE)
            self.log(f"حجم ملف النتائج: {file_size:,} بايت")

        if self.last_processed > 0:
            density = (self.total_primes_found / self.last_processed) * 100
            self.log(f"كثافة الأعداد الأولية: {density:.2f}%")

        self.log("=" * 60)

    def run(self) -> None:
        """تشغيل البرنامج الرئيسي"""
        try:
            self.log("بدء تشغيل مولد الأعداد الأولية المتقدم")

            # عرض الإحصائيات الحالية
            if self.last_processed > 0:
                self.display_statistics()

            # الحصول على المدخلات من المستخدم
            new_limit = self.get_user_input()

            # اختيار الطريقة المناسبة
            if new_limit <= 100000:
                # للأرقام الصغيرة، يمكن استخدام الطريقة المقترحة مباشرة
                self.log("استخدام طريقة جدول الضرب للأعداد الفردية")

                if self.last_processed == 0:
                    primes = self.matrix_method_primes(new_limit)
                    self.append_primes_to_file(primes)
                    self.save_state(new_limit)
                else:
                    # للنطاقات المتقدمة، استخدم الغربال المقطعي
                    self.advanced_segmented_sieve(new_limit)
            else:
                # للأرقام الكبيرة، استخدم الغربال المقطعي دائماً
                self.log("استخدام الغربال المقطعي المتقدم")
                self.advanced_segmented_sieve(new_limit)

            # عرض الإحصائيات النهائية
            self.display_statistics()

            # اقتراح مقارنة للمستخدم
            if new_limit <= 10000:
                response = input("\nهل تريد مقارنة الطرق المختلفة؟ (y/n): ")
                if response.lower() in ['y', 'yes', 'نعم']:
                    self.compare_methods(min(new_limit, 1000))

            self.log("تم إنجاز العملية بنجاح!")
            self.log(f"يمكنك العثور على النتائج في: {PRIMES_FILE}")

        except KeyboardInterrupt:
            self.log("تم إيقاف البرنامج بواسطة المستخدم")
        except Exception as e:
            self.log(f"خطأ غير متوقع: {e}")


def main():
    """الدالة الرئيسية"""
    generator = PrimeGenerator()
    generator.run()


if __name__ == "__main__":
    main()
