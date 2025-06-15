#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
واجهة Hugging Face التفاعلية لمولد الأعداد الأولية المتقدم
=======================================================

هذا الملف يوفر واجهة ويب تفاعلية للمشروع على منصة Hugging Face

المؤلف: مبتكر
التاريخ: 2025-06-15
"""

import gradio as gr
import json
import time
from prime_generator import PrimeGenerator

def generate_primes_interface(limit, show_details=False):
    """
    واجهة لتوليد الأعداد الأولية
    """
    try:
        # التحقق من صحة المدخل
        limit = int(limit)
        if limit < 2:
            return "❌ الحد الأدنى هو 2", "", ""
        if limit > 100000:
            return "⚠️ للحصول على أفضل أداء، استخدم حد أقل من 100,000", "", ""
        
        # إنشاء مولد جديد
        generator = PrimeGenerator()
        
        # قياس الوقت
        start_time = time.time()
        primes = generator.matrix_method_primes(limit)
        end_time = time.time()
        
        # إعداد النتائج
        execution_time = end_time - start_time
        prime_count = len(primes)
        density = (prime_count / limit) * 100
        
        # النتيجة الأساسية
        result = f"""
🎉 **تم العثور على {prime_count} عدد أولي حتى {limit:,}**

⏱️ **الوقت**: {execution_time:.4f} ثانية
📊 **الكثافة**: {density:.2f}%
🔢 **أكبر عدد أولي**: {max(primes)}

**آخر 10 أعداد أولية:**
{primes[-10:] if len(primes) >= 10 else primes}
"""
        
        # التفاصيل الإضافية
        details = ""
        if show_details:
            # حساب الفجوات
            gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
            avg_gap = sum(gaps) / len(gaps) if gaps else 0
            max_gap = max(gaps) if gaps else 0
            
            details = f"""
📈 **إحصائيات متقدمة:**
- متوسط الفجوة: {avg_gap:.2f}
- أكبر فجوة: {max_gap}
- أصغر عدد أولي: {min(primes)}

