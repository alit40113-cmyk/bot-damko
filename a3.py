
import os
import sys
import json
import hashlib
import datetime
import requests
import random
import time
import webbrowser
import subprocess
from pathlib import Path
from colorama import init, Fore, Back, Style, just_fix_windows_console

init()
just_fix_windows_console()

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT

class LanguageManager:
   
    
    def __init__(self):
        self.current_lang = 'en'
        self.languages = {
            'en': {
                'name': 'English',
                'flag': '🇺🇸',
                'translations': self.get_english_translations()
            },
            'ar': {
                'name': 'العربية',
                'flag': '🇮🇶',
                'translations': self.get_arabic_translations()
            },
            'es': {
                'name': 'Español',
                'flag': '🇪🇸',
                'translations': self.get_spanish_translations()
            },
            'fr': {
                'name': 'Français',
                'flag': '🇫🇷',
                'translations': self.get_french_translations()
            },
            'de': {
                'name': 'Deutsch',
                'flag': '🇩🇪',
                'translations': self.get_german_translations()
            },
            'ru': {
                'name': 'Русский',
                'flag': '🇷🇺',
                'translations': self.get_russian_translations()
            },
            'tr': {
                'name': 'Türkçe',
                'flag': '🇹🇷',
                'translations': self.get_turkish_translations()
            },
            'hi': {
                'name': 'हिन्दी',
                'flag': '🇮🇳',
                'translations': self.get_hindi_translations()
            },
            'cn': {
                'name': '中文',
                'flag': '🇨🇳',
                'translations': self.get_chinese_translations()
            }
        }
    
    def get_english_translations(self):
       
        return {
            'welcome_title': '✨ WELCOME TO INSTAGRAM USERNAME CHECKER PRO ✨',
            'select_language': '🌍 SELECT YOUR LANGUAGE',
            'features': '📋 Features:',
            'feature1': 'Advanced username generation',
            'feature2': 'Real-time Instagram checking',
            'feature3': 'Telegram notifications',
            'feature4': 'Professional interface',
            'feature5': '24-hour license activation',
            'license_warning': '⚠ This is a licensed software.',
            'license_key_prompt': '⚠ You need a valid license key to continue.',
            'enter_license': '[?] Enter license key: ',
            'license_activated': '[✓] License activated successfully!',
            'license_expires': '[✓] License expires in 24 hours',
            'license_failed': '[✗] Failed to activate license',
            'invalid_key': '[✗] Invalid license key',
            'try_again': '[?] Try again? (y/n): ',
            'exiting': 'Exiting...',
            'main_menu': '📋 MAIN MENU:',
            'option1': 'Start Username Checker',
            'option2': 'Configure Telegram Bot',
            'option3': 'View Statistics',
            'option4': 'Check for Updates',
            'option5': 'About & Help',
            'option0': 'Exit',
            'select_option': '[?] Select option (0-5): ',
            'invalid_option': '[!] Invalid option. Please try again.',
            'checking_libs': '[*] Checking and installing required libraries...',
            'already_installed': '[✓] {package} is already installed',
            'installing': '[*] Installing {package}...',
            'installed': '[✓] Successfully installed {package}',
            'failed_install': '[✗] Failed to install {package}',
            'all_requirements': '[✓] All requirements are satisfied!',
            'license_info': '📊 LICENSE INFORMATION:',
            'status': 'Status:',
            'expires': 'Expires in:',
            'telegram_config': '🤖 TELEGRAM BOT CONFIGURATION',
            'enter_token': '[?] Enter Telegram Bot Token: ',
            'enter_chat_id': '[?] Enter Chat ID: ',
            'testing_telegram': '[*] Testing Telegram connection...',
            'telegram_valid': '[✓] Telegram bot is valid',
            'settings_saved': '[✓] Settings saved successfully!',
            'join_telegram': '⚠ Join our Telegram channel: https://t.me/teamofghost',
            'invalid_token': '[✗] Invalid bot token',
            'connection_failed': '[✗] Connection failed: {error}',
            'token_required': '[✗] Token and Chat ID are required',
            'press_enter': 'Press Enter to continue...',
            'starting_checker': '🔍 STARTING USERNAME CHECKER',
            'how_many_usernames': '[?] How many usernames to generate? (default: 20): ',
            'generating': '[*] Generating {count} usernames...',
            'starting_process': '[*] Starting Instagram checking process...',
            'available': '[✓] AVAILABLE: {username}',
            'telegram_sent': '  ↪ Telegram notification sent',
            'taken': '[✗] TAKEN: {username}',
            'error': '[!] ERROR: {username}',
            'checking_completed': '📊 CHECKING COMPLETED!',
            'total_checked': 'Total checked:',
            'available_count': 'Available:',
            'taken_count': 'Taken:',
            'errors_count': 'Errors:',
            'time_taken': 'Time taken:',
            'avg_time': 'Average time per check:',
            'found_available': '🎉 {count} usernames are available!',
            'none_found': '😔 No available usernames found this time.',
            'checking_updates': '🔄 CHECKING FOR UPDATES',
            'current_version': '[*] Current version: {version}',
            'checking': '[*] Checking for updates...',
            'latest_version': '[✓] You are using the latest version!',
            'support_channel': 'For updates and support, join our Telegram channel:',
            'about_help': 'ℹ️ ABOUT & HELP',
            'description': '📖 Description:',
            'description_text': 'This tool checks the availability of Instagram usernames by generating random combinations and testing them against Instagram\'s signup system.',
            'features_title': '⚙️ Features:',
            'developer': '👤 Developer:',
            'support': '📞 Support:',
            'legal_notice': '⚠️ Legal Notice:',
            'legal_text': 'This tool is for educational purposes only. Use it responsibly and in accordance with Instagram\'s Terms of Service.',
            'program_exit': 'Exiting... Thank you for using Instagram Checker Pro!',
            'program_interrupted': 'Program interrupted by user. Exiting...',
            'error_occurred': 'An error occurred: {error}',
            'loading_license': '[*] Loading license information...',
            'license_expired': '[INFO] License has expired. Please renew.',
            'load_error': '[ERROR] Failed to load license: {error}',
            'save_error': '[ERROR] Failed to save license: {error}',
            'activated': 'ACTIVATED',
            'expired': 'EXPIRED',
            'hours': 'h',
            'minutes': 'm',
            'seconds': 's'
        }
    
    def get_arabic_translations(self):
       
        return {
            'welcome_title': '✨ مرحباً بكم في اده صيد يوزرات مستخدمي انستجرام المدفوعه ✨',
            'select_language': '🌍 اختر لغتك',
            'features': '📋 المميزات:',
            'feature1': 'صيد حقيقي',
            'feature2': 'صيد بدقه ',
            'feature3': 'صيد باكثر من نمط',
            'feature4': 'واجهة مدفوعه للمشتركين مدفوعين',
            'feature5': 'تفعيل الاشتراك لمدة 24 ساعة',
            'license_warning': '⚠ هذا الاده مدفوعه.',
            'license_key_prompt': '⚠ تحتاج إلى مفتاح المدفوع صالح للمتابعة.',
            'enter_license': '[?] أدخل مفتاح المدفوع: ',
            'license_activated': '[✓] تم تفعيل الاشتراك بنجاح!',
            'license_expires': '[✓] ينتهي الاشتراك خلال 24 ساعة',
            'license_failed': '[✗] فشل في تفعيل الترخيص',
            'invalid_key': '[✗] مفتاح ترخيص غير صالح',
            'try_again': '[?] حاول مرة أخرى؟ (y/n): ',
            'exiting': 'جاري الخروج...',
            'main_menu': '📋 القائمة الرئيسية:',
            'option1': 'بدء صيد',
            'option2': 'اضف بوتك',
            'option3': 'عرض الإحصائيات',
            'option4': 'التحقق من التحديثات',
            'option5': 'حول والمساعدة',
            'option0': 'خروج',
            'select_option': '[?] اختر خياراً (0-5): ',
            'invalid_option': '[!] خيار غير صالح. يرجى المحاولة مرة أخرى.',
            'checking_libs': '[*] جاري التحقق من المكتبات المطلوبة وتثبيتها...',
            'already_installed': '[✓] {package} مثبت مسبقاً',
            'installing': '[*] جاري تثبيت {package}...',
            'installed': '[✓] تم تثبيت {package} بنجاح',
            'failed_install': '[✗] فشل في تثبيت {package}',
            'all_requirements': '[✓] جميع المتطلبات متوفرة!',
            'license_info': '📊 معلومات اشتراكك:',
            'status': 'الحالة:',
            'expires': 'ينتهي خلال:',
            'telegram_config': '🤖 تهيئة بوت التليجرام',
            'enter_token': '[?] أدخل توكن بوت التليجرام: ',
            'enter_chat_id': '[?] أدخل ايدي حسابك: ',
            'testing_telegram': '[*] جاري اتصال التليجرام...',
            'telegram_valid': '[✓] بوت التليجرام صالح',
            'settings_saved': '[✓] تم حفظ الإعدادات بنجاح!',
            'join_telegram': '⚠ انضم إلى قناتنا على التليجرام: https://t.me/teamofghost',
            'invalid_token': '[✗] رمز البوت غير صالح',
            'connection_failed': '[✗] فشل الاتصال: {error}',
            'token_required': '[✗] رمز البوت ومعرف الدردشة مطلوبان',
            'press_enter': 'اضغط Enter للمتابعة...',
            'starting_checker': '🔍 بدء صيد يوزرات',
            'how_many_usernames': '[?] كم عدد يوزرات التي تريد صيدها؟ (الافتراضي: 20): ',
            'generating': '[*] جاري إنشاء {count} اسم مستخدم...',
            'starting_process': '[*] بدء عملية صيد انستجرام...',
            'available': '[✓] متاح: {username}',
            'telegram_sent': '  ↪ تم إرسال إشعار التليجرام',
            'taken': '[✗] محجوز: {username}',
            'error': '[!] خطأ: {username}',
            'checking_completed': '📊 اكتمل الفحص!',
            'total_checked': 'إجمالي المفحوص:',
            'available_count': 'المتاحة:',
            'taken_count': 'المحجوزة:',
            'errors_count': 'الأخطاء:',
            'time_taken': 'الوقت المستغرق:',
            'avg_time': 'متوسط الوقت لكل فحص:',
            'found_available': '🎉 {count} اسم مستخدم متاح!',
            'none_found': '😔 لم يتم العثور على أسماء مستخدمين متاحة هذه المرة.',
            'checking_updates': '🔄 التحقق من التحديثات',
            'current_version': '[*] النسخة الحالية: {version}',
            'checking': '[*] جاري التحقق من التحديثات...',
            'latest_version': '[✓] أنت تستخدم أحدث نسخة!',
            'support_channel': 'للتحديثات والدعم، انضم إلى قناتنا على التليجرام:',
            'about_help': 'ℹ️ حول والمساعدة',
            'description': '📖 الوصف:',
            'description_text': 'يتحقق هذا الأداة من توفر أسماء مستخدمي انستجرام عن طريق إنشاء توليفات عشوائية وصيدها.',
            'features_title': '⚙️ المميزات:',
            'developer': '👤 المطور:',
            'support': '📞 الدعم:',
            'legal_notice': '⚠️ إشعار قانوني:',
            'legal_text': 'هذه الأداة لأغراض تعليمية فقط. استخدمها بمسؤولية ووفقاً لشروط خدمة المبرمج.',
            'program_exit': 'جاري الخروج... شكراً لاستخدامك مدقق انستجرام المحترف!',
            'program_interrupted': 'تمت مقاطعة البرنامج من قبل المستخدم. جاري الخروج...',
            'error_occurred': 'حدث خطأ: {error}',
            'loading_license': '[*] جاري تحميل معلومات الترخيص...',
            'license_expired': '[معلومة] انتهت صلاحية الترخيص. يرجى التجديد.',
            'load_error': '[خطأ] فشل في تحميل الترخيص: {error}',
            'save_error': '[خطأ] فشل في حفظ الترخيص: {error}',
            'activated': 'مفعل',
            'expired': 'منتهي',
            'hours': 'س',
            'minutes': 'د',
            'seconds': 'ث'
        }
    
    def get_spanish_translations(self):
       
        return {
            'welcome_title': '✨ BIENVENIDO A INSTAGRAM USERNAME CHECKER PRO ✨',
            'select_language': '🌍 SELECCIONE SU IDIOMA',
            'features': '📋 Características:',
            'feature1': 'Generación avanzada de nombres de usuario',
            'feature2': 'Verificación de Instagram en tiempo real',
            'feature3': 'Notificaciones de Telegram',
            'feature4': 'Interfaz profesional',
            'feature5': 'Activación de licencia de 24 horas',
            'license_warning': '⚠ Este es un software con licencia.',
            'license_key_prompt': '⚠ Necesita una clave de licencia válida para continuar.',
            'enter_license': '[?] Ingrese la clave de licencia: ',
            'license_activated': '[✓] ¡Licencia activada con éxito!',
            'license_expires': '[✓] La licencia expira en 24 horas',
            'license_failed': '[✗] Error al activar la licencia',
            'invalid_key': '[✗] Clave de licencia inválida',
            'try_again': '[?] ¿Intentar de nuevo? (s/n): ',
            'exiting': 'Saliendo...',
            'main_menu': '📋 MENÚ PRINCIPAL:',
            'option1': 'Iniciar verificador de nombres de usuario',
            'option2': 'Configurar bot de Telegram',
            'option3': 'Ver estadísticas',
            'option4': 'Buscar actualizaciones',
            'option5': 'Acerca de y ayuda',
            'option0': 'Salir',
            'select_option': '[?] Seleccione opción (0-5): ',
            'invalid_option': '[!] Opción inválida. Intente nuevamente.',
            'checking_libs': '[*] Verificando e instalando bibliotecas requeridas...',
            'already_installed': '[✓] {package} ya está instalado',
            'installing': '[*] Instalando {package}...',
            'installed': '[✓] {package} instalado exitosamente',
            'failed_install': '[✗] Error al instalar {package}',
            'all_requirements': '[✓] ¡Todos los requisitos están satisfechos!',
            'license_info': '📊 INFORMACIÓN DE LICENCIA:',
            'status': 'Estado:',
            'expires': 'Expira en:',
            'telegram_config': '🤖 CONFIGURACIÓN DEL BOT DE TELEGRAM',
            'enter_token': '[?] Ingrese el token del bot de Telegram: ',
            'enter_chat_id': '[?] Ingrese el ID del chat: ',
            'testing_telegram': '[*] Probando conexión de Telegram...',
            'telegram_valid': '[✓] Bot de Telegram válido',
            'settings_saved': '[✓] ¡Configuración guardada exitosamente!',
            'join_telegram': '⚠ Únase a nuestro canal de Telegram: https://t.me/teamofghost',
            'invalid_token': '[✗] Token de bot inválido',
            'connection_failed': '[✗] Error de conexión: {error}',
            'token_required': '[✗] Se requieren token e ID de chat',
            'press_enter': 'Presione Enter para continuar...',
            'starting_checker': '🔍 INICIANDO VERIFICADOR DE NOMBRES DE USUARIO',
            'how_many_usernames': '[?] ¿Cuántos nombres de usuario generar? (predeterminado: 20): ',
            'generating': '[*] Generando {count} nombres de usuario...',
            'starting_process': '[*] Iniciando proceso de verificación de Instagram...',
            'available': '[✓] DISPONIBLE: {username}',
            'telegram_sent': '  ↪ Notificación de Telegram enviada',
            'taken': '[✗] TOMADO: {username}',
            'error': '[!] ERROR: {username}',
            'checking_completed': '📊 ¡VERIFICACIÓN COMPLETADA!',
            'total_checked': 'Total verificado:',
            'available_count': 'Disponibles:',
            'taken_count': 'Tomados:',
            'errors_count': 'Errores:',
            'time_taken': 'Tiempo tomado:',
            'avg_time': 'Tiempo promedio por verificación:',
            'found_available': '🎉 ¡{count} nombres de usuario disponibles!',
            'none_found': '😔 No se encontraron nombres de usuario disponibles esta vez.',
            'checking_updates': '🔄 BUSCANDO ACTUALIZACIONES',
            'current_version': '[*] Versión actual: {version}',
            'checking': '[*] Buscando actualizaciones...',
            'latest_version': '[✓] ¡Está usando la última versión!',
            'support_channel': 'Para actualizaciones y soporte, únase a nuestro canal de Telegram:',
            'about_help': 'ℹ️ ACERCA DE Y AYUDA',
            'description': '📖 Descripción:',
            'description_text': 'Esta herramienta verifica la disponibilidad de nombres de usuario de Instagram generando combinaciones aleatorias y probándolas contra el sistema de registro de Instagram.',
            'features_title': '⚙️ Características:',
            'developer': '👤 Desarrollador:',
            'support': '📞 Soporte:',
            'legal_notice': '⚠️ Aviso legal:',
            'legal_text': 'Esta herramienta es solo con fines educativos. Úsela responsablemente y de acuerdo con los Términos de Servicio de Instagram.',
            'program_exit': 'Saliendo... ¡Gracias por usar Instagram Checker Pro!',
            'program_interrupted': 'Programa interrumpido por el usuario. Saliendo...',
            'error_occurred': 'Ocurrió un error: {error}',
            'loading_license': '[*] Cargando información de licencia...',
            'license_expired': '[INFO] La licencia ha expirado. Por favor renueve.',
            'load_error': '[ERROR] Error al cargar la licencia: {error}',
            'save_error': '[ERROR] Error al guardar la licencia: {error}',
            'activated': 'ACTIVADA',
            'expired': 'EXPIRADA',
            'hours': 'h',
            'minutes': 'm',
            'seconds': 's'
        }
    
    def get_french_translations(self):
       
        return {
            'welcome_title': '✨ BIENVENUE DANS INSTAGRAM USERNAME CHECKER PRO ✨',
            'select_language': '🌍 SÉLECTIONNEZ VOTRE LANGUE',
            'features': '📋 Fonctionnalités:',
            'feature1': 'Génération avancée de noms d\'utilisateur',
            'feature2': 'Vérification Instagram en temps réel',
            'feature3': 'Notifications Telegram',
            'feature4': 'Interface professionnelle',
            'feature5': 'Activation de licence de 24 heures',
            'license_warning': '⚠ Ceci est un logiciel sous licence.',
            'license_key_prompt': '⚠ Vous avez besoin d\'une clé de licence valide pour continuer.',
            'enter_license': '[?] Entrez la clé de licence: ',
            'license_activated': '[✓] Licence activée avec succès!',
            'license_expires': '[✓] La licence expire dans 24 heures',
            'license_failed': '[✗] Échec de l\'activation de la licence',
            'invalid_key': '[✗] Clé de licence invalide',
            'try_again': '[?] Réessayer? (o/n): ',
            'exiting': 'Sortie...',
            'main_menu': '📋 MENU PRINCIPAL:',
            'option1': 'Démarrer le vérificateur de noms d\'utilisateur',
            'option2': 'Configurer le bot Telegram',
            'option3': 'Voir les statistiques',
            'option4': 'Vérifier les mises à jour',
            'option5': 'À propos et aide',
            'option0': 'Quitter',
            'select_option': '[?] Sélectionnez une option (0-5): ',
            'invalid_option': '[!] Option invalide. Veuillez réessayer.',
            'checking_libs': '[*] Vérification et installation des bibliothèques requises...',
            'already_installed': '[✓] {package} est déjà installé',
            'installing': '[*] Installation de {package}...',
            'installed': '[✓] {package} installé avec succès',
            'failed_install': '[✗] Échec de l\'installation de {package}',
            'all_requirements': '[✓] Toutes les exigences sont satisfaites!',
            'license_info': '📊 INFORMATIONS SUR LA LICENCE:',
            'status': 'Statut:',
            'expires': 'Expire dans:',
            'telegram_config': '🤖 CONFIGURATION DU BOT TELEGRAM',
            'enter_token': '[?] Entrez le token du bot Telegram: ',
            'enter_chat_id': '[?] Entrez l\'ID du chat: ',
            'testing_telegram': '[*] Test de la connexion Telegram...',
            'telegram_valid': '[✓] Bot Telegram valide',
            'settings_saved': '[✓] Paramètres enregistrés avec succès!',
            'join_telegram': '⚠ Rejoignez notre canal Telegram: https://t.me/teamofghost',
            'invalid_token': '[✗] Token de bot invalide',
            'connection_failed': '[✗] Échec de la connexion: {error}',
            'token_required': '[✗] Token et ID de chat requis',
            'press_enter': 'Appuyez sur Entrée pour continuer...',
            'starting_checker': '🔍 DÉMARRAGE DU VÉRIFICATEUR DE NOMS D\'UTILISATEUR',
            'how_many_usernames': '[?] Combien de noms d\'utilisateur générer? (par défaut: 20): ',
            'generating': '[*] Génération de {count} noms d\'utilisateur...',
            'starting_process': '[*] Démarrage du processus de vérification Instagram...',
            'available': '[✓] DISPONIBLE: {username}',
            'telegram_sent': '  ↪ Notification Telegram envoyée',
            'taken': '[✗] PRIS: {username}',
            'error': '[!] ERREUR: {username}',
            'checking_completed': '📊 VÉRIFICATION TERMINÉE!',
            'total_checked': 'Total vérifié:',
            'available_count': 'Disponibles:',
            'taken_count': 'Pris:',
            'errors_count': 'Errores:',
            'time_taken': 'Temps pris:',
            'avg_time': 'Temps moyen par vérification:',
            'found_available': '🎉 {count} noms d\'utilisateur disponibles!',
            'none_found': '😔 Aucun nom d\'utilisateur disponible trouvé cette fois.',
            'checking_updates': '🔄 VÉRIFICATION DES MISES À JOUR',
            'current_version': '[*] Version actuelle: {version}',
            'checking': '[*] Vérification des mises à jour...',
            'latest_version': '[✓] Vous utilisez la dernière version!',
            'support_channel': 'Pour les mises à jour et le support, rejoignez notre canal Telegram:',
            'about_help': 'ℹ️ À PROPOS ET AIDE',
            'description': '📖 Description:',
            'description_text': 'Cet outil vérifie la disponibilité des noms d\'utilisateur Instagram en générant des combinaisons aléatoires et en les testant contre le système d\'inscription d\'Instagram.',
            'features_title': '⚙️ Fonctionnalités:',
            'developer': '👤 Développeur:',
            'support': '📞 Support:',
            'legal_notice': '⚠️ Avis légal:',
            'legal_text': 'Cet outil est à des fins éducatives uniquement. Utilisez-le de manière responsable et conformément aux conditions d\'utilisation d\'Instagram.',
            'program_exit': 'Sortie... Merci d\'utiliser Instagram Checker Pro!',
            'program_interrupted': 'Programme interrompu par l\'utilisateur. Sortie...',
            'error_occurred': 'Une erreur s\'est produite: {error}',
            'loading_license': '[*] Chargement des informations de licence...',
            'license_expired': '[INFO] La licence a expiré. Veuillez renouveler.',
            'load_error': '[ERROR] Échec du chargement de la licence: {error}',
            'save_error': '[ERROR] Échec de l\'enregistrement de la licence: {error}',
            'activated': 'ACTIVÉE',
            'expired': 'EXPIRÉE',
            'hours': 'h',
            'minutes': 'm',
            'seconds': 's'
        }
    
    def get_german_translations(self):
       
        return {
            'welcome_title': '✨ WILLKOMMEN BEI INSTAGRAM USERNAME CHECKER PRO ✨',
            'select_language': '🌍 WÄHLEN SIE IHRE SPRACHE',
            'features': '📋 Funktionen:',
            'feature1': 'Erweiterte Benutzernamengenerierung',
            'feature2': 'Echtzeit-Instagram-Überprüfung',
            'feature3': 'Telegram-Benachrichtigungen',
            'feature4': 'Professionelle Oberfläche',
            'feature5': '24-Stunden-Lizenzaktivierung',
            'license_warning': '⚠ Dies ist eine lizenzierte Software.',
            'license_key_prompt': '⚠ Sie benötigen einen gültigen Lizenzschlüssel, um fortzufahren.',
            'enter_license': '[?] Lizenzschlüssel eingeben: ',
            'license_activated': '[✓] Lizenz erfolgreich aktiviert!',
            'license_expires': '[✓] Lizenz läuft in 24 Stunden ab',
            'license_failed': '[✗] Lizenzaktivierung fehlgeschlagen',
            'invalid_key': '[✗] Ungültiger Lizenzschlüssel',
            'try_again': '[?] Erneut versuchen? (j/n): ',
            'exiting': 'Beenden...',
            'main_menu': '📋 HAUPTMENÜ:',
            'option1': 'Benutzernamen-Checker starten',
            'option2': 'Telegram-Bot konfigurieren',
            'option3': 'Statistiken anzeigen',
            'option4': 'Auf Updates prüfen',
            'option5': 'Über & Hilfe',
            'option0': 'Beenden',
            'select_option': '[?] Option wählen (0-5): ',
            'invalid_option': '[!] Ungültige Option. Bitte versuchen Sie es erneut.',
            'checking_libs': '[*] Überprüfen und Installieren erforderlicher Bibliotheken...',
            'already_installed': '[✓] {package} ist bereits installiert',
            'installing': '[*] Installiere {package}...',
            'installed': '[✓] {package} erfolgreich installiert',
            'failed_install': '[✗] Installation von {package} fehlgeschlagen',
            'all_requirements': '[✓] Alle Anforderungen erfüllt!',
            'license_info': '📊 LIZENZINFORMATIONEN:',
            'status': 'Status:',
            'expires': 'Läuft ab in:',
            'telegram_config': '🤖 TELEGRAM-BOT-KONFIGURATION',
            'enter_token': '[?] Telegram-Bot-Token eingeben: ',
            'enter_chat_id': '[?] Chat-ID eingeben: ',
            'testing_telegram': '[*] Teste Telegram-Verbindung...',
            'telegram_valid': '[✓] Telegram-Bot ist gültig',
            'settings_saved': '[✓] Einstellungen erfolgreich gespeichert!',
            'join_telegram': '⚠ Treten Sie unserem Telegram-Kanal bei: https://t.me/teamofghost',
            'invalid_token': '[✗] Ungültiger Bot-Token',
            'connection_failed': '[✗] Verbindungsfehler: {error}',
            'token_required': '[✗] Token und Chat-ID erforderlich',
            'press_enter': 'Drücken Sie Enter, um fortzufahren...',
            'starting_checker': '🔍 BENUTZERNAMEN-CHECKER STARTEN',
            'how_many_usernames': '[?] Wie viele Benutzernamen generieren? (Standard: 20): ',
            'generating': '[*] Generiere {count} Benutzernamen...',
            'starting_process': '[*] Starte Instagram-Überprüfungsprozess...',
            'available': '[✓] VERFÜGBAR: {username}',
            'telegram_sent': '  ↪ Telegram-Benachrichtigung gesendet',
            'taken': '[✗] BELEGT: {username}',
            'error': '[!] FEHLER: {username}',
            'checking_completed': '📊 ÜBERPRÜFUNG ABGESCHLOSSEN!',
            'total_checked': 'Insgesamt überprüft:',
            'available_count': 'Verfügbar:',
            'taken_count': 'Belegt:',
            'errors_count': 'Fehler:',
            'time_taken': 'Benötigte Zeit:',
            'avg_time': 'Durchschnittszeit per Überprüfung:',
            'found_available': '🎉 {count} Benutzernamen verfügbar!',
            'none_found': '😔 Diesmal keine verfügbaren Benutzernamen gefunden.',
            'checking_updates': '🔄 AUF UPDATES PRÜFEN',
            'current_version': '[*] Aktuelle Version: {version}',
            'checking': '[*] Prüfe auf Updates...',
            'latest_version': '[✓] Sie verwenden die neueste Version!',
            'support_channel': 'Für Updates und Support, treten Sie unserem Telegram-Kanal bei:',
            'about_help': 'ℹ️ ÜBER & HILFE',
            'description': '📖 Beschreibung:',
            'description_text': 'Dieses Tool überprüft die Verfügbarkeit von Instagram-Benutzernamen durch Generieren zufälliger Kombinationen und Testen gegen Instagrams Anmeldesystem.',
            'features_title': '⚙️ Funktionen:',
            'developer': '👤 Entwickler:',
            'support': '📞 Unterstützung:',
            'legal_notice': '⚠️ Rechtlicher Hinweis:',
            'legal_text': 'Dieses Tool dient nur zu Bildungszwecken. Verwenden Sie es verantwortungsbewusst und gemäß den Nutzungsbedingungen von Instagram.',
            'program_exit': 'Beenden... Vielen Dank für die Verwendung von Instagram Checker Pro!',
            'program_interrupted': 'Programm vom Benutzer unterbrochen. Beenden...',
            'error_occurred': 'Ein Fehler ist aufgetreten: {error}',
            'loading_license': '[*] Lade Lizenzinformationen...',
            'license_expired': '[INFO] Lizenz ist abgelaufen. Bitte erneuern.',
            'load_error': '[ERROR] Laden der Lizenz fehlgeschlagen: {error}',
            'save_error': '[ERROR] Speichern der Lizenz fehlgeschlagen: {error}',
            'activated': 'AKTIVIERT',
            'expired': 'ABGELAUFEN',
            'hours': 'h',
            'minutes': 'm',
            'seconds': 's'
        }
    
    def get_russian_translations(self):
       
        return {
            'welcome_title': '✨ ДОБРО ПОЖАЛОВАТЬ В INSTAGRAM USERNAME CHECKER PRO ✨',
            'select_language': '🌍 ВЫБЕРИТЕ ЯЗЫК',
            'features': '📋 Функции:',
            'feature1': 'Продвинутая генерация имен пользователей',
            'feature2': 'Проверка Instagram в реальном времени',
            'feature3': 'Уведомления Telegram',
            'feature4': 'Профессиональный интерфейс',
            'feature5': 'Активация лицензии на 24 часа',
            'license_warning': '⚠ Это лицензионное программное обеспечение.',
            'license_key_prompt': '⚠ Для продолжения нужен действительный лицензионный ключ.',
            'enter_license': '[?] Введите лицензионный ключ: ',
            'license_activated': '[✓] Лицензия успешно активирована!',
            'license_expires': '[✓] Лицензия истекает через 24 часа',
            'license_failed': '[✗] Не удалось активировать лицензию',
            'invalid_key': '[✗] Недействительный лицензионный ключ',
            'try_again': '[?] Попробовать снова? (д/н): ',
            'exiting': 'Выход...',
            'main_menu': '📋 ГЛАВНОЕ МЕНЮ:',
            'option1': 'Запуск проверки имен пользователей',
            'option2': 'Настройка Telegram бота',
            'option3': 'Просмотр статистики',
            'option4': 'Проверить обновления',
            'option5': 'О программе и помощь',
            'option0': 'Выход',
            'select_option': '[?] Выберите опцию (0-5): ',
            'invalid_option': '[!] Неверная опция. Пожалуйста, попробуйте снова.',
            'checking_libs': '[*] Проверка и установка требуемых библиотек...',
            'already_installed': '[✓] {package} уже установлен',
            'installing': '[*] Установка {package}...',
            'installed': '[✓] {package} успешно установлен',
            'failed_install': '[✗] Не удалось установить {package}',
            'all_requirements': '[✓] Все требования удовлетворены!',
            'license_info': '📊 ИНФОРМАЦИЯ О ЛИЦЕНЗИИ:',
            'status': 'Статус:',
            'expires': 'Истекает через:',
            'telegram_config': '🤖 НАСТРОЙКА TELEGRAM БОТА',
            'enter_token': '[?] Введите токен Telegram бота: ',
            'enter_chat_id': '[?] Введите ID чата: ',
            'testing_telegram': '[*] Тестирование подключения Telegram...',
            'telegram_valid': '[✓] Telegram бот действителен',
            'settings_saved': '[✓] Настройки успешно сохранены!',
            'join_telegram': '⚠ Присоединяйтесь к нашему Telegram каналу: https://t.me/teamofghost',
            'invalid_token': '[✗] Недействительный токен бота',
            'connection_failed': '[✗] Ошибка подключения: {error}',
            'token_required': '[✗] Требуются токен и ID чата',
            'press_enter': 'Нажмите Enter, чтобы продолжить...',
            'starting_checker': '🔍 ЗАПУСК ПРОВЕРКИ ИМЕН ПОЛЬЗОВАТЕЛЕЙ',
            'how_many_usernames': '[?] Сколько имен пользователей сгенерировать? (по умолчанию: 20): ',
            'generating': '[*] Генерация {count} имен пользователей...',
            'starting_process': '[*] Запуск процесса проверки Instagram...',
            'available': '[✓] ДОСТУПНО: {username}',
            'telegram_sent': '  ↪ Уведомление Telegram отправлено',
            'taken': '[✗] ЗАНЯТО: {username}',
            'error': '[!] ОШИБКА: {username}',
            'checking_completed': '📊 ПРОВЕРКА ЗАВЕРШЕНА!',
            'total_checked': 'Всего проверено:',
            'available_count': 'Доступно:',
            'taken_count': 'Занято:',
            'errors_count': 'Ошибки:',
            'time_taken': 'Затраченное время:',
            'avg_time': 'Среднее время на проверку:',
            'found_available': '🎉 {count} имен пользователей доступно!',
            'none_found': '😔 На этот раз доступных имен пользователей не найдено.',
            'checking_updates': '🔄 ПРОВЕРКА ОБНОВЛЕНИЙ',
            'current_version': '[*] Текущая версия: {version}',
            'checking': '[*] Проверка обновлений...',
            'latest_version': '[✓] Вы используете последнюю версию!',
            'support_channel': 'Для обновлений и поддержки, присоединяйтесь к нашему Telegram каналу:',
            'about_help': 'ℹ️ О ПРОГРАММЕ И ПОМОЩЬ',
            'description': '📖 Описание:',
            'description_text': 'Этот инструмент проверяет доступность имен пользователей Instagram, генерируя случайные комбинации и тестируя их в системе регистрации Instagram.',
            'features_title': '⚙️ Функции:',
            'developer': '👤 Разработчик:',
            'support': '📞 Поддержка:',
            'legal_notice': '⚠️ Юридическое уведомление:',
            'legal_text': 'Этот инструмент предназначен только для образовательных целей. Используйте его ответственно и в соответствии с Условиями использования Instagram.',
            'program_exit': 'Выход... Спасибо за использование Instagram Checker Pro!',
            'program_interrupted': 'Программа прервана пользователем. Выход...',
            'error_occurred': 'Произошла ошибка: {error}',
            'loading_license': '[*] Загрузка информации о лицензии...',
            'license_expired': '[ИНФОРМАЦИЯ] Срок действия лицензии истек. Пожалуйста, обновите.',
            'load_error': '[ОШИБКА] Не удалось загрузить лицензию: {error}',
            'save_error': '[ОШИБКА] Не удалось сохранить лицензию: {error}',
            'activated': 'АКТИВИРОВАНА',
            'expired': 'ИСТЕКЛА',
            'hours': 'ч',
            'minutes': 'м',
            'seconds': 'с'
        }
    
    def get_turkish_translations(self):
       
        return {
            'welcome_title': '✨ INSTAGRAM USERNAME CHECKER PRO\'YA HOŞ GELDİNİZ ✨',
            'select_language': '🌍 DİLİNİZİ SEÇİN',
            'features': '📋 Özellikler:',
            'feature1': 'Gelişmiş kullanıcı adı oluşturma',
            'feature2': 'Gerçek zamanlı Instagram kontrolü',
            'feature3': 'Telegram bildirimleri',
            'feature4': 'Profesyonel arayüz',
            'feature5': '24 saat lisans aktivasyonu',
            'license_warning': '⚠ Bu lisanslı bir yazılımdır.',
            'license_key_prompt': '⚠ Devam etmek için geçerli bir lisans anahtarı gerekir.',
            'enter_license': '[?] Lisans anahtarını girin: ',
            'license_activated': '[✓] Lisans başarıyla etkinleştirildi!',
            'license_expires': '[✓] Lisans 24 saat sonra sona eriyor',
            'license_failed': '[✗] Lisans etkinleştirme başarısız',
            'invalid_key': '[✗] Geçersiz lisans anahtarı',
            'try_again': '[?] Tekrar deneyin? (e/h): ',
            'exiting': 'Çıkılıyor...',
            'main_menu': '📋 ANA MENÜ:',
            'option1': 'Kullanıcı adı kontrolcüsünü başlat',
            'option2': 'Telegram botunu yapılandır',
            'option3': 'İstatistikleri görüntüle',
            'option4': 'Güncellemeleri kontrol et',
            'option5': 'Hakkında ve Yardım',
            'option0': 'Çıkış',
            'select_option': '[?] Seçenek seçin (0-5): ',
            'invalid_option': '[!] Geçersiz seçenek. Lütfen tekrar deneyin.',
            'checking_libs': '[*] Gerekli kütüphaneler kontrol ediliyor ve yükleniyor...',
            'already_installed': '[✓] {package} zaten yüklü',
            'installing': '[*] {package} yükleniyor...',
            'installed': '[✓] {package} başarıyla yüklendi',
            'failed_install': '[✗] {package} yüklenemedi',
            'all_requirements': '[✓] Tüm gereksinimler karşılandı!',
            'license_info': '📊 LİSANS BİLGİLERİ:',
            'status': 'Durum:',
            'expires': 'Sona erme süresi:',
            'telegram_config': '🤖 TELEGRAM BOT YAPILANDIRMASI',
            'enter_token': '[?] Telegram Bot Token girin: ',
            'enter_chat_id': '[?] Sohbet ID girin: ',
            'testing_telegram': '[*] Telegram bağlantısı test ediliyor...',
            'telegram_valid': '[✓] Telegram bot geçerli',
            'settings_saved': '[✓] Ayarlar başarıyla kaydedildi!',
            'join_telegram': '⚠ Telegram kanalımıza katılın: https://t.me/teamofghost',
            'invalid_token': '[✗] Geçersiz bot token',
            'connection_failed': '[✗] Bağlantı başarısız: {error}',
            'token_required': '[✗] Token ve Sohbet ID gereklidir',
            'press_enter': 'Devam etmek için Enter tuşuna basın...',
            'starting_checker': '🔍 KULLANICI ADI KONTROL CÜSÜ BAŞLATILIYOR',
            'how_many_usernames': '[?] Kaç kullanıcı adı oluşturulsun? (varsayılan: 20): ',
            'generating': '[*] {count} kullanıcı adı oluşturuluyor...',
            'starting_process': '[*] Instagram kontrol süreci başlatılıyor...',
            'available': '[✓] UYGUN: {username}',
            'telegram_sent': '  ↪ Telegram bildirimi gönderildi',
            'taken': '[✗] ALINMIŞ: {username}',
            'error': '[!] HATA: {username}',
            'checking_completed': '📊 KONTROL TAMAMLANDI!',
            'total_checked': 'Toplam kontrol edilen:',
            'available_count': 'Uygun:',
            'taken_count': 'Alınmış:',
            'errors_count': 'Hatalar:',
            'time_taken': 'Geçen süre:',
            'avg_time': 'Kontrol başına ortalama süre:',
            'found_available': '🎉 {count} kullanıcı adı uygun!',
            'none_found': '😔 Bu sefer uygun kullanıcı adı bulunamadı.',
            'checking_updates': '🔄 GÜNCELLEMELER KONTROL EDİLİYOR',
            'current_version': '[*] Mevcut sürüm: {version}',
            'checking': '[*] Güncellemeler kontrol ediliyor...',
            'latest_version': '[✓] En son sürümü kullanıyorsunuz!',
            'support_channel': 'Güncellemeler ve destek için Telegram kanalımıza katılın:',
            'about_help': 'ℹ️ HAKKINDA VE YARDIM',
            'description': '📖 Açıklama:',
            'description_text': 'Bu araç, rastgele kombinasyonlar oluşturarak ve Instagram\'ın kayıt sisteminde test ederek Instagram kullanıcı adlarının kullanılabilirliğini kontrol eder.',
            'features_title': '⚙️ Özellikler:',
            'developer': '👤 Geliştirici:',
            'support': '📞 Destek:',
            'legal_notice': '⚠️ Yasal Uyarı:',
            'legal_text': 'Bu araç yalnızca eğitim amaçlıdır. Instagram\'ın Hizmet Şartları\'na uygun olarak sorumlu bir şekilde kullanın.',
            'program_exit': 'Çıkılıyor... Instagram Checker Pro kullandığınız için teşekkürler!',
            'program_interrupted': 'Program kullanıcı tarafından kesildi. Çıkılıyor...',
            'error_occurred': 'Bir hata oluştu: {error}',
            'loading_license': '[*] Lisans bilgileri yükleniyor...',
            'license_expired': '[BİLGİ] Lisans süresi doldu. Lütfen yenileyin.',
            'load_error': '[HATA] Lisans yüklenemedi: {error}',
            'save_error': '[HATA] Lisans kaydedilemedi: {error}',
            'activated': 'AKTİF',
            'expired': 'SÜRESİ DOLMUŞ',
            'hours': 's',
            'minutes': 'd',
            'seconds': 'sn'
        }
    
    def get_hindi_translations(self):
       
        return {
            'welcome_title': '✨ इंस्टाग्राम यूजरनेम चेकर प्रो में आपका स्वागत है ✨',
            'select_language': '🌍 अपनी भाषा चुनें',
            'features': '📋 सुविधाएँ:',
            'feature1': 'उन्नत उपयोगकर्ता नाम जनरेशन',
            'feature2': 'रियल-टाइम इंस्टाग्राम जांच',
            'feature3': 'टेलीग्राम सूचनाएं',
            'feature4': 'पेशेवर इंटरफेस',
            'feature5': '24-घंटे लाइसेंस सक्रियण',
            'license_warning': '⚠ यह एक लाइसेंस प्राप्त सॉफ्टवेयर है।',
            'license_key_prompt': '⚠ जारी रखने के लिए एक वैध लाइसेंस कुंजी की आवश्यकता है।',
            'enter_license': '[?] लाइसेंस कुंजी दर्ज करें: ',
            'license_activated': '[✓] लाइसेंस सफलतापूर्वक सक्रिय हुआ!',
            'license_expires': '[✓] लाइसेंस 24 घंटे में समाप्त होता है',
            'license_failed': '[✗] लाइसेंस सक्रिय करने में विफल',
            'invalid_key': '[✗] अवैध लाइसेंस कुंजी',
            'try_again': '[?] फिर से प्रयास करें? (ह/न): ',
            'exiting': 'बाहर निकल रहा है...',
            'main_menu': '📋 मुख्य मेनू:',
            'option1': 'यूजरनेम चेकर प्रारंभ करें',
            'option2': 'टेलीग्राम बॉट कॉन्फ़िगर करें',
            'option3': 'सांख्यिकी देखें',
            'option4': 'अपडेट जांचें',
            'option5': 'के बारे में और सहायता',
            'option0': 'बाहर निकलें',
            'select_option': '[?] विकल्प चुनें (0-5): ',
            'invalid_option': '[!] अमान्य विकल्प। कृपया पुनः प्रयास करें।',
            'checking_libs': '[*] आवश्यक लाइब्रेरी जाँच और स्थापित कर रहा है...',
            'already_installed': '[✓] {package} पहले से ही स्थापित है',
            'installing': '[*] {package} स्थापित कर रहा है...',
            'installed': '[✓] {package} सफलतापूर्वक स्थापित हो गया',
            'failed_install': '[✗] {package} स्थापित करने में विफल',
            'all_requirements': '[✓] सभी आवश्यकताएं पूरी हो गई हैं!',
            'license_info': '📊 लाइसेंस जानकारी:',
            'status': 'स्थिति:',
            'expires': 'समाप्त होता है:',
            'telegram_config': '🤖 टेलीग्राम बॉट कॉन्फ़िगरेशन',
            'enter_token': '[?] टेलीग्राम बॉट टोकन दर्ज करें: ',
            'enter_chat_id': '[?] चैट आईडी दर्ज करें: ',
            'testing_telegram': '[*] टेलीग्राम कनेक्शन परीक्षण...',
            'telegram_valid': '[✓] टेलीग्राम बॉट वैध है',
            'settings_saved': '[✓] सेटिंग्स सफलतापूर्वक सहेजी गईं!',
            'join_telegram': '⚠ हमारे टेलीग्राम चैनल से जुड़ें: https://t.me/teamofghost',
            'invalid_token': '[✗] अमान्य बॉट टोकन',
            'connection_failed': '[✗] कनेक्शन विफल: {error}',
            'token_required': '[✗] टोकन और चैट आईडी आवश्यक हैं',
            'press_enter': 'जारी रखने के लिए Enter दबाएं...',
            'starting_checker': '🔍 यूजरनेम चेकर शुरू कर रहा है',
            'how_many_usernames': '[?] कितने उपयोगकर्ता नाम जनरेट करें? (डिफ़ॉल्ट: 20): ',
            'generating': '[*] {count} उपयोगकर्ता नाम जनरेट कर रहा है...',
            'starting_process': '[*] इंस्टाग्राम जांच प्रक्रिया शुरू कर रहा है...',
            'available': '[✓] उपलब्ध: {username}',
            'telegram_sent': '  ↪ टेलीग्राम सूचना भेज दी गई',
            'taken': '[✗] लिया गया: {username}',
            'error': '[!] त्रुटि: {username}',
            'checking_completed': '📊 जांच पूरी हुई!',
            'total_checked': 'कुल जाँचे गए:',
            'available_count': 'उपलब्ध:',
            'taken_count': 'लिए गए:',
            'errors_count': 'त्रुटियाँ:',
            'time_taken': 'लिया गया समय:',
            'avg_time': 'प्रति जाँच औसत समय:',
            'found_available': '🎉 {count} उपयोगकर्ता नाम उपलब्ध हैं!',
            'none_found': '😔 इस बार कोई उपलब्ध उपयोगकर्ता नाम नहीं मिला।',
            'checking_updates': '🔄 अपडेट की जाँच कर रहा है',
            'current_version': '[*] वर्तमान संस्करण: {version}',
            'checking': '[*] अपडेट की जाँच कर रहा है...',
            'latest_version': '[✓] आप नवीनतम संस्करण का उपयोग कर रहे हैं!',
            'support_channel': 'अपडेट और सहायता के लिए, हमारे टेलीग्राम चैनल से जुड़ें:',
            'about_help': 'ℹ️ के बारे में और सहायता',
            'description': '📖 विवरण:',
            'description_text': 'यह टूल यादृच्छिक संयोजन उत्पन्न करके और उन्हें इंस्टाग्राम की साइनअप प्रणाली के खिलाफ परीक्षण करके इंस्टाग्राम उपयोगकर्ता नामों की उपलब्धता की जांच करता है।',
            'features_title': '⚙️ सुविधाएँ:',
            'developer': '👤 डेवलपर:',
            'support': '📞 समर्थन:',
            'legal_notice': '⚠️ कानूनी सूचना:',
            'legal_text': 'यह टूल केवल शैक्षिक उद्देश्यों के लिए है। इसे जिम्मेदारी से और इंस्टाग्राम की सेवा की शर्तों के अनुसार उपयोग करें।',
            'program_exit': 'बाहर निकल रहा है... Instagram Checker Pro का उपयोग करने के लिए धन्यवाद!',
            'program_interrupted': 'उपयोगकर्ता द्वारा कार्यक्रम बाधित। बाहर निकल रहा है...',
            'error_occurred': 'एक त्रुटि हुई: {error}',
            'loading_license': '[*] लाइसेंस जानकारी लोड कर रहा है...',
            'license_expired': '[जानकारी] लाइसेंस की समय सीमा समाप्त हो गई है। कृपया नवीनीकृत करें।',
            'load_error': '[त्रुटि] लाइसेंस लोड करने में विफल: {error}',
            'save_error': '[त्रुटि] लाइसेंस सहेजने में विफल: {error}',
            'activated': 'सक्रिय',
            'expired': 'समाप्त',
            'hours': 'घं',
            'minutes': 'मि',
            'seconds': 'से'
        }
    
    def get_chinese_translations(self):
       
        return {
            'welcome_title': '✨ 欢迎使用 Instagram 用户名检查器专业版 ✨',
            'select_language': '🌍 选择您的语言',
            'features': '📋 功能:',
            'feature1': '高级用户名生成',
            'feature2': '实时 Instagram 检查',
            'feature3': 'Telegram 通知',
            'feature4': '专业界面',
            'feature5': '24 小时许可证激活',
            'license_warning': '⚠ 这是许可软件。',
            'license_key_prompt': '⚠ 您需要有效的许可证密钥才能继续。',
            'enter_license': '[?] 输入许可证密钥: ',
            'license_activated': '[✓] 许可证激活成功！',
            'license_expires': '[✓] 许可证在 24 小时后过期',
            'license_failed': '[✗] 许可证激活失败',
            'invalid_key': '[✗] 无效的许可证密钥',
            'try_again': '[?] 再试一次？(是/否): ',
            'exiting': '正在退出...',
            'main_menu': '📋 主菜单:',
            'option1': '启动用户名检查器',
            'option2': '配置 Telegram 机器人',
            'option3': '查看统计信息',
            'option4': '检查更新',
            'option5': '关于和帮助',
            'option0': '退出',
            'select_option': '[?] 选择选项 (0-5): ',
            'invalid_option': '[!] 无效选项。请重试。',
            'checking_libs': '[*] 检查和安装必需的库...',
            'already_installed': '[✓] {package} 已经安装',
            'installing': '[*] 正在安装 {package}...',
            'installed': '[✓] 成功安装 {package}',
            'failed_install': '[✗] 安装 {package} 失败',
            'all_requirements': '[✓] 所有要求已满足！',
            'license_info': '📊 许可证信息:',
            'status': '状态:',
            'expires': '过期时间:',
            'telegram_config': '🤖 TELEGRAM 机器人配置',
            'enter_token': '[?] 输入 Telegram 机器人令牌: ',
            'enter_chat_id': '[?] 输入聊天 ID: ',
            'testing_telegram': '[*] 正在测试 Telegram 连接...',
            'telegram_valid': '[✓] Telegram 机器人有效',
            'settings_saved': '[✓] 设置成功保存！',
            'join_telegram': '⚠ 加入我们的 Telegram 频道: https://t.me/teamofghost',
            'invalid_token': '[✗] 无效的机器人令牌',
            'connection_failed': '[✗] 连接失败: {error}',
            'token_required': '[✗] 需要令牌和聊天 ID',
            'press_enter': '按 Enter 继续...',
            'starting_checker': '🔍 正在启动用户名检查器',
            'how_many_usernames': '[?] 要生成多少个用户名？(默认: 20): ',
            'generating': '[*] 正在生成 {count} 个用户名...',
            'starting_process': '[*] 正在启动 Instagram 检查过程...',
            'available': '[✓] 可用: {username}',
            'telegram_sent': '  ↪ 已发送 Telegram 通知',
            'taken': '[✗] 已占用: {username}',
            'error': '[!] 错误: {username}',
            'checking_completed': '📊 检查完成！',
            'total_checked': '总共检查:',
            'available_count': '可用:',
            'taken_count': '已占用:',
            'errors_count': '错误:',
            'time_taken': '所用时间:',
            'avg_time': '每次检查的平均时间:',
            'found_available': '🎉 {count} 个用户名可用！',
            'none_found': '😔 这次没有找到可用的用户名。',
            'checking_updates': '🔄 正在检查更新',
            'current_version': '[*] 当前版本: {version}',
            'checking': '[*] 正在检查更新...',
            'latest_version': '[✓] 您正在使用最新版本！',
            'support_channel': '要获取更新和支持，请加入我们的 Telegram 频道:',
            'about_help': 'ℹ️ 关于和帮助',
            'description': '📖 描述:',
            'description_text': '该工具通过生成随机组合并在 Instagram 的注册系统中测试它们来检查 Instagram 用户名的可用性。',
            'features_title': '⚙️ 功能:',
            'developer': '👤 开发者:',
            'support': '📞 支持:',
            'legal_notice': '⚠️ 法律声明:',
            'legal_text': '此工具仅用于教育目的。请负责任地使用它，并遵守 Instagram 的服务条款。',
            'program_exit': '正在退出... 感谢您使用 Instagram Checker Pro！',
            'program_interrupted': '程序被用户中断。正在退出...',
            'error_occurred': '发生错误: {error}',
            'loading_license': '[*] 正在加载许可证信息...',
            'license_expired': '[信息] 许可证已过期。请续订。',
            'load_error': '[错误] 加载许可证失败: {error}',
            'save_error': '[错误] 保存许可证失败: {error}',
            'activated': '已激活',
            'expired': '已过期',
            'hours': '小时',
            'minutes': '分钟',
            'seconds': '秒'
        }
    
    def t(self, key, **kwargs):
       
        translation = self.languages[self.current_lang]['translations'].get(key, key)
        
       
        if kwargs:
            for k, v in kwargs.items():
                translation = translation.replace(f'{{{k}}}', str(v))
        
        return translation
    
    def select_language(self):
       
        self.clear_screen()
        
       
        lang_logo = f"""
{C}{BRIGHT}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║                                                                ║
║     {G}{BRIGHT}INSTAGRAM USERNAME CHECKER PRO v2.1              {C}    ║
║     {Y}{BRIGHT}MULTILINGUAL SUPPORT                          {C}    ║
║     {M}{BRIGHT}DEVELOPER: @Alikhalafm and @K3t3t                          {C}    ║
╚════════════════════════════════════════════════════════════════╝
{RESET}
        """
        print(lang_logo)
        
       
        print(f"\n{BRIGHT}{C}{'═'*60}{RESET}")
        print(f"{BRIGHT}{G}🌍 SELECT YOUR LANGUAGE / اختر لغتك / SELECCIONE SU IDIOMA{RESET}")
        print(f"{BRIGHT}{C}{'═'*60}{RESET}\n")
        
        languages_list = list(self.languages.items())
        
       
        for i in range(0, len(languages_list), 3):
            row = languages_list[i:i+3]
            for lang_code, lang_data in row:
                flag = lang_data['flag']
                name = lang_data['name']
                index = list(self.languages.keys()).index(lang_code)
                print(f"{BRIGHT}{W}{index+1:2}.{RESET} {flag} {name:<15}", end="  ")
            print()
        
        print(f"\n{BRIGHT}{C}{'═'*60}{RESET}")
        
       
        while True:
            try:
                choice = input(f"\n{BRIGHT}{C}[?] Select language (1-{len(self.languages)}): {RESET}{G}")
                print(RESET, end="")
                
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(self.languages):
                    lang_code = list(self.languages.keys())[choice_idx]
                    self.current_lang = lang_code
                    
                   
                    lang_name = self.languages[lang_code]['name']
                    flag = self.languages[lang_code]['flag']
                    print(f"\n{G}{BRIGHT}[✓] Language selected: {flag} {lang_name}{RESET}")
                    time.sleep(1)
                    return
                else:
                    print(f"{R}[!] Invalid selection. Please try again.{RESET}")
            except ValueError:
                print(f"{R}[!] Please enter a valid number.{RESET}")
    
    def clear_screen(self):
       
        os.system('cls' if os.name == 'nt' else 'clear')

