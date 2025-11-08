
پروژه طوری طراحی شده که بتواند تجربه خرید آنلاین را شبیه یک فروشگاه واقعی ارائه دهد. بخش‌های اصلی شامل:

مدیریت محصولات با جزئیات کامل و چندگانه

اضافه کردن محصول به سبد خرید و تغییر تعداد آن

ثبت سفارش و مشاهده سفارش‌های کاربر

امکان نوشتن و مشاهده کامنت برای محصولات

تمامی بخش‌ها با Django و DRF ساخته شده و بک‌اند پروژه کاملاً تست شده است.

قابلیت‌های اصلی

نمایش محصولات و جزئیات آنها

سبد خرید با امکان تغییر تعداد محصول

ثبت سفارش و مدیریت سفارش‌های کاربر

امکان نوشتن و مشاهده کامنت برای محصولات

مدیریت بخش‌های مختلف فروشگاه از طریق پنل ادمین

تست‌های اولیه برای مدل‌ها و ویوها نوشته شده

قابلیت اجرای مستقل با Docker


تکنولوژی‌ها

Python

Django

Django REST Framework (DRF)

PostgreSQL

Docker & Docker Compose 

HTML, CSS, JavaScript

راه‌اندازی سریع
با Docker Compose
git clone <repo-link>

cd shop-project

cp .env.example .env

docker-compose up --build

بدون Docker
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

اجرای تست‌ها

تمام تست‌ها در پوشهٔ tests/ قرار دارند. برای اجرا:
python manage.py test

ساختار پروژه

accounts/ → مدیریت کاربران و احراز هویت

products/ → مدیریت محصولات و جزئیات آنها

cart/ → سبد خرید

orders/ → ثبت و مدیریت سفارش‌ها

payment/ → بخش پرداخت

templates/ → قالب‌های HTML

persian_translate/ → بخش ترجمه فارسی

وضعیت پروژه

پروژه کامل و آماده اجرا است

امکان توسعه و ادغام با ماژول‌های دیگر وجود دارد

کانفیگ Docker برای اجرای مستقل موجود است

نکات قبل از عمومی کردن ریپو

فایل‌های .env را حذف یا به .env.example تبدیل کنید

داده‌های حساس در پوشه‌ی media/ پاک یا نمونه‌سازی شوند