🔬 **تحليل الخوارزمية:**
- الأعداد الفردية المعالجة: {(limit + 1) // 2}
- توفير المساحة: ~50%
- التعقيد الزمني: O(n log log n)
"""
        
        # قائمة الأعداد الأولية (محدودة للعرض)
        if len(primes) <= 100:
            primes_list = ", ".join(map(str, primes))
        else:
            first_50 = ", ".join(map(str, primes[:50]))
            last_50 = ", ".join(map(str, primes[-50:]))
            primes_list = f"{first_50}\n...\n{last_50}"
        
        return result, details, primes_list
        
    except ValueError:
        return "❌ يرجى إدخال رقم صحيح", "", ""
    except Exception as e:
        return f"❌ خطأ: {str(e)}", "", ""

def find_twin_primes_interface(limit):
    """
    واجهة للبحث عن الأعداد الأولية التوأم
    """
    try:
        limit = int(limit)
        if limit < 3:
            return "❌ الحد الأدنى هو 3"
        if limit > 10000:
            return "⚠️ للحصول على أفضل أداء، استخدم حد أقل من 10,000"
        
        generator = PrimeGenerator()
        primes = generator.matrix_method_primes(limit)
        
        # البحث عن الأعداد الأولية التوأم
        twin_primes = []
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] == 2:
                twin_primes.append((primes[i], primes[i+1]))
        
        if not twin_primes:
            return f"لم يتم العثور على أعداد أولية توأم حتى {limit}"
        
        result = f"""
🔍 **تم العثور على {len(twin_primes)} زوج من الأعداد الأولية التوأم حتى {limit:,}**

**الأزواج:**
"""
        
        for i, (p1, p2) in enumerate(twin_primes[:20], 1):  # أول 20 زوج
            result += f"{i}. ({p1}, {p2})\n"
        
        if len(twin_primes) > 20:
            result += f"\n... و {len(twin_primes) - 20} زوج آخر"
        
        return result
        
    except ValueError:
        return "❌ يرجى إدخال رقم صحيح"
    except Exception as e:
        return f"❌ خطأ: {str(e)}"

def test_goldbach_interface(limit):
    """
    واجهة لاختبار حدسية جولدباخ
    """
    try:
        limit = int(limit)
        if limit < 4:
            return "❌ الحد الأدنى هو 4"
        if limit > 1000:
            return "⚠️ للحصول على أفضل أداء، استخدم حد أقل من 1000"
        
        generator = PrimeGenerator()
        primes = generator.matrix_method_primes(limit)
        primes_set = set(primes)
        
        result = """
🧮 **اختبار حدسية جولدباخ**
"كل عدد زوجي أكبر من 2 يمكن كتابته كمجموع عددين أوليين"

**النتائج:**
"""
        
        success_count = 0
        total_count = 0
        
        for even in range(4, min(limit + 1, 51), 2):  # اختبار حتى 50 أو الحد المحدد
            total_count += 1
            found = False
            
            for p1 in primes:
                if p1 > even // 2:
                    break
                p2 = even - p1
                if p2 in primes_set:
                    result += f"{even} = {p1} + {p2}\n"
                    success_count += 1
                    found = True
                    break
            
            if not found:
                result += f"❌ {even}: لم يتم العثور على تمثيل!\n"
        
        result += f"\n📊 **الإحصائيات:**\n"
        result += f"- نجح: {success_count}/{total_count}\n"
        result += f"- نسبة النجاح: {(success_count/total_count)*100:.1f}%"
        
        return result
        
    except ValueError:
        return "❌ يرجى إدخال رقم صحيح"
    except Exception as e:
        return f"❌ خطأ: {str(e)}"

# إنشاء الواجهة
with gr.Blocks(title="مولد الأعداد الأولية المتقدم", theme=gr.themes.Soft()) as demo:
    
    gr.Markdown("""
    # 🔢 مولد الأعداد الأولية المتقدم
    ## Advanced Prime Numbers Generator
    
    خوارزمية مبتكرة لإيجاد الأعداد الأولية باستخدام جدول ضرب الأعداد الفردية
    
    **الصيغة الرياضية:** `P_n = {2} ∪ {p ∈ O_n : p ∉ C_n ∧ p > 1}`
    """)
    
    with gr.Tabs():
        
        # التبويب الأول: توليد الأعداد الأولية
        with gr.TabItem("🔢 توليد الأعداد الأولية"):
            with gr.Row():
                with gr.Column():
                    limit_input = gr.Number(
                        label="الحد الأقصى",
                        value=100,
                        minimum=2,
                        maximum=100000,
                        step=1
                    )
                    show_details_checkbox = gr.Checkbox(
                        label="عرض التفاصيل المتقدمة",
                        value=False
                    )
                    generate_btn = gr.Button("🚀 توليد الأعداد الأولية", variant="primary")
                
                with gr.Column():
                    result_output = gr.Markdown(label="النتائج")
                    details_output = gr.Markdown(label="التفاصيل")
            
            primes_output = gr.Textbox(
                label="قائمة الأعداد الأولية",
                lines=10,
                max_lines=20
            )
            
            generate_btn.click(
                generate_primes_interface,
                inputs=[limit_input, show_details_checkbox],
                outputs=[result_output, details_output, primes_output]
            )
        
        # التبويب الثاني: الأعداد الأولية التوأم
        with gr.TabItem("👯 الأعداد الأولية التوأم"):
            with gr.Row():
                with gr.Column():
                    twin_limit_input = gr.Number(
                        label="الحد الأقصى",
                        value=100,
                        minimum=3,
                        maximum=10000,
                        step=1
                    )
                    twin_btn = gr.Button("🔍 البحث عن الأعداد التوأم", variant="primary")
                
                with gr.Column():
                    twin_output = gr.Textbox(
                        label="الأعداد الأولية التوأم",
                        lines=15,
                        max_lines=25
                    )
            
            twin_btn.click(
                find_twin_primes_interface,
                inputs=[twin_limit_input],
                outputs=[twin_output]
            )
        
        # التبويب الثالث: حدسية جولدباخ
        with gr.TabItem("🧮 حدسية جولدباخ"):
            with gr.Row():
                with gr.Column():
                    goldbach_limit_input = gr.Number(
                        label="الحد الأقصى",
                        value=50,
                        minimum=4,
                        maximum=1000,
                        step=2
                    )
                    goldbach_btn = gr.Button("🧪 اختبار حدسية جولدباخ", variant="primary")
                
                with gr.Column():
                    goldbach_output = gr.Textbox(
                        label="نتائج الاختبار",
                        lines=15,
                        max_lines=25
                    )
            
            goldbach_btn.click(
                test_goldbach_interface,
                inputs=[goldbach_limit_input],
                outputs=[goldbach_output]
            )
        
        # التبويب الرابع: معلومات المشروع
        with gr.TabItem("ℹ️ معلومات المشروع"):
            gr.Markdown("""
            ## 📖 حول المشروع
            
            هذا المشروع يطبق خوارزمية مبتكرة لإيجاد الأعداد الأولية تتميز بـ:
            
            ### ✨ المزايا الرئيسية:
            - **توفير 50% من المساحة**: بتجاهل الأعداد الزوجية من البداية
            - **دقة 100%**: نتائج مطابقة تماماً للطرق التقليدية
            - **صيغة رياضية أنيقة**: تعبير واضح باستخدام نظرية المجموعات
            - **قابلية التوسع**: يعمل مع أرقام كبيرة جداً
            
            ### 🧮 الصيغة الرياضية:
            ```
            P_n = {2} ∪ {p ∈ O_n : p ∉ C_n ∧ p > 1}
            ```
            
            حيث:
            - **O_n**: مجموعة الأعداد الفردية
            - **C_n**: مجموعة الأعداد المركبة الفردية
            - **P_n**: مجموعة الأعداد الأولية
            
            ### 📊 الأداء:
            | النطاق | الأعداد الأولية | الوقت |
            |--------|----------------|-------|
            | 100 | 25 | < 1s |
            | 1,000 | 168 | < 1s |
            | 10,000 | 1,229 | ~2s |
            
            ### 👨‍💻 المؤلف:
            **مبتكر (Mubtakir)**
            - GitHub: [@mubtakir](https://github.com/mubtakir)
            - Hugging Face: [@Mubtakir](https://huggingface.co/Mubtakir)
            
            ### 📄 الترخيص:
            MIT License - مفتوح المصدر
            """)

# تشغيل التطبيق
if __name__ == "__main__":
    demo.launch()
