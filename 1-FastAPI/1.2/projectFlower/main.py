import sys
from PyQt6.QtWidgets import QApplication
from ui import FlowerUI
from api import generate_image, identify_flower

def handle_generate(ui):
    # ۱. گرفتن متن از QLineEdit
    prompt = ui.textbox.text()

    if not prompt:
        ui.result_label.setText("لطفاً اول اسم یک گل را وارد کنید!")
        return

    # ۲. آپدیت وضعیت
    ui.set_status("در حال تولید تصویر با هوش مصنوعی...")
    ui.result_label.setText("لطفاً صبر کنید...")
    QApplication.processEvents() 

    # ۳. تولید تصویر
    image_path = generate_image(prompt)
    print(f"image_path:{image_path}")

    if not image_path:
        ui.set_status("خطا در تولید تصویر!")
        ui.result_label.setText("شاید اینترنت قطع است یا خطایی رخ داد.")
        return

    # ۴. نمایش تصویر
    ui.show_image(image_path)
    ui.set_status("تصویر ساخته شد! در حال شناسایی...")
    QApplication.processEvents() 

    # ۵. شناسایی گل (دریافت دیتا از API)
    # توجه: info اکنون همان دیتای خام JSON است که از PlantNet برگشته
    info = identify_flower(image_path)
    
    # پردازش دیتای خام در main.py
    if info and "results" in info and len(info["results"]) > 0:
        best_match = info["results"][0]
        species = best_match.get("species", {})
        
        # استخراج فیلدهای مورد نظر
        sci_name = species.get("scientificNameWithoutAuthor", "N/A")
        
        # دسترسی به نام علمی خانواده (که داخل یک دیکشنری دیگر است)
        family_data = species.get("family", {})
        family_name = family_data.get("scientificName", "N/A")
        
        # استخراج نام‌های رایج (اگر لیست بود، آن را به رشته تبدیل می‌کنیم)
        common_names_list = species.get("commonNames", [])
        common_names_str = ", ".join(common_names_list) if common_names_list else "N/A"
        
        # ساخت متن نهایی برای نمایش
        result_text = (
            f"نام علمی: {sci_name}\n\n"
            f"خانواده: {family_name}\n\n"
            f"نام‌های رایج: {common_names_str}"
        )
        
        ui.result_label.setText(result_text)
        ui.set_status("شناسایی با موفقیت انجام شد")
        
    else:
        ui.result_label.setText("گل شناسایی نشد یا خطایی در ارتباط رخ داد.")
        ui.set_status("خطا در شناسایی.")

# اجرای برنامه
app = QApplication(sys.argv)
ui = FlowerUI()
ui.button.clicked.connect(lambda: handle_generate(ui))
ui.show()
sys.exit(app.exec())