class InstagramChecker(LanguageManager):
    def __init__(self):
        super().__init__()
        self.version = "2.1 Multilingual"
        self.developer = "@Alikhalafm and @K3t3t"
        # تم حذف self.license_file لأنه لا يوجد ملفات تفعيل بعد الآن
        self.license_key = None
        self.license_expiry = None
        self.activated = False

    def get_hwid(self):
        import platform
        import subprocess
        try:
            if os.name == 'nt':
                # لجلب المعرف الفريد لويندوز
                cmd = "wmic csproduct get uuid"
                uuid = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
                return hashlib.sha256(uuid.encode()).hexdigest()
            else:
                # لأنظمة لينكس وماك
                id_str = platform.node() + platform.machine() + platform.processor()
                return hashlib.sha256(id_str.encode()).hexdigest()
        except:
            # حل احتياطي في حال فشل الأوامر أعلاه
            fallback = platform.node() + os.getlogin()
            return hashlib.sha256(fallback.encode()).hexdigest()
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_license(self):
        # استبدل YOUR_SERVER_IP بآي بي سيرفر Flask الخاص بك
        SERVER_URL = "https://license-server-production-0377.up.railway.app/check"
        current_hwid = self.get_hwid()
        
        self.clear_screen()
        self.display_logo()
        
        # عرض واجهة المميزات والترحيب
        print(f"\n{BRIGHT}{C}{'='*60}{RESET}")
        print(f"{BRIGHT}{G}{self.t('welcome_title')}{RESET}")
        print(f"{BRIGHT}{C}{'='*60}{RESET}\n")
        
        print(f"{Y}📋 {BRIGHT}{self.t('features')}{RESET}")
        print(f"  {G}✓{RESET} {self.t('feature1')}")
        print(f"  {G}✓{RESET} {self.t('feature2')}")
        print(f"  {G}✓{RESET} {self.t('feature3')}")
        print(f"  {G}✓{RESET} {self.t('feature4')}")
        print(f"  {G}✓{RESET} {self.t('feature5')}\n")
        
        print(f"{M}⚠ {BRIGHT}{self.t('license_warning')}{RESET}")
        print(f"{M}⚠ {BRIGHT}{self.t('license_key_prompt')}{RESET}\n")
        
        while True:
            license_key = input(f"{C}{BRIGHT}{self.t('enter_license')}{RESET}{G}").strip()
            print(RESET, end="")
            
            # تشفير الكود قبل الإرسال
            hashed_key = hashlib.sha256(license_key.encode()).hexdigest()

            try:
                payload = {"key": hashed_key, "hwid": current_hwid}
                response = requests.post(SERVER_URL, json=payload, timeout=10)

                if response.status_code == 200:
                    res_data = response.json()
                    # حفظ البيانات في الذاكرة (الرام) فقط طوال فترة تشغيل البرنامج
                    self.license_expiry = datetime.datetime.fromisoformat(res_data['expires'])
                    self.activated = True
                    
                    print(f"\n{G}{BRIGHT}{self.t('license_activated')}{RESET}")
                    print(f"{G}{BRIGHT}{self.t('license_expires')}{RESET} {res_data['expires']}")
                    time.sleep(2)
                    return True
                else:
                    print(f"{R}{self.t('invalid_key')}{RESET}")
                    retry = input(f"{Y}{self.t('try_again')} (y/n): {RESET}").lower()
                    if retry not in ['y', 's', 'д', 'ह', 'هـ', '是']:
                        print(f"{R}{self.t('exiting')}{RESET}")
                        time.sleep(1)
                        sys.exit(0)
                    
                    self.clear_screen()
                    self.display_logo()

            except Exception as e:
                print(f"\n{R}⚠️ خطأ في الاتصال بالسيرفر: {e}{RESET}")
                time.sleep(2)
                sys.exit(0)
    
    def display_logo(self):
       
        logo = f"""
{C}{BRIGHT}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████             █████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                    ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓███                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓██           ▓▓▓▓▓▓▓▓        ███▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓██          ▓▓▓▓▓▓▓▓▓▓▓▓       ██▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓██         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ██▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓██        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ███▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓██  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓█  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ██▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓██ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║    {W}{BRIGHT}▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C}    ║
║                                                                ║
║     {G}{BRIGHT}INSTAGRAM USERNAME CHECKER PRO v{self.version}          {C}    ║
║     {Y}{BRIGHT}DEVELOPER: {self.developer}                          {C}    ║
║     {M}{BRIGHT}Licensed Version - All Rights Reserved              {C}    ║
╚════════════════════════════════════════════════════════════════╝
{RESET}
        """
        print(logo)
    
    def install_requirements(self):
       
        requirements = [
            'requests',
            'colorama'
        ]
        
        print(f"\n{C}{BRIGHT}{self.t('checking_libs')}{RESET}")
        
        for package in requirements:
            try:
                __import__(package.replace('-', '_'))
                print(f"{G}{self.t('already_installed', package=package)}{RESET}")
            except ImportError:
                print(f"{Y}{self.t('installing', package=package)}{RESET}")
                try:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--quiet'])
                    print(f"{G}{self.t('installed', package=package)}{RESET}")
                except subprocess.CalledProcessError:
                    print(f"{R}{self.t('failed_install', package=package)}{RESET}")
        
        print(f"{G}{BRIGHT}{self.t('all_requirements')}{RESET}\n")
        time.sleep(1)
    
    def display_menu(self):
       
        self.clear_screen()
        self.display_logo()
        
       
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{M}{self.t('license_info')}{RESET}")
        print(f"{BRIGHT}{C}{'─'*60}{RESET}")
        
        if self.license_expiry is None:
            print(f"{Y}{self.t('status')}{RESET} {R}{BRIGHT}{self.t('expired')}{RESET}")
            print(f"{Y}{self.t('expires')}{RESET} {R}{BRIGHT}N/A{RESET}")
        else:
            print(f"{Y}{self.t('status')}{RESET} {G}{BRIGHT}{self.t('activated')}{RESET}")
            
           
            remaining_time = self.license_expiry - datetime.datetime.now()
            if remaining_time.total_seconds() > 0:
                hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f"{Y}{self.t('expires')}{RESET} {G}{BRIGHT}{hours}{self.t('hours')} {minutes}{self.t('minutes')} {seconds}{self.t('seconds')}{RESET}")
            else:
                print(f"{Y}{self.t('expires')}{RESET} {R}{BRIGHT}{self.t('expired')}{RESET}")
                self.activated = False
        
        print(f"{C}{BRIGHT}{'═'*60}{RESET}\n")
        
        print(f"{BRIGHT}{G}{self.t('main_menu')}{RESET}")
        print(f"{C}{BRIGHT}{'─'*60}{RESET}")
        print(f"{BRIGHT}{W}1.{RESET} {G}{self.t('option1')}{RESET}")
        print(f"{BRIGHT}{W}2.{RESET} {G}{self.t('option2')}{RESET}")
        print(f"{BRIGHT}{W}3.{RESET} {G}{self.t('option3')}{RESET}")
        print(f"{BRIGHT}{W}4.{RESET} {G}{self.t('option4')}{RESET}")
        print(f"{BRIGHT}{W}5.{RESET} {G}{self.t('option5')}{RESET}")
        print(f"{BRIGHT}{W}0.{RESET} {R}{self.t('option0')}{RESET}")
        print(f"{C}{BRIGHT}{'─'*60}{RESET}")
    
    def configure_telegram(self):
       
        self.clear_screen()
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{G}{self.t('telegram_config')}{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}\n")
        
        token = input(f"{C}{BRIGHT}{self.t('enter_token')}{RESET}{G}")
        print(RESET, end="")
        
        chat_id = input(f"{C}{BRIGHT}{self.t('enter_chat_id')}{RESET}{G}")
        print(RESET, end="")
        
       
        if token and chat_id:
            print(f"\n{Y}{self.t('testing_telegram')}{RESET}")
            try:
                url = f"https://api.telegram.org/bot{token}/getMe"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"{G}{self.t('telegram_valid')}{RESET}")
                    
                   
                    self.telegram_token = token
                    self.telegram_chat_id = chat_id
                    
                    print(f"{G}{self.t('settings_saved')}{RESET}")
                    print(f"\n{M}{self.t('join_telegram')}{RESET}")
                    webbrowser.open('https://t.me/teamofghost')
                else:
                    print(f"{R}{self.t('invalid_token')}{RESET}")
            except Exception as e:
                print(f"{R}{self.t('connection_failed', error=str(e))}{RESET}")
        else:
            print(f"{R}{self.t('token_required')}{RESET}")
        
        input(f"\n{BRIGHT}{C}{self.t('press_enter')}{RESET}")
    
    def send_telegram_message(self, user):
       
        if not hasattr(self, 'telegram_token') or not hasattr(self, 'telegram_chat_id'):
            return False
        
        try:
           
            current_lang_data = self.languages[self.current_lang]
            lang_flag = current_lang_data['flag']
            lang_name = current_lang_data['name']
            
            message = f"""
{C}{BRIGHT}════════════════════════════════════
{G}✅ USERNAME AVAILABLE!
{Y}Username: {W}{user}
{M}Checker: Instagram Checker Pro v{self.version}
{C}Language: {lang_flag} {lang_name}
{C}Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{C}════════════════════════════════════{RESET}
            """
            
            url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
            response = requests.post(url, json={
                "chat_id": self.telegram_chat_id,
                "text": message,
                "parse_mode": "HTML"
            }, timeout=10)
            
            return response.status_code == 200
        except:
            return False
    
    def generate_usernames(self, count=10):
       
        usernames = []
        patterns = [
            "{l}{n}{U}{a}{a}",
            "{n}_{a}_{l}",
            "{l}.{n}.{a}",
            "{l}{n}.{U}{a}{a}",
            "{l}{n}_{U}{a}{a}",
            "{l}{U}{n}{a}_",
            "{l}{U}{n}{a}.{l}",
            "{l}{l}_{a}{n}",
            "{l}{l}.{a}{n}",
            "{U}{l}{n}_{a}{U}",
            "{l}{U}{U}{n}{a}",
            "{U}{n}{l}.{a}{U}"
        ]
        
        for _ in range(count):
            l = random.choice('abcdefghijklmnopqrstuvwxyz')
            U = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            n = random.choice('0123456789')
            a = random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
            
            pattern = random.choice(patterns)
            username = pattern.format(l=l, U=U, n=n, a=a)
            usernames.append(username)
        
        return usernames
    
    def check_instagram_username(self, username):
        # تنظيف اليوزر وتحويله لحروف صغيرة (لحل مشكلة hBB60)

        username = str(username).lower().strip()
        
        # الرابط القوي (Mobile API)
        url = 'https://www.instagram.com/api/v1/users/check_username/'
        
        headers = {
            'User-Agent': 'Instagram 294.0.0.33.110 (iPhone14,3; iOS 16_6; en_US; en-US; scale=3.00; 1284x2778) AppleWebKit/605.1.15',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-IG-App-ID': '936619743392459',
            'X-CSRFToken': 'missing',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.instagram.com/accounts/emailsignup/'
        }
        
        data = {'username': username}
        
        try:
            response = requests.post(url, headers=headers, data=data, timeout=10)
            
            if response.status_code == 200:
                res_json = response.json()
                if res_json.get('available') == True:
                    return True
                else:
                    return False
            else:
                return None
        except Exception:
            return None

    def start_checker(self):
       
        self.clear_screen()
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{G}{self.t('starting_checker')}{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}\n")
        
       
        try:
            count_input = input(f"{C}{BRIGHT}{self.t('how_many_usernames')}{RESET}{G}")
            print(RESET, end="")
            count = int(count_input) if count_input else 20
        except:
            count = 20
        
        print(f"\n{Y}{self.t('generating', count=count)}{RESET}")
        usernames = self.generate_usernames(count)
        
        print(f"{Y}{self.t('starting_process')}{RESET}")
        print(f"{C}{BRIGHT}{'─'*60}{RESET}\n")
        
        stats = {
            'available': 0,
            'taken': 0,
            'error': 0,
            'total': len(usernames)
        }
        
        start_time = time.time()
        
        for i, username in enumerate(usernames, 1):
           
            progress = (i / len(usernames)) * 100
            bar_length = 40
            filled_length = int(bar_length * i // len(usernames))
            bar = f"{G}{'█' * filled_length}{C}{'░' * (bar_length - filled_length)}{RESET}"
            
            print(f"{BRIGHT}{C}[{i:03d}/{len(usernames):03d}] {bar} {progress:.1f}%{RESET}", end='\r')
            
           
            result = self.check_instagram_username(username)
            
            if result is True:
                stats['available'] += 1
                print(f"\n{G}{BRIGHT}{self.t('available', username=username)}{RESET}")
                
               
                if hasattr(self, 'telegram_token'):
                    if self.send_telegram_message(username):
                        print(f"{G}{self.t('telegram_sent')}{RESET}")
                
            elif result is False:
                stats['taken'] += 1
                print(f"\n{R}{BRIGHT}{self.t('taken', username=username)}{RESET}")
            else:
                stats['error'] += 1
                print(f"\n{Y}{BRIGHT}{self.t('error', username=username)}{RESET}")
            
           
            time.sleep(random.uniform(1, 2))
        
       
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{M}{self.t('checking_completed')}{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{Y}{self.t('total_checked')}{RESET} {W}{BRIGHT}{stats['total']}{RESET}")
        print(f"{G}{self.t('available_count')}{RESET} {W}{BRIGHT}{stats['available']}{RESET}")
        print(f"{R}{self.t('taken_count')}{RESET} {W}{BRIGHT}{stats['taken']}{RESET}")
        print(f"{Y}{self.t('errors_count')}{RESET} {W}{BRIGHT}{stats['error']}{RESET}")
        print(f"{C}{self.t('time_taken')}{RESET} {W}{BRIGHT}{total_time:.2f} seconds{RESET}")
        print(f"{C}{self.t('avg_time')}{RESET} {W}{BRIGHT}{(total_time/stats['total']):.2f} seconds{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}")
        
        if stats['available'] > 0:
            print(f"\n{G}{BRIGHT}{self.t('found_available', count=stats['available'])}{RESET}")
        else:
            print(f"\n{Y}{BRIGHT}{self.t('none_found')}{RESET}")
        
        input(f"\n{BRIGHT}{C}{self.t('press_enter')}{RESET}")
    
    def check_updates(self):
       
        self.clear_screen()
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{G}{self.t('checking_updates')}{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}\n")
        
        print(f"{Y}{self.t('current_version', version=self.version)}{RESET}")
        print(f"{Y}{self.t('checking')}{RESET}")
        
       
        time.sleep(2)
        
        print(f"{G}{self.t('latest_version')}{RESET}")
        print(f"\n{C}{self.t('support_channel')}{RESET}")
        print(f"{M}https://t.me/teamofghost{RESET}")
        
        input(f"\n{BRIGHT}{C}{self.t('press_enter')}{RESET}")
    
    def about_help(self):
       
        self.clear_screen()
        print(f"\n{C}{BRIGHT}{'═'*60}{RESET}")
        print(f"{BRIGHT}{G}{self.t('about_help')}{RESET}")
        print(f"{C}{BRIGHT}{'═'*60}{RESET}\n")
        
        print(f"{Y}{BRIGHT}{self.t('description')}{RESET}")
        print(f"{W}{self.t('description_text')}{RESET}\n")
        
        print(f"{Y}{BRIGHT}{self.t('features_title')}{RESET}")
        print(f"{G}✓{RESET} {self.t('feature1')}")
        print(f"{G}✓{RESET} {self.t('feature2')}")
        print(f"{G}✓{RESET} {self.t('feature3')}")
        print(f"{G}✓{RESET} {self.t('feature4')}")
        print(f"{G}✓{RESET} {self.t('feature5')}\n")
        
        print(f"{Y}{BRIGHT}{self.t('developer')}{RESET}")
        print(f"{W}Me: @Alikhalafm{RESET}\n")
        
        print(f"{Y}{BRIGHT}{self.t('support')}{RESET}")
        print(f"{W}{self.t('join_telegram')}{RESET}")
        print(f"{W}Contact: @Alikhalafm{RESET}\n")
        
        print(f"{Y}{BRIGHT}{self.t('legal_notice')}{RESET}")
        print(f"{W}{self.t('legal_text')}{RESET}")
        
        input(f"\n{BRIGHT}{C}{self.t('press_enter')}{RESET}")
    
    def main(self):
       
        try:
           
            self.select_language()
            
           
            if not self.check_license():
                return
            
           
            self.install_requirements()
            
           
            while True:
                self.display_menu()
                
                choice = input(f"\n{BRIGHT}{C}{self.t('select_option')}{RESET}{G}")
                print(RESET, end="")
                
                if choice == '1':
                    self.start_checker()
                elif choice == '2':
                    self.configure_telegram()
                elif choice == '3':
                   
                    print(f"\n{Y}[*] {self.t('option3')} coming soon...{RESET}")
                    time.sleep(2)
                elif choice == '4':
                    self.check_updates()
                elif choice == '5':
                    self.about_help()
                elif choice == '0':
                    print(f"\n{R}{BRIGHT}{self.t('program_exit')}{RESET}")
                    time.sleep(1)
                    break
                else:
                    print(f"\n{R}{self.t('invalid_option')}{RESET}")
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            print(f"\n{R}{BRIGHT}{self.t('program_interrupted')}{RESET}")
            time.sleep(1)
        except Exception as e:
            print(f"\n{R}{BRIGHT}{self.t('error_occurred', error=str(e))}{RESET}")
            input(f"\n{BRIGHT}{C}{self.t('press_enter')}{RESET}")

if __name__ == "__main__":
    app = InstagramChecker()
    app.main()